# from fixed_increment_stimuli import *
from fixed_increment import *
from staircase import *
from psychometric_function import *
# contrast_sensitivy_keyboard()
# print("Select the experiment you want to run:\n")
# print("Welcome to visual stimuli.\n")
# print("Press 1 for fixed increment experiment\n")
# print("Press 2 for staircase experiment\n")
# choice= input()
# if choice=='1':
#     print("Contrast Sensitivity Experiments:\n")
#     print("Press 1 for stimulus in two hemiscreens.\n")
#     print("Press 2 for stimulus in four quadrants.\n")
#     print("Spatial Frequency Sensitivity Experiments:\n")
#     print("Press 3 for stimulus in two hemiscreens.\n")
#     print("Press 4 for stimulus in four quadrants.\n")
#     print("Vernier Acuity Experiments:\n")
#     print("Press 5 for stimulus in two hemiscreens.\n")
#     print("Press 6 for stimulus in four quadrants.\n")

#     case= input()
#     if case=='3' or case=='4':
#         print("Enter minimum and maximum spatial frequency(in cycles/deg)\n")
#         print("Default values: minimum: 0.2 and maximum: 10. For default values press enter \n")        
#         min_spatial=input("Enter Minimum Spatial frequency\n")
#         if min_spatial == "":
#             min_spatial = "0.2"
#         if float(min_spatial) < 0.0:
#             print("Invalid input. Setting to default\n")
#             min_spatial = "0.2"
#         max_spatial= input("Enter Maximum Spatial frequency\n")
#         if max_spatial == "":
#             max_spatial = "10"
#         # if float(max_spatial)>10.0:
#         #     print("Invalid input. Setting to default\n")
#         #     max_spatial = "10"
#         fixed_contrast=input("Enter fixed contrast.Range: 0 to 1. Default value= 1\n")
#         if fixed_contrast == "":
#             fixed_contrast = "1"
#         if float(fixed_contrast) <0.0:
#             print("Invalid input. Setting to default\n")
#             fixed_contrast = "1"    
#         feedback,value,response=fixedincrement(case,min_spatial,max_spatial,fixed_contrast)
#     elif case=='1' or case=='2':
#         print("Enter minimum and maximum contrast. Range: 0 to 1. \n")
#         print("Default values: minimum: 0.02 and maximum: 1. For default values press enter \n")
#         min_contrast=input("Enter Minimum contrast\n")
#         if min_contrast == "":
#             min_contrast = "0.02"
#         if float(min_contrast) < 0.0:
#             print("Invalid input. Setting to default\n")
#             min_contrast = "0.02"
#         max_contrast= input("Enter Maximum contrast\n")
#         if max_contrast == "":
#             max_contrast = "1"
#         # if float(max_contrast) > 10.0:
#         #     print("Invalid input. Setting to default\n")
#         #     min_contrast = "1"
#         fixed_spatial=input("Enter fixed spatial frequency.Range: 0 to 1. Default value= 0.5\n")
#         if fixed_spatial == "":
#             fixed_spatial = "0.5"
#         if float(fixed_spatial) < 0.0:
#             print("Invalid input. Setting to default\n")
#             fixed_spatial = "0.5"
#         feedback,value,response=fixedincrement(case,min_contrast,max_contrast,fixed_spatial)
#     else:
#         print("Enter minimum and maximum phase\n")
#         print("Default values: minimum: 0.25 and maximum: 8. For default values press enter \n")
#         min_phase=input("Enter Minimum phase\n")
#         if min_phase == "":
#             min_phase = "0.25"
#         if float(min_phase)<0.0:
#             print("Invalid input. Setting to default\n")
#             min_phase = "0.25"
#         max_phase= input("Enter Maximum phase\n")
#         if max_phase == "":
#             max_phase = "8"
#         fixed_spatial=input("Enter fixed spatial frequency.Range: 0 to 1. Default value= 0.5\n")
#         if fixed_spatial == "":
#             fixed_spatial = "0.5"
#         if float(fixed_spatial) < 0.0:
#             print("Invalid input. Setting to default\n")
#             fixed_spatial = "0.5"
#         fixed_contrast=input("Enter fixed contrast.Range: 0 to 1. Default value= 0.5\n")
#         if fixed_contrast == "":
#             fixed_contrast = "0.5"
#         if float(fixed_contrast) < 0.0:
#             print("Invalid input. Setting to default\n")
#             fixed_contrast = "0.5"
#         feedback,value,response=fixedincrement_vernier(case,min_phase,max_phase,fixed_contrast,fixed_spatial)
#     psychometric_function(feedback,value,response)

# elif choice=='2':
#     print("Contrast Sensitivity Experiments:\n")
#     print("Press 1 for stimulus in two hemiscreens.\n")
#     print("Press 2 for stimulus in four quadrants.\n")
#     print("Spatial Frequency Sensitivity Experiments:\n")
#     print("Press 3 for stimulus in two hemiscreens.\n")
#     print("Press 4 for stimulus in four quadrants.\n")
#     print("Vernier Acuity Experiments:\n")
#     print("Press 5 for stimulus in two hemiscreens.\n")
#     print("Press 6 for stimulus in four quadrants.\n")

