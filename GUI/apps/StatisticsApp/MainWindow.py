# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainStatsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBoxChoice1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxChoice1.setObjectName("checkBoxChoice1")
        self.verticalLayout.addWidget(self.checkBoxChoice1)
        self.checkBoxChoice2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxChoice2.setObjectName("checkBoxChoice2")
        self.verticalLayout.addWidget(self.checkBoxChoice2)
        self.pushButtonNext = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.verticalLayout.addWidget(self.pushButtonNext)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBoxChoice1.setText(_translate("MainWindow", "Tool 1 (Yes/No)"))
        self.checkBoxChoice2.setText(_translate("MainWindow", "Tool 2 (Yes/No)"))
        self.pushButtonNext.setText(_translate("MainWindow", "Next"))