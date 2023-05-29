# from fixed_increment_stimuli import *
from stimuli3 import *
from stimuli4 import *
import matplotlib as plt
from psychometric_func import *
# contrast_sensitivy_keyboard()
# print("Select the experiment you want to run:\n")
print("Welcome to visual stimuli.\n")
print("Press 1 for fixed increment experiment\n")
print("Press 2 for staircase experiment\n")
choice= input()
if choice=='1':
    print("Contrast Sensitivity Experiments:\n")
    print("Press 1 for stimulus in two hemiscreens.\n")
    print("Press 2 for stimulus in four quadrants.\n")
    print("Spatial Frequency Sensitivity Experiments:\n")
    print("Press 3 for stimulus in two hemiscreens.\n")
    print("Press 4 for stimulus in four quadrants.\n")

    case= input()
    if case=='3' or case=='4':
        print("Enter start spatial frequency\n")
        start_spatial= input()
        print("Enter fixed contrast\n")
        start_contrast=input()
    else:
        print("Enter start contrast\n")
        start_contrast= input()
        print("Enter fixed spatial frequency\n")
        start_spatial=input()
    response,value = fixedincrement(case,start_contrast,start_spatial)

elif choice=='2':
    print("Contrast Sensitivity Experiments:\n")
    print("Press 1 for stimulus in two hemiscreens.\n")
    print("Press 2 for stimulus in four quadrants.\n")
    print("Spatial Frequency Sensitivity Experiments:\n")
    print("Press 3 for stimulus in two hemiscreens.\n")
    print("Press 4 for stimulus in four quadrants.\n")

    case= input()
    if case=='3' or case=='4':
        print("Enter start spatial frequency\n")
        start_spatial= input()
        print("Enter fixed contrast\n")
        start_contrast=input()
    else:
        print("Enter start contrast\n")
        start_contrast= input()
        print("Enter fixed spatial frequency\n")
        start_spatial=input()
    staircase(case,start_contrast,start_spatial)