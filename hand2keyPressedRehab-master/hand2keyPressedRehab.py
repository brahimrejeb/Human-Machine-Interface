###########################################################
# hand2keyPressedRehab 
# LeapMotion Solution 
# Contact: hackahealth.geneva@gmail.com 
# Authors: Bastien Orset (V1), Odile Andres, Nada Guerraoui, Thomas Peeters, Brahim Rejeb (V2)
# (include your names if you do any collaboration in the code)
###########################################################

#Import required librairies
import numpy as np
import ctypes
import os
import Leap
import threading
import time
import configparser
import ast
import sys
import win32process
from pygame import mixer
from tkinter import *
import subprocess
import pyttsx3
import cv2
from gtts import gTTS
from LeapMotion_detection import LeapMotionListener
from pynput.keyboard import Key,KeyCode, Controller, Listener
from pynput import keyboard
#from PIL import Image, ImageTk
from tkinter import *
from PyQt5 import QtCore, QtGui, QtWidgets

import Settings
from Settings import Ui_Dialog
import mainwindows
from mainwindows import Ui_AnglesValues
import PerformanceWindow
from PerformanceWindow import Ui_Rin
import time

#from mainwindows import External


# LIST CMD 
OPTIONS = ['None','Alt','Win',
   'Ctrl','Tab','Shift','Caps','Esc','AltGr']

# DICTIONARY TO USE 
DICT_PYNPUT_KEYBOARD = {'none':None,'alt':Key.alt_l,'win': Key.cmd,
   'del': Key.delete,'down':Key.down,'ctrl':Key.ctrl_l,
   'tab':Key.tab,'shift':Key.shift,'f1':Key.f1,
   'f2':Key.f2,'f3':Key.f3,'f4':Key.f4,
   'f5':Key.f5,'f6':Key.f6,'f7':Key.f7,
   'f8':Key.f8,'f9':Key.f9,'f10':Key.f10,
   'f11':Key.f11,'f12':Key.f12,'end':Key.end,
   'bksp':Key.backspace,'enter':Key.enter,
   'caps': Key.caps_lock,'esc':Key.esc,
   'up': Key.up,'left': Key.left,'right':Key.right, 'altgr':Key.alt_r
}

# LABELS FINGERS
NB_INPUTS=6
DEFAULT_LABELS_FINGERS = ['thumb','index','middle','ring','pinky','wrist']
DEFAULT_DATA_HEADER= "THUMB,INDEX,MIDDLE,RING,PINKY,WRIST,TH_THB,TH_IN,TH_MID,TH_RG,TH_PK,TH_WRIST"


