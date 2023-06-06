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
        print("Enter minimum and maximum spatial frequency(in cycles/deg)\n")
        print("Default values: minimum: 0.2 and maximum: 10. For default values press enter \n")
        min_spatial=input("Enter Minimum Spatial frequency\n")
        max_spatial= input("Enter Maximum Spatial frequency\n")
        fixed_contrast=input("Enter fixed contrast. Default value= 1\n")
        if min_spatial == "":
            min_spatial = "0.2"
        if max_spatial == "":
            max_spatial = "10"
        if fixed_contrast == "":
            fixed_contrast = "1"
        feedback,value,response=fixedincrement(case,min_spatial,max_spatial,fixed_contrast)
    else:
        print("Enter minimum and maximum contrast\n")
        print("Default values: minimum: 0.02 and maximum: 1. For default values press enter \n")
        min_contrast=input("Enter Minimum contrast\n")
        max_contrast= input("Enter Maximum contrast\n")
        fixed_spatial=input("Enter fixed spatial frequency. Default value= 0.5\n")
        if min_contrast == "":
            min_contrast = "0.02"
        if max_contrast == "":
            max_contrast = "1"
        if fixed_spatial == "":
            fixed_spatial = "0.5"
        feedback,value,response=fixedincrement(case,min_contrast,max_contrast,fixed_spatial)
    # psychometric_function(feedback,value,response)

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
        print("Default value: 0.9  . For default values press enter \n")
        start_spatial= input()
        print("Enter fixed contrast(maximum 1). Default value= 1\n")
        start_contrast=input()
        if start_spatial=="":
            start_spatial= "0.9"
        if start_contrast=="":
            start_contrast="1"
    else:
        print("Enter start contrast(maximum=1 and minimum=0.02)\n")
        print("Default value: 0.09  . For default values press enter \n")
        start_contrast= input()
        print("Enter fixed spatial frequency(in cycles/deg). Default value= 0.5\n")
        start_spatial=input()
        if start_spatial=="":
            start_spatial= "0.5"
        if start_contrast=="":
            start_contrast="0.09"
    feedback,value=staircase(case,start_contrast,start_spatial)
    # psychometric_function(feedback,value,case)
core.quit()