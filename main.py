from fixed_increment_stimuli import *


# contrast_sensitivy_keyboard()
# print("Select the experiment you want to run:\n")
print("Welcome to visual stimuli.\n")
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
    start_contrast=0.5
else:
    print("Enter start contrast\n")
    start_contrast= input()
    start_spatial=0.5
stimuli(case,start_contrast,start_spatial)