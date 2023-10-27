#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on May 02, 2023, at 09:41
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from predict import *
import cv2
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
import platform


def staircase_icatcher(response, str_contrast, str_spatial):
    # Ensure that relative paths start from the same directory as this script
    os_name = platform.system()
    _thisDir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(_thisDir)
    # Store info about the experiment session
    psychopyVersion = '2022.2.5'
    expName = 'stimuli4'  # from the Builder filename that created this script
    expInfo = {
        'participant': f"{randint(0, 999999):06.0f}",
        'session': '001',
        'stimulus duration': '3',
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
        originPath='C:\\Users\\soham\\Desktop\\automated-preferential-looking\\stimuli4.py',
        savePickle=True, saveWideText=True,
        dataFileName=filename)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    frameTolerance = 0.001  # how close to onset before 'same' frame
    cap = cv2.VideoCapture(0)

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
   
    feedback={}
    value=[]
    # create a default keyboard (e.g. to check for escape)
    if os_name == "Windows" or os_name == "Linux" :
         # --- Setup input devices ---
        ioConfig = {}
        # Setup iohub keyboard
        ioConfig['Keyboard'] = dict(use_keymap='psychopy')

        ioSession = '1'
        if 'session' in expInfo:
            ioSession = str(expInfo['session'])
        ioServer = io.launchHubServer(window=win, **ioConfig)
        eyetracker = None
        defaultKeyboard = keyboard.Keyboard(backend='iohub')
    else:
        ioConfig = {}
        ioSession = ioServer = eyetracker = None
        # create a default keyboard (e.g. to check for escape)
        defaultKeyboard = keyboard.Keyboard(backend='ptb')
   

    # --- Initialize components for Routine "start_opt" ---
    if response=='1' or response=='3':
        text_2 = visual.TextStim(win=win, name='text_2',
            text="Press spacebar to start the experiment\n\n",
            font='Open Sans',
            pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
            color='white', colorSpace='rgb', opacity=None, 
            languageStyle='LTR',
            depth=0.0);
        key_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "grating_acuity" ---
    # Set experiment start values for variable component position
    position = (0, 0)
    positionContainer = []
    GA = visual.GratingStim(
        win=win, name='GA',units='deg', 
        tex='sqr', mask='circle', anchor='center',
        ori=0.0, pos=[0,0], size=[8.5], sf=float(str_spatial), phase=0.0,
        color=[1,1,1], colorSpace='rgb',
        opacity=None, contrast=1.0, blendmode='avg',
        texRes=512.0, interpolate=True, depth=-2.0)
    polygon = visual.ShapeStim(
        win=win, name='polygon',
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.0000, 0.0000, 0.0000], fillColor=[0.0000, 0.0000, 0.0000],
        opacity=None, depth=-3.0, interpolate=True)
    text_3 = visual.TextStim(win=win, name='text_3',
        text='',
        font='Open Sans',
        pos=(0,0.125), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);

    # --- Initialize components for Routine "central_fixation" ---
    
    polygon_2 = visual.ShapeStim(
        win=win, name='polygon_2',
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.0000, 0.0000, 0.0000], fillColor=[0.0000, 0.0000, 0.0000],
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
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.0000, 0.0000, 0.0000], fillColor=[0.0000, 0.0000, 0.0000],
        opacity=None, depth=0.0, interpolate=True)

    # --- Initialize components for Routine "grating_acuity_2" ---
    # Set experiment start values for variable component position_2
    position_2 = (0, 0)
    position_2Container = []
    GA_2 = visual.GratingStim(
        win=win, name='GA_2',units='deg', 
        tex='sqr', mask='circle', anchor='center',
        ori=0.0, pos=[0,0], size=[8.5], sf=1.0, phase=0.0,
        color=[1,1,1], colorSpace='rgb',
        opacity=None, contrast=1.0, blendmode='avg',
        texRes=512.0, interpolate=True, depth=-2.0)
    polygon_4 = visual.ShapeStim(
        win=win, name='polygon_4',
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.0000, 0.0000, 0.0000], fillColor=[0.0000, 0.0000, 0.0000],
        opacity=None, depth=-3.0, interpolate=True)
    text_5 = visual.TextStim(win=win, name='text_5',
        text='',
        font='Open Sans',
        pos=(0,0.125), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);

    # --- Initialize components for Routine "central_fixation_2" ---

    polygon_5 = visual.ShapeStim(
        win=win, name='polygon_5',
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.0000, 0.0000, 0.0000], fillColor=[0.0000, 0.0000, 0.0000],
        opacity=None, depth=-2.0, interpolate=True)
    text_6 = visual.TextStim(win=win, name='text_6',
        text='',
        font='Open Sans',
        pos=(0,0.125), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);

    # --- Initialize components for Routine "delay_2" ---
    polygon_6 = visual.ShapeStim(
        win=win, name='polygon_6',
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.0000, 0.0000, 0.0000], fillColor=[0.0000, 0.0000, 0.0000],
        opacity=None, depth=0.0, interpolate=True)

    # Create some handy timers
    globalClock = core.Clock()  # to track the time since experiment started
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

    # --- Prepare to start Routine "start_exp" ---
    continueRoutine = True
    routineForceEnded = False
   
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1

   
    # Run 'End Routine' code from code_4
    if response== '1':
        opt=1
        opt1=1
        opt2=0
    
    elif response== '3':
        opt=3
        opt1=0
        opt2=1
   
    # the Routine "start_exp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

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
    opt1 = data.TrialHandler(nReps=opt1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='opt1')
    thisExp.addLoop(opt1)  # add the loop to the experiment
    thisOpt1 = opt1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisOpt1.rgb)
    if thisOpt1 != None:
        for paramName in thisOpt1:
            exec('{} = thisOpt1[paramName]'.format(paramName))

    for thisOpt1 in opt1:
        currentLoop = opt1
        # abbreviate parameter names if possible (e.g. rgb = thisOpt1.rgb)
        if thisOpt1 != None:
            for paramName in thisOpt1:
                exec('{} = thisOpt1[paramName]'.format(paramName))
        
        # --------Prepare to start Staircase "staircase_loop" --------
        # set up handler to look after next chosen value etc
        staircase_loop = data.StairHandler(startVal=float(str_contrast), extraInfo=expInfo,
            stepSizes=[0.005], stepType='lin',
            nReversals=1.0, nTrials=20.0, 
            nUp=2.0, nDown=1.0,
            minVal=0.02, maxVal=1.0,
            originPath=-1, name='staircase_loop')
        thisExp.addLoop(staircase_loop)  # add the loop to the experiment
        level = thisStaircase_loop = float(str_contrast)  # initialise some vals
        
        for thisStaircase_loop in staircase_loop:
            currentLoop = staircase_loop
            level = thisStaircase_loop
            if level==0.02 and min_count==5:
                break
            elif level==0.02 and min_count<5:
                min_count+=1
            # --- Prepare to start Routine "grating_acuity" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from code_3
            if opt==1 :
                pos=(randchoice([-1, 1])*16,0)
            
            position = pos  # Set routine start values for position

            GA.setContrast(level)
            GA.setPos(position)
            text_3.setText("Spatial frequency: " +  str(float(str_spatial))+"\n"+"Contrast: "+ f'{level:.3f}')
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
            
            # --- Prepare to start Routine "central_fixation" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from code
            
            if (opt==1 or opt==3) and (position==(-16,0)):
                b=1
            elif (opt==1 or opt==3) and (position==(16,0)):
                b=2
            
            
            text_4.setText("Spatial frequency: " +  str(float(str_spatial))+"\n"+"Contrast: "+ f'{level:.3f}'
    )
            # keep track of which components have finished
            central_fixationComponents = [GA, polygon_2, text_4]
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
            rep=0
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
                if GA.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > GA.tStartRefresh + float(expInfo["stimulus duration"])-frameTolerance:
                        # keep track of stop time/frame for later
                        GA.tStop = t  # not accounting for scr refresh
                        GA.frameNStop = frameN  # exact frame index
                        GA.setAutoDraw(False)
                
                
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
                if polygon_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > polygon_2.tStartRefresh + float(expInfo["stimulus duration"])-frameTolerance:
                        # keep track of stop time/frame for later
                        polygon_2.tStop = t  # not accounting for scr refresh
                        polygon_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'polygon_2.stopped')
                        polygon_2.setAutoDraw(False)
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
                if text_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_4.tStartRefresh + float(expInfo["stimulus duration"])-frameTolerance:
                        # keep track of stop time/frame for later
                        text_4.tStop = t  # not accounting for scr refresh
                        text_4.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_4.stopped')
                        text_4.setAutoDraw(False)
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                if(rep==0):
                    print("gaze detection")
                    answers,confidences,frames= predict_from_frame(cap)
                    print(answers)
                    print(confidences)
                    # print(frames)
                    if answers[np.argmax(confidences)]==b:
                        correct = 1  # correct non-response
                    else:
                        correct = 0
                    rep+=1
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
         
            staircase_loop.addResponse(correct, level)
            # feedback.append(key_resp_2.corr)
            # value.append(level)
            if level in feedback:
                feedback[level].append(correct)  # Append the new value to the existing list
            else:
                feedback[level] = [correct]
            # staircase_loop.addOtherData('key_resp_2.rt', correct)
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
            
        # staircase completed
    
        thisExp.nextEntry()
     
    # completed opt1 repeats of 'opt1'


    # set up handler to look after randomisation of conditions etc
    opt2 = data.TrialHandler(nReps=opt2, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='opt2')
    thisExp.addLoop(opt2)  # add the loop to the experiment
    thisOpt2 = opt2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisOpt2.rgb)
    if thisOpt2 != None:
        for paramName in thisOpt2:
            exec('{} = thisOpt2[paramName]'.format(paramName))

    for thisOpt2 in opt2:
        currentLoop = opt2
        # abbreviate parameter names if possible (e.g. rgb = thisOpt2.rgb)
        if thisOpt2 != None:
            for paramName in thisOpt2:
                exec('{} = thisOpt2[paramName]'.format(paramName))
        
        # --------Prepare to start Staircase "staircase_loop2" --------
        # set up handler to look after next chosen value etc
        staircase_loop2 = data.StairHandler(startVal=float(str_spatial), extraInfo=expInfo,
            stepSizes=[0.05], stepType='lin',
            nReversals=1.0, nTrials=20.0, 
            nUp=2.0, nDown=1.0,
            minVal=0.2, maxVal=5.0,
            originPath=-1, name='staircase_loop2')
        thisExp.addLoop(staircase_loop2)  # add the loop to the experiment
        level = thisStaircase_loop2 = float(str_spatial)  # initialise some vals
        maxval=5.0
        for thisStaircase_loop2 in staircase_loop2:
            currentLoop = staircase_loop2
            level = maxval-thisStaircase_loop2
            if level==0.2 and min_count==5:
                break
            elif level==0.2 and min_count<5:
                min_count+=1
            # --- Prepare to start Routine "grating_acuity_2" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from code_5
            if  opt==3:
                pos=(randchoice([-1, 1])*16,0)
            elif opt==4:
                pos= (randchoice([-1, 1])*16,randchoice([-1, 1])*8)
            position_2 = pos  # Set routine start values for position_2
            GA_2.setContrast(float(str_contrast))
            GA_2.setPos(position_2)
            GA_2.setSF(level)
            text_5.setText("Spatial frequency: " + f'{level:.3f}' +"\n"+"Contrast: "+str(float(str_contrast)) 
    )
            # keep track of which components have finished
            grating_acuity_2Components = [GA_2, polygon_4, text_5]
            for thisComponent in grating_acuity_2Components:
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
        
            # --- Prepare to start Routine "central_fixation_2" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from code_6
            
            if (opt==3) and (position_2==(-16,0)):
                b=1
            elif (opt==3) and (position_2==(16,0)):
                b=2

            text_6.setText("Spatial frequency: " + f'{level:.3f}' +"\n"+"Contrast: "+str(float(str_contrast)) 
    )
            # keep track of which components have finished
            central_fixation_2Components = [GA_2, polygon_5, text_6]
            for thisComponent in central_fixation_2Components:
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
            # --- Run Routine "central_fixation_2" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *key_resp_3* updates
                waitOnFlip = False
                if GA_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    GA_2.frameNStart = frameN  # exact frame index
                    GA_2.tStart = t  # local t and not account for scr refresh
                    GA_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(GA_2, 'tStartRefresh')  # time at next scr refresh
                    GA_2.setAutoDraw(True)
                if GA_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > GA_2.tStartRefresh + float(expInfo["stimulus duration"])-frameTolerance:
                        # keep track of stop time/frame for later
                        GA_2.tStop = t  # not accounting for scr refresh
                        GA_2.frameNStop = frameN  # exact frame index
                        GA_2.setAutoDraw(False)    
 
                # *polygon_5* updates
                if polygon_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    polygon_5.frameNStart = frameN  # exact frame index
                    polygon_5.tStart = t  # local t and not account for scr refresh
                    polygon_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(polygon_5, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon_5.started')
                    polygon_5.setAutoDraw(True)
                if polygon_5.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > polygon_5.tStartRefresh + float(expInfo["stimulus duration"])-frameTolerance:
                        # keep track of stop time/frame for later
                        polygon_5.tStop = t  # not accounting for scr refresh
                        polygon_5.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'polygon_5.stopped')
                        polygon_5.setAutoDraw(False)
                # *text_6* updates
                if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_6.frameNStart = frameN  # exact frame index
                    text_6.tStart = t  # local t and not account for scr refresh
                    text_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_6.started')
                    text_6.setAutoDraw(True)
                if text_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_6.tStartRefresh + float(expInfo["stimulus duration"])-frameTolerance:
                        # keep track of stop time/frame for later
                        text_6.tStop = t  # not accounting for scr refresh
                        text_6.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_6.stopped')
                        text_6.setAutoDraw(False)
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in central_fixation_2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
                if(rep==0):
                    print("gaze detection")
                    answers,confidences,frames= predict_from_frame(cap)
                    print(answers)
                    print(confidences)
                    # print(frames)
                    if answers[np.argmax(confidences)]==b:
                        correct = 1  # correct non-response
                    else:
                        correct = 0
                    rep+=1
            # --- Ending Routine "central_fixation_2" ---
            for thisComponent in central_fixation_2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
    
            staircase_loop2.addResponse(correct, level)
            if level in feedback:
                feedback[level].append(correct)  # Append the new value to the existing list
            else:
                feedback[level] = [correct]
            staircase_loop2.addOtherData('key_resp_3.rt', '')
            # the Routine "central_fixation_2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "delay_2" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # keep track of which components have finished
            delay_2Components = [polygon_6]
            for thisComponent in delay_2Components:
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
            
            # --- Run Routine "delay_2" ---
            while continueRoutine and routineTimer.getTime() < 0.5:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *polygon_6* updates
                if polygon_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    polygon_6.frameNStart = frameN  # exact frame index
                    polygon_6.tStart = t  # local t and not account for scr refresh
                    polygon_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(polygon_6, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon_6.started')
                    polygon_6.setAutoDraw(True)
                if polygon_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > polygon_6.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        polygon_6.tStop = t  # not accounting for scr refresh
                        polygon_6.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'polygon_6.stopped')
                        polygon_6.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in delay_2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "delay_2" ---
            for thisComponent in delay_2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.500000)
            thisExp.nextEntry()
            
        # staircase completed
        
        thisExp.nextEntry()
    
    # completed opt2 repeats of 'opt2'
    for level in feedback:
        feedback[level]= sum(feedback[level])/len(feedback[level])

    feedback_key = list(feedback.keys())
    feedback_value = list(feedback.values())
    # --- End experiment ---
    # Flip one final time so any remaining win.callOnFlip() 
    # and win.timeOnFlip() tasks get executed before quitting
    win.flip()

    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename+'.csv', delim='auto')
    thisExp.saveAsPickle(filename)
    logging.flush()
    # make sure everything is closed down
    if eyetracker:
        eyetracker.setConnectionState(False)
    thisExp.abort()  # or data files will save again on exit
    win.close()
    return feedback_value,feedback_key, response 
    # core.quit()

