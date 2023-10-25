"""
file uses functions from icatcher to correctly predict the gaze direction of the infant using the frames collected.
to integrate any other model can make changes here.
"""

import logging
import torch
import numpy as np
import cv2
from PIL import Image
from pathlib import Path
import pooch
from icatcher.cli import *
def extract_crop(frame, bbox):
    """
    extracts a crop from a frame using bbox, and transforms it
    :param frame: the frame
    :param bbox: opencv bbox 4x1
    :return: the crop and the 5x1 box features
    """
    if bbox is None:
        return None, None
    img_shape = np.array(frame.shape)
    face_box = np.array([bbox[1], bbox[1] + bbox[3], bbox[0], bbox[0] + bbox[2]])
    crop = frame[bbox[1]:bbox[1] + bbox[3], bbox[0]:bbox[0] + bbox[2]]

    test_transforms = models.DataTransforms(100,
                                          [0.485, 0.456, 0.406],
                                          [0.229, 0.224, 0.225]).transformations["test"]
    crop = test_transforms(Image.fromarray(crop))
    crop = crop.permute(1, 2, 0).unsqueeze(0).numpy()
    ratio = np.array([face_box[0] / img_shape[0], face_box[1] / img_shape[0],
                      face_box[2] / img_shape[1], face_box[3] / img_shape[1]])
    face_size = (ratio[1] - ratio[0]) * (ratio[3] - ratio[2])
    face_ver = (ratio[0] + ratio[1]) / 2
    face_hor = (ratio[2] + ratio[3]) / 2
    face_height = ratio[1] - ratio[0]
    face_width = ratio[3] - ratio[2]
    my_box = np.array([face_size, face_ver, face_hor, face_height, face_width])
    return crop, my_box
def load_models():
    """
    loads all relevant neural network models to perform predictions
    models will be automatically downloaded if not found in the cache,
    user may overide downloaded location with the env variable ICATCHER_DATA_DIR
    defaults:
    :Mac: "~/Library/Caches/<AppName>"
    :Unix: "~/.cache/<AppName>" or the value of the "XDG_CACHE_HOME"
    environment variable, if defined.
    :Windows: "C:\\Users\\<user>\\AppData\\Local\\<AppAuthor>\\<AppName>\\Cache"
    :param opt: command line options
    :return all nn models
    """
    GOODBOY = pooch.create(path=pooch.os_cache("icatcher_plus"),
                           base_url="https://osf.io/ycju8/download",
                           version=version,
                           version_dev="main",
                           env="ICATCHER_DATA_DIR",
                           registry={"zip_content.txt": "d81bfb5a183edea6dc74f7f342d516a9843865570b9ecfbf481209ec5114110a",
                                     "icatcher+_models.zip": "d78385b3a08f3d55ce75249142d15549e4c5552d5e1231cad3b69063bb778ce9"},
                           urls={"zip_content.txt":"https://osf.io/v4w53/download",
                                 "icatcher+_models.zip":"https://osf.io/ycju8/download"})
    # zip_content_file = GOODBOY.fetch("zip_content.txt")
    # with open(zip_content_file, "r") as f:
        # zip_content = [x.strip() for x in f]
    file_paths = GOODBOY.fetch("icatcher+_models.zip",
                               processor=pooch.Unzip(),
                               progressbar=True)
    file_names = [Path(x).name for x in file_paths]
    face_detector_model_file = file_paths[file_names.index("face_model.caffemodel")]
    config_file = file_paths[file_names.index("config.prototxt")]
    path_to_gaze_model = file_paths[file_names.index("icatcher+_lookit.pth")]
    path_to_fc_model = file_paths[file_names.index("face_classifier_lookit.pth")]
    
    gaze_model = models.GazeCodingModel().to('cpu')
    
    state_dict = torch.load(str(path_to_gaze_model), map_location=torch.device('cpu'))
    
    try:
        gaze_model.load_state_dict(state_dict)
    except RuntimeError as e:  # hack to deal with models trained on distributed setup
        from collections import OrderedDict
        new_state_dict = OrderedDict()
        for k, v in state_dict.items():
            name = k[7:]  # remove `module.`
            new_state_dict[name] = v
        # load params
        gaze_model.load_state_dict(new_state_dict)
    gaze_model.eval()


    face_classifier_model = None
    face_classifier_data_transforms = None
    # load face extractor model
    face_detector_model = cv2.dnn.readNetFromCaffe(str(config_file), str(face_detector_model_file))    
    return gaze_model, face_detector_model, face_classifier_model, face_classifier_data_transforms

