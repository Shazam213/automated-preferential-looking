# automated-preferential-looking
This project aims to develop a ready-to-deploy application suite that will address these limitations by integrating hardware devices or deep learning-based infant eye trackers, and visual stimuli analysis into a user-friendly graphical user interface (GUI).

## Getting Started
* Clone the repository:
```sh 
git clone https://github.com/Shazam213/automated-preferential-looking.git 
```
* Navigate to the cloned directory:
```sh
cd automated-preferential-looking
```

* Switch to the visual-stimuli branch:
```sh
git checkout visual-stimuli
```
* Because calling pip install psychopy generates issues, we would have to specifically install pyWinhook before installing psychopy and all its dependencies.

* Check your python version using:
```sh
python --version
```
* Download the pyWinhook wheel file that corresponds to your Python version. The version of Python is denoted by cp___. For example, if you are using Python 3.10.11, you must obtain the cp10 whl file from:
[Download Link](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pywinhook)

*  Navigate to the directory of the downloaded whl file and run:
```sh
pip install whl_file_name
```
* Now install psychopy and its dependencies:
```sh
pip install psychopy
```
* Now run the main.py file:
```sh
python main.py
```
## File structure

* **main.py** file contains the code that runs all the experiments by making function calls to the respective python files
* stimuli_1.py and stimuli_2.py were the initial experiment python files which were initially created for testing but now not in use.
* **fixed_increment.py** is the python file for the fixed increment experiment.
* **staircase.py** is the python file for staircase expreriment. 
* stimuli3.py and stimuli4.py are imported in main.py file
* **.psyexp** files are the psychopy experiment files and **.lastrun** are the auto-generated .py files for the corresponding experiments.
* **The fixed_increment.py and staircase.py files are now in use, along with the main.py file; the rest of the files are not.**