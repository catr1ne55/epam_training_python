# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weather_forecast.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 562)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.forecast_button = QtWidgets.QPushButton(self.centralwidget)
        self.forecast_button.setGeometry(QtCore.QRect(410, 100, 371, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.forecast_button.setFont(font)
        self.forecast_button.setObjectName("forecast_button")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 20, 761, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.current_button = QtWidgets.QPushButton(self.centralwidget)
        self.current_button.setGeometry(QtCore.QRect(20, 100, 371, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.current_button.setFont(font)
        self.current_button.setObjectName("current_button")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(20, 190, 761, 351))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 759, 349))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.listWidget = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 761, 351))
        self.listWidget.setObjectName("listWidget")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Weather forecast"))
        self.forecast_button.setText(_translate("MainWindow", "5 day/3 hour forecast"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Enter location(country, city, street, housenumber)..."))
        self.current_button.setText(_translate("MainWindow", "Current wether data"))

