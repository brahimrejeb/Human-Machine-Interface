# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '2windows.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal, QObject
import Settings
from Settings import Ui_Dialog
import time





class External(QObject):
    NewFingerValues = QtCore.pyqtSignal(list)

#    value=0
#    def run(self):
#        while True:
#            self.valueChanged.emit(self.value)

OPTIONS = ['None','Alt','Win',
   'Ctrl','Tab','Shift','Caps','Esc','AltGr']

class Ui_AnglesValues(object):
    def setupUi(self, AnglesValues):
        AnglesValues.setObjectName("AnglesValues")
        AnglesValues.resize(507, 387)
        AnglesValues.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(AnglesValues)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.ModeSelector = QtWidgets.QComboBox(self.centralwidget)
        self.ModeSelector.setObjectName("ModeSelector")
        self.ModeSelector.addItem("")
        self.ModeSelector.addItem("")
        self.ModeSelector.addItem("")
        self.gridLayout.addWidget(self.ModeSelector, 0, 0, 1, 6)
        self.ProgessLayout = QtWidgets.QVBoxLayout()
        self.ProgessLayout.setSpacing(20)
        self.ProgessLayout.setObjectName("ProgessLayout")
        self.ThumbValue = QtWidgets.QProgressBar(self.centralwidget)
        self.ThumbValue.setProperty("value", 0)
        self.ThumbValue.setObjectName("ThumbValue")
        self.ThumbValue.setStyleSheet("QProgressBar::chunk "
                                      "{ "
                                      "background-color: red;"
                                      "text-align: right;"
                                      "}")
        self.ProgessLayout.addWidget(self.ThumbValue)
        self.IndexValue = QtWidgets.QProgressBar(self.centralwidget)
        self.IndexValue.setProperty("value", 0)
        self.IndexValue.setObjectName("IndexValue")
        self.IndexValue.setStyleSheet("QProgressBar::chunk "
                                      "{ "
                                      "background-color: red;"
                                      "text-align: right;"
                                      "}")
        self.ProgessLayout.addWidget(self.IndexValue)
        self.MiddleValue = QtWidgets.QProgressBar(self.centralwidget)
        self.MiddleValue.setProperty("value", 0)
        self.MiddleValue.setObjectName("MiddleValue")
        self.MiddleValue.setStyleSheet("QProgressBar::chunk "
                                      "{ "
                                      "background-color: red;"
                                      "text-align: right;"
                                      "}")
        self.ProgessLayout.addWidget(self.MiddleValue)
        self.RingValue = QtWidgets.QProgressBar(self.centralwidget)
        self.RingValue.setProperty("value", 0)
        self.RingValue.setObjectName("RingValue")
        self.RingValue.setStyleSheet("QProgressBar::chunk "
                                      "{ "
                                      "background-color: red;"
                                      "text-align: right;"
                                      "}")
        self.ProgessLayout.addWidget(self.RingValue)
        self.PinkyValue = QtWidgets.QProgressBar(self.centralwidget)
        self.PinkyValue.setProperty("value", 0)
        self.PinkyValue.setObjectName("PinkyValue")
        self.PinkyValue.setStyleSheet("QProgressBar::chunk "
                                      "{ "
                                      "background-color: red;"
                                      "text-align: right;"
                                      "}")
        self.ProgessLayout.addWidget(self.PinkyValue)
        self.WristValue = QtWidgets.QProgressBar(self.centralwidget)
        self.WristValue.setProperty("value", 0)
        self.WristValue.setStyleSheet("QProgressBar::chunk "
                                      "{ "
                                      "background-color: red;"
                                      "text-align: right;"
                                      "}")
        self.WristValue.setObjectName("WristValue")
        self.ProgessLayout.addWidget(self.WristValue)
        self.gridLayout.addLayout(self.ProgessLayout, 1, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Thumb = QtWidgets.QLabel(self.centralwidget)
        self.Thumb.setObjectName("Thumb")
        self.verticalLayout_4.addWidget(self.Thumb)
        self.ThumbIndex = QtWidgets.QLabel(self.centralwidget)
        self.ThumbIndex.setObjectName("ThumbIndex")
        self.verticalLayout_4.addWidget(self.ThumbIndex)
        self.ThumbMiddle = QtWidgets.QLabel(self.centralwidget)
        self.ThumbMiddle.setObjectName("ThumbMiddle")
        self.verticalLayout_4.addWidget(self.ThumbMiddle)
        self.ThumbRing = QtWidgets.QLabel(self.centralwidget)
        self.ThumbRing.setObjectName("ThumbRing")
        self.verticalLayout_4.addWidget(self.ThumbRing)
        self.ThumbPinky = QtWidgets.QLabel(self.centralwidget)
        self.ThumbPinky.setObjectName("ThumbPinky")
        self.verticalLayout_4.addWidget(self.ThumbPinky)
        self.Fist = QtWidgets.QLabel(self.centralwidget)
        self.Fist.setObjectName("Fist")
        self.verticalLayout_4.addWidget(self.Fist)
        self.gridLayout.addLayout(self.verticalLayout_4, 1, 1, 1, 1)
        self.KeysLayout = QtWidgets.QVBoxLayout()
        self.KeysLayout.setSpacing(20)
        self.KeysLayout.setObjectName("KeysLayout")
        self.ThumbKey = QtWidgets.QComboBox(self.centralwidget)
        self.ThumbKey.setObjectName("ThumbKey")
        self.ThumbKey.addItem("")
        self.ThumbKey.addItem("")
        self.ThumbKey.addItem("")
        self.ThumbKey.addItem("")
        self.ThumbKey.addItem("")
        self.ThumbKey.addItem("")
        self.ThumbKey.addItem("")
        self.ThumbKey.addItem("")
        self.ThumbKey.addItem("")
        self.KeysLayout.addWidget(self.ThumbKey)
        self.IndexKey = QtWidgets.QComboBox(self.centralwidget)
        self.IndexKey.setObjectName("IndexKey")
        self.IndexKey.addItem("")
        self.IndexKey.addItem("")
        self.IndexKey.addItem("")
        self.IndexKey.addItem("")
        self.IndexKey.addItem("")
        self.IndexKey.addItem("")
        self.IndexKey.addItem("")
        self.IndexKey.addItem("")
        self.IndexKey.addItem("")
        self.KeysLayout.addWidget(self.IndexKey)
        self.MiddleKey = QtWidgets.QComboBox(self.centralwidget)
        self.MiddleKey.setObjectName("MiddleKey")
        self.MiddleKey.addItem("")
        self.MiddleKey.addItem("")
        self.MiddleKey.addItem("")
        self.MiddleKey.addItem("")
        self.MiddleKey.addItem("")
        self.MiddleKey.addItem("")
        self.MiddleKey.addItem("")
        self.MiddleKey.addItem("")
        self.MiddleKey.addItem("")
        self.KeysLayout.addWidget(self.MiddleKey)
        self.RingKey = QtWidgets.QComboBox(self.centralwidget)
        self.RingKey.setObjectName("RingKey")
        self.RingKey.addItem("")
        self.RingKey.addItem("")
        self.RingKey.addItem("")
        self.RingKey.addItem("")
        self.RingKey.addItem("")
        self.RingKey.addItem("")
        self.RingKey.addItem("")
        self.RingKey.addItem("")
        self.RingKey.addItem("")
        self.KeysLayout.addWidget(self.RingKey)
        self.PinkyKey = QtWidgets.QComboBox(self.centralwidget)
        self.PinkyKey.setObjectName("PinkyKey")
        self.PinkyKey.addItem("")
        self.PinkyKey.addItem("")
        self.PinkyKey.addItem("")
        self.PinkyKey.addItem("")
        self.PinkyKey.addItem("")
        self.PinkyKey.addItem("")
        self.PinkyKey.addItem("")
        self.PinkyKey.addItem("")
        self.PinkyKey.addItem("")
        self.KeysLayout.addWidget(self.PinkyKey)
        self.WristKey = QtWidgets.QComboBox(self.centralwidget)
        self.WristKey.setObjectName("WristKey")
        self.WristKey.addItem("")
        self.WristKey.addItem("")
        self.WristKey.addItem("")
        self.WristKey.addItem("")
        self.WristKey.addItem("")
        self.WristKey.addItem("")
        self.WristKey.addItem("")
        self.WristKey.addItem("")
        self.WristKey.addItem("")
        self.KeysLayout.addWidget(self.WristKey)
        self.gridLayout.addLayout(self.KeysLayout, 1, 4, 1, 2)
        self.FingersLayout = QtWidgets.QVBoxLayout()
        self.FingersLayout.setSpacing(20)
        self.FingersLayout.setObjectName("FingersLayout")
        self.ThumbLabel = QtWidgets.QLabel(self.centralwidget)
        self.ThumbLabel.setObjectName("ThumbLabel")
        self.FingersLayout.addWidget(self.ThumbLabel)
        self.IndexLabel = QtWidgets.QLabel(self.centralwidget)
        self.IndexLabel.setObjectName("IndexLabel")
        self.FingersLayout.addWidget(self.IndexLabel)
        self.MiddleLabel = QtWidgets.QLabel(self.centralwidget)
        self.MiddleLabel.setObjectName("MiddleLabel")
        self.FingersLayout.addWidget(self.MiddleLabel)
        self.RingLabel = QtWidgets.QLabel(self.centralwidget)
        self.RingLabel.setObjectName("RingLabel")
        self.FingersLayout.addWidget(self.RingLabel)
        self.PinkyLabel = QtWidgets.QLabel(self.centralwidget)
        self.PinkyLabel.setObjectName("PinkyLabel")
        self.FingersLayout.addWidget(self.PinkyLabel)
        self.WristLabel = QtWidgets.QLabel(self.centralwidget)
        self.WristLabel.setObjectName("WristLabel")
        self.FingersLayout.addWidget(self.WristLabel)
        self.gridLayout.addLayout(self.FingersLayout, 1, 2, 1, 1)
        self.LayoutSettings = QtWidgets.QHBoxLayout()
        self.LayoutSettings.setObjectName("LayoutSettings")
        self.PressButton = QtWidgets.QCheckBox(self.centralwidget)
        self.PressButton.setObjectName("PressButton")
        self.LayoutSettings.addWidget(self.PressButton)
        self.Sound = QtWidgets.QCheckBox(self.centralwidget)
        self.Sound.setObjectName("Sound")
        self.LayoutSettings.addWidget(self.Sound)
        self.Visualizer = QtWidgets.QCheckBox(self.centralwidget)
        self.Visualizer.setObjectName("Visualizer")
        self.LayoutSettings.addWidget(self.Visualizer)
        self.Initialization = QtWidgets.QPushButton(self.centralwidget)
        self.Initialization.setObjectName("Initialization")
        self.LayoutSettings.addWidget(self.Initialization)
        self.gridLayout.addLayout(self.LayoutSettings, 4, 0, 1, 2)
        self.LayoutFirstMode = QtWidgets.QHBoxLayout()
        self.LayoutFirstMode.setObjectName("LayoutFirstMode")
        self.PressedKeyLabel = QtWidgets.QLabel(self.centralwidget)
        self.PressedKeyLabel.setObjectName("PressedKeyLabel")
        self.LayoutFirstMode.addWidget(self.PressedKeyLabel)
        self.CurrentKey = QtWidgets.QLabel(self.centralwidget)
        self.CurrentKey.setObjectName("CurrentKey")
        self.LayoutFirstMode.addWidget(self.CurrentKey)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.FingerShifter = QtWidgets.QComboBox(self.centralwidget)
        self.FingerShifter.setObjectName("FingerShifter")
        self.FingerShifter.addItem("")
        self.FingerShifter.addItem("")
        self.FingerShifter.addItem("")
        self.FingerShifter.addItem("")
        self.FingerShifter.addItem("")
        self.FingerShifter.addItem("")
        self.gridLayout_2.addWidget(self.FingerShifter, 0, 1, 1, 1)
        self.ShifterLabel = QtWidgets.QLabel(self.centralwidget)
        self.ShifterLabel.setObjectName("ShifterLabel")
        self.gridLayout_2.addWidget(self.ShifterLabel, 0, 0, 1, 1)
        self.LayoutFirstMode.addLayout(self.gridLayout_2)
        self.gridLayout.addLayout(self.LayoutFirstMode, 2, 0, 1, 1)
        AnglesValues.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AnglesValues)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 507, 21))
        self.menubar.setObjectName("menubar")
        self.menuSetting_2 = QtWidgets.QMenu(self.menubar)
        self.menuSetting_2.setObjectName("menuSetting_2")
        AnglesValues.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AnglesValues)
        self.statusbar.setObjectName("statusbar")
        AnglesValues.setStatusBar(self.statusbar)
        self.actionAcces_setting = QtWidgets.QAction(AnglesValues)
        self.actionAcces_setting.setObjectName("actionAcces_setting")
        self.menuSetting_2.addAction(self.actionAcces_setting)
        self.menubar.addAction(self.menuSetting_2.menuAction())

        self.retranslateUi(AnglesValues)
        QtCore.QMetaObject.connectSlotsByName(AnglesValues)

        #activated current key
        self.FingerKeyNumber=[self.ThumbKey.currentIndex(), self.IndexKey.currentIndex(), self.MiddleKey.currentIndex(), self.RingKey.currentIndex(), self.PinkyKey.currentIndex(), self.WristKey.currentIndex()]
        # Simple mode parameter
        self.currentKeyNumber = 0
        #dialogue window
        self.Dialog = QtWidgets.QDialog()
        self.dia = Ui_Dialog()
        self.dia.setupUi(self.Dialog)
        self.Dialog.setWindowIcon(QtGui.QIcon('logo_app.jpg'))
        self.actionAcces_setting.triggered.connect(self.Dialog.show)

        self.progress_bars=[self.ThumbValue,self.IndexValue,self.MiddleValue,self.RingValue,self.PinkyValue,self.WristValue]

        #threshold:
        self.thresh_thumb=self.dia.ThumbThresh.tickPosition()
        self.thresh_index = self.dia.IndexThresh.tickPosition()
        self.thresh_middle = self.dia.MiddleThresh.tickPosition()
        self.thresh_ring = self.dia.RingThresh.tickPosition()
        self.thresh_pinky = self.dia.PinkyThresh.tickPosition()
        self.thresh_wrist = self.dia.WristThresh.tickPosition()
        self.bar_origin_threshold=[self.thresh_thumb, self.thresh_index, self.thresh_middle, self.thresh_ring, self.thresh_pinky, self.thresh_wrist]


        # Save the states of the keys' functions to init them each time we change the mode
        self.KeyShifterInit = [self.ThumbKey.currentIndex(), self.IndexKey.currentIndex(), self.MiddleKey.currentIndex(), self.RingKey.currentIndex(), self.PinkyKey.currentIndex(), self.WristKey.currentIndex()]
        self.KeyAllFingersUsedInit = [self.ThumbKey.currentIndex(), self.IndexKey.currentIndex(), self.MiddleKey.currentIndex(), self.RingKey.currentIndex(), self.PinkyKey.currentIndex(), self.WristKey.currentIndex()]

        #mode selector box
        self.update_mode()
        self.ModeSelector.currentIndexChanged.connect(self.update_mode)
        self.ModeSelector.currentIndexChanged.connect(self.dia.print_names)

        #was the key activated before
        self.ActivatedFinger=[False, False, False, False, False, False]

        #change the bars value
        self.ext = External()
        self.ext.NewFingerValues.connect(self.ChangingValue)

        #update the thresh values
        self.dia.ThumbThresh.valueChanged.connect(self.update_threshold)
        self.dia.IndexThresh.valueChanged.connect(self.update_threshold)
        self.dia.MiddleThresh.valueChanged.connect(self.update_threshold)
        self.dia.RingThresh.valueChanged.connect(self.update_threshold)
        self.dia.PinkyThresh.valueChanged.connect(self.update_threshold)
        self.dia.WristThresh.valueChanged.connect(self.update_threshold)

        # update selected keys
        self.ThumbKey.currentIndexChanged.connect(self.update_key)
        self.IndexKey.currentIndexChanged.connect(self.update_key)
        self.MiddleKey.currentIndexChanged.connect(self.update_key)
        self.RingKey.currentIndexChanged.connect(self.update_key)
        self.PinkyKey.currentIndexChanged.connect(self.update_key)
        self.WristKey.currentIndexChanged.connect(self.update_key)
        # Re-initialization of measures :
        self.reInit = False
        self.Initialization.clicked.connect(self.set_reInit)



    def set_reInit(self):
        self.reInit = True


    def init_threshold_sliders(self,values):
        self.dia.ThumbThresh.setValue(values[0])
        self.dia.IndexThresh.setValue(values[1])
        self.dia.MiddleThresh.setValue(values[2])
        self.dia.RingThresh.setValue(values[3])
        self.dia.PinkyThresh.setValue(values[4])
        self.dia.WristThresh.setValue(values[5])

    def update_threshold(self):
       self.thresh_thumb = self.dia.ThumbThresh.value()
       self.thresh_index = self.dia.IndexThresh.value()
       self.thresh_middle = self.dia.MiddleThresh.value()
       self.thresh_ring = self.dia.RingThresh.value()
       self.thresh_pinky = self.dia.PinkyThresh.value()
       self.thresh_wrist = self.dia.WristThresh.value()

       self.dia.ThumbThreshValue.setText(str(self.thresh_thumb))
       self.dia.IndexThreshValue.setText(str(self.thresh_index))
       self.dia.MiddleThreshValue.setText(str(self.thresh_middle))
       self.dia.RingThreshValue.setText(str(self.thresh_ring))
       self.dia.PinkyThreshValue.setText(str(self.thresh_pinky))
       self.dia.WristThreshValue.setText(str(self.thresh_wrist))

       self.bar_origin_threshold = [self.thresh_thumb, self.thresh_index, self.thresh_middle, self.thresh_ring, self.thresh_pinky, self.thresh_wrist]

    def update_key(self, index):
        self.FingerKeyNumber = [self.ThumbKey.currentIndex(), self.IndexKey.currentIndex(),
                                self.MiddleKey.currentIndex(), self.RingKey.currentIndex(),
                                self.PinkyKey.currentIndex(), self.WristKey.currentIndex()]
        if self.ModeSelector.currentText() == 'Shifter Mode':
            self.KeyShifterInit=self.FingerKeyNumber
        else:
            self.KeyAllFingersUsedInit=self.FingerKeyNumber

    def check_no_other_finger_pressed(self, value):
        key_released = True
        for i in range(6):
            if i != self.FingerShifter.currentIndex() and int(value[i])> self.bar_origin_threshold[i]:
                key_released = False
        return key_released

    def ChangingValue(self,value):
        self.ThumbValue.setValue(value[0])
        self.IndexValue.setValue(value[1])
        self.MiddleValue.setValue(value[2])
        self.RingValue.setValue(value[3])
        self.PinkyValue.setValue(value[4])
        self.WristValue.setValue(value[5])

        #print('selfqctivstedfinger',self.ActivatedFinger[self.FingerShifter.currentIndex()])
        ''' print('bar_tresh:', self.bar_origin_threshold[self.FingerShifter.currentIndex()])
        print('tresh',self.thresh_thumb)
        print('value',value[self.FingerShifter.currentIndex()])
        print('thumb_value',self.ThumbValue.value())'''

        if self.ModeSelector.currentText() == 'Shifter Mode':
            if not self.ActivatedFinger[self.FingerShifter.currentIndex()]:
                if int(value[self.FingerShifter.currentIndex()])> self.bar_origin_threshold[self.FingerShifter.currentIndex()]:
                    if self.check_no_other_finger_pressed(value):
                        self.currentKeyNumber+=1
                        self.currentKeyNumber = self.currentKeyNumber % len(OPTIONS)
                        self.FingerKeyNumber[0] = self.currentKeyNumber
                        self.FingerKeyNumber[1] = self.currentKeyNumber
                        self.FingerKeyNumber[2] = self.currentKeyNumber
                        self.FingerKeyNumber[3] = self.currentKeyNumber
                        self.FingerKeyNumber[4] = self.currentKeyNumber
                        self.FingerKeyNumber[5] = self.currentKeyNumber
                        self.FingerKeyNumber[self.FingerShifter.currentIndex()] = 0
                        self.ActivatedFinger[self.FingerShifter.currentIndex()] = True
                    #time.sleep(0.2)
                    #if self.currentKeyNumber>=len(OPTIONS):
                 #   self.currentKeyNumber=0
                self.CurrentKey.setText(OPTIONS[self.currentKeyNumber])

        if self.ThumbValue.value() >self.thresh_thumb:
            self.ThumbValue.setStyleSheet("QProgressBar::chunk "
                                      "{ "
                                      "background-color: green;"
                                      "text-align: right;"
                                      "}")
            self.ActivatedFinger[0]=True
        else:
            self.ThumbValue.setStyleSheet("QProgressBar::chunk "
                                      "{ "
                                      "background-color: red;"
                                      "text-align: right;"
                                      "}")
            self.ActivatedFinger[0]= False
        if self.IndexValue.value() >self.thresh_index:
            self.IndexValue.setStyleSheet("QProgressBar::chunk "
                                      "{ "
                                      "background-color: green;"
                                      "text-align: right;"
                                      "}")
            self.ActivatedFinger[1]= True
        else:
            self.IndexValue.setStyleSheet("QProgressBar::chunk "
                                      "{ "
                                      "background-color: red;"
                                      "text-align: right;"
                                      "}")
            self.ActivatedFinger[1]= False
        if self.MiddleValue.value() >self.thresh_middle:
            self.MiddleValue.setStyleSheet("QProgressBar::chunk "
                                      "{ "
                                      "background-color: green;"
                                      "text-align: right;"
                                      "}")
            self.ActivatedFinger[2]=True
        else:
            self.MiddleValue.setStyleSheet("QProgressBar::chunk "
                                      "{ "
                                      "background-color: red;"
                                      "text-align: right;"
                                      "}")
            self.ActivatedFinger[2]= False
        if self.RingValue.value() >self.thresh_ring:
            self.RingValue.setStyleSheet("QProgressBar::chunk "
                                      "{ "
                                      "background-color: green;"
                                      "text-align: right;"
                                      "}")
            self.ActivatedFinger[3]= True
        else:
            self.RingValue.setStyleSheet("QProgressBar::chunk "
                                      "{ "
                                      "background-color: red;"
                                      "text-align: right;"
                                      "}")
            self.ActivatedFinger[3]= False
        if self.PinkyValue.value() >self.thresh_pinky:
            self.PinkyValue.setStyleSheet("QProgressBar::chunk "
                                      "{ "
                                      "background-color: green;"
                                      "text-align: right;"
                                      "}")
            self.ActivatedFinger[4]= True
        else:
            self.PinkyValue.setStyleSheet("QProgressBar::chunk "
                                      "{ "
                                      "background-color: red;"
                                      "text-align: right;"
                                      "}")
            self.ActivatedFinger[4]= False
        if self.WristValue.value() >self.thresh_wrist:
            self.WristValue.setStyleSheet("QProgressBar::chunk "
                                      "{ "
                                      "background-color: green;"
                                      "text-align: right;"
                                      "}")
            self.ActivatedFinger[5]= True
        else:
            self.WristValue.setStyleSheet("QProgressBar::chunk "
                                      "{ "
                                      "background-color: red;"
                                      "text-align: right;"
                                      "}")
            self.ActivatedFinger[5] = False





    def update_mode(self):
        if self.ModeSelector.currentText() == 'All Fingers Mode':
            self.FingerKeyNumber=self.KeyAllFingersUsedInit
            self.CurrentKey.setHidden(True)
            self.ThumbKey.show()
            self.IndexKey.show()
            self.MiddleKey.show()
            self.RingKey.show()
            self.PinkyKey.show()
            self.WristKey.show()
            self.ThumbLabel.setHidden(False)
            self.PressedKeyLabel.setHidden(True)
            self.IndexLabel.setHidden(False)
            self.MiddleLabel.setHidden(False)
            self.RingLabel.setHidden(False)
            self.PinkyLabel.setHidden(False)
            self.WristLabel.setHidden(False)
            self.ShifterLabel.setHidden(True)
            self.FingerShifter.hide()
            self.Thumb.setHidden(True)
            self.ThumbIndex.setHidden(True)
            self.ThumbMiddle.setHidden(True)
            self.ThumbRing.setHidden(True)
            self.ThumbPinky.setHidden(True)
            self.Fist.setHidden(True)
        elif self.ModeSelector.currentText() =='Shifter Mode':
            self.FingerKeyNumber = self.KeyShifterInit
            self.CurrentKey.setHidden(False)
            self.ShifterLabel.setHidden(False)
            self.FingerShifter.show()
            self.ThumbKey.hide()
            self.IndexKey.hide()
            self.MiddleKey.hide()
            self.RingKey.hide()
            self.PinkyKey.hide()
            self.WristKey.hide()
            self.Thumb.setHidden(True)
            self.PressedKeyLabel.setHidden(False)
            self.ThumbIndex.setHidden(True)
            self.ThumbMiddle.setHidden(True)
            self.ThumbRing.setHidden(True)
            self.ThumbPinky.setHidden(True)
            self.Fist.setHidden(True)
            self.ThumbLabel.setHidden(False)
            self.IndexLabel.setHidden(False)
            self.MiddleLabel.setHidden(False)
            self.RingLabel.setHidden(False)
            self.PinkyLabel.setHidden(False)
            self.WristLabel.setHidden(False)
        else:
            self.FingerKeyNumber = self.KeyAllFingersUsedInit
            self.CurrentKey.setHidden(True)
            self.ShifterLabel.setHidden(True)
            self.FingerShifter.hide()
            self.ThumbKey.show()
            self.IndexKey.show()
            self.MiddleKey.show()
            self.RingKey.show()
            self.PinkyKey.show()
            self.WristKey.show()
            self.Thumb.setHidden(False)
            self.PressedKeyLabel.setHidden(True)
            self.ThumbIndex.setHidden(False)
            self.ThumbMiddle.setHidden(False)
            self.ThumbRing.setHidden(False)
            self.ThumbPinky.setHidden(False)
            self.Fist.setHidden(False)
            self.ThumbLabel.setHidden(True)
            self.IndexLabel.setHidden(True)
            self.MiddleLabel.setHidden(True)
            self.RingLabel.setHidden(True)
            self.PinkyLabel.setHidden(True)
            self.WristLabel.setHidden(True)


    def retranslateUi(self, AnglesValues):
        _translate = QtCore.QCoreApplication.translate
        AnglesValues.setWindowTitle(_translate("AnglesValues", "Angle Value"))
        self.ModeSelector.setItemText(0, _translate("AnglesValues", "Shifter Mode"))
        self.ModeSelector.setItemText(1, _translate("AnglesValues", "All fingers used"))
        self.ModeSelector.setItemText(2, _translate("AnglesValues", "Advanced Movements"))
        self.Thumb.setText(_translate("AnglesValues", "Thumb"))
        self.ThumbIndex.setText(_translate("AnglesValues", "Thumb-Index"))
        self.ThumbMiddle.setText(_translate("AnglesValues", "Thumb-Middle"))
        self.ThumbRing.setText(_translate("AnglesValues", "Thumb-Ring"))
        self.ThumbPinky.setText(_translate("AnglesValues", "Thumb-Pinky"))
        self.Fist.setText(_translate("AnglesValues", "Closed fist"))
        self.ThumbKey.setItemText(0, _translate("AnglesValues", "None"))
        self.ThumbKey.setItemText(1, _translate("AnglesValues", "Alt"))
        self.ThumbKey.setItemText(2, _translate("AnglesValues", "Win"))
        self.ThumbKey.setItemText(3, _translate("AnglesValues", "Ctrl"))
        self.ThumbKey.setItemText(4, _translate("AnglesValues", "Tab"))
        self.ThumbKey.setItemText(5, _translate("AnglesValues", "Shift"))
        self.ThumbKey.setItemText(6, _translate("AnglesValues", "Caps"))
        self.ThumbKey.setItemText(7, _translate("AnglesValues", "Esc"))
        self.ThumbKey.setItemText(8, _translate("AnglesValues", "AltGr"))
        self.IndexKey.setItemText(0, _translate("AnglesValues", "None"))
        self.IndexKey.setItemText(1, _translate("AnglesValues", "Alt"))
        self.IndexKey.setItemText(2, _translate("AnglesValues", "Win"))
        self.IndexKey.setItemText(3, _translate("AnglesValues", "Ctrl"))
        self.IndexKey.setItemText(4, _translate("AnglesValues", "Tab"))
        self.IndexKey.setItemText(5, _translate("AnglesValues", "Shift"))
        self.IndexKey.setItemText(6, _translate("AnglesValues", "Caps"))
        self.IndexKey.setItemText(7, _translate("AnglesValues", "Esc"))
        self.IndexKey.setItemText(8, _translate("AnglesValues", "AltGr"))
        self.MiddleKey.setItemText(0, _translate("AnglesValues", "None"))
        self.MiddleKey.setItemText(1, _translate("AnglesValues", "Alt"))
        self.MiddleKey.setItemText(2, _translate("AnglesValues", "Win"))
        self.MiddleKey.setItemText(3, _translate("AnglesValues", "Ctrl"))
        self.MiddleKey.setItemText(4, _translate("AnglesValues", "Tab"))
        self.MiddleKey.setItemText(5, _translate("AnglesValues", "Shift"))
        self.MiddleKey.setItemText(6, _translate("AnglesValues", "Caps"))
        self.MiddleKey.setItemText(7, _translate("AnglesValues", "Esc"))
        self.MiddleKey.setItemText(8, _translate("AnglesValues", "AltGr"))
        self.RingKey.setItemText(0, _translate("AnglesValues", "None"))
        self.RingKey.setItemText(1, _translate("AnglesValues", "Alt"))
        self.RingKey.setItemText(2, _translate("AnglesValues", "Win"))
        self.RingKey.setItemText(3, _translate("AnglesValues", "Ctrl"))
        self.RingKey.setItemText(4, _translate("AnglesValues", "Tab"))
        self.RingKey.setItemText(5, _translate("AnglesValues", "Shift"))
        self.RingKey.setItemText(6, _translate("AnglesValues", "Caps"))
        self.RingKey.setItemText(7, _translate("AnglesValues", "Esc"))
        self.RingKey.setItemText(8, _translate("AnglesValues", "AltGr"))
        self.PinkyKey.setItemText(0, _translate("AnglesValues", "None"))
        self.PinkyKey.setItemText(1, _translate("AnglesValues", "Alt"))
        self.PinkyKey.setItemText(2, _translate("AnglesValues", "Win"))
        self.PinkyKey.setItemText(3, _translate("AnglesValues", "Ctrl"))
        self.PinkyKey.setItemText(4, _translate("AnglesValues", "Tab"))
        self.PinkyKey.setItemText(5, _translate("AnglesValues", "Shift"))
        self.PinkyKey.setItemText(6, _translate("AnglesValues", "Caps"))
        self.PinkyKey.setItemText(7, _translate("AnglesValues", "Esc"))
        self.PinkyKey.setItemText(8, _translate("AnglesValues", "AltGr"))
        self.WristKey.setItemText(0, _translate("AnglesValues", "None"))
        self.WristKey.setItemText(1, _translate("AnglesValues", "Alt"))
        self.WristKey.setItemText(2, _translate("AnglesValues", "Win"))
        self.WristKey.setItemText(3, _translate("AnglesValues", "Ctrl"))
        self.WristKey.setItemText(4, _translate("AnglesValues", "Tab"))
        self.WristKey.setItemText(5, _translate("AnglesValues", "Shift"))
        self.WristKey.setItemText(6, _translate("AnglesValues", "Caps"))
        self.WristKey.setItemText(7, _translate("AnglesValues", "Esc"))
        self.WristKey.setItemText(8, _translate("AnglesValues", "AltGr"))
        self.ThumbLabel.setText(_translate("AnglesValues", "Thumb"))
        self.IndexLabel.setText(_translate("AnglesValues", "Index"))
        self.MiddleLabel.setText(_translate("AnglesValues", "Middle"))
        self.RingLabel.setText(_translate("AnglesValues", "Ring"))
        self.PinkyLabel.setText(_translate("AnglesValues", "Pinky"))
        self.WristLabel.setText(_translate("AnglesValues", "Wrist"))
        self.PressButton.setText(_translate("AnglesValues", "Press Button"))
        self.Sound.setText(_translate("AnglesValues", "Sound"))
        self.Visualizer.setText(_translate("AnglesValues", "Visualizer"))
        self.Initialization.setText(_translate("AnglesValues", "Initialization"))
        self.PressedKeyLabel.setText(_translate("AnglesValues", "Pressed Key:"))
        self.CurrentKey.setText(_translate("AnglesValues", "None"))
        self.FingerShifter.setItemText(0, _translate("AnglesValues", "Thumb"))
        self.FingerShifter.setItemText(1, _translate("AnglesValues", "Index"))
        self.FingerShifter.setItemText(2, _translate("AnglesValues", "Middle"))
        self.FingerShifter.setItemText(3, _translate("AnglesValues", "Ring"))
        self.FingerShifter.setItemText(4, _translate("AnglesValues", "Pinky"))
        self.FingerShifter.setItemText(5, _translate("AnglesValues", "Wrist"))
        self.ShifterLabel.setText(_translate("AnglesValues", "Shifter"))
        self.menuSetting_2.setTitle(_translate("AnglesValues", "Setting"))
        self.actionAcces_setting.setText(_translate("AnglesValues", "Acces setting"))
