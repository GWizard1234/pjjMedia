# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(366, 297)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.play_button = QtWidgets.QPushButton(self.centralwidget)
        self.play_button.setGeometry(QtCore.QRect(90, 10, 191, 71))
        self.play_button.setStyleSheet("\n"
"border: 2px solid black;\n"
"border-radius: 25px;\n"
"background-color: #fbeee0;\n"
"font-size: 30px;\n"
"\n"
"")
        self.play_button.setObjectName("play_button")
        self.stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_button.setGeometry(QtCore.QRect(90, 90, 191, 71))
        self.stop_button.setStyleSheet("\n"
"border: 2px solid black;\n"
"border-radius: 25px;\n"
"background-color: #fbeee0;\n"
"font-size: 30px;\n"
"\n"
"")
        self.stop_button.setObjectName("stop_button")
        self.select_button = QtWidgets.QPushButton(self.centralwidget)
        self.select_button.setGeometry(QtCore.QRect(90, 170, 191, 71))
        self.select_button.setStyleSheet("\n"
"border: 2px solid black;\n"
"border-radius: 25px;\n"
"background-color: #fbeee0;\n"
"font-size: 30px;\n"
"\n"
"")
        self.select_button.setObjectName("select_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 366, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.play_button.setText(_translate("MainWindow", "Play"))
        self.stop_button.setText(_translate("MainWindow", "Stop"))
        self.select_button.setText(_translate("MainWindow", "Select"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
