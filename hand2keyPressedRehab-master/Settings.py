# -*- coding: utf-8 -*-
#Authors: Odile Andres, Nada Guerraoui, Thomas Peeters, Brahim Rejeb (V2)
# (include your names if you do any collaboration in the code)
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
        '''
        creation of the elements of the setting window
        '''
        Dialog.setObjectName("Dialog")
        Dialog.resize(336, 243)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.SimpleModeLayout = QtWidgets.QVBoxLayout()

        #finger labels for simple and all fingers modes
        self.SimpleModeLayout.setObjectName("SimpleModeLayout")
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
        self.gridLayout.addLayout(self.SimpleModeLayout, 1, 3, 1, 1)

        #movements label for advanced mode
        self.AdvancedLayout = QtWidgets.QVBoxLayout()
        self.AdvancedLayout.setObjectName("AdvancedLayout")
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
        self.gridLayout.addLayout(self.AdvancedLayout, 1, 4, 1, 1)

        #threshold value label
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ThumbThreshValue = QtWidgets.QLabel(Dialog)
        self.ThumbThreshValue.setObjectName("ThumbThreshValue")
        self.verticalLayout_2.addWidget(self.ThumbThreshValue)
        self.IndexThreshValue = QtWidgets.QLabel(Dialog)
        self.IndexThreshValue.setObjectName("IndexThreshValue")
        self.verticalLayout_2.addWidget(self.IndexThreshValue)
        self.MiddleThreshValue = QtWidgets.QLabel(Dialog)
        self.MiddleThreshValue.setObjectName("MiddleThreshValue")
        self.verticalLayout_2.addWidget(self.MiddleThreshValue)
        self.RingThreshValue = QtWidgets.QLabel(Dialog)
        self.RingThreshValue.setObjectName("RingThreshValue")
        self.verticalLayout_2.addWidget(self.RingThreshValue)
        self.PinkyThreshValue = QtWidgets.QLabel(Dialog)
        self.PinkyThreshValue.setObjectName("PinkyThreshValue")
        self.verticalLayout_2.addWidget(self.PinkyThreshValue)
        self.WristThreshValue = QtWidgets.QLabel(Dialog)
        self.WristThreshValue.setObjectName("WristThreshValue")
        self.verticalLayout_2.addWidget(self.WristThreshValue)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 2, 1, 1)

        #OK button
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Ok = QtWidgets.QPushButton(Dialog)

        #color code of the window
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
        self.horizontalLayout.addWidget(self.Ok)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 2, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)

        # threshold slider
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
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

        #when OK clicked, the window closed
        self.Ok.clicked.connect(Dialog.reject)

        #by default the setting window present the simple and all fingers design
        self.ThumbLabel.setHidden(False)
        self.IndexLabel.setHidden(False)
        self.MiddleLabel.setHidden(False)
        self.RingLabel.setHidden(False)
        self.PinkyLabel.setHidden(False)
        self.WristLabel.setHidden(False)
        self.ThumbAdvanced.setHidden(True)
        self.ThumbIndex.setHidden(True)
        self.ThumbMiddle.setHidden(True)
        self.ThumbRing.setHidden(True)
        self.ThumbPinky.setHidden(True)
        self.Fist.setHidden(True)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def print_names(self, signal):
        '''
        Change the design of the window depending on the chosen mode in mainwindow
        '''
        if signal==0 or signal==1:
            self.ThumbLabel.setHidden(False)
            self.IndexLabel.setHidden(False)
            self.MiddleLabel.setHidden(False)
            self.RingLabel.setHidden(False)

            self.PinkyLabel.setHidden(False)
            self.WristLabel.setHidden(False)
            self.ThumbAdvanced.setHidden(True)
            self.ThumbIndex.setHidden(True)
            self.ThumbMiddle.setHidden(True)
            self.ThumbRing.setHidden(True)
            self.ThumbPinky.setHidden(True)
            self.Fist.setHidden(True)

        else:
            self.ThumbLabel.setHidden(True)
            self.IndexLabel.setHidden(True)
            self.MiddleLabel.setHidden(True)
            self.RingLabel.setHidden(True)
            self.PinkyLabel.setHidden(True)
            self.WristLabel.setHidden(True)

            self.ThumbAdvanced.setHidden(False)
            self.ThumbIndex.setHidden(False)
            self.ThumbMiddle.setHidden(False)
            self.ThumbRing.setHidden(False)
            self.ThumbPinky.setHidden(False)
            self.Fist.setHidden(False)



    def retranslateUi(self, Dialog):
        '''
        set the values of the label of the simulation
        '''
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
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
        self.ThumbThreshValue.setText(_translate("Dialog", "0"))
        self.IndexThreshValue.setText(_translate("Dialog", "0"))
        self.MiddleThreshValue.setText(_translate("Dialog", "0"))
        self.RingThreshValue.setText(_translate("Dialog", "0"))
        self.PinkyThreshValue.setText(_translate("Dialog", "0"))
        self.WristThreshValue.setText(_translate("Dialog", "0"))
        self.Ok.setText(_translate("Dialog", "Ok"))
        self.label.setText(_translate("Dialog", "Thresholds"))





