from contrast_sensitivity_keyboard import *
from stimuli_1 import *
from stimuli_2 import *


# contrast_sensitivy_keyboard()
print("Select the experiment you want to run:\n")
print("1. Contrast sensitivity experiment\n")
print("2. Spatial Frequency experiment\n")
case= int(input())
if case==1 :
    stimulus1()
elif case==2:
    stimulus2()