def staircase_vernier_icatcher(response,start_phase,contrast,spatial):
    # Ensure that relative paths start from the same directory as this script
    os_name = platform.system()
    
    _thisDir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(_thisDir)
    # Store info about the experiment session
    psychopyVersion = '2022.2.5'
    expName = 'stimuli4'  # from the Builder filename that created this script
    expInfo = {
        'participant': f"{randint(0, 999999):06.0f}",
        'session': '001',
        'stimulus duration': '3',
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
        originPath='C:\\Users\\soham\\Desktop\\automated-preferential-looking\\stimuli4.py',
        savePickle=True, saveWideText=True,
        dataFileName=filename)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    frameTolerance = 0.001  # how close to onset before 'same' frame

    # Start Code - component code to be run after the window creation
    answers = []  # list of answers for each frame
    confidences = []
    cap = cv2.VideoCapture(0)
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
   
    feedback={}
    value=[]
    # create a default keyboard (e.g. to check for escape)
    if os_name == "Windows" or os_name == "Linux" :
         # --- Setup input devices ---
        ioConfig = {}
        # Setup iohub keyboard
        ioConfig['Keyboard'] = dict(use_keymap='psychopy')

        ioSession = '1'
        if 'session' in expInfo:
            ioSession = str(expInfo['session'])
        ioServer = io.launchHubServer(window=win, **ioConfig)
        eyetracker = None
        defaultKeyboard = keyboard.Keyboard(backend='iohub')
    else:
        ioConfig = {}
        ioSession = ioServer = eyetracker = None

        # create a default keyboard (e.g. to check for escape)
        defaultKeyboard = keyboard.Keyboard(backend='ptb')

    # --- Initialize components for Routine "start_opt" ---
    if response=='5':
        opt=5
        text_2 = visual.TextStim(win=win, name='text_2',
            text="Press spacebar to start the experiment\n\n",
            font='Open Sans',
            pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
            color='white', colorSpace='rgb', opacity=None, 
            languageStyle='LTR',
            depth=0.0);
        key_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "grating_acuity" ---
    # Set experiment start values for variable component position
    position = (0, 0)
    positionContainer = []
    GA = visual.GratingStim(
        win=win, name='GA',units='deg', 
        tex='sqr', mask='sqr', anchor='center',
        ori=0.0, pos=[0,0], size=[128,32], sf=float(spatial), phase=0.0,
        color=[1,1,1], colorSpace='rgb',
        opacity=None, contrast=float(contrast), blendmode='avg',
        texRes=512.0, interpolate=True, depth=-2.0)

    GA_2 = visual.GratingStim(
        win=win, name='GA',units='deg', 
        tex='sqr', mask='sqr', anchor='center',
        ori=0.0, pos=[0,0], size=[32,16], sf=float(spatial), phase=float(start_phase),
        color=[1,1,1], colorSpace='rgb',
        opacity=None, contrast=float(contrast), blendmode='avg',
        texRes=512.0, interpolate=True, depth=-2.0)


    text_3 = visual.TextStim(win=win, name='text_3',
        text='',
        font='Open Sans',
        pos=(0,0.125), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);

    # --- Initialize components for Routine "central_fixation" ---
    key_resp_2 = keyboard.Keyboard()
    
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
        lineWidth=1.0,     colorSpace='rgb',   lineColor=[0.0000, 0.0000, 0.0000], fillColor=[0.0000, 0.0000, 0.0000],
        opacity=None, depth=0.0, interpolate=True)

    # Create some handy timers
    globalClock = core.Clock()  # to track the time since experiment started
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

    # --- Prepare to start Routine "start_exp" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
   
    min_count=0
   
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1

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

        # --------Prepare to start Staircase "staircase_loop" --------
        # set up handler to look after next chosen value etc
    staircase_loop = data.StairHandler(startVal=float(start_phase), extraInfo=expInfo,
        stepSizes=[0.05], stepType='log',
        nReversals=1.0, nTrials=20.0, 
        nUp=2.0, nDown=1.0,
        minVal=0.02, maxVal=0.99,
        originPath=-1, name='staircase_loop')
    thisExp.addLoop(staircase_loop)  # add the loop to the experiment
    level = thisStaircase_loop = float(start_phase)  # initialise some vals
    
    for thisStaircase_loop in staircase_loop:
        currentLoop = staircase_loop
        level = thisStaircase_loop
        if level==0.02 and min_count==5:
            break
        elif level==0.02 and min_count<5:
            min_count+=1
        # --- Prepare to start Routine "grating_acuity" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_3
        if opt==5 :
            pos=(randchoice([-1, 1])*16,0)
        else:
            pos= (randchoice([-1, 1])*16,randchoice([-1, 1])*8)
        position = pos  # Set routine start values for position

        GA.setContrast(float(contrast))
        GA.setPos((0,0))
        GA.setSF(float(spatial))
        GA_2.setContrast(float(contrast))
        GA_2.setPos(position)
        GA_2.setSF(float(spatial))
        GA_2.setPhase(float(level))
        text_3.setText("Spatial frequency: " +  f'{spatial}' +"\n"+"Contrast: "+ f'{contrast}' +"\n"+"Phase: "+ f'{level:.3f}')
        # keep track of which components have finished
        grating_acuityComponents = [GA,GA_2, text_3]
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
       
        
        # --- Prepare to start Routine "central_fixation" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code
        
        if (opt==5) and (position==(-16,0)):
            b=1
        elif (opt==5) and (position==(16,0)):
            b=2
        
        text_4.setText("Spatial frequency: " +  f'{spatial}' +"\n"+"Contrast: "+ f'{contrast}' +"\n"+"Phase: "+ f'{level:.3f}')

        # keep track of which components have finished
        central_fixationComponents = [GA,GA_2, text_4]
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
        rep=0
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
            if GA.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > GA.tStartRefresh + float(expInfo["stimulus duration"])-frameTolerance:
                    # keep track of stop time/frame for later
                    GA.tStop = t  # not accounting for scr refresh
                    GA.frameNStop = frameN  # exact frame index
                    GA.setAutoDraw(False)
            if GA_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                GA_2.frameNStart = frameN  # exact frame index
                GA_2.tStart = t  # local t and not account for scr refresh
                GA_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(GA_2, 'tStartRefresh')  # time at next scr refresh
                GA_2.setAutoDraw(True)
            if GA_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > GA_2.tStartRefresh + float(expInfo["stimulus duration"])-frameTolerance:
                    # keep track of stop time/frame for later
                    GA_2.tStop = t  # not accounting for scr refresh
                    GA_2.frameNStop = frameN  # exact frame index
                    GA_2.setAutoDraw(False)
            
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
            if text_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_4.tStartRefresh + float(expInfo["stimulus duration"])-frameTolerance:
                    # keep track of stop time/frame for later
                    text_4.tStop = t  # not accounting for scr refresh
                    text_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_4.stopped')
                    text_4.setAutoDraw(False)
            if(rep==0):
                    print("gaze detection")
                    answers,confidences,frames= predict_from_frame(cap)
                    print(answers)
                    print(confidences)
                    # print(frames)
                    if answers[np.argmax(confidences)]==b:
                        correct = 1  # correct non-response
                    else:
                        correct = 0
                    rep+=1
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
       
        # store data for staircase_loop (StairHandler)
        staircase_loop.addResponse(correct, level)
        # feedback.append(key_resp_2.corr)
        # value.append(level)
        if level in feedback:
            feedback[level].append(correct.corr)  # Append the new value to the existing list
        else:
            feedback[level] = [correct]
        staircase_loop.addOtherData('key_resp_2.rt', '')
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
        
    # staircase completed

    thisExp.nextEntry()
     
    # completed opt1 repeats of 'opt1'
    for level in feedback:
        feedback[level]= sum(feedback[level])/len(feedback[level])

    feedback_key = list(feedback.keys())
    feedback_value = list(feedback.values())
    # --- End experiment ---
    # Flip one final time so any remaining win.callOnFlip() 
    # and win.timeOnFlip() tasks get executed before quitting
    win.flip()

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