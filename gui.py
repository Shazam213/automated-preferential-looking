import tkinter as tk
from tkinter import ttk

class ExperimentGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Experiment GUI")
        self.root.attributes('-fullscreen', True)  # Open GUI in full screen

        # Initialize variables and set default values
        self.current_screen = 0  # To keep track of the current screen
        self.test_var = tk.StringVar(value="")
        self.experiment_var = tk.StringVar(value="")
        self.eye_tracker_var = tk.StringVar(value="")
        self.hemisphere_var = tk.StringVar(value="")

        # First screen: Select Test
        self.screen1 = ttk.Frame(self.root)
        self.screen1.pack(expand=True, fill='both')

        test_label = ttk.Label(self.screen1, text="Select Test:", font=("Helvetica", 20))
        test_label.pack(pady=50)

        contrast_button = ttk.Button(self.screen1, text="Contrast Sensitivity Test", command=self.select_contrast_test, style="Custom.TButton")
        contrast_button.pack(pady=20)

        spatial_button = ttk.Button(self.screen1, text="Spatial Frequency Test", command=self.select_spatial_test, style="Custom.TButton")
        spatial_button.pack(pady=20)

        vernier_button = ttk.Button(self.screen1, text="Vernier Acuity Test", command=self.select_vernier_test, style="Custom.TButton")
        vernier_button.pack(pady=20)

        # Second screen: Experiment and Eye Tracker Type
        self.screen2 = None

        # Third screen: Hemisphere Option
        self.screen3 = None

        # Fourth screen: Parameter Selection
        self.screen4 = None
        self.min_var=None
        self.max_var=None
        self.param1=None
        self.param2=None
        self.show_test_screen()

    def select_contrast_test(self):
        self.test_var.set("Contrast Sensitivity")
        self.show_experiment_screen()

    def select_spatial_test(self):
        self.test_var.set("Spatial Frequency")
        self.show_experiment_screen()

    def select_vernier_test(self):
        self.test_var.set("Vernier Acuity")
        self.show_experiment_screen()

    def show_test_screen(self):
        if self.screen2:
            self.screen2.pack_forget()
        if self.screen3:
            self.screen3.pack_forget()
        if self.screen4:
            self.screen4.pack_forget()
        
        self.screen1.pack(expand=True, fill='both')

    def show_experiment_screen(self):
        if self.screen1:
            self.screen1.pack_forget()
        if self.screen3:
            self.screen3.pack_forget()
        if self.screen4:
            self.screen4.pack_forget()

        self.screen2 = ttk.Frame(self.root)
        self.screen2.pack(expand=True, fill='both')

        experiment_label = ttk.Label(self.screen2, text="Select Experiment:", font=("Helvetica", 20))
        experiment_label.pack(pady=50)

        experiment_options = ["Fixed Increment", "Staircase"]
        experiment_menu = tk.OptionMenu(self.screen2, self.experiment_var, *experiment_options)
        experiment_menu.config(font=("Helvetica", 12))
        experiment_menu.pack(pady=20)

        eye_tracker_label = ttk.Label(self.screen2, text="Select Eye Tracker Type:", font=("Helvetica", 20))
        eye_tracker_label.pack(pady=50)

        eye_tracker_options = ["Eye Tracker", "Eye Tracking Model"]
        eye_tracker_frame = ttk.Frame(self.screen2)
        eye_tracker_frame.pack(pady=20)

        for option in eye_tracker_options:
            tk.Radiobutton(eye_tracker_frame, text=option, variable=self.eye_tracker_var, value=option, font=("Helvetica", 12)).pack(side=tk.LEFT, padx=10)

        back_button2 = ttk.Button(self.screen2, text="Back", command=self.show_test_screen, style="Custom.TButton")
        back_button2.pack(side=tk.LEFT, pady=20)

        next_button2 = ttk.Button(self.screen2, text="Next", command=self.show_hemisphere_screen, style="Custom.TButton")
        next_button2.pack(side=tk.RIGHT, pady=20)

    def show_hemisphere_screen(self):
        if self.screen1:
            self.screen1.pack_forget()
        if self.screen2:
            self.screen2.pack_forget()
        if self.screen4:
            self.screen4.pack_forget()

        self.screen3 = ttk.Frame(self.root)
        self.screen3.pack(expand=True, fill='both')

        eye_tracker_type = self.eye_tracker_var.get()

        hemisphere_options = ["Two Hemispheres"]
        if eye_tracker_type == "Eye Tracker":
            hemisphere_options.append("Four Hemispheres")

        hemisphere_label = ttk.Label(self.screen3, text="Select Hemisphere Option:", font=("Helvetica", 20))
        hemisphere_label.pack(pady=50)

        hemisphere_menu = tk.OptionMenu(self.screen3, self.hemisphere_var, *hemisphere_options)
        hemisphere_menu.config(font=("Helvetica", 12))
        hemisphere_menu.pack(pady=20)

        back_button3 = ttk.Button(self.screen3, text="Back", command=self.show_experiment_screen, style="Custom.TButton")
        back_button3.pack(pady=20)

        next_button3 = ttk.Button(self.screen3, text="Next", command=self.show_parameter_screen, style="Custom.TButton")
        next_button3.pack(pady=20)

    def show_parameter_screen(self):
        if self.screen1:
            self.screen1.pack_forget()
        if self.screen2:
            self.screen2.pack_forget()
        if self.screen3:
            self.screen3.pack_forget()

        self.screen4 = ttk.Frame(self.root)
        self.screen4.pack(expand=True, fill='both')

        test_type = self.test_var.get()
        experiment_type = self.experiment_var.get()
        eye_tracker_type = self.eye_tracker_var.get()
        hemisphere_type = self.hemisphere_var.get()

        # TODO: Add parameter selection components here based on test_type, experiment_type, and eye_tracker_type
        if(experiment_type=="Fixed Increment"):
            if(test_type=="Contrast Sensitivity"):
                self.min_scale = tk.Scale(self.screen4, from_=0, to=1, resolution=0.001, orient=tk.HORIZONTAL, label="Min Contrast:")
                self.min_scale.set(0.02)
                self.min_scale.pack()

                # Create a Scale widget for controlling the maximum value
                self.max_scale = tk.Scale(self.screen4, from_=0, to=1, resolution=0.001, orient=tk.HORIZONTAL, label="Max Contrast:")
                self.max_scale.set(1)
                self.max_scale.pack()

                # Create a Scale widget for controlling param1 value
                self.param1_scale = tk.Scale(self.screen4, from_=0, to=10, resolution=0.001, orient=tk.HORIZONTAL, label="Spatial frequency:")
                self.param1_scale.set(0.5)
                self.param1_scale.pack()

    
            elif(test_type=="Spatial Frequency"):
                self.min_scale = tk.Scale(self.screen4, from_=0, to=10, resolution=0.001, orient=tk.HORIZONTAL, label="Min Spatial Frequency:")
                self.min_scale.set(0.2)  
                self.min_scale.pack()

                # Create a Scale widget for controlling the maximum value
                self.max_scale = tk.Scale(self.screen4, from_=0, to=10, resolution=0.001, orient=tk.HORIZONTAL, label="Max Spatial Frequency:")
                self.max_scale.set(5)
                self.max_scale.pack()

                # Create a Scale widget for controlling param1 value
                self.param1_scale = tk.Scale(self.screen4, from_=0, to=1, resolution=0.001, orient=tk.HORIZONTAL, label="Contrast:")
                self.param1_scale.set(1)
                self.param1_scale.pack()

            elif(test_type=="Vernier Acuity"):
                self.min_scale = tk.Scale(self.screen4, from_=0, to=1, resolution=0.001, orient=tk.HORIZONTAL, label="Min Phase:")
                self.min_scale.set(0.01)  
                self.min_scale.pack()

                # Create a Scale widget for controlling the maximum value
                self.max_scale = tk.Scale(self.screen4, from_=0, to=1, resolution=0.001, orient=tk.HORIZONTAL, label="Max Phase:")
                self.max_scale.set(1)
                self.max_scale.pack()

                # Create a Scale widget for controlling param1 value
                self.param1_scale = tk.Scale(self.screen4, from_=0, to=1, resolution=0.001, orient=tk.HORIZONTAL, label="Contrast:")
                self.param1_scale.set(1)
                self.param1_scale.pack()

                # Create a Scale widget for controlling param2 value
                self.param2_scale = tk.Scale(self.screen4, from_=0, to=10, resolution=0.001, orient=tk.HORIZONTAL, label="Spatial Frequency")
                self.param2_scale.set(1)
                self.param2_scale.pack()

                self.min_var = self.min_scale.get()
                self.max_var = self.max_scale.get()
                self.param1 = self.param1_scale.get()
                self.param2 = self.param2_scale.get()
        elif(experiment_type=="Staircase"):
            if(test_type=="Contrast Sensitivity"):
                self.min_scale = tk.Scale(self.screen4, from_=0, to=1, resolution=0.001, orient=tk.HORIZONTAL, label="Start Contrast:")
                self.min_scale.set(0.5)
                self.min_scale.pack()

                # Create a Scale widget for controlling param1 value
                self.param1_scale = tk.Scale(self.screen4, from_=0, to=10, resolution=0.001, orient=tk.HORIZONTAL, label="Spatial frequency:")
                self.param1_scale.set(0.5)
                self.param1_scale.pack()

    
            elif(test_type=="Spatial Frequency"):
                self.min_scale = tk.Scale(self.screen4, from_=0, to=10, resolution=0.001, orient=tk.HORIZONTAL, label="Start Spatial Frequency:")
                self.min_scale.set(5)  
                self.min_scale.pack()

           
                # Create a Scale widget for controlling param1 value
                self.param1_scale = tk.Scale(self.screen4, from_=0, to=1, resolution=0.001, orient=tk.HORIZONTAL, label="Contrast:")
                self.param1_scale.set(1)
                self.param1_scale.pack()

                self.max_scale.set(0)
                self.param2_scale(0)
            elif(test_type=="Vernier Acuity"):
                self.min_scale = tk.Scale(self.screen4, from_=0, to=1, resolution=0.001, orient=tk.HORIZONTAL, label="Start Phase:")
                self.min_scale.set(0.5)  
                self.min_scale.pack()

                # Create a Scale widget for controlling param1 value
                self.param1_scale = tk.Scale(self.screen4, from_=0, to=1, resolution=0.001, orient=tk.HORIZONTAL, label="Contrast:")
                self.param1_scale.set(1)
                self.param1_scale.pack()

                # Create a Scale widget for controlling param2 value
                self.param2_scale = tk.Scale(self.screen4, from_=0, to=10, resolution=0.001, orient=tk.HORIZONTAL, label="Spatial Frequency")
                self.param2_scale.set(1)
                self.param2_scale.pack()

             
        # Pack the label to display it on the screen
        back_button4 = ttk.Button(self.screen4, text="Back", command=self.show_hemisphere_screen, style="Custom.TButton")
        back_button4.pack(pady=20)

        start_button = ttk.Button(self.screen4, text="Start Experiment", command=self.start_experiment, style="Custom.TButton")
        start_button.pack(pady=20)

    def start_experiment(self):
        if hasattr(self, 'param2_scale'):
            param2=self.param2_scale.get()
        else:
            param2=0
        if hasattr(self, 'max_scale'):
            max_var=self.max_scale.get()
        else: 
            max_var=0    
        selected_values = {
        "test": self.test_var.get(),
        "experiment": self.experiment_var.get(),
        "eye_tracker": self.eye_tracker_var.get(),
        "hemisphere": self.hemisphere_var.get(),
        "min_var": self.min_scale.get(),
        "max_var": max_var,
        "param1": self.param1_scale.get(),
        "param2": param2,
        } 
        self.root.quit()
        return selected_values
       