#     case= input()
#     if case=='3' or case=='4':
#         print("Enter start spatial frequency(in cycles/deg). Range: 0.2 to 5\n")
#         print("Default value: 2.5  . For default values press enter \n")
#         start_spatial= input()
#         if start_spatial=="":
#             start_spatial= "2.5"
#         if float(start_spatial)<0.0:
#             print("Invalid input. Setting to default\n")
#             start_spatial = "2.5"
#         print("Enter fixed contrast(Range: 0 to 1). Default value= 1\n")
#         start_contrast=input()
#         if start_contrast=="":
#             start_contrast="1"
#         if float(start_contrast)<0.0:
#             print("Invalid input. Setting to default\n")
#             start_contrast = "1"
#         feedback,value=staircase(case,start_contrast,start_spatial)
        
#     elif case=='1' or case=='2':
#         print("Enter start contrast(maximum=1 and minimum=0.02)\n")
#         print("Default value: 0.09  . For default values press enter \n")
#         start_contrast= input()
#         if start_contrast=="":
#             start_contrast="0.09"
#         if float(start_contrast)<0.0:
#             print("Invalid input. Setting to default\n")
#             start_spatial = "0.09"
#         print("Enter fixed spatial frequency(in cycles/deg).Range: 0 to 1. Default value= 0.5\n")
#         start_spatial=input()
#         if start_spatial=="":
#             start_spatial= "0.5"
#         if float(start_spatial)<0.0:
#             print("Invalid input. Setting to default\n")
#             start_spatial = "0.5"
#         feedback,value=staircase(case,start_contrast,start_spatial)
#     else:
#         print("Enter starting phase: minimum=0 and maximum=1\n")
#         print("Default value: 0.5. For default value press enter \n")
#         start_phase=input()
#         if start_phase == "":
#             start_phase = "0.5"
#         if float(start_phase)<0.0:
#             print("Invalid input. Setting to default\n")
#             start_phase = "0.5"
#         fixed_spatial=input("Enter fixed spatial frequency.Range: 0 to 1. Default value= 0.5\n")
#         if fixed_spatial == "":
#             fixed_spatial = "0.5"
#         if float(fixed_spatial)<0.0:
#             print("Invalid input. Setting to default\n")
#             fixed_spatial = "0.5"
#         fixed_contrast=input("Enter fixed contrast.Range: 0 to 1. Default value= 0.5\n")
#         if fixed_contrast == "":
#             fixed_contrast = "0.5"
#         if float(fixed_contrast)<0.0:
#             print("Invalid input. Setting to default\n")
#             fixed_contrast = "0.5"
#         feedback,value=staircase_vernier(case,start_phase,fixed_contrast,fixed_spatial)
#     psychometric_function(feedback,value,case)
# core.quit()

import tkinter as tk
from gui import ExperimentGUI  # Import the ExperimentGUI class from experiment_gui.py


def main():
    root = tk.Tk()
    gui = ExperimentGUI(root)
    print("gui object created")
    root.mainloop()

    # After the mainloop finishes (GUI window is closed), retrieve the selected values
    selected_values = gui.start_experiment()
    print("retrieved the values")
    root.destroy()
    del gui
    print("obj deleted")
    print("Selected Values:", selected_values)
    if selected_values["experiment"]=="Fixed Increment":
        if selected_values["test"]=="Contrast Sensitivity":
            if selected_values["hemisphere"]== "Two Hemispheres":
                case='1'
                print("case is 1")
            elif selected_values["hemisphere"]== "Four Hemispheres":
                case='2'
            feedback,value,response=fixedincrement(case,selected_values["min_var"],selected_values["max_var"],selected_values["param1"])
        elif selected_values["test"]=="Spatial Frequency":
            if selected_values["hemisphere"]== "Two Hemispheres":
                case='3'
            elif selected_values["hemisphere"]== "Four Hemispheres":
                case='4'
            feedback,value,response=fixedincrement(case,selected_values["min_var"],selected_values["max_var"],selected_values["param1"])
        else:
            if selected_values["hemisphere"]== "Two Hemispheres":
                case='5'
            elif selected_values["hemisphere"]== "Four Hemispheres":
                case='6'
            feedback,value,response=fixedincrement_vernier(case,selected_values["min_var"],selected_values["max_var"],selected_values["param1"],selected_values["param2"])
        psychometric_function(feedback,value,response)

    elif selected_values["experiment"]=="Staircase":
        if selected_values["test"]=="Contrast Sensitivity":
            if selected_values["hemisphere"]== "Two Hemispheres":
                case='1'
            elif selected_values["hemisphere"]== "Four Hemispheres":
                case='2'
            feedback,value,response=staircase(case,selected_values["min_var"],selected_values["param1"])
        elif selected_values["test"]=="Spatial Frequency":
            if selected_values["hemisphere"]== "Two Hemispheres":
                case='3'
            elif selected_values["hemisphere"]== "Four Hemispheres":
                case='4'
            feedback,value,response=staircase(case,selected_values["min_var"],selected_values["param1"])
        else:
            if selected_values["hemisphere"]== "Two Hemispheres":
                case='5'
            elif selected_values["hemisphere"]== "Four Hemispheres":
                case='6'
            feedback,value,response=staircase_vernier(case,selected_values["min_var"],selected_values["param1"],selected_values["param2"])
        psychometric_function(feedback,value,case)
# core.quit()

if __name__ == "__main__":
    main()