def predict_from_frame(cap):
    buffer_size=15
    loc = -5  
    cursor = -5 
    gaze_model, face_detector_model, face_classifier_model, face_classifier_data_transforms = load_models()
    answers = []  # list of answers for each frame
    confidences = []  # list of confidences for each frame
    image_sequence = []  # list of (crop, valid) for each frame in the sliding window
    box_sequence = []  # list of bounding boxes for each frame in the sliding window
    bbox_sequence = []  # list of bounding boxes for each frame in the sliding window
    frames = []  # list of frames for each frame in the sliding window
    from_tracker = []  # list of booleans indicating whether the bounding box was obtained from the tracker
    last_known_valid_bbox = None  # last known valid bounding box
    frame_count = 0  # frame counter
    hor, ver = 0.5, 1  # initial guess for face location
    cur_fps = video.FPS()  # for debugging purposes
    last_class_text = ""  # Initialize so that we see the first class assignment as an event to record
    ret, frame = cap.read()
    h_start_at=0
    w_start_at=0
    h_end_at, w_end_at, channels = frame.shape
    while ret:
        frame = draw.mask_regions(frame, h_start_at, h_end_at, w_start_at, w_end_at)  # mask roi
        frames.append(frame)
        cv2_bboxes = detect_face_opencv_dnn(face_detector_model, frame, 0.7)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        if not cv2_bboxes and (last_known_valid_bbox is None or not "False"):
            answers.append(classes['noface'])  # if face detector fails, treat as away and mark invalid
            confidences.append(-1)
            image = np.zeros((1, 100, 100, 3), np.float64)
            my_box = np.array([0, 0, 0, 0, 0])
            image_sequence.append((image, True))
            box_sequence.append(my_box)
            bbox_sequence.append(None)
            from_tracker.append(False)
        else:
            if cv2_bboxes:
                from_tracker.append(False)
            else:
                from_tracker.append(True)
                cv2_bboxes = [last_known_valid_bbox]
            selected_bbox = select_face(cv2_bboxes, frame, face_classifier_model, face_classifier_data_transforms, hor, ver, 'cpu')
            crop, my_box = extract_crop(frame, selected_bbox)
            if selected_bbox is None:
                    answers.append(classes['nobabyface'])  # if selecting face fails, treat as away and mark invalid
                    confidences.append(-1)
                    image = np.zeros((1, 100,100, 3), np.float64)
                    my_box = np.array([0, 0, 0, 0, 0])
                    image_sequence.append((image, True))
                    box_sequence.append(my_box)
                    bbox_sequence.append(None)
            else:
                if crop.size == 0:
                    raise ValueError("crop size is 0, what just happend?")
                answers.append(classes['left'])  # if face detector succeeds, treat as left and mark valid
                confidences.append(-1)
                image_sequence.append((crop, False))
                box_sequence.append(my_box)
                bbox_sequence.append(selected_bbox)
                if not from_tracker[-1]:
                    last_known_valid_bbox = selected_bbox.copy()
            if len(image_sequence) == 9:  # we have enough frames for prediction, predict for middle frame
                cur_frame = frames[cursor]
                cur_bbox = bbox_sequence[cursor]
                is_from_tracker = from_tracker[cursor]
                frames.pop(0)
                bbox_sequence.pop(0)
                from_tracker.pop(0)
                if not image_sequence[9 // 2][1]:  # if middle image is valid
                    to_predict = {"imgs": torch.tensor(np.array([x[0] for x in image_sequence[0::2]]), dtype=torch.float).squeeze().permute(0, 3, 1, 2).to('cpu'),
                                    "boxs": torch.tensor(np.array(box_sequence[::2]), dtype=torch.float).to('cpu')
                                    }
                    with torch.set_grad_enabled(False):
                        outputs = gaze_model(to_predict)  # actual gaze prediction
                        probs = torch.nn.functional.softmax(outputs, dim=1)
                        _, prediction = torch.max(outputs, 1)
                        confidence, _ = torch.max(probs, 1)
                        float32_conf = confidence.cpu().numpy()[0]
                        int32_pred = prediction.cpu().numpy()[0]
                    answers[loc] = int32_pred  # update answers for the middle frame
                    confidences[loc] = float32_conf  # update confidences for the middle frame
                image_sequence.pop(0)
                box_sequence.pop(0)
        ret, frame = cap.read()
        frame_count += 1
        if(frame_count>buffer_size):
            break
    return answers,confidences,frames