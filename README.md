# automated-preferential-looking
This project aims to develop a ready-to-deploy application suite that will address these limitations by integrating hardware devices or deep learning-based infant eye trackers, and visual stimuli analysis into a user-friendly graphical user interface (GUI).

## Steps to test the program:
### To test the gui:
* Navigate to the cloned directory:
```sh
cd automated-preferential-looking
```

* Get the latest changes in the local repo:
```sh
git pull
```

* Also clone all the newly added branches:
```sh
git fetch
```
* Change to the final directory to test the gui:
```sh
git checkout final
```
* Now run the main.py file:
```sh
python main.py
```
### To test the icatcher integration with the dummy experiment:
* Navigate to the cloned directory:
```sh
cd automated-preferential-looking
```

* Get the latest changes in the local repo:
```sh
git pull
```

* Also clone all the newly added branches:
```sh
git fetch
```
* Change to the final directory to test the gui:
```sh
git checkout icatcher-integration
```
* Install the required dependencies:
```sh
pip install icatcher
```
```sh
pip install ffmpeg-python   
```
* Now run the main.py file:
```sh
python main.py
```


# APL: Automated Preferential Looking
<!-- TABLE OF CONTENTS -->
<h2 id="table-of-contents"> :book: Table of Contents</h2>

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project"> ➤ About The Project</a></li>
    <li><a href="#prerequisites"> ➤ Prerequisites</a></li>
    <li><a href="#roadmap"> ➤ Roadmap</a></li>
    <li><a href="#folder-structure"> ➤ Folder Structure</a></li>
    <li><a href="#implementation"> ➤ Implementation</a></li>
    <li><a href="#future"> ➤ Future Goals</a></li>
    <li><a href="#acknowledgments"> ➤ Acknowledgments</a></li>
    <li><a href="#license"> ➤ License</a></li
  </ol>
</details>

-----------------------------------------------------

<h2 id="about-the-project"> :pencil: About The project</h2>

This project is the work for the Google Summer of Code 2023, with the organisation INCF. The project is created by [Soham Mulye](@Shazam213) under the mentoring of Suresh Krishna, PhD from McGill University.

The project aims at creating an easy to use python program to automate the traditional preferential looking tests for infants.


-----------------------------------------------------

<!-- PREREQUISITES -->
<h2 id="prerequisites"> Prerequisites</h2>

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) <br>


<!--This project is written in Python programming language. <br>-->
The following open source packages are used in this project:
* Numpy
* Matplotlib
* Scikit-Learn
* TensorFlow
* Keras
* PsychoPy
* OpenCV
* Tkinter

-----------------------------------------------------


<!-- ROADMAP -->
<h2 id="roadmap"> :dart: Roadmap</h2>

The result of this work which was about 420 hours, is divided in the following parts:

1. Psychophysics Research and Experimentation:
    *   In-depth research into psychophysics, including the study of various psychophysical experiments and the underlying psychometric functions.Exploration and understanding of the theoretical aspects related to visual perception and responses.

2. Psychopy Experiment Development:

    * Design and implementation of psychophysical experiments using the Psychopy library. Creation of controlled experimental environments with systematic manipulation of visual stimuli, such as grating acuity and contrast sensitivity tests.

3. Eye Tracking Integration:
    * Seamless integration of an eye-tracking model into the developed experiments to enable automated gaze tracking Development of psychometric function to monitor and analyze infant gaze, eye movements, and responses to visual stimuli.

4. User-Friendly GUI and Program Integration:

    * Development of an intuitive and user-friendly graphical user interface (GUI) using Tkinter. Integration of all three components, including the visual stimuli experiments, eye-tracking functionality, and data analysis, into a cohesive Python program.

