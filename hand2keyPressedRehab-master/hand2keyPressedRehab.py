###########################################################
# hand2keyPressedRehab 
# LeapMotion Solution 
# Contact: hackahealth.geneva@gmail.com 
# Autors: Bastien Orset (include your names if you do any collaboration in the code)
###########################################################


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
from pynput.keyboard import Key,KeyCode, Controller
from PIL import Image, ImageTk
from tkinter import *
from PyQt5 import QtCore, QtGui, QtWidgets

import Settings
from Settings import Ui_Dialog
import mainwindows
from mainwindows import Ui_AnglesValues

import PerformanceWindow
from PerformanceWindow import Ui_Rin
#from mainwindows import External


# LIST CMD 
OPTIONS = ['None','Alt','Win',
   'Ctrl','Tab','Shift','Caps','Esc']
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
   'up': Key.up,'left': Key.left,'right':Key.right
}

# LABELS FINGERS
NB_INPUTS=6
DEFAULT_LABELS_FINGERS = ['thumb','index','middle','ring','pinky','wrist']
#DEFAULT_DATA_HEADER_LEFT = "WRIST,PINKY,RING,MIDDLE,INDEX,THUMB,TH_WRIST, TH_PK,TH_RG,TH_MID,TH_IN,TH_THB"
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


        # DEFAULT PARAMS
        #self.hand2use = self.config.get("options","hand2use")
        self.labels_buttons = ast.literal_eval(self.config.get("options", "labels_buttons"))
        # False only for checking script
        #Maybe remove this
        self.use_setup = self.config.getboolean("options","use_setup") 
        self.close_cmd = self.config.getboolean("options","close_cmd")
        # by default the sound is on
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
        mainwin.CurrentKey.setText(OPTIONS[self.current_key])


        # DATA RECORDING
        if self.record_data:
            self.folderData = ".\Data"
            if not os.path.exists(self.folderData):
                os.makedirs(self.folderData)
            self.timestr = time.strftime("%Y%m%d-%H%M%S")
            self.file_object  = open(os.path.join(self.folderData,self.timestr + '.txt'), "w+")
            '''if self.hand2use == 'left':
               self.file_object.write(DEFAULT_DATA_HEADER_LEFT + "\n") 
            else:'''
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
        self.decisionPressButton = [False,False,False,False,False,False]
        self.last_decisionPressButton = self.decisionPressButton[:]
        self.distance_rest = [None,None,None,None,None,None]

        

        '''if self.hand2use == 'left' :
            self.distance_rest_default = [-70,1.5,1.5,1.5,1.5,25.0]#[3.0,3.0,3.0,3.0,100.0]
            self.advance_distance_rest_default = [200,120,110,100,90,25.0]#[3.0,3.0,3.0,3.0,100.0]
        elif self.hand2use == 'right' :'''
        self.distance_rest_default = [25.0,1.5,1.5,1.5,1.5,-70]#[3.0,3.0,3.0,3.0,100.0]
        self.advance_distance_rest_default = [25.0,90,100,110,120,200]#[3.0,3.0,3.0,3.0,100.0]
        self.subtracted = [0.0,0.0,0.0,0.0,0.0,0.0]

        # Save best performance:
        self.performance = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]

        # [INTERFACE] - PARAMS INITIALIZATION
        self.nButton = len(self.labels_buttons)
        self.calibrated = False
        self.slider_value = mainwin.bar_origin_threshold[:] #100- threshold
        mainwin.init_threshold_sliders(values=mainwin.bar_origin_threshold)
        self.threshold = mainwin.bar_origin_threshold[:]
        print('tresh :',self.threshold)
        self.key = 0
        #it corresponds to what?
        self.solution2Use = 0
        self.firstTime = False

        # selection buttons of the interface
        # sound
        mainwin.dia.Sound.setChecked(self.use_sound)
        # check_button = Checkbutton(btm_frame4,bg='Sky Blue', text="Sound", variable=self.var1,command=self.check_sound_use).grid(row=0,column = 0,padx=10)

        # which button is pressed
        mainwin.dia.PressButton.setChecked(self.use_setup)
        # check_button = Checkbutton(btm_frame4,bg='Sky Blue', text="Press Button", variable=self.var2,command=self.check_setup_use).grid(row=0,column = 1,padx=80)

        #show visualizer or not
        mainwin.dia.Visualizer.setChecked(self.show_visualizer)


        mainwin.ThumbValue.setValue(self.slider_value[0])
        mainwin.IndexValue.setValue(self.slider_value[1])
        mainwin.MiddleValue.setValue(self.slider_value[2])
        mainwin.RingValue.setValue(self.slider_value[3])
        mainwin.PinkyValue.setValue(self.slider_value[4])
        mainwin.WristValue.setValue(self.slider_value[5])
        #for i in range(NB_INPUTS):

        
        #    l2 = Label(btm_frame2, bg='Sky Blue', text=self.slider_name[i].lower(),font=("Helvetica", 11))
        #    w2 = Scale(btm_frame2,bg='Sky Blue', from_=0, to=100, orient=HORIZONTAL,length=450,command=self.updata_value_list[i])
        #    w2.set(self.slider_value[i])
        #    l2.grid(row=i, column=0,padx=10)
        #    w2.grid(row=i, column=1,padx=50)
        #    for i in range(5):
        #        var = StringVar(value=self.labels_fingers[i])
        #        o_vars.append(var)
        #        self.o[i] = OptionMenu(btm_frame3, var, *OPTIONS,command=self.on_button_list[i])
        #        self.o[i].grid(row=0, column=i)

        #var2 = IntVar()
        #Checkbutton(btm_frame4, text="Button", variable=var2).grid(row=0,column = 2)
        #Button(btm_frame4, text='Calibration',height=2,width=30).grid(row=0,padx=60)

        #mainwin.update_progress()

        self._thread  = None
        self._thread = threading.Thread(target=self.run_loop)
        self._thread.start()
        

        #self.protocol("WM_DELETE_WINDOW",self.on_close)
        # RUN MAIN LOOP
        #self.mainloop()

    def popupmsg(self,msg, title):
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
        self.use_sound = mainwin.dia.Sound.isChecked()
        
    def check_setup_use(self):
        global mainwin
        '''
        Boolean variable, determine whether button is pressed or not
        '''
        self.use_setup = mainwin.dia.PressButton.isChecked()
        
    def check_vis_use(self):
        global mainwin
        '''
        Boolean variable
        '''
        self.show_visualizer = mainwin.dia.Visualizer.isChecked()
        if self.show_visualizer :
            if not self.visualizer_open:
                self.move_leap_motion_visualizer()
                self.visualizer_open=True
                self.visualizer_closed = False
        elif not self.visualizer_closed:
            self.visualizer_closed = True
            self.visualizer_open=False
            print("close visualization")
            subprocess.call(["taskkill","/F","/IM",'Visualizer.exe'])
    
    def check_mode(self):
        global mainwin
        '''
        Boolean variable, determine whether shifter is ON or OFF
        '''
        self.check_finger_use = (mainwin.ModeSelector.currentText()=='Simple Mode')
            
            # subprocess.Popen(['C:\\Program Files (x86)\\Leap Motion\\Core Services\\Visualizer.exe', '-new-tab'])
        
    '''
    get the values of the slider threshold for each finger
    '''    
    #def updata_value(self,selection):self.slider_value[0] = int(selection)
    #def updata_value1(self,selection):self.slider_value[1] = int(selection)
    #def updata_value2(self,selection):self.slider_value[2] = int(selection)
    #def updata_value3(self,selection):self.slider_value[3] = int(selection)
    #def updata_value4(self,selection):self.slider_value[4] = int(selection)
    
    '''
    What value is pressed by each finger, value store into a list 
    '''
    #def on_button(self,selection):self.labels_buttons[0] = selection
    #def on_button1(self,selection):self.labels_buttons[1] = selection
    #def on_button2(self,selection):self.labels_buttons[2] = selection
    #def on_button3(self,selection):self.labels_buttons[3] = selection
    #def on_button4(self,selection):self.labels_buttons[4] = selection
             

    # def exitui(self):
    def on_close(self):
        '''
        closing of the interface
        '''
        # stop the drawing thread.

        global app
        print("**** Exit interface ****")
        if self.keyboard.shift_pressed:
            self.keyboard.release(Key.shift_l)
            print("release shift")
        if self.keyboard.alt_pressed:
            self.keyboard.release(Key.alt_l)
            print("release alt")
        if self.keyboard.ctrl_pressed:
            self.keyboard.release(Key.ctrl_l)
            print("release ctrl")
        self.controller.remove_listener(self.listener)

        Rin = QtWidgets.QWidget()
        Rin.setWindowIcon(QtGui.QIcon('th.png'))
        PerformancePopUp = Ui_Rin()
        PerformancePopUp.setupUi(Rin, self.performance)
        Rin.show()

        subprocess.call(["taskkill", "/F", "/IM", 'Visualizer.exe'])
        self._thread = None
        self.update_config_file()
        date = self.timestr[6:8] + '/' + self.timestr[4:6] + '/' + self.timestr[:4] + ' ' + 'at' + ' ' + self.timestr[
                                                                                                         9:11] + 'h' + self.timestr[
                                                                                                                       11:13] + 'm' + ' :'
        '''if self.hand2use == 'left':
            self.popupmsg(
                'Performance of the day is: \n Wrist: ' + str(int(self.performance[0])) + 'mm\n''Pinky: ' + str(
                    int(self.performance[1])) + 'mm\n' 'Ring: ' + str(
                    int(self.performance[2])) + 'mm\n' 'Middle: ' + str(
                    int(self.performance[3])) + 'mm\n' 'Index: ' + str(
                    int(self.performance[4])) + 'mm\n''Thumb: ' + str(int(self.performance[5])) + 'mm\n',
                'Performance window')
        else:'''
        self.popupmsg(
                'Performance of the day is: \n Wrist: ' + str(int(self.performance[5])) + 'mm\n''Pinky: ' + str(
                    int(self.performance[4])) + 'mm\n' 'Ring: ' + str(
                    int(self.performance[3])) + 'mm\n' 'Middle: ' + str(
                    int(self.performance[2])) + 'mm\n' 'Index: ' + str(
                    int(self.performance[1])) + 'mm\n''Thumb: ' + str(int(self.performance[0])) + 'mm\n',
                'Performance window')


        destFile = r"performance.txt"
        with open(destFile, 'a') as f:
            '''if self.hand2use == 'left':
                f.write(date)
                f.write(str(round(self.performance[0], 2)) + '(W),')
                f.write(str(round(self.performance[1], 2)) + '(P),')
                f.write(str(round(self.performance[2], 2)) + '(R),')
                f.write(str(round(self.performance[3], 2)) + '(M),')
                f.write(str(round(self.performance[4], 2)) + '(I),')
                f.write(str(round(self.performance[5], 2)) + "(T)\n")
            else:'''
            f.write(date)
            f.write(str(round(self.performance[5], 2)) + '(W),')
            f.write(str(round(self.performance[4], 2)) + '(P),')
            f.write(str(round(self.performance[3], 2)) + '(R),')
            f.write(str(round(self.performance[2], 2)) + '(M),')
            f.write(str(round(self.performance[1], 2)) + '(I),')
            f.write(str(round(self.performance[0], 2)) + "(T)\n")
            f.write(str(round(self.performance[6], 2)) + "(C)\n")


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

    '''def define_labels_fingers_based_onhand(self,DEFAULT_LABELS_FINGERS):
        
        label each fingers based on which hand it is
        print which hand is used on the terminal
        return the fingers labels in the right way
        
        #if self.hand2use == 'right':
         #   print("R")
        labels_fingers = DEFAULT_LABELS_FINGERS
        #elif self.hand2use == 'left':
         #   print("L")
          #  labels_fingers = DEFAULT_LABELS_FINGERS[::-1]
        print(labels_fingers)
        return labels_fingers'''
    
    def press_key_on_keyboard(self,keyboard,decisionPressButton,last_decisionPressButton,labels_buttons):
        '''
        Function to Emulate keyboard
        input: 
        decisionPressButton: array of pinching detection for the different fingers
        labels_buttons: array of labels to press when detection 
        
        if the button was activated the last time the programm call this loop, the button is released
        '''
        for index, (n_choice, o_choice) in enumerate(zip(decisionPressButton, last_decisionPressButton)):
            fn_button = DICT_PYNPUT_KEYBOARD[labels_buttons[index].lower()]
            if fn_button is not None:
                if n_choice and not o_choice:
                    if self.use_setup:
                        keyboard.press(fn_button)
                        print(labels_buttons[index] + ' pressed')
                        self.performance[6] += 1
                    if self.use_sound:
                        mixer.music.load(os.path.join(self.sound_path,labels_buttons[index]+'.mp3'))
                        mixer.music.play()
                elif not n_choice and o_choice:
                    if self.use_setup:
                        keyboard.release(fn_button)
                        print(labels_buttons[index] + ' released')

    def move_leap_motion_visualizer(self):
        subprocess.Popen([self.path_leap_folder , '-new-tab'])
        time.sleep(0.1)
        # # [LEAP MOTION VISUALIZER] - moving window 
        user32 = ctypes.windll.user32
        # get screen resolution of primary monitor
        res = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
        # res is (2293, 960) for 3440x1440 display at 150% scaling
        user32.SetProcessDPIAware()
        res = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
        # res is now (3440, 1440) for 3440x1440 display at 150% scaling
        handle = user32.FindWindowW(None, u'Leap Motion Diagnostic Visualizer')
        user32.ShowWindow(handle, 6)
        user32.ShowWindow(handle, 9)
        user32.ShowWindow(handle, 1)
        user32.MoveWindow(handle, 5, 0, 705, 620, True)
        print("Moving Leap Motion Visualizer on predefined position")
        
        for i in range(3):
           self.keyboard.press('v')
           self.keyboard.release('v')
        
        for i in range(5):
           self.keyboard.press(KeyCode.from_char('='))
           self.keyboard.release(KeyCode.from_char('='))
        self.keyboard.press('c')
        self.keyboard.release('c')
        self.keyboard.press('g')
        self.keyboard.release('g')
    #     self.keyboard.press(KeyCode.from_char('='))
    #     self.keyboard.release(KeyCode.from_char('='))
    #     self.keyboard.press(KeyCode.from_char('='))
    #     self.keyboard.release(KeyCode.from_char('='))
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
        palm, distance, advance_distance, distance_performance = listener.on_frame(controller)
        #print('read distance', distance)
        #print('read palm position', palm)
        # if self.advanced_mode :
        #    distance = advance_distance

        return palm, distance, advance_distance, distance_performance

    def loading_pic_from_folder(self,pathFolderPicture,dim_pic):
        """NOT USED in this version"""
        pic_img = []
        for file in os.listdir(pathFolderPicture):
            if file.endswith(".png"):
                file_path = os.path.join(pathFolderPicture, file)
                print(file_path) 
                f = cv2.imread(file_path)
                f = cv2.resize(f, dim_pic)
                pic_img.append(f)
        return pic_img

    def update_config_file(self):
        self.slider_value=mainwin.bar_origin_threshold
        #if self.hand2use == 'right':
        data = "[" + str(self.slider_value[0]) + "," + str(self.slider_value[1]) + "," + str(
                self.slider_value[2]) + "," + str(self.slider_value[3]) + "," + str(self.slider_value[4]) + "," + str(
                self.slider_value[5]) + "]"
        self.config.set("drawing", "bar_origin_threshold", data)
        '''if self.hand2use == 'left':
            data = "[" + str(self.slider_value[5]) + "," + str(self.slider_value[4]) + "," + str(
                self.slider_value[3]) + "," + str(self.slider_value[2]) + "," + str(self.slider_value[1]) + "," + str(
                self.slider_value[0]) + "]"
            self.config.set("drawing", "bar_origin_threshold", data)'''

        data = "['" + str(self.labels_buttons[0]) + "','" + str(self.labels_buttons[1]) + "','" + str(
            self.labels_buttons[2]) + "','" + str(self.labels_buttons[3]) + "','" + str(
            self.labels_buttons[4]) + "','" + str(self.labels_buttons[5]) + "']"
        self.config.set("options", "labels_buttons", data)

        with open(self.config_file + '.bak', 'w') as configfile:
            self.config.write(configfile)
        if os.path.exists(self.config_file):
            os.remove(self.config_file)  # else rename won't work when target exists
        os.rename(self.config_file + '.bak', self.config_file)
        print("[CONFIG_FILE] Ini file has been updated")


    def run_loop(self):
        global mainwin


        print("**** Start Running interface ****")
        #img = np.zeros((self.img_h,self.img_v,3), np.uint8)
        counter_no_data = 0
        counter_init = 0
        previous_index = 0
        while self._thread is not None:
            if previous_index != mainwin.ModeSelector.currentIndex():
                self.init = True
            previous_index = mainwin.ModeSelector.currentIndex()
            if mainwin.ModeSelector.currentIndex() == 2:
                self.distance_rest = self.advance_distance_rest_default[:]
                self.distance = self.advance_distance[:]
            else:
                self.distance_rest = self.distance_rest_default[:]
           
                
            self.check_vis_use()
            self.check_setup_use() #button press
            self.check_mode()
            if self.init and not None in self.distance :
                counter_init +=1
                if counter_init == 10:
                    self.distance_init=self.distance.copy()
                    self.palm_init = self.palm.copy()
                    counter_init = 0

                    self.init=False

                    #print('self.distance_init',self.distance_init)
                    #print('self.palm.init',self.palm_init)

            self.key = cv2.waitKeyEx(1) #maybe remove this


            #if self.hand2use == 'right':
            self.distance_hand = self.distance[:] #- self.distance_init[:]
            if not None in self.distance_hand and not self.init :
                self.subtracted = list()
                    #print('distance_hand',self.distance_hand)
                for item1, item2 in zip(self.distance_init, self.distance_hand):
                    item = item1 - item2
                    self.subtracted.append(item)
            '''elif self.hand2use == 'left':
                self.distance_hand = self.distance[::-1]# - self.distance_init[::-1]
                if not None in self.distance_hand and not self.init :
                    #print('distance_hand',self.distance_hand)
                    self.subtracted = list()
                    for item1, item2 in zip(self.distance_init[::-1], self.distance_hand):
                        item = item1 - item2
                        self.subtracted.append(item)'''

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

            if None in self.distance_hand:
                self.calibrated = False
                counter_no_data += 1
                if counter_no_data == 1:
                    pass
                    #print("Waiting for values from LeapMotion")
                elif counter_no_data == 5:
                    #cv2.putText(img,"Waiting for LeapMotion ...",(self.circle_first_coord+20,self.circle_y),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255))
                    #img_ = Image.fromarray(img)
                    #nimg = ImageTk.PhotoImage(image=img_)
                    #self.v1.n_img = nimg
                    #self.v1.configure(image=nimg)
                    # make initialisation 
                    self.init=True
                    counter_init=0
                continue
            else:
                counter_no_data = 0
                #print('substracted',self.subtracted)
                #print('distance_init',self.distance_init)
            # print('difference', difference)

            # if (not self.calibrated and None not in self.distance_hand):
            #     # if s2 == 1: 
            #     #     self.distance_rest = self.distance_hand[:]
            #     # else:
            #     self.distance_rest = self.distance_rest_default[:]
            #     print(self.distance_rest)
            #     self.calibrated = True



            #print(self.subtracted[0] / self.distance_rest[0])
            #External.value=int(self.bar_h[0]*100)
            for i in range(self.nButton):
                # Labelling 
                #coord = self.circle_first_coord + i*self.circle_space
                #cv2.putText(img,self.labels_fingers[i],(coord-30,self.circle_y-50),cv2.FONT_HERSHEY_SIMPLEX,0.8,self.text_color)

                #Bar Plot Visualization - continuous
                self.bar_h[i] = 100*(self.subtracted[i]/self.distance_rest[i]) # 1-self.distance_hand[i]/self.distance_rest[i] #generates a segmentation fault
                if not None in self.distance_performance :
                    if self.distance_performance[i] > self.performance[i]:
                        self.performance[i] = self.distance_performance[i]

                self.threshold[i] = self.slider_value[i] #(self.slider_value[i] / 100.0)


                #External.value=self.bar_h[0] #test
                #cv2.rectangle(img, (coord-30,self.img_h), (coord+30,self.img_h-int(self.bar_h[i]*self.bar_max)), self.bar_color, -1)
                #cv2.line(img, (coord-20,self.img_h-int(self.threshold[i]*self.bar_max)), (coord+20,self.img_h-int(self.threshold[i]*self.bar_max)), self.bar_color_th, 3)

                # Boolean Visualization  - discrete
                if self.bar_h[i] >= self.threshold[i]:
            #    cv2.circle(img, (coord,self.circle_y), self.circle_radius, self.text_color_selec, self.circle_thickness)
                     self.decisionPressButton[i] = True
            #    cv2.putText(img,self.labels_buttons[i],(coord-30,self.circle_y-150),cv2.FONT_HERSHEY_SIMPLEX,1,self.text_color_selec)
            #    cv2.rectangle(img, (coord-30-30,self.circle_y-150-50), (coord-40+70,self.circle_y-150+50), self.text_color_selec, 3)
                else:
                     self.decisionPressButton[i] = False
            #    cv2.putText(img,self.labels_buttons[i],(coord-30,self.circle_y-150),cv2.FONT_HERSHEY_SIMPLEX,1,self.text_color_selec)
            #    cv2.circle(img, (coord,self.circle_y), self.circle_radius, self.circle_color, self.circle_thickness)

            mainwin.ext.NewFingerValues.emit(self.bar_h.tolist())
            # Keyboard Pressing/Release Process
            '''if self.check_finger_use:
                if self.decisionPressButton[5] and not self.last_decisionPressButton[5]:
                    self.current_key+=1
                    self.current_key= self.current_key % len(OPTIONS)
                    self.labels_buttons[5]= OPTIONS[0]
                    for index in range(0, len(self.labels_buttons)-1):
                        self.labels_buttons[index]= OPTIONS[self.current_key]'''

            #
            # 
            #print('mainwin : ',mainwin.FingerKeyNumber)   
            # get label button fron mainzwin 
            for index in range(0, len(self.labels_buttons)):
                self.labels_buttons[index]= OPTIONS[mainwin.FingerKeyNumber[index]]
            
            self.press_key_on_keyboard(self.keyboard,self.decisionPressButton,self.last_decisionPressButton,self.labels_buttons)
            self.last_decisionPressButton = self.decisionPressButton[:]

            if self.record_data:
                # print(self.bar_h,self.threshold)
                self.write_in_text_file(self.file_object,self.bar_h,self.threshold)


            #img_ = Image.fromarray(img)
            #nimg = ImageTk.PhotoImage(image=img_)
            #self.v1.n_img = nimg
            #self.v1.configure(image=nimg)

            #self.after(self.refresh_rate)
            #img*=0
    
if __name__=="__main__":
    config_file = r".\config.ini"
    app = QtWidgets.QApplication(sys.argv)

    AnglesValues = QtWidgets.QMainWindow()
    AnglesValues.setWindowIcon(QtGui.QIcon('th.png'))
    mainwin = Ui_AnglesValues()
    mainwin.setupUi(AnglesValues)
    AnglesValues.show()
    interface = Interface(config_file)
    app.aboutToQuit.connect(interface.on_close)
    app.exec_()