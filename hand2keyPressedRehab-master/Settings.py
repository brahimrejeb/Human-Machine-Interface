# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hand2key2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal, QObject

class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(299, 324)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.SettingLayout = QtWidgets.QVBoxLayout()
        self.SettingLayout.setObjectName("SettingLayout")
        self.SettingTitle = QtWidgets.QLabel(Dialog)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(23, 10, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(23, 10, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(23, 10, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(23, 10, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(23, 10, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(23, 10, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.SettingTitle.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SettingTitle.setFont(font)
        self.SettingTitle.setObjectName("SettingTitle")
        self.SettingLayout.addWidget(self.SettingTitle)
        self.PressButton = QtWidgets.QCheckBox(Dialog)
        self.PressButton.setObjectName("PressButton")
        self.SettingLayout.addWidget(self.PressButton)
        self.Sound = QtWidgets.QCheckBox(Dialog)
        self.Sound.setObjectName("Sound")
        self.SettingLayout.addWidget(self.Sound)
        self.Visualizer = QtWidgets.QCheckBox(Dialog)
        self.Visualizer.setObjectName("Visualizer")
        self.SettingLayout.addWidget(self.Visualizer)
        self.gridLayout.addLayout(self.SettingLayout, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.ThumbThresh = QtWidgets.QSlider(Dialog)
        self.ThumbThresh.setOrientation(QtCore.Qt.Horizontal)
        self.ThumbThresh.setObjectName("ThumbThresh")
        self.verticalLayout.addWidget(self.ThumbThresh)
        self.IndexThresh = QtWidgets.QSlider(Dialog)
        self.IndexThresh.setOrientation(QtCore.Qt.Horizontal)
        self.IndexThresh.setObjectName("IndexThresh")
        self.verticalLayout.addWidget(self.IndexThresh)
        self.MiddleThresh = QtWidgets.QSlider(Dialog)
        self.MiddleThresh.setOrientation(QtCore.Qt.Horizontal)
        self.MiddleThresh.setObjectName("MiddleThresh")
        self.verticalLayout.addWidget(self.MiddleThresh)
        self.RingThresh = QtWidgets.QSlider(Dialog)
        self.RingThresh.setOrientation(QtCore.Qt.Horizontal)
        self.RingThresh.setObjectName("RingThresh")
        self.verticalLayout.addWidget(self.RingThresh)
        self.PinkyThresh = QtWidgets.QSlider(Dialog)
        self.PinkyThresh.setOrientation(QtCore.Qt.Horizontal)
        self.PinkyThresh.setObjectName("PinkyThresh")
        self.verticalLayout.addWidget(self.PinkyThresh)
        self.WristThresh = QtWidgets.QSlider(Dialog)
        self.WristThresh.setOrientation(QtCore.Qt.Horizontal)
        self.WristThresh.setObjectName("WristThresh")
        self.verticalLayout.addWidget(self.WristThresh)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 2)
        self.SimpleModeLayout = QtWidgets.QVBoxLayout()
        self.SimpleModeLayout.setObjectName("SimpleModeLayout")
        self.space = QtWidgets.QLabel(Dialog)
        self.space.setText("")
        self.space.setObjectName("space")
        self.SimpleModeLayout.addWidget(self.space)
        self.ThumbLabel = QtWidgets.QLabel(Dialog)
        self.ThumbLabel.setObjectName("ThumbLabel")
        self.SimpleModeLayout.addWidget(self.ThumbLabel)
        self.IndexLabel = QtWidgets.QLabel(Dialog)
        self.IndexLabel.setObjectName("IndexLabel")
        self.SimpleModeLayout.addWidget(self.IndexLabel)
        self.MiddleLabel = QtWidgets.QLabel(Dialog)
        self.MiddleLabel.setObjectName("MiddleLabel")
        self.SimpleModeLayout.addWidget(self.MiddleLabel)
        self.RingLabel = QtWidgets.QLabel(Dialog)
        self.RingLabel.setObjectName("RingLabel")
        self.SimpleModeLayout.addWidget(self.RingLabel)
        self.PinkyLabel = QtWidgets.QLabel(Dialog)
        self.PinkyLabel.setObjectName("PinkyLabel")
        self.SimpleModeLayout.addWidget(self.PinkyLabel)
        self.WristLabel = QtWidgets.QLabel(Dialog)
        self.WristLabel.setObjectName("WristLabel")
        self.SimpleModeLayout.addWidget(self.WristLabel)
        self.gridLayout.addLayout(self.SimpleModeLayout, 1, 2, 1, 1)
        self.AdvancedLayout = QtWidgets.QVBoxLayout()
        self.AdvancedLayout.setObjectName("AdvancedLayout")
        self.space_2 = QtWidgets.QLabel(Dialog)
        self.space_2.setText("")
        self.space_2.setObjectName("space_2")
        self.AdvancedLayout.addWidget(self.space_2)
        self.ThumbAdvanced = QtWidgets.QLabel(Dialog)
        self.ThumbAdvanced.setObjectName("ThumbAdvanced")
        self.AdvancedLayout.addWidget(self.ThumbAdvanced)
        self.ThumbIndex = QtWidgets.QLabel(Dialog)
        self.ThumbIndex.setObjectName("ThumbIndex")
        self.AdvancedLayout.addWidget(self.ThumbIndex)
        self.ThumbMiddle = QtWidgets.QLabel(Dialog)
        self.ThumbMiddle.setObjectName("ThumbMiddle")
        self.AdvancedLayout.addWidget(self.ThumbMiddle)
        self.ThumbRing = QtWidgets.QLabel(Dialog)
        self.ThumbRing.setObjectName("ThumbRing")
        self.AdvancedLayout.addWidget(self.ThumbRing)
        self.ThumbPinky = QtWidgets.QLabel(Dialog)
        self.ThumbPinky.setObjectName("ThumbPinky")
        self.AdvancedLayout.addWidget(self.ThumbPinky)
        self.Fist = QtWidgets.QLabel(Dialog)
        self.Fist.setObjectName("Fist")
        self.AdvancedLayout.addWidget(self.Fist)
        self.gridLayout.addLayout(self.AdvancedLayout, 1, 3, 1, 1)
        self.Ok = QtWidgets.QPushButton(Dialog)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.Ok.setPalette(palette)
        self.Ok.setObjectName("Ok")
        self.gridLayout.addWidget(self.Ok, 2, 1, 1, 1)

        self.Ok.clicked.connect(Dialog.reject)

        self.ThumbLabel.setHidden(False)
        self.IndexLabel.setHidden(False)
        self.MiddleLabel.setHidden(False)
        self.RingLabel.setHidden(False)
        self.PinkyLabel.setHidden(False)
        self.WristLabel.setHidden(False)
        self.space.setHidden(False)
        self.ThumbAdvanced.setHidden(True)
        self.ThumbIndex.setHidden(True)
        self.ThumbMiddle.setHidden(True)
        self.ThumbRing.setHidden(True)
        self.ThumbPinky.setHidden(True)
        self.space_2.setHidden(True)
        self.Fist.setHidden(True)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def print_names(self, signal):
        if signal==0 or signal==1:
            self.ThumbLabel.setHidden(False)
            self.IndexLabel.setHidden(False)
            self.MiddleLabel.setHidden(False)
            self.RingLabel.setHidden(False)
            self.space.setHidden(False)
            self.PinkyLabel.setHidden(False)
            self.WristLabel.setHidden(False)
            self.ThumbAdvanced.setHidden(True)
            self.ThumbIndex.setHidden(True)
            self.ThumbMiddle.setHidden(True)
            self.ThumbRing.setHidden(True)
            self.ThumbPinky.setHidden(True)
            self.Fist.setHidden(True)
            self.space_2.setHidden(True)
        else:
            self.ThumbLabel.setHidden(True)
            self.IndexLabel.setHidden(True)
            self.MiddleLabel.setHidden(True)
            self.RingLabel.setHidden(True)
            self.PinkyLabel.setHidden(True)
            self.WristLabel.setHidden(True)
            self.space.setHidden(True)
            self.ThumbAdvanced.setHidden(False)
            self.ThumbIndex.setHidden(False)
            self.ThumbMiddle.setHidden(False)
            self.ThumbRing.setHidden(False)
            self.ThumbPinky.setHidden(False)
            self.Fist.setHidden(False)
            self.space_2.setHidden(False)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.SettingTitle.setText(_translate("Dialog", "Setting"))
        self.PressButton.setText(_translate("Dialog", "Press Button"))
        self.Sound.setText(_translate("Dialog", "Sound"))
        self.Visualizer.setText(_translate("Dialog", "Visualizer"))
        self.label.setText(_translate("Dialog", "Thresholds"))
        self.ThumbLabel.setText(_translate("Dialog", "Thumb"))
        self.IndexLabel.setText(_translate("Dialog", "Index"))
        self.MiddleLabel.setText(_translate("Dialog", "Middle"))
        self.RingLabel.setText(_translate("Dialog", "Ring"))
        self.PinkyLabel.setText(_translate("Dialog", "Pinky"))
        self.WristLabel.setText(_translate("Dialog", "Wrist"))
        self.ThumbAdvanced.setText(_translate("Dialog", "Thumb"))
        self.ThumbIndex.setText(_translate("Dialog", "Thumb-Index"))
        self.ThumbMiddle.setText(_translate("Dialog", "Thumb-Middle"))
        self.ThumbRing.setText(_translate("Dialog", "Thumb-Ring"))
        self.ThumbPinky.setText(_translate("Dialog", "Thumb-Pinky"))
        self.Fist.setText(_translate("Dialog", "Fist"))
        self.Ok.setText(_translate("Dialog", "Ok"))





