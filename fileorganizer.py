#Import all the libraies
#Install os , pyqt5
import os
import shutil
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color:#02111b;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(-30, -30, 851, 181))
        self.graphicsView.setStyleSheet("background-color:#3f4045;")
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-30, -30, 341, 241))
        self.label.setStyleSheet("background-color:none;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("file.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, -10, 421, 91))
        self.label_2.setStyleSheet("background-color:none;\n"
"font: 75 italic 45pt \"LEMON MILK Bold\";\n"
"color:white;\n"
"border:2px;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 60, 481, 91))
        self.label_3.setStyleSheet("background-color:none;\n"
"font: 75 italic 45pt \"LEMON MILK Bold\";\n"
"color:white;\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 250, 411, 91))
        self.label_4.setStyleSheet("background-color:none;\n"
"color:white;\n"
"font: 75 25pt \"LEMON MILK Bold\";")
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(310, 270, 471, 51))
        self.textEdit.setStyleSheet("background-color:#3f4045;\n"
                                    "font:16pt \"Impact\";\n")
        self.textEdit.setObjectName("textEdit")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 380, 281, 61))
        self.pushButton.setStyleSheet("background-color:white;\n"
"font: 16pt \"Impact\";\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"border-color: black;\n"
"padding: 4px;\n"
"")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.fileoragnizer)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "File "))
        self.label_3.setText(_translate("MainWindow", "ORGANIZER"))
        self.label_4.setText(_translate("MainWindow", "Enter path:"))
        self.pushButton.setText(_translate("MainWindow", "Proceed"))
    def photo(self):
            self.label.setPixmap(QtGui.QPixmap("file.png"))
#This is the function for the main logic
    def fileoragnizer(self):
        path=self.textEdit.toPlainText()
        path=str(path)
        print(path)
        files=os.listdir(path)
        for filename in files:
                name,extension=os.path.splitext(filename)
                extension=extension[1:]
                if os.path.exists(path+'/'+extension):
                        shutil.move(path+'/'+filename,path+'/'+extension+'/'+filename)
                else:
                        os.makedirs(path+'/'+extension)
                        shutil.move(path+'/'+filename,path+'/'+extension+'/'+filename)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
