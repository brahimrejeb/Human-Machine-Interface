# Development of human-machine interface based on detection of fingers movements

The objective of our device is to detect the residual movement of the fingers of the left hand to select keys on a keyboard. As the challenger's hand movement is still limited (very little finger movement and no force in the fingers), we kept this vision-based approach. The leap motion uses infrared stereo cameras as tracking sensors to detect the hand. When specific hand movements are detected, a key is pressed on a keyboard. 

# Prerequisites

Windows
Python 3.7  
OrionV4: https://developer.leapmotion.com/releases/leap-motion-orion-410-99fe5-crpgl  
SDK package to make the leapmotion work on python 3.7  
Ananconda is recomended  
The packages required are :  
- PyQt5 
- Numpy
- 

# Installation
- Install Anaconda
- Create a new environment with python 3.7 using Anaconda: conda create --name myenv python=3.7 (to get python3.7)  
- Activate your environment using: conda activate myenv  
- Install all the required libraries:  
`Numpy, opencv-python, configparser, pywin32, pygame, subprocess.run, pynput, Pillow, ctypes-callable, tkintertable, AST, pyttsx3 gtts'.  
- Code:  
Load the code from the github: https://github.com/brahimrejeb/LeapOrion.git. 
Modify in the config.ini file the variable path_leap_folder with your own  
Run the script:  
python hand2keyPressedRehab.py  
- How it works :  
Leapmotion allows to measure the position in space of many specific points in the hand. We will use those measures to detect some specific movement. 
