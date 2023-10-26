<!-- # automated-preferential-looking
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
``` -->


# APL: Automated Preferential Looking
<!-- TABLE OF CONTENTS -->
<h2 id="table-of-contents"> :book: Table of Contents</h2>

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project"> ➤ About The Project</a></li>
    <li><a href="#libraries-used"> ➤ Libraries Used</a></li>
    <li><a href="#roadmap"> ➤ Roadmap</a></li>
    <li><a href="#folder-structure"> ➤ Folder Structure</a></li>
    <li><a href="#implementation"> ➤ Implementation</a></li>
    <li><a href="#future"> ➤ Future Goals</a></li>
    <li><a href="#acknowledgments"> ➤ Acknowledgments</a></li>
  </ol>
</details>

-----------------------------------------------------

<h2 id="about-the-project"> :pencil: About The project</h2>

This project is the work for the Google Summer of Code 2023, with the organisation INCF. The project is created by [Soham Mulye](@Shazam213) under the mentoring of Suresh Krishna, PhD from McGill University.
This project aims to develop a ready-to-deploy application suite that will address these limitations by integrating hardware devices or deep learning-based infant eye trackers, and visual stimuli analysis into a user-friendly graphical user interface (GUI).


-----------------------------------------------------

<!-- PREREQUISITES -->
<h2 id="libraries-used"> Prerequisites</h2>

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


<!-- :paw_prints:-->
<!-- FOLDER STRUCTURE -->
<h2 id="folder-structure"> :cactus: Folder Structure</h2>

-----------------------------------------------------
<!-- :paw_prints:-->
<!-- IMPLEMENTATION -->
<h2 id="implementation"> Implementation</h2>

To execute the program on your system, please follow these steps.
* Clone the repository into your local system:
    ```sh
    git clone https://github.com/Shazam213/automated-preferential-looking.git
    ```

* Navigate to the cloned directory:
    ```sh
    cd automated-preferential-looking
    ```

* Download all the required packages:
    ```sh
    pip install -r requirements.txt
    ```

* Now execute the program:
    ```sh
    python main.py
    ```
Ps- You might face errors while psychopy installations. You can refer this [link](https://github.com/Shazam213/automated-preferential-looking/tree/visual-stimuli#getting-started).


-----------------------------------------------------
<!-- FUTURE -->
<h2 id="future"> Future Goals </h2>

Alas, the end of Summer of Code shouldn't be the end of this project! With an amazing scope to go forward, I would love to put much more effort and create a full-working application that could be used in a clinical setting with help and testing from other researchers and labs we already had contact with.The project has laid a strong foundation for efficient measurement of visual functions in infants and young children. Future work may include:

* Further refinement and optimization of the deep learning-based infant eye tracker model to improve accuracy.

* Collaborations with healthcare professionals and researchers to refine and validate the application's use in clinical settings.
* Deploy the program as a pip package or on a website.

Also due to the unavailibility of traditional eye tracking devices, eye tracker integration was not possible so instead for those experiments currently input is being taken through keyboard. But later it can also be implemented easily using the API developed by [Ioannis Valasakis](https://github.com/wizofe/ao-baby-tracker)

-----------------------------------------------------

<!-- Acknowledgments -->
<h2 id="acknowledgments"> Acknowledgments! </h2>
I'd like to express my gratitude to my mentor, Dr. Suresh Krishna from McGill University, for providing invaluable insights and information throughout this project. While at times the information was quite complex, I understand that it will greatly benefit future iterations of the application and collaborative research with other scientists.

I would also like to extend my appreciation to the developers of iCatcher+, the eye-tracking model that has been seamlessly integrated into the program for gaze detection and test automation.

With the generous support of Google's open-source initiatives, I hope that I've sown the seeds of a useful program and provided valuable code suggestions. These contributions have the potential to make a significant impact in clinical settings in the future. Thank you, Google!