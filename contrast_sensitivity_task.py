﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on June 22, 2023, at 20:44
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from predict import *
from icatcher.cli import *
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard
import cv2
import platform

def extract_crop(frame, bbox):
    """
    extracts a crop from a frame using bbox, and transforms it
    :param frame: the frame
    :param bbox: opencv bbox 4x1
    :param opt: command line options
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

def cst():
    buffer_size=15
    answers = []  # list of answers for each frame
    confidences = [] 
    os_name = platform.system()
    cap = cv2.VideoCapture(0)
    frame_buffer = []
    _thisDir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(_thisDir)
    # output_file = 'output.mp4'
    # current_dir = os.path.dirname(os.path.abspath(__file__))
    # output_path = os.path.join(_thisDir, 'output.mp4')
    # codec = cv2.VideoWriter_fourcc(*'mp4v')
    # fps = 15.0
    # frame_size = (640, 480)
    # out = cv2.VideoWriter(output_path, codec, fps, frame_size)
    # Ensure that relative paths start from the same directory as this script

    # Store info about the experiment session
    psychopyVersion = '2022.2.5'
    expName = 'iva'  # from the Builder filename that created this script
    expInfo = {
        'participant': f"{randint(0, 999999):06.0f}",
        'session': '001',
        'stimulus size': '8.5',
        'spatial freq': '0.8',
        'start contrast': '1',
        'step contrast': '-0.2',
        'end contrast': '0.2',
        'stimulus duration': '1',
    }
    # --- Show participant info dialog --
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    expInfo['date'] = data.getDateStr()  # add a simple timestamp
    expInfo['expName'] = expName
    expInfo['psychopyVersion'] = psychopyVersion

    # Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

    # An ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\soham\\Desktop\\gsoc\\incf\\contrast sensitivity task\\contrast_sensitivity_task.py',
        savePickle=True, saveWideText=True,
        dataFileName=filename)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    frameTolerance = 0.001  # how close to onset before 'same' frame

    # Start Code - component code to be run after the window creation

    # --- Setup the Window ---
    win = visual.Window(
        size=[1536, 864], fullscr=True, screen=0, 
        winType='pyglet', allowStencil=True,
        monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
        blendMode='avg', useFBO=True, 
        units='height')
    win.mouseVisible = False
    # store frame rate of monitor if we can measure it
    expInfo['frameRate'] = win.getActualFrameRate()
    if expInfo['frameRate'] != None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    # --- Setup input devices ---
    ioConfig = {}

    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')

    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    eyetracker = None

    # create a default keyboard (e.g. to check for escape)
    if os_name == "Windows":    
        defaultKeyboard = keyboard.Keyboard(backend='iohub')
    else:
        defaultKeyboard = keyboard.Keyboard(backend='ptb')

    # --- Initialize components for Routine "set_values" ---
    # Set experiment start values for variable component contrast
    contrast = float(expInfo['start contrast'])-float(expInfo['step contrast'])
    contrastContainer = []

    # --- Initialize components for Routine "grating_acuity" ---
    # Set experiment start values for variable component position
    position = (0, 0)
    positionContainer = []
    GA = visual.GratingStim(
        win=win, name='GA',units='deg', 
        tex='sqr', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=[32,16], sf=float(expInfo['spatial freq']), phase=0.0,
        color=[1,1,1], colorSpace='rgb',
        opacity=None, contrast=1.0, blendmode='avg',
        texRes=512.0, interpolate=True, depth=-1.0)
    aperture = visual.Aperture(
        win=win, name='aperture',
        units='deg', size=[8], pos=[0,0], ori=0.0,
        shape='circle', anchor='center'
    )
    aperture.disable()  # disable until its actually used

    # --- Initialize components for Routine "central_fixation" ---
    placeholder = visual.TextStim(win=win, name='placeholder',
        text='initial contrast sensitivity \ntask',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);

    # Create some handy timers
    globalClock = core.Clock()  # to track the time since experiment started
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

    # set up handler to look after randomisation of conditions etc
    GA_loop = data.TrialHandler(nReps=(float(expInfo['end contrast'])-float(expInfo['start contrast']))//float(expInfo['step contrast']), method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='GA_loop')
    thisExp.addLoop(GA_loop)  # add the loop to the experiment
    thisGA_loop = GA_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisGA_loop.rgb)
    if thisGA_loop != None:
        for paramName in thisGA_loop:
            exec('{} = thisGA_loop[paramName]'.format(paramName))

    for thisGA_loop in GA_loop:
        currentLoop = GA_loop
        # abbreviate parameter names if possible (e.g. rgb = thisGA_loop.rgb)
        if thisGA_loop != None:
            for paramName in thisGA_loop:
                exec('{} = thisGA_loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "set_values" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        contrast = contrast+float(expInfo['step contrast'])  # Set routine start values for contrast
        # keep track of which components have finished
        set_valuesComponents = []
        for thisComponent in set_valuesComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "set_values" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in set_valuesComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "set_values" ---
        for thisComponent in set_valuesComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('contrast.routineEndVal', contrast)  # Save end routine value
        # the Routine "set_values" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trials = data.TrialHandler(nReps=4.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials')
        thisExp.addLoop(trials)  # add the loop to the experiment
        thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        for thisTrial in trials:
            currentLoop = trials
            # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
            if thisTrial != None:
                for paramName in thisTrial:
                    exec('{} = thisTrial[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "grating_acuity" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            position = (randchoice([-1, 1])*16, 0)  # Set routine start values for position
            GA.setContrast(contrast)
            GA.setPos(position)
            aperture.setPos(position)
            # keep track of which components have finished
            grating_acuityComponents = [GA, aperture]
            for thisComponent in grating_acuityComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            rep=0
            # --- Run Routine "grating_acuity" ---
            while continueRoutine:
                # get current time

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
                # cur_fps = video.FPS()  # for debugging purposes
                # last_class_text = ""  # Initialize so that we see the first class assignment as an event to record
                ret, frame = cap.read()
                h_start_at=0
                w_start_at=0
                h_end_at, w_end_at, channels = frame.shape
                # answers,confidences=predict_from_frame(cap)
                # print(answers)
                # print(confidences)               
              # Display the frame
              # cv2.imshow('Video', frame)
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *GA* updates
                print("ga starting")
                if GA.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    GA.frameNStart = frameN  # exact frame index
                    GA.tStart = t  # local t and not account for scr refresh
                    GA.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(GA, 'tStartRefresh')  # time at next scr refresh
                    GA.setAutoDraw(True)
                if GA.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > GA.tStartRefresh + float(expInfo["stimulus duration"])-frameTolerance:
                        # keep track of stop time/frame for later
                        GA.tStop = t  # not accounting for scr refresh
                        GA.frameNStop = frameN  # exact frame index
                        GA.setAutoDraw(False)
                print("aperture starting")
    # *aperture* updates
                if aperture.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    aperture.frameNStart = frameN  # exact frame index
                    aperture.tStart = t  # local t and not account for scr refresh
                    aperture.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(aperture, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'aperture.started')
                    aperture.enabled = True
                if aperture.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > aperture.tStartRefresh + float(expInfo["stimulus duration"])-frameTolerance:
                        # keep track of stop time/frame for later
                        aperture.tStop = t  # not accounting for scr refresh
                        aperture.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'aperture.stopped')
                        aperture.enabled = False
                if(rep==0):
                    print("gaze detection")
                    while (ret) and (frame_count<buffer_size):
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
                    print(answers)
                    print(confidences)
                    rep+=1
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in grating_acuityComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "grating_acuity" ---
            for thisComponent in grating_acuityComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('position.routineEndVal', position)  # Save end routine value
            aperture.enabled = False  # just in case it was left enabled
            # the Routine "grating_acuity" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "central_fixation" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # keep track of which components have finished
            central_fixationComponents = [placeholder]
            for thisComponent in central_fixationComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "central_fixation" ---
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *placeholder* updates
                if placeholder.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    placeholder.frameNStart = frameN  # exact frame index
                    placeholder.tStart = t  # local t and not account for scr refresh
                    placeholder.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(placeholder, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'placeholder.started')
                    placeholder.setAutoDraw(True)
                if placeholder.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > placeholder.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        placeholder.tStop = t  # not accounting for scr refresh
                        placeholder.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'placeholder.stopped')
                        placeholder.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in central_fixationComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "central_fixation" ---
            for thisComponent in central_fixationComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            thisExp.nextEntry()
            
        # completed 4.0 repeats of 'trials'
        
    # completed (float(expInfo['end contrast'])-float(expInfo['start contrast']))//float(expInfo['step contrast']) repeats of 'GA_loop'


    # --- End experiment ---
    # Flip one final time so any remaining win.callOnFlip() 
    # and win.timeOnFlip() tasks get executed before quitting
    win.flip()
    cap.release()
    cv2.destroyAllWindows()
    

    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename+'.csv', delim='auto')
    thisExp.saveAsPickle(filename)
    logging.flush()
    # make sure everything is closed down
    if eyetracker:
        eyetracker.setConnectionState(False)
    thisExp.abort()  # or data files will save again on exit
    win.close()

    # input=f"{output_path} --output_video_path {_thisDir}"
    
    return input
# main(input)
# core.quit()