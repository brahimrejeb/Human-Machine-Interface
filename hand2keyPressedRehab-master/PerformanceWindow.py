# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'performance.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Rin(object):
    def setupUi(self, Rin):
        Rin.setObjectName("Rin")
        Rin.resize(364, 253)
        self.verticalLayoutWidget = QtWidgets.QWidget(Rin)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(19, 19, 125, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.PerfOfDay = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.PerfOfDay.setObjectName("PerfOfDay")
        self.verticalLayout.addWidget(self.PerfOfDay)
        self.Wrist = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Wrist.setObjectName("Wrist")
        self.verticalLayout.addWidget(self.Wrist)
        self.Pinky = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Pinky.setObjectName("Pinky")
        self.verticalLayout.addWidget(self.Pinky)
        self.Ring = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Ring.setObjectName("Ring")
        self.verticalLayout.addWidget(self.Ring)
        self.Middle = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Middle.setObjectName("Middle")
        self.verticalLayout.addWidget(self.Middle)
        self.Index = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Index.setObjectName("Index")
        self.verticalLayout.addWidget(self.Index)
        self.Thumb = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Thumb.setObjectName("Thumb")
        self.verticalLayout.addWidget(self.Thumb)
        self.CountLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.CountLabel.setObjectName("CountLabel")
        self.verticalLayout.addWidget(self.CountLabel)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Rin)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(180, 40, 71, 161))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.PerformancesLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.PerformancesLayout.setContentsMargins(0, 0, 0, 0)
        self.PerformancesLayout.setObjectName("PerformancesLayout")
        self.WristPerf = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.WristPerf.setObjectName("WristPerf")
        self.PerformancesLayout.addWidget(self.WristPerf)
        self.PinkyPerf = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.PinkyPerf.setObjectName("PinkyPerf")
        self.PerformancesLayout.addWidget(self.PinkyPerf)
        self.RingPerf = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.RingPerf.setObjectName("RingPerf")
        self.PerformancesLayout.addWidget(self.RingPerf)
        self.MiddlePerf = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.MiddlePerf.setObjectName("MiddlePerf")
        self.PerformancesLayout.addWidget(self.MiddlePerf)
        self.IndexPerf = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.IndexPerf.setObjectName("IndexPerf")
        self.PerformancesLayout.addWidget(self.IndexPerf)
        self.ThumbPerf = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.ThumbPerf.setObjectName("ThumbPerf")
        self.PerformancesLayout.addWidget(self.ThumbPerf)
        self.CountValue = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.CountValue.setObjectName("CountValue")
        self.PerformancesLayout.addWidget(self.CountValue)



        self.OK = QtWidgets.QPushButton(Rin)
        self.OK.setGeometry(QtCore.QRect(130, 210, 75, 23))
        self.OK.setObjectName("OK")
        self.OK.clicked.connect(Rin.close)

        #close the page when OK activated
        self.retranslateUi(Rin)
        QtCore.QMetaObject.connectSlotsByName(Rin)


    def setValuesPerformance(self, performance):
        #init the values of the interface
        print("coincée ici")
        self.WristPerf.setText(str(int(performance[5]))+ 'mm')
        self.PinkyPerf.setText(str(int(performance[4]))+ 'mm')
        self.RingPerf.setText(str(int(performance[3]))+ 'mm')
        self.MiddlePerf.setText(str(int(performance[2]))+ 'mm')
        self.IndexPerf.setText(str(int(performance[1]))+ 'mm')
        self.ThumbPerf.setText(str(int(performance[0]))+ 'mm')
        self.CountValue.setText(str(int(performance[6])))


    def retranslateUi(self, Rin):
        _translate = QtCore.QCoreApplication.translate
        Rin.setWindowTitle(_translate("Rin", "Dialog"))
        self.PerfOfDay.setText(_translate("Rin", "Performances of the day:"))
        self.Wrist.setText(_translate("Rin", "Wrist:"))
        self.Pinky.setText(_translate("Rin", "Pinky:"))
        self.Ring.setText(_translate("Rin", "Ring:"))
        self.Middle.setText(_translate("Rin", "Middle:"))
        self.Index.setText(_translate("Rin", "Index:"))
        self.Thumb.setText(_translate("Rin", "Thumb:"))
        self.CountLabel.setText(_translate("Rin", "Number of pressed keys:"))
        self.WristPerf.setText(_translate("Rin", "WristPerf"))
        self.PinkyPerf.setText(_translate("Rin", "PinkyPerf"))
        self.RingPerf.setText(_translate("Rin", "RingPerf"))
        self.MiddlePerf.setText(_translate("Rin", "MiddlePerf"))
        self.IndexPerf.setText(_translate("Rin", "IndexPerf"))
        self.ThumbPerf.setText(_translate("Rin", "ThumbPerf"))
        self.CountValue.setText(_translate("Rin", "CountValue"))

        self.OK.setText(_translate("Rin", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Rin = QtWidgets.QDialog()
    ui = Ui_Rin()
    ui.setupUi(Rin)
    Rin.show()
    sys.exit(app.exec_())