class Interface():
    '''
    Initialisation of the paramter of the simulation
    Recording of the Data in a file
    Sound feedback
    Drawing of the interface
    '''
    def __init__(self,config_file):
        
        global mainwin

        # Initialisation : 
        self.init=True

        # READ CONFIG FILE
        self.config_file = config_file
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file)


        # GET DEFAULT PARAMS FROM THE CONFIG FILE 
        self.labels_buttons = ast.literal_eval(self.config.get("options", "labels_buttons"))
        self.index_buttons = ast.literal_eval(self.config.get("options", "index_buttons"))
        self.use_setup = self.config.getboolean("options","use_setup") 
        self.close_cmd = self.config.getboolean("options","close_cmd")

        # by default the sound is off
        self.use_sound = self.config.getboolean("options","use_sound")
        self.show_visualizer = self.config.getboolean("options","show_visualizer")
        self.record_data = self.config.getboolean("options","record_data")
        self.path_leap_folder = ast.literal_eval(self.config.get("options", "path_leap_folder"))
        #by default the application is used with the shifter mode
        self.current_key= self.config.getint("options","current_key")

        # DRAWING PARAMS
        mainwin.bar_origin_threshold = ast.literal_eval(self.config.get("drawing", "bar_origin_threshold"))
        self.bar_h = np.zeros((NB_INPUTS))

        # Initialisation our window:
        mainwin.KeyAllFingersUsedInit = self.index_buttons
        mainwin.CurrentKey.setText(OPTIONS[self.current_key])

        mainwin.ThumbKey.setCurrentIndex(self.index_buttons[0])
        mainwin.IndexKey.setCurrentIndex(self.index_buttons[1])
        mainwin.MiddleKey.setCurrentIndex(self.index_buttons[2])
        mainwin.RingKey.setCurrentIndex(self.index_buttons[3])
        mainwin.PinkyKey.setCurrentIndex(self.index_buttons[4])
        mainwin.WristKey.setCurrentIndex(self.index_buttons[5])

        # DATA RECORDING
        if self.record_data:
            self.folderData = ".\Data"
            if not os.path.exists(self.folderData):
                os.makedirs(self.folderData)
            self.timestr = time.strftime("%Y%m%d-%H%M%S")
            self.file_object  = open(os.path.join(self.folderData,self.timestr + '.txt'), "w+")
            self.file_object.write(DEFAULT_DATA_HEADER + "\n")

        
        # SOUND FEEDBACK
        mixer.init()
        self.sound_path = r'.\Sound'
        if not os.path.exists(self.sound_path) and self.use_sound:
            self.loading_sound_on_computer(OPTIONS)
        
        # CLOSE TERMINAL 
        hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        if hwnd != 0 and self.close_cmd:
            ctypes.windll.user32.ShowWindow(hwnd, 0)
            ctypes.windll.kernel32.CloseHandle(hwnd)
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            os.system('taskkill /PID ' + str(pid) + ' /f')
        
        # READING KEYBOARD
        self.keyboard = Controller()

        # HAND USE
        self.labels_fingers = DEFAULT_LABELS_FINGERS

        # [LEAP MOTION] INITIALIZATION
        self.visualizer_open=False
        self.visualizer_closed = False
        
        self.listener,self.controller = self.initialize_leap_motion()
        self.palm, self.distance, self.advance_distance, self.distance_performance   = self.read_values_from_devices(self.listener,self.controller)

        
        # [INTERFACE] - DRAWING PARAMETERS
        self.decisionPressButton = [False,False,False,False,False,False] # Boolean variable to check if we are above the threshold
        self.last_decisionPressButton = self.decisionPressButton[:]
        
        self.prev_condition_press = [0,0,0,0,0,0]                        # Boolean variable to make sure that only one key is pressed
        self.condition_pressed = [0,0,0,0,0,0]

        self.distance_rest = [None,None,None,None,None,None]             # Value to normalize the data to make sure that they are between 0 and 1
        self.distance_rest_default = [25.0,1.5,1.5,1.5,1.5,-70]
        self.advance_distance_rest_default = [25.0,90,100,110,120,200]

        self.distance_init = [0.0,0.0,0.0,0.0,0.0,0.0]                   # Metrics at initialisation (at rest)
        self.distance_hand = [0.0,0.0,0.0,0.0,0.0,0.0]                   # Metrics during the simulation (simple of advance metrics depending on the mode)
        self.subtracted = [0.0,0.0,0.0,0.0,0.0,0.0]                      # distance_hand-distance_init
        
        self.count_slider= [0.0,0.0,0.0,0.0,0.0,0.0]                     # Values of the slider on the interface (value of the treshold)   
        
        
        
        # Save best performance:
        self.performance = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]                 # Performance values (will save maximal displacement of eahc finger)

        # [INTERFACE] - PARAMS INITIALIZATION
        self.nButton = len(self.labels_buttons)                         
        
        self.slider_value = mainwin.bar_origin_threshold[:] 
        mainwin.init_threshold_sliders(values=mainwin.bar_origin_threshold)     # update treshold values on the interface
        self.threshold = mainwin.bar_origin_threshold[:]
    
    

        # selection buttons of the interface
        # sound
        mainwin.Sound.setChecked(self.use_sound)
        

        # which button is pressed
        mainwin.PressButton.setChecked(self.use_setup)


        #show visualizer or not
        mainwin.Visualizer.setChecked(self.show_visualizer)
        

        mainwin.ThumbValue.setValue(0)
        mainwin.IndexValue.setValue(0)
        mainwin.MiddleValue.setValue(0)
        mainwin.RingValue.setValue(0)
        mainwin.PinkyValue.setValue(0)
        mainwin.WristValue.setValue(0)


        #Key board listener for pyinput
        self.keyboard_listener = keyboard.Listener()
        self.keyboard_listener.start()


        #Create thread for run loop
        self._thread  = None
        self._thread = threading.Thread(target=self.run_loop)
        self._thread.start()

    
    def popupmsg(self,msg, title):
        '''
        Make popup message for the performance with tkinter library
        '''
        root = Tk()
        root.title(title)
        label = Label(root, text=msg)
        label.pack(side="top", fill="x", pady=10, padx=50)
        B1 = Button(root, text="Okay", command = root.destroy)
        B1.pack()
        root.mainloop()

    def check_sound_use(self):
        global mainwin
        '''
        Boolean variable, determine whether sound is ON or OFF
        '''
        self.use_sound = mainwin.Sound.isChecked()
        
    def check_setup_use(self):
        global mainwin
        '''
        Boolean variable, determine whether button is pressed or not
        '''
        self.use_setup = mainwin.PressButton.isChecked()
        
    def check_vis_use(self):
        global mainwin
        '''
        Boolean variable
        '''
        self.show_visualizer = mainwin.Visualizer.isChecked()
        if self.show_visualizer :
            if not self.visualizer_open:
                self.move_leap_motion_visualizer()
                self.visualizer_open=True
                self.visualizer_closed = False
        elif not self.visualizer_closed:
            self.visualizer_closed = True
            self.visualizer_open=False
            print("close visualization")
            subprocess.call(["taskkill","/F","/IM",'VRVisualizer.exe'])
    
    def check_mode(self):
        global mainwin
        '''
        Boolean variable, determine whether shifter is ON or OFF
        '''
        self.check_finger_use = (mainwin.ModeSelector.currentText()=='Simple Mode')
            
    
        
    def check_released(self):
        '''
        check if all the keys are released before closing the application 
        '''

        if sum(self.condition_pressed) != 0:
            for i in range(6):
                if self.use_setup and self.condition_pressed[i] == 1:
                    fn_button = DICT_PYNPUT_KEYBOARD[self.labels_buttons[i].lower()]
                    self.keyboard.release(fn_button)
                    print(self.labels_buttons[i] + ' released')



    def on_close(self):
        '''
        closing of the interface
        '''
        # stop the drawing thread.

        global app
        print("**** Exit interface ****")
        self._thread = None
        #make sure that the run loop has finish running
        time.sleep(0.5)
        

        self.controller.remove_listener(self.listener)

        self.check_released()
        print("**** All buttons released ****")

        subprocess.call(["taskkill", "/F", "/IM", 'VRVisualizer.exe'])
        
       #update the config file with the latest value setted by the user 
        self.update_config_file()
    
        date = self.timestr

        #compute the running time of the application 
        self.run_time = (time.time() - self.start_time)
        
        #create and update the perfomance file 
        write_title  = False
        if not os.path.exists(".\performance.txt"):
            write_title  = True
        destFile = r"performance.txt"
        with open(destFile, 'a') as f:
            if write_title  == True:
                f.write('Date; Wrist; Pinky; Ring; Middle; Index; Thumb; Count Value; Run Time\n')
            f.write(date + ';')
            f.write(str(round(self.performance[5], 2)) + ';')
            f.write(str(round(self.performance[4], 2)) + ';')
            f.write(str(round(self.performance[3], 2)) + ';')
            f.write(str(round(self.performance[2], 2)) + ';')
            f.write(str(round(self.performance[1], 2)) + ';')
            f.write(str(round(self.performance[0], 2)) + ";")
            f.write(str(round(self.performance[6], 2)) + ";")
            f.write(str(int(self.run_time)) + "\n")
            
            #launch the popup msg with the best performance recorded
            self.popupmsg(
            'Performance of the day is: \n Wrist: ' + str(int(self.performance[5])) + ' [mm]\n''Pinky: ' + str(
                int(self.performance[4])) + ' [mm]\n' 'Ring: ' + str(
                int(self.performance[3])) + ' [mm]\n' 'Middle: ' + str(
                int(self.performance[2])) + ' [mm]\n' 'Index: ' + str(
                int(self.performance[1])) + ' [mm]\n''Thumb: ' + str(int(self.performance[0])) + ' [mm]\n''Count Value: ' + str(int(self.performance[6])) + '\n' 'Run Time: ' + str(int(self.run_time)) + ' [s]\n',
            'Performance window')
            
        mixer.quit()        
        sys.exit()


    def loading_sound_on_computer(self,OPTIONS):
        '''
        allow to load the sound on the computer by creating a new folder
        '''
        engine = pyttsx3.init(driverName='sapi5')
        print("*** Creating Sound folder ****")
        folderData = ".\Sound"
        if not os.path.exists(folderData):
            os.makedirs(folderData)
        for i,opt in enumerate(OPTIONS):
            print(opt)
            theText = opt
            tts = gTTS(text=theText, lang='en')
            tts.save(os.path.join(folderData,theText + ".mp3"))
        print("File saved!")

    def write_in_text_file(self,filehandle,distance,threshold):
        '''
        write the values of the distance made by the fingers, with the linked threshold
        '''
        filehandle.write(",".join(str(item) for item in np.concatenate((distance,threshold))) + "\n")


    def press_key_on_keyboard(self,keyboard,decisionPressButton,last_decisionPressButton,labels_buttons,condition_press, prev_condition_press):
        '''
        Function to Emulate keyboard
        input: 
        decisionPressButton: array of pinching detection for the different fingers
        labels_buttons: array of labels to press when detection 
        condition_press: variable to make sure that only one kew is pressed at a time
        prev_condition_press: variable to make sure that all the keys are realesed correctly
        
        '''

        for index, (n_choice, o_choice) in enumerate(zip(decisionPressButton, last_decisionPressButton)):
            fn_button = DICT_PYNPUT_KEYBOARD[labels_buttons[index].lower()]
            if fn_button is not None:
                if n_choice and not o_choice:
                    if self.use_setup and condition_press[index] == 1:

                        keyboard.press(fn_button)
                        print(labels_buttons[index] + ' pressed')
                        self.performance[6] += 1

                    if self.use_sound:
                        mixer.music.load(os.path.join(self.sound_path,labels_buttons[index]+'.mp3'))
                        mixer.music.play()

                elif not n_choice and o_choice:
                    if self.use_setup and prev_condition_press[index] == 1:
                        keyboard.release(fn_button)
                        print(labels_buttons[index] + ' released')

    def move_leap_motion_visualizer(self):
        '''
        function to create the visualser window to make sure that hand is detected correctly
        '''
        subprocess.Popen([self.path_leap_folder , '-new-tab'])
        #time sleep necessary to add to make sure that the window will be smaller at the launching of the application (PS: the value can be different from computer to another try different if needed)
        time.sleep(4)

        # # [LEAP MOTION VISUALIZER] - moving window 
        user32 = ctypes.windll.user32
        # get screen resolution of primary monitor
        res = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
        # res is (2293, 960) for 3440x1440 display at 150% scaling
        user32.SetProcessDPIAware()
        res = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
        # res is now (3440, 1440) for 3440x1440 display at 150% scaling
        handle = user32.FindWindowW(None, u'VRVisualizer')
        test=user32.MoveWindow(handle, 5, 0, 705, 620, True)
        print("Moving Leap Motion Visualizer on predefined position")

    # # [LEAP MOTION] - initiation
    
    def initialize_leap_motion(self):
        try:
            listener = LeapMotionListener()
            controller=Leap.Controller()
            controller.add_listener(listener)
        except:
            print("[ERROR] Leap Motion Devices is not connected")
            pass
        return listener,controller

    def read_values_from_devices(self,listener,controller):
        '''
        read the different metrics from leap motion controller using leapMotion_detection.py
        '''
        palm, distance, advance_distance, distance_performance = listener.on_frame(controller)


        return palm, distance, advance_distance, distance_performance

    def update_config_file(self):
        '''
        update the config file with the latest value setted by the user
        '''

        #data for the threshold
        self.slider_value=mainwin.bar_origin_threshold
        data = "[" + str(self.slider_value[0]) + "," + str(self.slider_value[1]) + "," + str(
                self.slider_value[2]) + "," + str(self.slider_value[3]) + "," + str(self.slider_value[4]) + "," + str(
                self.slider_value[5]) + "]"
        self.config.set("drawing", "bar_origin_threshold", data)
       

        #data for the key labels     
        data = "['" + str(self.labels_buttons[0]) + "','" + str(self.labels_buttons[1]) + "','" + str(
            self.labels_buttons[2]) + "','" + str(self.labels_buttons[3]) + "','" + str(
            self.labels_buttons[4]) + "','" + str(self.labels_buttons[5]) + "']"
        self.config.set("options", "labels_buttons", data)

        #data for the key index
        data = "[" + str(mainwin.KeyAllFingersUsedInit[0]) + "," + str(mainwin.KeyAllFingersUsedInit[1]) + "," + str(
            mainwin.KeyAllFingersUsedInit[2]) + "," + str(mainwin.KeyAllFingersUsedInit[3]) + "," + str(
            mainwin.KeyAllFingersUsedInit[4]) + "," + str(mainwin.KeyAllFingersUsedInit[5]) + "]"
        self.config.set("options", "index_buttons", data)

        #write on the config file the latest values
        with open(self.config_file + '.bak', 'w') as configfile:
            self.config.write(configfile)
        if os.path.exists(self.config_file):
            os.remove(self.config_file)  # else rename won't work when target exists
        os.rename(self.config_file + '.bak', self.config_file)
        print("[CONFIG_FILE] Ini file has been updated")


    def run_loop(self):
        '''
        Main loop for the application that receive the measures from leapMotion_detection.py and the keys from mainwindow.py 
        '''
        #starting time for the running 
        self.start_time = time.time()
        global mainwin



        print("**** Start Running interface ****")
        counter_no_data = 0
        counter_init = 0
        previous_index = 0
        

        while self._thread is not None:

            # restart reinitialisation if we press the specific checkbox on the interface 
            if mainwin.reInit == True:
                self.init = True 
                mainwin.reInit = False

            # redo initialisation in case we change mode 
            if previous_index != mainwin.ModeSelector.currentIndex():
                self.init = True
                counter_init = 0
            previous_index = mainwin.ModeSelector.currentIndex()

            # if advance movement select advance distance and advance_distance_rest
            if mainwin.ModeSelector.currentIndex() == 2:
                self.distance_rest = self.advance_distance_rest_default[:]
                self.previous_distance_hand = self.distance_hand
                self.distance_hand  = self.advance_distance[:]
                
                # Put everything back to 0 if no hand is detected
                if self.distance_hand == self.previous_distance_hand:
                    self.distance_hand = self.distance_init

            # if simple movement select distance and distance_rest  
            else:
                self.distance_rest = self.distance_rest_default[:]
                self.previous_distance_hand = self.distance_hand
                self.distance_hand = self.distance[:]
                
                # Put everything back to 0 if no hand is detected
                if self.distance_hand[:] == self.previous_distance_hand[:]:
                    self.distance_hand = self.distance_init

            # check if the button from the interface are pressed correctly : 
            self.check_vis_use()
            self.check_setup_use() 
            self.check_mode()
            self.check_sound_use()

            # Wait 10 frame before finishing the initialisation so that we are sure that the hand is stable (due to leap motion unprecision at the begining)
            if self.init and not None in self.distance_hand :
                counter_init +=1
                if counter_init == 10:
                    self.distance_init=self.distance_hand.copy()
                    self.palm_init = self.palm.copy()
                    counter_init = 0

                    self.init=False

                  

            # Do substraction with the current value and the rest value to be more robust to the threshold detection : 
            if not None in self.distance_hand and not self.init :
                self.subtracted = list()
                    #print('distance_hand',self.distance_hand)
                for item1, item2 in zip(self.distance_init, self.distance_hand):
                    item = item1 - item2
                    self.subtracted.append(item)

            # Check if we need to redo initialisation : 
            if not self.init:
                if not None in self.palm and not None in self.palm_init:
                    array_actual_palm= np.array(self.palm)
                    array_init_palm= np.array(self.palm_init)
                    dist=np.linalg.norm(array_init_palm-array_actual_palm)
                    if dist> 80:
                        self.init=True
                        counter_init=0
                        print('init because of distance')
            
            for i in range(self.nButton):

                #Bar Plot Visualization - continuous
                self.bar_h[i] = 100*(self.subtracted[i]/self.distance_rest[i]) # 1-self.distance_hand[i]/self.distance_rest[i] #generates a segmentation fault

                # Check if we have reach better performance (distance between the actual finger tip and the finger tip at rest) and update it if it is the case
                if not None in self.distance_performance :
                    if self.distance_performance[i] > self.performance[i]:
                        self.performance[i] = self.distance_performance[i]

                self.threshold[i] = self.slider_value[i] #(self.slider_value[i] / 100.0)

                # update condition_press 
                self.prev_condition_press[i] = self.condition_pressed[i]

                # Part to make sure that only one key is pressed at a time 
                if self.bar_h[i] >= self.threshold[i]:
                    if sum(self.condition_pressed) == 0 :
                       
                        self.condition_pressed[i] = 1
                    self.count_slider[i] += 1 

                    self.decisionPressButton[i] = True

                    # Redo initialisation if the key is pressed too much time (mean it is a bug since the user don't want to press a key for a long time)
                    if self.count_slider[i] > 300:
                        
                        self.init = True
                        self.count_slider[i]= 0
            
                else:
                    self.decisionPressButton[i] = False
                    self.count_slider[i] = 0
                    self.condition_pressed[i] = 0

            # send bar_h value to mainwin 
            mainwin.ext.NewFingerValues.emit(self.bar_h.tolist())

            # select the button for each finger corresponding to those chosen on the interface
            for index in range(0, len(self.labels_buttons)):
                self.labels_buttons[index]= OPTIONS[mainwin.FingerKeyNumber[index]]
            
            # press key on the keyboard : 
            self.press_key_on_keyboard(self.keyboard,self.decisionPressButton,self.last_decisionPressButton,self.labels_buttons,self.condition_pressed,self.prev_condition_press)
            # Update press decision :
            self.last_decisionPressButton = self.decisionPressButton[:]

            # If we want to save them, write them in the text file
            if self.record_data:           
                self.write_in_text_file(self.file_object,self.bar_h,self.threshold)

            time.sleep(0.02) # Use to make sure that at each iteration of the run_loop we have the time to extract new values from the leapmotion

    
if __name__=="__main__":
    config_file = r".\config.ini"
    app = QtWidgets.QApplication(sys.argv)

    AnglesValues = QtWidgets.QMainWindow()
    AnglesValues.setWindowIcon(QtGui.QIcon('logo_app.jpg'))
    mainwin = Ui_AnglesValues()
    mainwin.setupUi(AnglesValues)
    AnglesValues.show()
    interface = Interface(config_file)
    Rin = QtWidgets.QWidget()
    Rin.setWindowIcon(QtGui.QIcon('logo_app.jpg'))
    app.aboutToQuit.connect(interface.on_close)
    sys.exit(app.exec_())
