# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '2windows.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AnglesValues(object):
    def setupUi(self, AnglesValues):
        AnglesValues.setObjectName("AnglesValues")
        AnglesValues.resize(675, 376)
        AnglesValues.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(AnglesValues)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.ModeSelector = QtWidgets.QComboBox(self.centralwidget)
        self.ModeSelector.setObjectName("ModeSelector")
        self.ModeSelector.addItem("")
        self.ModeSelector.addItem("")
        self.gridLayout.addWidget(self.ModeSelector, 0, 0, 1, 3)
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
        self.KeysLayout.addWidget(self.WristKey)
        self.gridLayout.addLayout(self.KeysLayout, 1, 2, 1, 1)
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName("mdiArea")
        self.gridLayout.addWidget(self.mdiArea, 1, 3, 3, 1)
        self.ProgessLayout = QtWidgets.QVBoxLayout()
        self.ProgessLayout.setSpacing(20)
        self.ProgessLayout.setObjectName("ProgessLayout")
        self.ThumbValue = QtWidgets.QProgressBar(self.centralwidget)
        self.ThumbValue.setProperty("value", 24)
        self.ThumbValue.setObjectName("ThumbValue")
        self.ProgessLayout.addWidget(self.ThumbValue)
        self.IndexValue = QtWidgets.QProgressBar(self.centralwidget)
        self.IndexValue.setProperty("value", 24)
        self.IndexValue.setObjectName("IndexValue")
        self.ProgessLayout.addWidget(self.IndexValue)
        self.MiddleValue = QtWidgets.QProgressBar(self.centralwidget)
        self.MiddleValue.setProperty("value", 24)
        self.MiddleValue.setObjectName("MiddleValue")
        self.ProgessLayout.addWidget(self.MiddleValue)
        self.RingValue = QtWidgets.QProgressBar(self.centralwidget)
        self.RingValue.setProperty("value", 24)
        self.RingValue.setObjectName("RingValue")
        self.ProgessLayout.addWidget(self.RingValue)
        self.PinkyValue = QtWidgets.QProgressBar(self.centralwidget)
        self.PinkyValue.setProperty("value", 24)
        self.PinkyValue.setObjectName("PinkyValue")
        self.ProgessLayout.addWidget(self.PinkyValue)
        self.WristValue = QtWidgets.QProgressBar(self.centralwidget)
        self.WristValue.setProperty("value", 24)
        self.WristValue.setObjectName("WristValue")
        self.ProgessLayout.addWidget(self.WristValue)
        self.gridLayout.addLayout(self.ProgessLayout, 1, 0, 1, 1)
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
        self.gridLayout.addLayout(self.FingersLayout, 1, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.CurrentKey = QtWidgets.QLabel(self.centralwidget)
        self.CurrentKey.setObjectName("CurrentKey")
        self.verticalLayout.addWidget(self.CurrentKey)
        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)
        self.ShifterLayout = QtWidgets.QFormLayout()
        self.ShifterLayout.setObjectName("ShifterLayout")
        self.ShifterLabel = QtWidgets.QLabel(self.centralwidget)
        self.ShifterLabel.setObjectName("ShifterLabel")
        self.ShifterLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ShifterLabel)
        self.FingerShifter = QtWidgets.QComboBox(self.centralwidget)
        self.FingerShifter.setObjectName("FingerShifter")
        self.FingerShifter.addItem("")
        self.FingerShifter.addItem("")
        self.FingerShifter.addItem("")
        self.FingerShifter.addItem("")
        self.FingerShifter.addItem("")
        self.FingerShifter.addItem("")
        self.ShifterLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.FingerShifter)
        self.gridLayout.addLayout(self.ShifterLayout, 2, 1, 1, 2)
        AnglesValues.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AnglesValues)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 675, 21))
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

    def retranslateUi(self, AnglesValues):
        _translate = QtCore.QCoreApplication.translate
        AnglesValues.setWindowTitle(_translate("AnglesValues", "Angle Value"))
        self.ModeSelector.setItemText(0, _translate("AnglesValues", "Simple Mode"))
        self.ModeSelector.setItemText(1, _translate("AnglesValues", "Advanced Mode"))
        self.ThumbKey.setItemText(0, _translate("AnglesValues", "None"))
        self.ThumbKey.setItemText(1, _translate("AnglesValues", "Alt"))
        self.ThumbKey.setItemText(2, _translate("AnglesValues", "Win"))
        self.ThumbKey.setItemText(3, _translate("AnglesValues", "Ctrl"))
        self.ThumbKey.setItemText(4, _translate("AnglesValues", "Tab"))
        self.ThumbKey.setItemText(5, _translate("AnglesValues", "Shift"))
        self.ThumbKey.setItemText(6, _translate("AnglesValues", "Caps"))
        self.ThumbKey.setItemText(7, _translate("AnglesValues", "Esc"))
        self.IndexKey.setItemText(0, _translate("AnglesValues", "None"))
        self.IndexKey.setItemText(1, _translate("AnglesValues", "Alt"))
        self.IndexKey.setItemText(2, _translate("AnglesValues", "Win"))
        self.IndexKey.setItemText(3, _translate("AnglesValues", "Ctrl"))
        self.IndexKey.setItemText(4, _translate("AnglesValues", "Tab"))
        self.IndexKey.setItemText(5, _translate("AnglesValues", "Shift"))
        self.IndexKey.setItemText(6, _translate("AnglesValues", "Caps"))
        self.IndexKey.setItemText(7, _translate("AnglesValues", "Esc"))
        self.MiddleKey.setItemText(0, _translate("AnglesValues", "None"))
        self.MiddleKey.setItemText(1, _translate("AnglesValues", "Alt"))
        self.MiddleKey.setItemText(2, _translate("AnglesValues", "Win"))
        self.MiddleKey.setItemText(3, _translate("AnglesValues", "Tab"))
        self.MiddleKey.setItemText(4, _translate("AnglesValues", "Shift"))
        self.MiddleKey.setItemText(5, _translate("AnglesValues", "Caps"))
        self.MiddleKey.setItemText(6, _translate("AnglesValues", "Esc"))
        self.RingKey.setItemText(0, _translate("AnglesValues", "None"))
        self.RingKey.setItemText(1, _translate("AnglesValues", "Alt"))
        self.RingKey.setItemText(2, _translate("AnglesValues", "Win"))
        self.RingKey.setItemText(3, _translate("AnglesValues", "Ctrl"))
        self.RingKey.setItemText(4, _translate("AnglesValues", "Tab"))
        self.RingKey.setItemText(5, _translate("AnglesValues", "Shift"))
        self.RingKey.setItemText(6, _translate("AnglesValues", "Caps"))
        self.RingKey.setItemText(7, _translate("AnglesValues", "Esc"))
        self.PinkyKey.setItemText(0, _translate("AnglesValues", "None"))
        self.PinkyKey.setItemText(1, _translate("AnglesValues", "Alt"))
        self.PinkyKey.setItemText(2, _translate("AnglesValues", "Win"))
        self.PinkyKey.setItemText(3, _translate("AnglesValues", "Ctrl"))
        self.PinkyKey.setItemText(4, _translate("AnglesValues", "Tab"))
        self.PinkyKey.setItemText(5, _translate("AnglesValues", "Shift"))
        self.PinkyKey.setItemText(6, _translate("AnglesValues", "Caps"))
        self.PinkyKey.setItemText(7, _translate("AnglesValues", "Esc"))
        self.WristKey.setItemText(0, _translate("AnglesValues", "None"))
        self.WristKey.setItemText(1, _translate("AnglesValues", "Alt"))
        self.WristKey.setItemText(2, _translate("AnglesValues", "Win"))
        self.WristKey.setItemText(3, _translate("AnglesValues", "Ctrl"))
        self.WristKey.setItemText(4, _translate("AnglesValues", "Tab"))
        self.WristKey.setItemText(5, _translate("AnglesValues", "Shift"))
        self.WristKey.setItemText(6, _translate("AnglesValues", "Caps"))
        self.WristKey.setItemText(7, _translate("AnglesValues", "Esc"))
        self.ThumbLabel.setText(_translate("AnglesValues", "Thumb"))
        self.IndexLabel.setText(_translate("AnglesValues", "Index"))
        self.MiddleLabel.setText(_translate("AnglesValues", "Middle"))
        self.RingLabel.setText(_translate("AnglesValues", "Ring"))
        self.PinkyLabel.setText(_translate("AnglesValues", "Pinky"))
        self.WristLabel.setText(_translate("AnglesValues", "Wrist"))
        self.CurrentKey.setText(_translate("AnglesValues", "None"))
        self.ShifterLabel.setText(_translate("AnglesValues", "Shifter"))
        self.FingerShifter.setItemText(0, _translate("AnglesValues", "Thumb"))
        self.FingerShifter.setItemText(1, _translate("AnglesValues", "Index"))
        self.FingerShifter.setItemText(2, _translate("AnglesValues", "Middle"))
        self.FingerShifter.setItemText(3, _translate("AnglesValues", "Ring"))
        self.FingerShifter.setItemText(4, _translate("AnglesValues", "Pinky"))
        self.FingerShifter.setItemText(5, _translate("AnglesValues", "Wrist"))
        self.menuSetting_2.setTitle(_translate("AnglesValues", "Setting"))
        self.actionAcces_setting.setText(_translate("AnglesValues", "Acces setting"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AnglesValues = QtWidgets.QMainWindow()
    ui = Ui_AnglesValues()
    ui.setupUi(AnglesValues)
    AnglesValues.show()
    sys.exit(app.exec_())
