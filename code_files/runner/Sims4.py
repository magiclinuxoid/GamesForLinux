# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Sims4.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget,
    QPushButton, QAction, QLineEdit, QMessageBox,QProgressBar)
import queue     #If this template is not loaded, pyinstaller may not be able to run the requests template after packaging
import requests
import tarfile 


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 180)
        MainWindow.setMinimumSize(QtCore.QSize(320, 180))
        MainWindow.setMaximumSize(QtCore.QSize(320, 180))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 80, 301, 27))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 291, 71))
        self.label.setObjectName("label")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(100, 120, 100, 27))
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(210, 120, 100, 27))
        self.toolButton_2.setObjectName("toolButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.text3 = '/home/'+os.getlogin()+'/Games/Games4Linux/Sims4'
        self.toolButton.clicked.connect(self.change)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def change(self):
        self.selectedLayers = self.comboBox.currentText()
        if self.selectedLayers == 'Русский':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
  
            msg.setWindowTitle("Информация")
            msg.setText("Вы запустили скрипт установки игры Sims4. \n\nЭто не коммерческий продукт!\nАвтор не несет ответственности за данное программное обеспечение!\nПродолжая установку Вы соглашаетесь с данными условиями!")
  
            okButton = msg.addButton('Ок', QMessageBox.AcceptRole)
            okButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(233, 15, 131, 255), stop:1 rgba(25, 206, 246, 255));")
            msg.setStyleSheet("border-radius:5px;"
"background-color: rgb(48, 48, 48);"
"color: rgb(255, 255, 255);"
"font:11pt;"
"font-weight:900;")
            MainWindow.close() 
            msg.exec()
            self.modal = QtWidgets.QWidget()              # тоннкость видимо здесь: не надо указывать родителя;
            self.centralwidget = QtWidgets.QWidget(self.modal)
            self.centralwidget.setObjectName("centralwidget")
            self.label = QtWidgets.QLabel(self.centralwidget)
            self.label.setGeometry(QtCore.QRect(10, 0, 310, 18))
            self.label.setObjectName("label")
            self.pushButton = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton.setGeometry(QtCore.QRect(5, 60, 310, 34))
            self.pushButton.setObjectName("pushButton")
            self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_3.setGeometry(QtCore.QRect(5, 20, 310, 34))
            self.pushButton_3.setObjectName("pushButton_3")
            _translate = QtCore.QCoreApplication.translate
            self.label.setText(_translate("MainWindow", "Выберете способ установки: "))
            self.pushButton.setText(_translate("MainWindow", "Wine"))
            self.pushButton_3.setText(_translate("MainWindow", "Origin"))
            self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
            self.progressBar.setGeometry(QtCore.QRect(10, 100, 261, 23))
            self.progressBar.setProperty("value", 0)
            self.progressBar.setObjectName("progressBar")    
            self.modal.resize(320, 100)
            self.modal.setMinimumSize(QtCore.QSize(320, 100))
            self.modal.setMaximumSize(QtCore.QSize(320, 100))
            self.modal.setWindowTitle('Установка Sims4')
            self.modal.show()
            self.pushButton.clicked.connect(self.download_wine)


            print('Русский')
        else:
            print('English')
    def download_wine(self):
        self.modal.close()
        self.modal2 = QtWidgets.QWidget() 
        self.modal2.resize(320, 180)
        self.modal2.setMinimumSize(QtCore.QSize(320, 180))
        self.modal2.setMaximumSize(QtCore.QSize(320, 180))         
        self.centralwidget2 = QtWidgets.QWidget(self.modal2)
        self.centralwidget2.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget2)
        self.progressBar.setGeometry(QtCore.QRect(10, 100, 261, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.modal2.setWindowTitle('Загрузка Wine...')
        self.modal2.show()
        files = "/home/"+os.getlogin()+"/.Games4Linux/code_files/wine/4.19-staging.tar.gz"
        if os.path.exists(files) != True:
            the_url = 'https://games4linux.su/download/wine/4.19-staging.tar.gz'
            the_filesize = requests.get(the_url, stream=True).headers['Content-Length']
            the_filepath = "/home/"+os.getlogin()+"/.Games4Linux/code_files/wine/4.19-staging.tar.gz"
            the_fileobj = open(the_filepath, 'wb')
            #### Create a download thread
            self.downloadThread = downloadThread(the_url, the_filesize, the_fileobj, buffer=10240)
            self.downloadThread.download_proess_signal.connect(self.set_progressbar_value)
            self.downloadThread.start()
            #tar = tarfile.open("/home/"+os.getlogin()+"/.Games4Linux/code_files/wine/4.19-staging.tar.gz", "r")
            #tar.extractall(r"/home/"+os.getlogin()+"/.Games4Linux/code_files/wine/")
        else:
            
            self.modal3 = QtWidgets.QWidget() 
            self.modal3.resize(320, 180)
            self.modal3.setMinimumSize(QtCore.QSize(320, 180))
            self.modal3.setMaximumSize(QtCore.QSize(320, 180))
            self.centralwidget3 = QtWidgets.QWidget(self.modal3)
            self.centralwidget3.setObjectName("centralwidget")
            self.modal3.setWindowTitle('Установка Sims4вв')
            self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget3)
            self.pushButton_4.setGeometry(QtCore.QRect(10, 60, 221, 34))
            self.pushButton_4.setObjectName("pushButton")
            self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget3)
            self.pushButton_5.setGeometry(QtCore.QRect(10, 20, 221, 34))
            self.pushButton_5.setObjectName("pushButton_3")
            _translate = QtCore.QCoreApplication.translate
            self.pushButton_4.setText(_translate("MainWindow", "Стандартный путь"))
            self.pushButton_5.setText(_translate("MainWindow", "Свой путь"))
            self.pushButton_4.clicked.connect(self.standart_path_games)
            self.pushButton_5.clicked.connect(self.path_games)
            print(self.text3)
            self.modal2.close()
            self.modal3.show()
            
    def standart_path_games(self):
        self.modal3.close()
        #os.mkdir(self.text3)
        self.modal4 = QtWidgets.QWidget() 
        self.modal4.resize(320, 180)
        self.modal4.setMinimumSize(QtCore.QSize(320, 180))
        self.modal4.setMaximumSize(QtCore.QSize(320, 180))
        self.centralwidget4 = QtWidgets.QWidget(self.modal4)
        self.centralwidget4.setObjectName("centralwidget")
        self.modal4.setWindowTitle('Распаковка Wine')
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
  
        msg.setWindowTitle("Информация")
        msg.setText("началась распаковка Wine.")
  
        okButton = msg.addButton('Ок', QMessageBox.AcceptRole)
        okButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(233, 15, 131, 255), stop:1 rgba(25, 206, 246, 255));")
        msg.setStyleSheet("border-radius:5px;"
"background-color: rgb(48, 48, 48);"
"color: rgb(255, 255, 255);"
"font:11pt;"
"font-weight:900;")
        msg.exec()
        
        msg2 = QMessageBox()
        msg2.setIcon(QMessageBox.Information)
  
        msg2.setWindowTitle("Информация")
        msg2.setText("успешно распакован Wine.")
  
        okButton2 = msg2.addButton('Ок', QMessageBox.AcceptRole)
        okButton2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(233, 15, 131, 255), stop:1 rgba(25, 206, 246, 255));")
        msg2.setStyleSheet("border-radius:5px;"
"background-color: rgb(48, 48, 48);"
"color: rgb(255, 255, 255);"
"font:11pt;"
"font-weight:900;")
        tar = tarfile.open("/home/"+os.getlogin()+"/.Games4Linux/code_files/wine/4.19-staging.tar.gz")
        tar.extractall("/home/"+os.getlogin()+"/.Games4Linux/code_files/wine")
        tar.close()
        msg2.exec()
    def path_games(self):
            directory3 = QtWidgets.QFileDialog.getExistingDirectory()
            print(directory3)
            self.text3 = str(directory3)
            run2 = 'tar -xvzf /home/'+os.getlogin()+'/.Games4Linux/code_files/wine/4.19-staging.tar.gz -C '+ self.text3 
            os.system("bash -c '%s'" % run2)
        
    def set_progressbar_value(self, value):
        self.progressBar.setValue(value)
        if value == 100:
            print('скачалось')
            #self.modal2.close()
            #self.modal4 = QtWidgets.QWidget() 
            #self.modal4.resize(240, 120)
            #self.centralwidget4 = QtWidgets.QWidget(self.modal4)
            #self.centralwidget4.setObjectName("centralwidget")
            #self.modal4.setWindowTitle('Установка Sims4')
            #self.modal4.show()
            self.modal3 = QtWidgets.QWidget() 
            self.modal3.resize(320, 180)
            self.modal3.setMinimumSize(QtCore.QSize(320, 180))
            self.modal3.setMaximumSize(QtCore.QSize(320, 180))
            self.centralwidget3 = QtWidgets.QWidget(self.modal3)
            self.centralwidget3.setObjectName("centralwidget")
            self.modal3.setWindowTitle('Установка Sims4')
            self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget3)
            self.pushButton_4.setGeometry(QtCore.QRect(10, 60, 221, 34))
            self.pushButton_4.setObjectName("pushButton")
            self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget3)
            self.pushButton_5.setGeometry(QtCore.QRect(10, 20, 221, 34))
            self.pushButton_5.setObjectName("pushButton_3")
            _translate = QtCore.QCoreApplication.translate
            self.pushButton_4.setText(_translate("MainWindow", "Стандартный путь"))
            self.pushButton_5.setText(_translate("MainWindow", "Свой путь"))
            self.pushButton_4.clicked.connect(self.standart_path_games)
            self.pushButton_5.clicked.connect(self.path_games)
            print(self.text3)
            self.modal2.close()
            self.modal3.show()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Русский"))
        self.comboBox.setItemText(1, _translate("MainWindow", "English"))
        self.label.setText(_translate("MainWindow", "Select the instalation language\n"
"\n"
"Выберете язык установки"))
        self.toolButton.setText(_translate("MainWindow", "Далее"))
        self.toolButton_2.setText(_translate("MainWindow", "Отмена"))
    
    
class downloadThread(QThread):
    download_proess_signal = pyqtSignal(int)  #Create signal

    def __init__(self, url, filesize, fileobj, buffer):
        super(downloadThread, self).__init__()
        self.url = url
        self.filesize = filesize
        self.fileobj = fileobj
        self.buffer = buffer


    def run(self):
        try:
            rsp = requests.get(self.url, stream=True)                #Streaming download mode
            offset = 0
            for chunk in rsp.iter_content(chunk_size=self.buffer):
                if not chunk: break
                self.fileobj.seek(offset)                            #Setting Pointer Position
                self.fileobj.write(chunk)                            #write file
                offset = offset + len(chunk)
                proess = offset / int(self.filesize) * 100
                self.download_proess_signal.emit(int(proess))        #Sending signal
            #######################################################################
            self.fileobj.close()    #Close file
            self.exit(0)            #Close thread


        except Exception as e:
            print(e)

    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
