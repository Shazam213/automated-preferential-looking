#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on May 02, 2023, at 09:42
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import  gui, visual, core, data, event, logging, clock, colors, layout
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
import matplotlib.pyplot as plt
from psychometric_function import *
import random


# Run 'Before Experiment' code from code_3
#if opt==1 or opt==3:
#    pos=(randchoice([-1, 1])*16,0)
#else:
#    pos= (randchoice([-1, 1])*16,randchoice([-1, 1])*8)

def fixedincrement(response, min, max, fixed):
    # Ensure that relative paths start from the same directory as this script
    _thisDir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(_thisDir)
    # Store info about the experiment session
    psychopyVersion = '2022.2.5'
    expName = 'stimuli3'  # from the Builder filename that created this script
    expInfo = {
        'participant': f"{randint(0, 999999):06.0f}",
        'session': '001',
        'stimulus duration': '0.1',
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
        originPath='C:\\Users\\soham\\Desktop\\automated-preferential-looking\\stimuli3.py',
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
        winType='pyglet', allowStencil=False,
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
    defaultKeyboard = keyboard.Keyboard(backend='iohub')

    # --- Initialize components for Routine "start_exp" ---
    # text = visual.TextStim(win=win, name='text',
    #     text='Welcome to visual stimuli.\nContrast Sensitivity Experiments:\nPress 1 for stimulus in two hemiscreens.\nPress 2 for stimulus in four quadrants.\nSpatial Frequency Sensitivity Experiments:\nPress 3 for stimulus in two hemiscreens.\nPress 4 for stimulus in four quadrants.\n\n',
    #     font='Open Sans',
    #     pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    #     color='white', colorSpace='rgb', opacity=None, 
    #     languageStyle='LTR',
    #     depth=0.0);
    # option_resp = keyboard.Keyboard()

    # --- Initialize components for Routine "start_opt" ---
    if response=='1' or response=='3':
        text_2 = visual.TextStim(win=win, name='text_2',
            text="Press spacebar to start the experiment\n\nUse the 'j','k' keys to point to respective directions of the stimuli",
            font='Open Sans',
            pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
            color='white', colorSpace='rgb', opacity=None, 
            languageStyle='LTR',
            depth=0.0);
        key_resp = keyboard.Keyboard()
    else:
        text_2 = visual.TextStim(win=win, name='text_2',
            text="Press spacebar to start the experiment\n\nUse the 'u','i','j','k' keys to point to respective directions of the stimuli",
            font='Open Sans',
            pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
            color='white', colorSpace='rgb', opacity=None, 
            languageStyle='LTR',
            depth=0.0);
        key_resp = keyboard.Keyboard()

    # --- Initialize components for Routine "set_values" ---
    # Set experiment start values for variable component contrast
    if response=='1':
        opt=1
        contrast_values = np.logspace(np.log10(float(min)), np.log10(float(max)), num=19)
        contrast_values=contrast_values.tolist()
        contrast_dict={}
        pos_choices = [(-16, 0), (16, 0),(-16, 0), (16, 0)]
        for element in contrast_values:
            random.shuffle(pos_choices)
            contrast_dict[element] = pos_choices[:]
        contrast_values=contrast_values*4
        random.shuffle(contrast_values)
        contrastContainer = []
    # Set experiment start values for variable component spatial
        spatial = float(fixed)
        spatialContainer = []
        # left_max= len(contrast_values)/2
        # right_max=left_max
        # contrast_values2=contrast_values[:]
    elif  response=='2':
        opt=2
        contrast_values = np.logspace(np.log10(float(min)), np.log10(float(max)), num=19)
        contrast_values=contrast_values.tolist()
        contrast_dict={}
        pos_choices = [(-16, 8), (16, -8),(-16, -8), (16, 8)]
        for element in contrast_values:
            random.shuffle(pos_choices)
            contrast_dict[element] = pos_choices[:]
        contrast_values=contrast_values*4
        random.shuffle(contrast_values)
        contrastContainer = []
    # Set experiment start values for variable component spatial
        spatial = float(fixed)
        spatialContainer = []
        # left_max= len(contrast_values)/2
        # right_max=left_max
        # contrast_values2=contrast_values[:]
    elif  response=='3':
        opt=3
        spatial_values = np.logspace(np.log10(float(min)), np.log10(float(max)), num=19)
        spatial_values=spatial_values.tolist()
        spatial_dict={}
        pos_choices = [(-16, 0), (16, 0),(-16, 0), (16, 0)]
        for element in spatial_values:
            random.shuffle(pos_choices)
            contrast_dict[element] = pos_choices[:]
        spatial_values=spatial_values*4
        random.shuffle(spatial_values)
        contrastContainer = []
    # Set experiment start values for variable component spatial
        contrast = float(fixed)
        spatialContainer = []
        # left_max= len(spatial_values)/2
        # right_max=left_max
        # spatial_values2=spatial_values[:]
    else:
        opt=4
        spatial_values = np.logspace(np.log10(float(min)), np.log10(float(max)), num=19)
        spatial_values=spatial_values.tolist()
        spatial_dict={}
        pos_choices = [(-16, 8), (16, -8),(-16, -8), (16, 8)]
        for element in spatial_values:
            random.shuffle(pos_choices)
            contrast_dict[element] = pos_choices[:]
        spatial_values=spatial_values*4
        random.shuffle(spatial_values)
        contrastContainer = []
    # Set experiment start values for variable component spatial
        contrast = float(fixed)
        spatialContainer = []
        # left_max= len(spatial_values)/2
        # right_max=left_max
        # spatial_values2=spatial_values[:]


    # --- Initialize components for Routine "grating_acuity" ---
    # Set experiment start values for variable component position
    position = (0, 0)
    positionContainer = []
    GA = visual.GratingStim(
        win=win, name='GA',units='deg', 
        tex='sqr', mask='circle', anchor='center',
        ori=0.0, pos=[0,0], size=[8.5], sf=1.0, phase=0.0,
        color=[1,1,1], colorSpace='rgb',
        opacity=None, contrast=1.0, blendmode='avg',
        texRes=512.0, interpolate=True, depth=-2.0)
    polygon = visual.ShapeStim(
        win=win, name='polygon',
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=[1.0000, -1.0000, -1.0000],
        opacity=None, depth=-3.0, interpolate=True)
    text_3 = visual.TextStim(win=win, name='text_3',
        text='',
        font='Open Sans',
        pos=(0,0.125), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);

    # --- Initialize components for Routine "central_fixation" ---
    key_resp_2 = keyboard.Keyboard()
    polygon_2 = visual.ShapeStim(
        win=win, name='polygon_2',
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=[1.0000, -1.0000, -1.0000],
        opacity=None, depth=-2.0, interpolate=True)
    text_4 = visual.TextStim(win=win, name='text_4',
        text='',
        font='Open Sans',
        pos=(0,0.125), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);

    # --- Initialize components for Routine "delay" ---
    polygon_3 = visual.ShapeStim(
        win=win, name='polygon_3',
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[1.0000, -1.0000, -1.0000], fillColor=[1.0000, -1.0000, -1.0000],
        opacity=None, depth=0.0, interpolate=True)

    # Create some handy timers
    globalClock = core.Clock()  # to track the time since experiment started
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

    # --- Prepare to start Routine "start_exp" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # option_resp.keys = []
    # option_resp.rt = []
    # _option_resp_allKeys = []
    # # keep track of which components have finished
    # start_expComponents = [text, option_resp]
    # for thisComponent in start_expComponents:
    #     thisComponent.tStart = None
    #     thisComponent.tStop = None
    #     thisComponent.tStartRefresh = None
    #     thisComponent.tStopRefresh = None
    #     if hasattr(thisComponent, 'status'):
    #         thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1

    # --- Run Routine "start_exp" ---
    # while continueRoutine:
    #     # get current time
    #     t = routineTimer.getTime()
    #     tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    #     tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    #     frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    #     # update/draw components on each frame
        
    #     # *text* updates
    #     if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
    #         # keep track of start time/frame for later
    #         text.frameNStart = frameN  # exact frame index
    #         text.tStart = t  # local t and not account for scr refresh
    #         text.tStartRefresh = tThisFlipGlobal  # on global time
    #         win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
    #         # add timestamp to datafile
    #         thisExp.timestampOnFlip(win, 'text.started')
    #         text.setAutoDraw(True)
        
    #     # *option_resp* updates
    #     waitOnFlip = False
    #     if option_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
    #         # keep track of start time/frame for later
    #         option_resp.frameNStart = frameN  # exact frame index
    #         option_resp.tStart = t  # local t and not account for scr refresh
    #         option_resp.tStartRefresh = tThisFlipGlobal  # on global time
    #         win.timeOnFlip(option_resp, 'tStartRefresh')  # time at next scr refresh
    #         # add timestamp to datafile
    #         thisExp.timestampOnFlip(win, 'option_resp.started')
    #         option_resp.status = STARTED
    #         # keyboard checking is just starting
    #         waitOnFlip = True
    #         win.callOnFlip(option_resp.clock.reset)  # t=0 on next screen flip
    #         win.callOnFlip(option_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    #     if option_resp.status == STARTED and not waitOnFlip:
    #         theseKeys = option_resp.getKeys(keyList=['1','2','3','4'], waitRelease=False)
    #         _option_resp_allKeys.extend(theseKeys)
    #         if len(_option_resp_allKeys):
    #             option_resp.keys = _option_resp_allKeys[-1].name  # just the last key pressed
    #             option_resp.rt = _option_resp_allKeys[-1].rt
    #             # a response ends the routine
    #             continueRoutine = False
        
    #     # check for quit (typically the Esc key)
    #     if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
    #         core.quit()
        
    #     # check if all components have finished
    #     if not continueRoutine:  # a component has requested a forced-end of Routine
    #         routineForceEnded = True
    #         break
    #     continueRoutine = False  # will revert to True if at least one component still running
    #     for thisComponent in start_expComponents:
    #         if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
    #             continueRoutine = True
    #             break  # at least one component has not yet finished
        
    #     # refresh the screen
    #     if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
    #         win.flip()

    # # --- Ending Routine "start_exp" ---
    # for thisComponent in start_expComponents:
    #     if hasattr(thisComponent, "setAutoDraw"):
    #         thisComponent.setAutoDraw(False)
    # # check responses
    # if option_resp.keys in ['', [], None]:  # No response was made
    #     option_resp.keys = None
    # thisExp.addData('option_resp.keys',option_resp.keys)
    # if option_resp.keys != None:  # we had a response
    #     thisExp.addData('option_resp.rt', option_resp.rt)
    # thisExp.nextEntry()
    # Run 'End Routine' code from code_4
    # if response== '1':
    #     opt=1
    #     pos_choices = [(-16, 0), (16, 0),(-16, 0), (16, 0)]
    #     for key in contrast_dict:
    #         contrast_dict[key]=random.shuffle(pos_choices) 
         
    # # start_contrast=float(expInfo['start contrast'])
    # #   start_spatial=0.5
    # elif response== '2':
    #     opt=2
    #     pos_choices = [(-16, 8), (16, -8),(-16, -8), (16, 8)]
    #     for key in contrast_dict:
    #         contrast_dict[key]=random.shuffle(pos_choices)  
    # #   start_contrast=float(expInfo['start contrast'])
    # #   start_spatial=0.5
    # elif response== '3':
    #     opt=3
    #     pos_choices = [(-16, 0), (16, 0),(-16, 0), (16, 0)]
    #     for key in spatial_dict:
    #         spatial_dict[key]=random.shuffle(pos_choices) 
    # #    start_spatial=float(expInfo['start spatial freq'])
    # #    start_contrast=1
    # elif response== '4':
    #     opt=4
    #     pos_choices = [(-16, 8), (16, -8),(-16, -8), (16, 8)]
    #     for key in spatial_dict:
    #         spatial_dict[key]=random.shuffle(pos_choices)  

    #    start_spatial=float(expInfo['start spatial freq'])
    #    start_contrast=1
    # the Routine "start_exp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    feedback={}
    # value=[]
    # --- Prepare to start Routine "start_opt" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    start_optComponents = [text_2, key_resp]
    for thisComponent in start_optComponents:
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

    # --- Run Routine "start_opt" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.started')
            text_2.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in start_optComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # --- Ending Routine "start_opt" ---
    for thisComponent in start_optComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    thisExp.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        thisExp.addData('key_resp.rt', key_resp.rt)
    thisExp.nextEntry()
    # the Routine "start_opt" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # set up handler to look after randomisation of conditions etc
    ga_loop = data.TrialHandler(nReps=19.0*4, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='ga_loop')
    thisExp.addLoop(ga_loop)  # add the loop to the experiment
    thisGa_loop = ga_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisGa_loop.rgb)
    if thisGa_loop != None:
        for paramName in thisGa_loop:
            exec('{} = thisGa_loop[paramName]'.format(paramName))

    for thisGa_loop in ga_loop:
        currentLoop = ga_loop
        # abbreviate parameter names if possible (e.g. rgb = thisGa_loop.rgb)
        if thisGa_loop != None:
            for paramName in thisGa_loop:
                exec('{} = thisGa_loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "set_values" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_2
        
        if opt==1:
            contrast= float(contrast_values.pop())    
            # value.append(contrast)
            spatial=float(fixed)
        elif opt==2:
            contrast= float(contrast_values.pop())
            # value.append(contrast)
            spatial=float(fixed)
        elif opt==3:
            spatial= float(spatial_values.pop())
            # value.append(spatial)
            contrast= float(fixed)
        elif opt==4:
            spatial= float(spatial_values.pop())
            # value.append(spatial)
            contrast= float(fixed)
        
        # contrast = contrast  # Set routine start values for contrast
        # spatial = spatial  # Set routine start values for spatial
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
        thisExp.addData('spatial.routineEndVal', spatial)  # Save end routine value
        # the Routine "set_values" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        psychometric_func = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='psychometric_func')
        thisExp.addLoop(psychometric_func)  # add the loop to the experiment
        thisPsychometric_func = psychometric_func.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisPsychometric_func.rgb)
        if thisPsychometric_func != None:
            for paramName in thisPsychometric_func:
                exec('{} = thisPsychometric_func[paramName]'.format(paramName))
 

        for thisPsychometric_func in psychometric_func:
            currentLoop = psychometric_func
            # abbreviate parameter names if possible (e.g. rgb = thisPsychometric_func.rgb)
            if thisPsychometric_func != None:
                for paramName in thisPsychometric_func:
                    exec('{} = thisPsychometric_func[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "grating_acuity" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from code_3
            if opt==1 or opt==2:
                pos_list=[]
                pos_list = contrast_dict[contrast]
                pos = pos_list.pop()
                contrast_dict[contrast]=pos_list
                # pos=pos_choices.pop()
            else:
                pos_list=[]
                pos_list = spatial_dict[spatial]
                pos = pos_list.pop()
                spatial_dict[spatial]=pos_list
                # pos=pos_choices.pop()
            
            position = pos  # Set routine start values for position
            GA.setContrast(contrast)
            GA.setPos(position)
            GA.setSF(spatial)
            text_3.setText("Spatial frequency: " +  f'{spatial:.3f}'+"\n"+"Contrast: "+ f'{contrast:.3f}'
    )
            # keep track of which components have finished
            grating_acuityComponents = [GA, polygon, text_3]
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
            
            # --- Run Routine "grating_acuity" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *GA* updates
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
                
                # *polygon* updates
                if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    polygon.frameNStart = frameN  # exact frame index
                    polygon.tStart = t  # local t and not account for scr refresh
                    polygon.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon.started')
                    polygon.setAutoDraw(True)
                if polygon.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > polygon.tStartRefresh + float(expInfo["stimulus duration"])-frameTolerance:
                        # keep track of stop time/frame for later
                        polygon.tStop = t  # not accounting for scr refresh
                        polygon.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'polygon.stopped')
                        polygon.setAutoDraw(False)
                
                # *text_3* updates
                if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_3.frameNStart = frameN  # exact frame index
                    text_3.tStart = t  # local t and not account for scr refresh
                    text_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_3.started')
                    text_3.setAutoDraw(True)
                if text_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_3.tStartRefresh + float(expInfo["stimulus duration"])-frameTolerance:
                        # keep track of stop time/frame for later
                        text_3.tStop = t  # not accounting for scr refresh
                        text_3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_3.stopped')
                        text_3.setAutoDraw(False)
                
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
            # the Routine "grating_acuity" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "central_fixation" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            key_resp_2.keys = []
            key_resp_2.rt = []
            _key_resp_2_allKeys = []
            

            # Run 'Begin Routine' code from code
            
            if (opt==1 or opt==3) and (position==(-16,0)):
                b='j'
            elif (opt==1 or opt==3) and (position==(16,0)):
                b='k'
            elif (opt==2 or opt==4) and (position==(-16,-8) ):
                b='j'
            elif (opt==2 or opt==4) and (position==(-16,8) ):
                b='u'
            elif (opt==2 or opt==4) and (position==(16,-8) ):
                b='k'
            elif (opt==2 or opt==4) and (position==(16,8) ):
                b='i'    
            text_4.setText("Spatial frequency: " +  f'{spatial:.3f}'+"\n"+"Contrast: "+ f'{contrast:.3f}'
    )
            # keep track of which components have finished
            central_fixationComponents = [GA,key_resp_2, polygon_2, text_4]
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
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *key_resp_2* updates
                waitOnFlip = False
                if GA.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    GA.frameNStart = frameN  # exact frame index
                    GA.tStart = t  # local t and not account for scr refresh
                    GA.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(GA, 'tStartRefresh')  # time at next scr refresh
                    GA.setAutoDraw(True)
                if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_2.frameNStart = frameN  # exact frame index
                    key_resp_2.tStart = t  # local t and not account for scr refresh
                    key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_2.started')
                    key_resp_2.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_2.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_2.getKeys(keyList=['u','i','j','k'], waitRelease=False)
                    _key_resp_2_allKeys.extend(theseKeys)
                    if len(_key_resp_2_allKeys):
                        key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                        key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                        # was this correct?
                        if (key_resp_2.keys == str(b)) or (key_resp_2.keys == b):
                            key_resp_2.corr = 1
                        else:
                            key_resp_2.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                

                # *polygon_2* updates
                if polygon_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    polygon_2.frameNStart = frameN  # exact frame index
                    polygon_2.tStart = t  # local t and not account for scr refresh
                    polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon_2.started')
                    polygon_2.setAutoDraw(True)
                
                # *text_4* updates
                if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_4.frameNStart = frameN  # exact frame index
                    text_4.tStart = t  # local t and not account for scr refresh
                    text_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_4.started')
                    text_4.setAutoDraw(True)
                
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
            # check responses
            if key_resp_2.keys in ['', [], None]:  # No response was made
                key_resp_2.keys = None
                # was no response the correct answer?!
                if str(b).lower() == 'none':
                    key_resp_2.corr = 1;  # correct non-response
                else:
                    key_resp_2.corr = 0;  # failed to respond (incorrectly)
            # store data for psychometric_func (TrialHandler)
            psychometric_func.addData('key_resp_2.keys',key_resp_2.keys)
            psychometric_func.addData('key_resp_2.corr', key_resp_2.corr)
            if opt=='1' or opt=='2':
                if contrast in feedback:
                    feedback[contrast].append(key_resp_2.corr)  # Append the new value to the existing list
                else:
                    feedback[contrast] = [key_resp_2.corr]
            else:
                if spatial in feedback:
                    feedback[spatial].append(key_resp_2.corr)  # Append the new value to the existing list
                else:
                    feedback[spatial] = [key_resp_2.corr]
            if key_resp_2.keys != None:  # we had a response
                psychometric_func.addData('key_resp_2.rt', key_resp_2.rt)
            # the Routine "central_fixation" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "delay" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # keep track of which components have finished
            delayComponents = [polygon_3]
            for thisComponent in delayComponents:
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
            
            # --- Run Routine "delay" ---
            while continueRoutine and routineTimer.getTime() < 0.5:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *polygon_3* updates
                if polygon_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    polygon_3.frameNStart = frameN  # exact frame index
                    polygon_3.tStart = t  # local t and not account for scr refresh
                    polygon_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(polygon_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon_3.started')
                    polygon_3.setAutoDraw(True)
                if polygon_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > polygon_3.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        polygon_3.tStop = t  # not accounting for scr refresh
                        polygon_3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'polygon_3.stopped')
                        polygon_3.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in delayComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "delay" ---
            for thisComponent in delayComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.500000)
            thisExp.nextEntry()
            
        # completed 4.0 repeats of 'psychometric_func'
        
        thisExp.nextEntry()
        
    # completed 19.0 repeats of 'ga_loop'


    # --- End experiment ---
    # Flip one final time so any remaining win.callOnFlip() 
    # and win.timeOnFlip() tasks get executed before quitting
    win.flip()
    percent_corr=[]
    #reversing the feedback list as we get the values in reverse order due to pop()
    
    if response=='1' or response=='2':
        for contrast in feedback:
            feedback[contrast]= sum(feedback[contrast])/len(feedback[contrast])
    else:
        for spatial in feedback:
            feedback[spatial]= sum(feedback[spatial])/len(feedback[spatial])

    # for i in range(0,len(feedback),4):
    #     percent_corr.append((feedback[i]+feedback[i+1]+feedback[i+2]+feedback[i+3])/4)
    feedback_key = list(feedback.keys())
    feedback_value = list(feedback.values())
    # psychometric_function(percent_corr,value,response)
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename+'.csv', delim='auto')
    thisExp.saveAsPickle(filename)
    logging.flush()
    # make sure everything is closed down
    if eyetracker:
        eyetracker.setConnectionState(False)
    thisExp.abort()  # or data files will save again on exit
    win.close()
    return feedback_value,feedback_key,response
    
    # core.quit()
    
    # return value,feedback,response
