# from fixed_increment_stimuli import *
from fixed_increment import *
from staircase import *
import matplotlib as plt
from psychometric_function import *
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
        print("Enter start spatial frequency(in cycles/deg)\n")
        start_spatial= input()
        print("Enter fixed contrast(maximum 1)\n")
        start_contrast=input()
    else:
        print("Enter start contrast(maximum 1)\n")
        start_contrast= input()
        print("Enter fixed spatial frequency(in cycles/deg)\n")
        start_spatial=input()
    feedback,value,response=fixedincrement(case,start_contrast,start_spatial)
    psychometric_function(feedback,value,response)

elif choice=='2':
    print("Contrast Sensitivity Experiments:\n")
    print("Press 1 for stimulus in two hemiscreens.\n")
    print("Press 2 for stimulus in four quadrants.\n")
    print("Spatial Frequency Sensitivity Experiments:\n")
    print("Press 3 for stimulus in two hemiscreens.\n")
    print("Press 4 for stimulus in four quadrants.\n")

    case= input()
    if case=='3' or case=='4':
        print("Enter start spatial frequency(in cycles/deg)\n")
        start_spatial= input()
        print("Enter fixed contrast(maximum 1)\n")
        start_contrast=input()
    else:
        print("Enter start contrast(maximum 1)\n")
        start_contrast= input()
        print("Enter fixed spatial frequency(in cycles/deg)\n")
        start_spatial=input()
    feedback,value=staircase(case,start_contrast,start_spatial)
    psychometric_function(feedback,value,case)