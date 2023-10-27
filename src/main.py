# from fixed_increment_stimuli import *
from fixed_increment import *
from staircase import *
from psychometric_function import *
from fixed_increment_icatcher import *
from staircase_icatcher import *
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
            if selected_values["eye_tracker"]=="Eye Tracker":
                if selected_values["hemisphere"]== "Two Hemispheres":
                    case='1'
                    print("case is 1")
                elif selected_values["hemisphere"]== "Four Hemispheres":
                    case='2'
                feedback,value,response= fixedincrement(case,selected_values["min_var"],selected_values["max_var"],selected_values["param1"])
            else:
                case='1'
                feedback,value,response= fixedincrement_icatcher(case,selected_values["min_var"],selected_values["max_var"],selected_values["param1"])
                
        elif selected_values["test"]=="Spatial Frequency":
            if selected_values["eye_tracker"]=="Eye Tracker":
                if selected_values["hemisphere"]== "Two Hemispheres":
                    case='3'
                elif selected_values["hemisphere"]== "Four Hemispheres":
                    case='4'
                feedback,value,response=fixedincrement(case,selected_values["min_var"],selected_values["max_var"],selected_values["param1"])
            else:
                case='3'
                feedback,value,response= fixedincrement_icatcher(case,selected_values["min_var"],selected_values["max_var"],selected_values["param1"])
        else:
            if selected_values["eye_tracker"]=="Eye Tracker":
                if selected_values["hemisphere"]== "Two Hemispheres":
                    case='5'
                elif selected_values["hemisphere"]== "Four Hemispheres":
                    case='6'
                feedback,value,response=fixedincrement_vernier(case,selected_values["min_var"],selected_values["max_var"],selected_values["param1"],selected_values["param2"])
            else:
                case='5'
                feedback,value,response=fixedincrement_vernier_icatcher(case,selected_values["min_var"],selected_values["max_var"],selected_values["param1"],selected_values["param2"])
                
        psychometric_function(feedback,value,response)

    elif selected_values["experiment"]=="Staircase":
        if selected_values["test"]=="Contrast Sensitivity":
            if selected_values["eye_tracker"]=="Eye Tracker":
                if selected_values["hemisphere"]== "Two Hemispheres":
                    case='1'
                elif selected_values["hemisphere"]== "Four Hemispheres":
                    case='2'
                feedback,value,response=staircase(case,selected_values["min_var"],selected_values["param1"])
            else:
                case='1'
                feedback,value,response=staircase_icatcher(case,selected_values["min_var"],selected_values["param1"])
        elif selected_values["test"]=="Spatial Frequency":
            if selected_values["eye_tracker"]=="Eye Tracker":
                if selected_values["hemisphere"]== "Two Hemispheres":
                    case='3'
                elif selected_values["hemisphere"]== "Four Hemispheres":
                    case='4'
                feedback,value,response=staircase(case,selected_values["min_var"],selected_values["param1"])
            else:
                case='3'
                feedback,value,response=staircase_icatcher(case,selected_values["min_var"],selected_values["param1"])
        else:
            if selected_values["eye_tracker"]=="Eye Tracker":
                if selected_values["hemisphere"]== "Two Hemispheres":
                    case='5'
                elif selected_values["hemisphere"]== "Four Hemispheres":
                    case='6'
                feedback,value,response=staircase_vernier(case,selected_values["min_var"],selected_values["param1"],selected_values["param2"])
            else:
                case='5'
                feedback,value,response=staircase_vernier_icatcher(case,selected_values["min_var"],selected_values["param1"],selected_values["param2"])
        psychometric_function(feedback,value,case)
# core.quit()

if __name__ == "__main__":
    main()
