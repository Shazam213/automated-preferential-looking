#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
on April 24, 2023, at 16:41
If you publish work using this script the most relevant publication is:

Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
    PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
    https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
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


def stimulus1():
    # Ensure that relative paths start from the same directory as this script
    _thisDir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(_thisDir)
    # Store info about the experiment session
    psychopyVersion = '2022.2.5'
    expName = 'stimuli_1'  # from the Builder filename that created this script
    expInfo = {
        'participant': f"{randint(0, 999999):06.0f}",
        'session': '001',
        'spatial freq': '0.8',
        'stimulus duration': '1',
        'start contrast': '0.02',
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
        originPath='C:\\Users\\soham\\Desktop\\automated-preferential-looking\\stimuli_1.py',
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
    win.mouseVisible = True
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
    text = visual.TextStim(win=win, name='text',
        text='Welcome to contrast sensitivity experiment.\nPress 1 for stimulus in two hemiscreens.\nPress 2 for stimulus in four quadrants.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    option_resp = keyboard.Keyboard()

    # --- Initialize components for Routine "start_opt1" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text='Press spacebar to start the experiment\n\nUse the arrow keys to point to the direction of the stimuli',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp = keyboard.Keyboard()

    # --- Initialize components for Routine "set_values1" ---
    # Set experiment start values for variable component contrast
    contrast = float(expInfo['start contrast'])
    contrastContainer = []

    # --- Initialize components for Routine "grating_acuity1" ---
    # Set experiment start values for variable component position
    position = (0, 0)
    positionContainer = []
    GA = visual.GratingStim(
        win=win, name='GA',units='deg', 
        tex='sqr', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=[8.5], sf=float(expInfo['spatial freq']), phase=0.0,
        color=[1,1,1], colorSpace='rgb',
        opacity=None, contrast=1.0, blendmode='avg',
        texRes=512.0, interpolate=True, depth=-1.0)
    aperture = visual.Aperture(
        win=win, name='aperture',
        units='deg', size=[8.5], pos=[0,0], ori=0.0,
        shape='circle', anchor='center'
    )
    aperture.disable()  # disable until its actually used

    # --- Initialize components for Routine "central_fixation1" ---
    key_resp_2 = keyboard.Keyboard()

    # --- Initialize components for Routine "set_values2" ---
    # Set experiment start values for variable component contrast_2
    contrast_2 = float(expInfo['start contrast'])
    contrast_2Container = []

    # --- Initialize components for Routine "grating_acuity2" ---
    # Set experiment start values for variable component position_2
    position_2 = (0, 0)
    position_2Container = []
    GA_2 = visual.GratingStim(
        win=win, name='GA_2',units='deg', 
        tex='sqr', mask=None, anchor='center',
        ori=0.0, pos=[0,0], size=[8.5], sf=float(expInfo['spatial freq']), phase=0.0,
        color=[1,1,1], colorSpace='rgb',
        opacity=None, contrast=1.0, blendmode='avg',
        texRes=512.0, interpolate=True, depth=-1.0)
    aperture_2 = visual.Aperture(
        win=win, name='aperture_2',
        units='deg', size=[8.5], pos=[0,0], ori=0.0,
        shape='circle', anchor='center'
    )
    aperture_2.disable()  # disable until its actually used

    # --- Initialize components for Routine "central_fixation2" ---
    key_resp_3 = keyboard.Keyboard()

    # Create some handy timers
    globalClock = core.Clock()  # to track the time since experiment started
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

    # --- Prepare to start Routine "start_exp" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    option_resp.keys = []
    option_resp.rt = []
    _option_resp_allKeys = []
    # keep track of which components have finished
    start_expComponents = [text, option_resp]
    for thisComponent in start_expComponents:
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

    # --- Run Routine "start_exp" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            text.setAutoDraw(True)
        
        # *option_resp* updates
        waitOnFlip = False
        if option_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            option_resp.frameNStart = frameN  # exact frame index
            option_resp.tStart = t  # local t and not account for scr refresh
            option_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(option_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'option_resp.started')
            option_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(option_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(option_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if option_resp.status == STARTED and not waitOnFlip:
            theseKeys = option_resp.getKeys(keyList=['1','2'], waitRelease=False)
            _option_resp_allKeys.extend(theseKeys)
            if len(_option_resp_allKeys):
                option_resp.keys = _option_resp_allKeys[-1].name  # just the last key pressed
                option_resp.rt = _option_resp_allKeys[-1].rt
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
        for thisComponent in start_expComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # --- Ending Routine "start_exp" ---
    for thisComponent in start_expComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if option_resp.keys in ['', [], None]:  # No response was made
        option_resp.keys = None
    thisExp.addData('option_resp.keys',option_resp.keys)
    if option_resp.keys != None:  # we had a response
        thisExp.addData('option_resp.rt', option_resp.rt)
    thisExp.nextEntry()
    # Run 'End Routine' code from code_5
    if option_resp.keys== '1':
        opt1=1
        opt2=0
    elif option_resp.keys== '2':
        opt2=1
        opt1=0
    # the Routine "start_exp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # --- Prepare to start Routine "start_opt1" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    start_opt1Components = [text_2, key_resp]
    for thisComponent in start_opt1Components:
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

    # --- Run Routine "start_opt1" ---
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
        for thisComponent in start_opt1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # --- Ending Routine "start_opt1" ---
    for thisComponent in start_opt1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    thisExp.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        thisExp.addData('key_resp.rt', key_resp.rt)
    thisExp.nextEntry()
    # the Routine "start_opt1" was not non-slip safe, so reset the non-slip timer
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
        
        # set up handler to look after randomisation of conditions etc
        ga_loop = data.TrialHandler(nReps=19.0, method='random', 
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
            
            # --- Prepare to start Routine "set_values1" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            contrast = contrast  # Set routine start values for contrast
            # Run 'Begin Routine' code from code_2
            contrast= (45**(1/19))*contrast
            # keep track of which components have finished
            set_values1Components = []
            for thisComponent in set_values1Components:
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
            
            # --- Run Routine "set_values1" ---
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
                for thisComponent in set_values1Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "set_values1" ---
            for thisComponent in set_values1Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('contrast.routineEndVal', contrast)  # Save end routine value
            # the Routine "set_values1" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "grating_acuity1" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            position = (randchoice([-1, 1])*16,0)  # Set routine start values for position
            GA.setContrast(contrast)
            GA.setPos(position)
            aperture.setPos(position)
            # keep track of which components have finished
            grating_acuity1Components = [GA, aperture]
            for thisComponent in grating_acuity1Components:
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
            
            # --- Run Routine "grating_acuity1" ---
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
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in grating_acuity1Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "grating_acuity1" ---
            for thisComponent in grating_acuity1Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('position.routineEndVal', position)  # Save end routine value
            aperture.enabled = False  # just in case it was left enabled
            # the Routine "grating_acuity1" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "central_fixation1" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            key_resp_2.keys = []
            key_resp_2.rt = []
            _key_resp_2_allKeys = []
            # Run 'Begin Routine' code from code
            
            if (position==(-16,0)):
                b='left'
            else:
                b='right'
            # keep track of which components have finished
            central_fixation1Components = [key_resp_2]
            for thisComponent in central_fixation1Components:
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
            
            # --- Run Routine "central_fixation1" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *key_resp_2* updates
                waitOnFlip = False
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
                    theseKeys = key_resp_2.getKeys(keyList=['left','right'], waitRelease=False)
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
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in central_fixation1Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "central_fixation1" ---
            for thisComponent in central_fixation1Components:
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
            # store data for ga_loop (TrialHandler)
            ga_loop.addData('key_resp_2.keys',key_resp_2.keys)
            ga_loop.addData('key_resp_2.corr', key_resp_2.corr)
            if key_resp_2.keys != None:  # we had a response
                ga_loop.addData('key_resp_2.rt', key_resp_2.rt)
            # the Routine "central_fixation1" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 19.0 repeats of 'ga_loop'
        
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
        
        # set up handler to look after randomisation of conditions etc
        ga_loop2 = data.TrialHandler(nReps=19.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='ga_loop2')
        thisExp.addLoop(ga_loop2)  # add the loop to the experiment
        thisGa_loop2 = ga_loop2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisGa_loop2.rgb)
        if thisGa_loop2 != None:
            for paramName in thisGa_loop2:
                exec('{} = thisGa_loop2[paramName]'.format(paramName))
        
        for thisGa_loop2 in ga_loop2:
            currentLoop = ga_loop2
            # abbreviate parameter names if possible (e.g. rgb = thisGa_loop2.rgb)
            if thisGa_loop2 != None:
                for paramName in thisGa_loop2:
                    exec('{} = thisGa_loop2[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "set_values2" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            contrast_2 = contrast_2  # Set routine start values for contrast_2
            # Run 'Begin Routine' code from code_3
            contrast_2 = (45**(1/19))*contrast_2
            # keep track of which components have finished
            set_values2Components = []
            for thisComponent in set_values2Components:
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
            
            # --- Run Routine "set_values2" ---
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
                for thisComponent in set_values2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "set_values2" ---
            for thisComponent in set_values2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('contrast_2.routineEndVal', contrast_2)  # Save end routine value
            # the Routine "set_values2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "grating_acuity2" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            position_2 = (randchoice([-1, 1])*16,randchoice([-1, 1])*8)  # Set routine start values for position_2
            GA_2.setContrast(contrast_2)
            GA_2.setPos(position_2)
            aperture_2.setPos(position_2)
            # keep track of which components have finished
            grating_acuity2Components = [GA_2, aperture_2]
            for thisComponent in grating_acuity2Components:
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
            
            # --- Run Routine "grating_acuity2" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *GA_2* updates
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
                
    # *aperture_2* updates
                if aperture_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    aperture_2.frameNStart = frameN  # exact frame index
                    aperture_2.tStart = t  # local t and not account for scr refresh
                    aperture_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(aperture_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'aperture_2.started')
                    aperture_2.enabled = True
                if aperture_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > aperture_2.tStartRefresh + float(expInfo["stimulus duration"])-frameTolerance:
                        # keep track of stop time/frame for later
                        aperture_2.tStop = t  # not accounting for scr refresh
                        aperture_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'aperture_2.stopped')
                        aperture_2.enabled = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in grating_acuity2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "grating_acuity2" ---
            for thisComponent in grating_acuity2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('position_2.routineEndVal', position_2)  # Save end routine value
            aperture_2.enabled = False  # just in case it was left enabled
            # the Routine "grating_acuity2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "central_fixation2" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            key_resp_3.keys = []
            key_resp_3.rt = []
            _key_resp_3_allKeys = []
            # Run 'Begin Routine' code from code_4
            
            if position==(-16,8) or position==(-16,-8):
                b='left'
            else:
                b='right'
            # keep track of which components have finished
            central_fixation2Components = [key_resp_3]
            for thisComponent in central_fixation2Components:
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
            
            # --- Run Routine "central_fixation2" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *key_resp_3* updates
                waitOnFlip = False
                if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_3.frameNStart = frameN  # exact frame index
                    key_resp_3.tStart = t  # local t and not account for scr refresh
                    key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_3.started')
                    key_resp_3.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_3.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_3.getKeys(keyList=['left','right'], waitRelease=False)
                    _key_resp_3_allKeys.extend(theseKeys)
                    if len(_key_resp_3_allKeys):
                        key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                        key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                        # was this correct?
                        if (key_resp_3.keys == str(b)) or (key_resp_3.keys == b):
                            key_resp_3.corr = 1
                        else:
                            key_resp_3.corr = 0
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
                for thisComponent in central_fixation2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "central_fixation2" ---
            for thisComponent in central_fixation2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_resp_3.keys in ['', [], None]:  # No response was made
                key_resp_3.keys = None
                # was no response the correct answer?!
                if str(b).lower() == 'none':
                    key_resp_3.corr = 1;  # correct non-response
                else:
                    key_resp_3.corr = 0;  # failed to respond (incorrectly)
            # store data for ga_loop2 (TrialHandler)
            ga_loop2.addData('key_resp_3.keys',key_resp_3.keys)
            ga_loop2.addData('key_resp_3.corr', key_resp_3.corr)
            if key_resp_3.keys != None:  # we had a response
                ga_loop2.addData('key_resp_3.rt', key_resp_3.rt)
            # the Routine "central_fixation2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 19.0 repeats of 'ga_loop2'
        
        thisExp.nextEntry()
        
    # completed opt2 repeats of 'opt2'


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
    core.quit()
