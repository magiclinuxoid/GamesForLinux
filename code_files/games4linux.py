#!/usr/bin/env python
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QMovie)
from PyQt5.QtWidgets import *
import requests
import tarfile
import theme # Это наш конвертированный файл дизайна
from theme import Ui_MainWindow
import time
import os
from ui_splash_screen import Ui_SplashScreen
counter = 0
jumper = 10
class CustomWidget (QtWidgets.QWidget,theme.Ui_MainWindow):                       # QtWidgets
    def __init__ (self, parent = None):
        super(CustomWidget, self).__init__(parent)

        label = QLabel("custom label text")
        layout = QGridLayout()
        layout.addWidget(label,0, 1, 1, 1)
        self.pushButton = QPushButton()
        self.pushButton.setFixedSize(30, 30)
        layout.addWidget(self.pushButton,0, 0, 1, 1)
        self.setLayout(layout)



class ExampleApp(QtWidgets.QMainWindow, theme.Ui_MainWindow):
    def __init__(self, maya=False):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле theme.py
        super(ExampleApp,self).__init__()
        #self.setWindowFlags(Qt.FramelessWindowHint)
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.Createprefix.clicked.connect(self.browse_folder_prefix)
        self.Selectwine.clicked.connect(self.browse_folder_wine)
        self.Prefixload.clicked.connect(self.install_file)
        self.Winetricks.clicked.connect(self.Winetricks_run)
        self.WineCfg.clicked.connect(self.winecfg)
        self.selectexe.clicked.connect(self.Selectexe)
        self.installexe.clicked.connect(self.Installexe)
        #self.Selectscript.clicked.connect(self.browse_folder_script)
        self.Installscript.clicked.connect(self.scripts_run)
        self.selectItem_6 = ""
        self.Prefixload.clicked.connect(self.base)
        self.deleteitem.clicked.connect(self.delete)
        self.toolButton_12.clicked.connect(self.wine_select_path)
        self.text = ''
        self.text2 = 'wine' #строки text теперь атрибуты класса и могут вызываться в любой функции
        self.text3 = ''
        self.text4 = 'MANGOHUD=1'
        self.text5 = self.lineEdit_5.text()
        self.toolButton_3.clicked.connect(self.printItem)
        self.selectItem_3 = ""
        self.toolButton_11.hide()
        self.toolButton_11.clicked.connect(self.lineEdit_5_update)
        self.toolButton_9.clicked.connect(self.searchItem)
        self.toolButton_2.clicked.connect(self.clear_search)
        self.toolButton_10.clicked.connect(self.open_icon)
        self.toolButton_7.clicked.connect(self.delete_icon)
        self.toolButton_5.clicked.connect(self.mango_hud)
        self.toolButton_13.clicked.connect(self.wine_ver_update)
        self.toolButton_14.clicked.connect(self.wine_ver_select)
        self.toolButton_15.clicked.connect(self.exe_select_path)
        self.pushButton.clicked.connect(self.download_wine)
        #self.toolButton_14.clicked.connect(self.base)
        self.listWidget_3.itemClicked.connect(self.software_hud)
        self.directory_6 = '/home/'+os.getlogin()+'/GamesForLinux/code_files/runner/'
        self.directory_14 = '/home/'+os.getlogin()+'/GamesForLinux/code_files/prefix_locate_wine_ver/'
        self.groupBox_7.hide()
        self.groupBox_8.hide()
        self.groupBox_10.hide()
        self.toolButton_12.hide()
        self.progressBar.hide()
        self.progressBar.setValue(1)
        print(self.directory_6)


        wget_wine = 'wget ' + 'https://games4linux.su/download/wine/download_verwine.txt -O' +'/home/'+os.getlogin()+'/download_verwine.txt'
        os.system("bash -c '%s'" % wget_wine )
        for item in os.listdir(self.directory_6):  # для каждого файла в директории
            self.listWidget_5.addItem(item)  # добавить файл в listWidget


        self.directory_7 = '/home/'+os.getlogin()+'/GamesForLinux/code_files/prefix_locate/'
        for self.item_2 in os.listdir(self.directory_7):  # для каждого файла в директории
            self.listWidget_2.addItem(self.item_2)   # добавить файл в listWidget

        self.directory_15 = '/home/'+os.getlogin()+'/GamesForLinux/code_files/img_icon'

        self.directory_9 = '/home/'+os.getlogin()+'/GamesForLinux/code_files/icon/'
        self.icons = os.listdir(self.directory_15)
        files = os.listdir(self.directory_9)

        for self.item_3 in os.listdir(self.directory_9):  # для каждого файла в директории
            if self.item_3 != self.icons:
                print(self.item_3)
                icon='/home/'+os.getlogin()+'/GamesForLinux/code_files/img_icon/'+self.item_3
                self.item_3 = QtWidgets.QListWidgetItem(self.item_3)
                self.run = QIcon(icon)
                self.item_3.setIcon(self.run)
                self.listWidget.setIconSize(QtCore.QSize(40, 40))
                self.listWidget_3.addItem(self.item_3)

        f = open("download_verwine.txt","r")
        lines = f.readlines()


        spisok = []
        for adress,dirs,files in os.walk('/home/dron/Prefix x64 for Simcity/drive_c/'):
            for file in files:
                full=os.path.join(adress,file)
                if '.exe' in full:
                    if time.time() - os.path.getctime(full) < 300:
                        spisok.append(full)
        for i in spisok:
            print(i)
            self.listWidget.addItem(i)



        for self.line in lines:
            if self.line != "":
                self.line=self.line.replace("\n", "")
                self.line = QtWidgets.QListWidgetItem(self.line)
                icon='/home/'+os.getlogin()+'/GamesForLinux/code_files/img_icon/Prefix x64 | Download Studio.png'
                print(icon)
                self.run = QIcon(icon)
                self.line.setIcon(self.run)
                self.line.setSizeHint(self.listWidget.sizeHint())
                self.line.setTextAlignment(Qt.AlignCenter)
                self.line.setSizeHint(QtCore.QSize(-1, 10))
                self.listWidget_3.setIconSize(QtCore.QSize())
                self.listWidget.addItem(self.line)
                #self.listWidget.setItemWidget(self.line,self.toolButton_10)
                print(self.line)

    def printItem(self):
        self.listWidget_2.addItem('f')
        self.listWidget_2.currentItem().setTextUp()


    def mango_hud(self):
        #self.text4 = self.lineEdit_5.text()
        #print(self.text4)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        #msg.setIconPixmap(pixmap)  # Своя картинка

        msg.setWindowTitle("Информация")
        msg.setText("MangoHud")
        msg.setInformativeText("Установить MangoHud?")

        okButton = msg.addButton( '  Да  ', QMessageBox.AcceptRole)
        msg.addButton('Нет', QMessageBox.RejectRole)
        okButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(233, 15, 131, 255), stop:1 rgba(25, 206, 246, 255));")
        msg.setStyleSheet("border-radius:5px;"
"background-color: rgb(48, 48, 48);"
"color: rgb(255, 255, 255);"
"font:11pt;"
"font-weight:900;")
        msg.exec()
        if msg.clickedButton() == okButton:
            download ='python3 /home/'+os.getlogin()+'/GamesForLinux/code_files/' + 'setPassword.py'
            os.system("bash -c '%s'" % download)
            #download_2 ='cd '+patch_1
            #print(download_2)
            #os.system("bash -c '%s'" % download_2)

    def clear_search(self):
        self.listWidget_2.clear()
        self.directory_7 = '/home/'+os.getlogin()+'/GamesForLinux/code_files/prefix_locate/'
        for self.item_2 in os.listdir(self.directory_7):  # для каждого файла в директории
            self.listWidget_2.addItem(self.item_2)   # добавить файл в listWidget

    def searchItem(self):
        self.search_string = self.lineEdit_4.text()
        #out = self.listWidget_3.findItems(self.search_string,
                                        #Qt.MatchContains |          # +++
                                        #Qt.MatchCaseSensitive)      # +++

        #print("out->", [ i.text() for i in out ] )

        #print(self.search_string)
        #for self.item_3 in os.listdir(self.directory_9):
            #if self.item_3 == self.search_string:
                #print(self.item_3)
                #self.listWidget_3.clear()
                #self.listWidget_3.addItem(self.the)

        if self.search_string == "":
                self.listWidget_3.clear()
                for self.item_3 in os.listdir(self.directory_9):  # для каждого файла в директории
                    if self.item_3 != self.icons:
                        icon='/home/'+os.getlogin()+'/GamesForLinux/code_files/img_icon/'+self.item_3
                        self.item_3 = QtWidgets.QListWidgetItem(self.item_3)
                        self.run = QIcon(icon)
                        self.item_3.setIcon(self.run)
                        self.listWidget.setIconSize(QtCore.QSize(40, 40))
                        self.listWidget_3.addItem(self.item_3)
        else:
            match_items = self.listWidget_3.findItems(self.search_string,
                                        Qt.MatchContains |          # +++
                                        Qt.MatchCaseSensitive)
            for i in range(self.listWidget_3.count()):
                it = self.listWidget_3.item(i)
                it.setHidden(it not in match_items)


    def browse_folder_prefix(self):
        #self.hide()
        #self.treeView.show()
        #print(file_path)
        self.directory = QtWidgets.QFileDialog.getExistingDirectory()
        self.text = str(self.directory)
        self.label.setText(self.text)

    def browse_folder_wine(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        # msg.setIconPixmap(pixmap)  # Своя картинка

        msg.setWindowTitle("Информация")
        msg.setText("Wine")
        msg.setInformativeText("Выберете wine")

        okButton = msg.addButton( '  системный wine  ', QMessageBox.AcceptRole)
        msg.addButton(' выбрать wine ', QMessageBox.RejectRole)
        okButton_2 = msg.addButton(' загрузить wine ', QMessageBox.RejectRole)
        okButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(233, 15, 131, 255), stop:1 rgba(25, 206, 246, 255));")
        msg.setStyleSheet("border-radius:5px;"
"background-color: rgb(48, 48, 48);"
"color: rgb(255, 255, 255);"
"font:11pt;"
"font-weight:900;")

        msg.exec()
        if msg.clickedButton() == okButton:
            self.wine = 'wine'
            self.label_2.setText(self.wine)
        elif msg.clickedButton() == okButton_2:
            self.label_9.hide()
            self.listWidget_4.clear()
            self.groupBox_7.show()
            self.toolButton_12.show()
            self.groupBox_5.hide()
            self.groupBox_6.hide()
            self.toolButton_12.hide()
            f = open("download_verwine.txt","r")
            lines = f.readlines()
            for self.line in lines:
                if self.line != "":
                    self.line=self.line.replace("\n", "")
                    self.line = QtWidgets.QListWidgetItem(self.line)
                    self.line.setSizeHint(self.listWidget.sizeHint())
                    self.line.setSizeHint(QtCore.QSize(-1, 10))
                    self.listWidget_4.setIconSize(QtCore.QSize(32, 32))
                    self.listWidget_4.addItem(self.line)
                    #self.listWidget.setItemWidget(self.line,self.toolButton_10)
                    print(self.line)
        else:
            self.listWidget_4.clear()
            for item in os.listdir(self.directory_6):  # для каждого файла в директории
                self.listWidget_4.addItem(item)   # добавить файл в listWidget
            self.groupBox_7.show()
            self.toolButton_12.show()
            self.groupBox_5.hide()
            self.groupBox_6.hide()

    def download_wine(self):
        self.directory_13 = '/home/'+os.getlogin()+'/GamesForLinux/code_files/runner/'
        self.selectItem_5 = self.listWidget_4.currentItem().text()
        the_url = 'https://games4linux.su/download/wine/'+self.selectItem_5
        the_filesize = requests.get(the_url, stream=True).headers['Content-Length']
        the_filepath = "/tmp/"+self.selectItem_5
        the_fileobj = open(the_filepath, 'wb')
        self.files = "/tmp/"+self.selectItem_5
        if os.path.exists(self.files) == True:
            self.downloadThread = downloadThread(the_url, the_filesize, the_fileobj, buffer=10240)
            self.downloadThread.download_proess_signal.connect(self.set_progressbar_value)
            self.downloadThread.start()
        #else:
            #tar = tarfile.open('/home/'+os.getlogin()+'/GamesForLinux/code_files/runner/'+self.selectItem_5, "r")
            #tar.extractall(r"/home/"+os.getlogin()+"/GamesForLinux/code_files/runner/")

    def set_progressbar_value(self, value):
        self.progressBar.show()
        self.progressBar.setValue(value)
        if value == 100:
            self.label_9.show()
            #self.progressBar.hide()
            self.listWidget_4.clear()
            #self.progressBar.setValue(0)
            if value == 100:
                self.progressBar.hide()
                tar = 'tar xf '+self.files +" -C /tmp/"
                os.system("bash -c '%s'" % tar)
                files_repace=self.selectItem_5.replace('.tar.xz',"")
                mv = 'mv ' +'/tmp/'+files_repace + ' /home/'+os.getlogin()+'/GamesForLinux/code_files/runner/'
                os.system("bash -c '%s'" % mv)
                for item in os.listdir(self.directory_6):  # для каждого файла в директории
                    self.listWidget_4.addItem(item)   # добавить файл в listWidget
                    self.groupBox_7.show()
                    self.toolButton_12.show()
                    self.groupBox_5.hide()
                    self.groupBox_6.hide()
                    self.pushButton.hide()


    def wine_select_path(self):
        self.directory_13 = '/home/'+os.getlogin()+'/GamesForLinux/code_files/runner/'
        self.selectItem_5 = self.listWidget_4.currentItem().text()
        self.text2 = self.directory_13 + self.selectItem_5 + '/dist'
        #directory_2 = QtWidgets.QFileDialog.getExistingDirectory()
        #self.text2 = str(directory_2)
        self.label_2.setText(self.text2)

    def scripts_run(self):
        self.selectedLayers=self.comboBox_2.currentText()
        self.text5 = str(self.directory_6)
        self.selectedLayers=self.comboBox_2.currentText()
        setup = 'python3 ' + self.text5 + self.selectedLayers + ' &'
        os.system("bash -c '%s'" % setup)
        print(setup)

    def wine_ver_update(self):
        try:
            self.selectItem_3 = self.listWidget_2.currentItem().text()
            if  self.selectItem_3 != "":
                self.groupBox_9.hide()
                self.groupBox_8.show()
        except AttributeError:
            error_1 = 'Ошибка, выбери префикс!'

            QMessageBox.question(self, 'Введено', error_1, QMessageBox.Ok, QMessageBox.Ok)

    def wine_ver_select(self):
        self.directory_13 = '/home/'+os.getlogin()+'/GamesForLinux/code_files/runner/'
        self.selectItem_3 = self.listWidget_2.currentItem().text()
        self.selectItem_6 = self.listWidget_5.currentItem().text()
        self.directory_14 = '/home/'+os.getlogin()+'/GamesForLinux/code_files/prefix_locate_wine_ver/'
        self.text7 = self.directory_14 + self.selectItem_3
        self.f_12 = self.text7
        self.f_12 = open(self.f_12, mode="w", encoding="utf_8")
        self.f_12.write('GamesForLinux='+self.directory_13+self.selectItem_6+'/dist/bin/wine'+'\n')
        self.f_12.close()
        self.f_13 = self.text7
        self.f_13 = open(self.f_13, mode="r", encoding="utf_8")
        self.wine_ver = str(self.f_13.readlines()[0])
        self.wine_ver=self.wine_ver.replace("\n", "")
        #self.f_13.close()
        print(self.wine_ver)

    def delete(self):
        try:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            # msg.setIconPixmap(pixmap)  # Своя картинка

            msg.setWindowTitle("Информация")
            msg.setText("Удалить?")
            msg.setInformativeText("Удалить файл префикса?")

            okButton = msg.addButton( '  Да  ', QMessageBox.AcceptRole)
            msg.addButton('Нет', QMessageBox.RejectRole)
            okButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(233, 15, 131, 255), stop:1 rgba(25, 206, 246, 255));")
            msg.setStyleSheet("border-radius:5px;"
"background-color: rgb(48, 48, 48);"
"color: rgb(255, 255, 255);"
"font:11pt;"
"font-weight:900;")

            msg.exec()
            if msg.clickedButton() == okButton:
                self.directory_8 = '/home/'+os.getlogin()+'/GamesForLinux/code_files/prefix_locate_delete/'
                self.selectItem_3 = self.listWidget_2.currentItem().text()
                setups = 'rm '+'"'+self.directory_7 + self.selectItem_3+'"'
                print(setups)
                delete_prefix = 'sh '+ '"'+self.directory_8 + self.selectItem_3+'"'
                print(delete_prefix)
                delete_prefix_sh = 'rm '+ '"'+self.directory_8 + self.selectItem_3+'"'
                os.system("bash -c '%s'" % delete_prefix)
                os.system("bash -c '%s'" % delete_prefix_sh)
                os.system("bash -c '%s'" % setups)
                self.listWidget_2.clear()
                self.directory_7 = '/home/'+os.getlogin()+'/GamesForLinux/code_files/prefix_locate/'
                for self.item_2 in os.listdir(self.directory_7):  # для каждого файла в директории
                    self.listWidget_2.addItem(str(self.item_2))   # добавить файл в listWidget
                self.listWidget_3.clear()
                self.directory_9 = '/home/'+os.getlogin()+'/GamesForLinux/code_files/icon/'
                for self.item_3 in os.listdir(self.directory_9):  # для каждого файла в директории
                    self.listWidget_3.addItem(self.item_3)
        except AttributeError:
            error_1 = 'Выбери пути!'

            QMessageBox.question(self, 'Введено', error_1, QMessageBox.Ok, QMessageBox.Ok)


    def base(self):
        self.name = QFileInfo(str(self.directory)).fileName()
        print(self.name)
        self.nameprefix = self.name
        self.icon_path = '/home/'+os.getlogin()+'/GamesForLinux/code_files/icon/' + self.nameprefix
        os.system("bash -c '%s'" % self.icon_path)
        print(self.icon_path)
        if self.text2 == 'wine':
            if self.nameprefix != "":
                self.cb=self.comboBox.currentText()
                self.directory_14 = '/home/'+os.getlogin()+'/GamesForLinux/code_files/prefix_locate_wine_ver/'
                self.text7 = self.directory_14 + self.name
                self.f_12 = self.text7
                self.f_12 = open(self.f_12, mode="w", encoding="utf_8")
                self.f_12.write('GamesForLinux=/bin/wine'+'\n')
                self.f_12.close()
                f = '/home/'+os.getlogin()+'/GamesForLinux/code_files/prefix_locate/' + self.nameprefix
                f = open(f, mode="w", encoding="utf_8")
                f.write('#!/bin/sh'+'\n')
                f.write('WINEARCH=''"'+self.cb+'"' + ' WINEPREFIX='+'"'+self.text+'"'+' WINE=/bin/wine ' + '/home/'+os.getlogin()+'/GamesForLinux/code_files/winetricks &'+'\n')
                f.write('WINEARCH='+self.cb+ ' WINEPREFIX='+'"'+self.text+'"' +' '+'/bin/wine '+ ' winecfg &'+'\n')
                f.write(self.text+'/drive_c/'+'\n')
                #f.write('WINEARCH='+self.cb+ ' WINEPREFIX='+'"'+self.text+'"'+' '+'/bin/wine' +' "')
                f.close()
                f2='/home/'+os.getlogin()+'/GamesForLinux/code_files/prefix_locate_delete/' + self.nameprefix
                f2 = open(f2, mode="w", encoding="utf_8")
                f2.write('#!/bin/sh'+'\n')
                f2.write('rm -r '+'"'+self.text+'"'+'\n')
                f2.close()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)

                msg.setWindowTitle("Информация")
                msg.setText("\nОшибка, поле имени пусто!")

                okButton = msg.addButton('Ок', QMessageBox.AcceptRole)
                okButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(233, 15, 131, 255), stop:1 rgba(25, 206, 246, 255));")
                msg.setStyleSheet("border-radius:5px;"
"background-color: rgb(48, 48, 48);"
"color: rgb(255, 255, 255);"
"font:11pt;"
"font-weight:900;")
                msg.exec()
        self.name = QFileInfo(str(self.directory)).fileName()
        print(self.name)
        self.nameprefix = self.name
        if self.text2 != 'wine':
            if self.nameprefix != "":
                self.directory_14 = '/home/'+os.getlogin()+'/GamesForLinux/code_files/prefix_locate_wine_ver/'
                self.text7 = self.directory_14 + self.name
                self.f_12 = self.text7
                self.f_12 = open(self.f_12, mode="w", encoding="utf_8")
                self.f_12.write('GamesForLinux='+"'"+self.directory_13+self.selectItem_5+'/dist/bin/wine'+"'"+'\n')
                self.f_12.close()
                self.cb=self.comboBox.currentText()
                f = '/home/'+os.getlogin()+'/GamesForLinux/code_files/prefix_locate/' + self.nameprefix
                f = open(f, mode="w", encoding="utf_8")
                f.write('#!/bin/sh'+'\n')
                f.write('WINEARCH=''"'+self.cb+'"' + ' WINEPREFIX='+'"'+self.text+'"' ' WINE=$GamesForLinux'+' /home/'+os.getlogin()+'/GamesForLinux/code_files/winetricks &'+'\n')
                f.write('WINEARCH='+self.cb+ ' WINEPREFIX='+'"'+self.text+'"' +' '+' $GamesForLinux'+' winecfg &'+'\n')
                f.write(self.text+'/drive_c/'+'\n')
                f.write('WINEARCH='+self.cb+ ' WINEPREFIX='+'"'+self.text+'"'+' '+' $GamesForLinux '+' "'+'\n')
                f.close()
                f2='/home/'+os.getlogin()+'/GamesForLinux/code_files/prefix_locate_delete/' + self.nameprefix
                f2 = open(f2, mode="w", encoding="utf_8")
                f2.write('#!/bin/sh'+'\n')
                f2.write('rm -r '+'"'+self.text+'"'+'\n')
                f2.close()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)

                msg.setWindowTitle("Информация")
                msg.setText("\nОшибка, поле имени пусто!")

                okButton = msg.addButton('Ок', QMessageBox.AcceptRole)
                okButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(233, 15, 131, 255), stop:1 rgba(25, 206, 246, 255));")
                msg.setStyleSheet("border-radius:5px;"
"background-color: rgb(48, 48, 48);"
"color: rgb(255, 255, 255);"
"font:11pt;"
"font-weight:900;")
                msg.exec()
        self.listWidget_2.clear()
        self.directory_7 = '/home/'+os.getlogin()+'/GamesForLinux/code_files/prefix_locate/'
        for self.item_2 in os.listdir(self.directory_7):  # для каждого файла в директории
            self.listWidget_2.addItem(str(self.item_2))   # добавить файл в listWidget

    def Installexe(self):
        self.start_time = time.time()
        self.selectItem_3 = self.listWidget_2.currentItem().text()
        self.text7 = self.directory_14 + self.selectItem_3
        self.f_13 = self.text7
        self.f_13 = open(self.f_13, mode="r", encoding="utf_8")
        self.wine_ver = str(self.f_13.readlines()[0])
        self.f_13.close()
        self.wine_ver=self.wine_ver.replace("\n", "")
        print(self.wine_ver)
        try:
            self.directory_8 = '/home/'+os.getlogin()+'/GamesForLinux/code_files/prefix_locate_delete/'
            self.selectItem_3 = self.listWidget_2.currentItem().text()
            self.f_3 = self.directory_7+ self.selectItem_3
            self.f_3 = open(self.f_3, mode="r", encoding="utf_8")
            print(self.f_3)
            e = str(self.f_3.readlines()[4])
            e = e.replace("\n", "")
            installexe ='export '+self.wine_ver+' && '+ e + self.text3 + '"'
            os.system("bash -c '%s'" % installexe)
            print(installexe)
            self.selectItem_4 = self.listWidget_2.currentItem().text()
            self.f_4 = self.directory_7+ self.selectItem_4
            self.f_4 = open(self.f_4, mode="r", encoding="utf_8")
            self.str2=str(self.f_4.readlines()[4])
            self.selectItem_5 = self.listWidget_2.currentItem().text()
            self.f_5 = self.directory_7+ self.selectItem_5
            self.f_5 = open(self.f_5, mode="r", encoding="utf_8")
            path=self.f_5.readlines()[3]
            path.replace("\n", "")
            path = str(path)
            self.str2=self.str2.replace("\n", "")
            print(self.str2)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            # msg.setIconPixmap(pixmap)  # Своя картинка

            msg.setWindowTitle("Информация")
            msg.setText("Установка...")
            msg.setInformativeText("нажмите ОК после установки")

            okButton = msg.addButton( ' ok ', QMessageBox.AcceptRole)
            okButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(233, 15, 131, 255), stop:1 rgba(25, 206, 246, 255));")
            msg.setStyleSheet("border-radius:5px;"
    "background-color: rgb(48, 48, 48);"
    "color: rgb(255, 255, 255);"
    "font:11pt;"
    "font-weight:900;")

            msg.exec()
            if msg.clickedButton() == okButton:
                end_time = time.time()
                spisok = []
                spisok_2 = []
                for adress,dirs,files in os.walk(self.selectItem_5):
                    for file in files:
                        full=os.path.join(adress,file)
                        if '.exe' in full:
                            if self.start_time < os.path.getctime(full) < end_time:
                                spisok.append(full)
                                spisok_2.append(adress)

                #self.directory_10 = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберете папку приложения",path)
                #directory_11 = QtWidgets.QFileDialog.getOpenFileNames(self,"выберете файл запуска",  self.directory_10,"Windows Files (*.msi)(*.exe)")[0]
            #for self.p in spisok_2:
                #self.spi_3=self.p.split('/')
            for self.exe in spisok:
                print(self.exe)
                self.listWidget_6.addItem(self.exe)

        except AttributeError:
            error_1 = 'Выбери пути!'
            QMessageBox.question(self, 'Введено', error_1, QMessageBox.Ok, QMessageBox.Ok)
        except IndexError:
            error_2 = 'Выбери пути!'
            QMessageBox.question(self, 'Введено', error_2, QMessageBox.Ok, QMessageBox.Ok)

    def exe_select_path(self):
        end_time = time.time()
        self.selectItem_7 = self.listWidget_6.currentItem().text()
        spisok_2 = []
        for adress,dirs,files in os.walk(self.selectItem_5):
            for file in files:
                full=os.path.join(adress,file)
                if self.selectItem_7 in full:
                    if self.start_time < os.path.getctime(full) < end_time:
                        spisok_2.append(adress)
        for a in spisok_2:
            self.spi_2=a.split('/')
        for self.name in self.spi_2:
            if self.name != 'bina1' and self.name != 'bin':
                print(self.name)
                self.filename = self.name
        #for i in spisok_2:
            #self.spi=i.split('/')
            #print(self.spi)
        self.split_selectItem_7= self.selectItem_7.split('.exe')[0]
        print(self.split_selectItem_7)
        path_exe = a
        exe_file='export' + ' myBaseName='+'"'+self.selectItem_3 + ' | ' + self.filename +'"'+ ' && '+ ' /home/'+os.getlogin()+'/GamesForLinux/code_files/wine-create-shortcut '+" "+'"'+self.selectItem_7+'"'
        print(exe_file)
        os.system("bash -c '%s'" % exe_file)
        print(path_exe)
        print(self.filename)
        self.path_2 = '/home/'+os.getlogin()+'/GamesForLinux/code_files/icon/' +self.selectItem_3 + ' | ' + self.filename
        f_11 = self.directory_8 + self.selectItem_3
        f_11 = open(f_11, mode="a", encoding="utf_8")
        f_11.write('rm '+'"'+self.path_2+'"' +'\n')
        f_11.close()
        f_1 = '/home/'+os.getlogin()+'/GamesForLinux/code_files/icon/' +self.selectItem_3 + ' | ' + self.filename
        f_1 = open(f_1, mode="w", encoding="utf_8")
        f_1.write('#!/bin/sh'+'\n')
        f_1.write('cd '+"'"+'/home/'+os.getlogin()+'/'+a+"'"+'\n')
        f_1.write('Exec='+self.str2+'/home/'+os.getlogin()+'/'+self.split_selectItem_7+'.exe'+'"'+'\n')
        f_1.close()
        f_6 = '/home/'+os.getlogin()+'/GamesForLinux/code_files/software_icon_delete/' + self.selectItem_3 + ' | ' + self.filename
        f_6 = open(f_6, mode="w", encoding="utf_8")
        f_6.write('#!/bin/sh'+'\n')
        f_6.write(self.str2+'uninstaller'+'"'+'\n')
        f_6.write('/home/'+os.getlogin()+'/GamesForLinux/code_files/icon/' + self.selectItem_3 + ' | ' + self.filename)
        f_6.close()
        f_9 = '/home/'+os.getlogin()+'/GamesForLinux/code_files/software_HUD/' + self.selectItem_3 + ' | ' + self.filename
        f_9 = open(f_9, mode="w", encoding="utf_8")
        f_9.write(self.text4)
        f_9.close()
        chmod = 'chmod +x '+ '/home/'+os.getlogin()+'/GamesForLinux/code_files/software_icon_delete/' + '"'+self.selectItem_3 + ' | ' + self.filename+'"'
        os.system("bash -c '%s'" % chmod)
        chmod_2 = 'chmod +x '+ '/home/'+os.getlogin()+'/GamesForLinux/code_files/icon/' + '"'+self.selectItem_3 + ' | ' + self.filename+'"'
        os.system("bash -c '%s'" % chmod_2)
        self.listWidget_3.clear()
        self.directory_9 = '/home/'+os.getlogin()+'/GamesForLinux/code_files/icon/'
        for self.item_3 in os.listdir(self.directory_9):  # для каждого файла в директории
            if self.item_3 != self.icons:
                print(self.item_3)
                icon='/home/'+os.getlogin()+'/GamesForLinux/code_files/img_icon/'+self.item_3
                self.item_3 = QtWidgets.QListWidgetItem(self.item_3)
                self.run = QIcon(icon)
                self.item_3.setIcon(self.run)
                self.listWidget.setIconSize(QtCore.QSize(40, 40))
                self.listWidget_3.addItem(self.item_3)

    def software_hud(self):
        self.selectItem_4 = self.listWidget_3.currentItem().text()
        f_10 = '/home/'+os.getlogin()+'/GamesForLinux/code_files/software_HUD/'+self.selectItem_4
        f_10 = open(f_10, mode="r", encoding="utf_8")
        f_10=str(f_10.readlines()[0])
        f_10 = self.lineEdit_5.setText(f_10)

    def delete_icon(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        # msg.setIconPixmap(pixmap)  # Своя картинка

        msg.setWindowTitle("Информация")
        msg.setText("Удалить?")
        msg.setInformativeText("Удалить приложение?")

        okButton = msg.addButton( '  Да  ', QMessageBox.AcceptRole)
        msg.addButton('Нет', QMessageBox.RejectRole)
        okButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(233, 15, 131, 255), stop:1 rgba(25, 206, 246, 255));")
        msg.setStyleSheet("border-radius:5px;"
"background-color: rgb(48, 48, 48);"
"color: rgb(255, 255, 255);"
"font:11pt;"
"font-weight:900;")

        msg.exec()
        if msg.clickedButton() == okButton:
            self.selectItem_4 = self.listWidget_3.currentItem().text()
            self.split_selectItem_4 = self.selectItem_4.split(' |')[0]
            print(self.split_selectItem_4)
            self.text7 = self.directory_14 + self.split_selectItem_4
            self.f_13 = self.text7
            self.f_13 = open(self.f_13, mode="r", encoding="utf_8")
            self.wine_ver = str(self.f_13.readlines()[0])
            self.f_13.close()
            self.wine_ver=self.wine_ver.replace("\n", "")
            print(self.wine_ver)
            self.directory_12 = '/home/'+os.getlogin()+'/GamesForLinux/code_files/software_icon_delete/'
            self.f_8 = self.directory_12 + self.selectItem_4
            self.f_8 = open(self.f_8, mode="r", encoding="utf_8")
            self.str2=str(self.f_8.readlines()[1])
            start_uninstaller = 'export '+self.wine_ver+' && '+self.str2
            os.system("bash -c '%s'" % start_uninstaller)
            self.f_7 = self.directory_12 + self.selectItem_4
            self.f_7 = open(self.f_7, mode="r", encoding="utf_8")
            self.str3=str(self.f_7.readlines()[2])
            print(self.str3)
            rm_icon = 'rm ' + '"'+self.str3+'"'
            os.system("bash -c '%s'" % rm_icon)
            rm_software_icon_delete = 'rm ' + '"'+self.directory_12 + self.selectItem_4+'"'
            os.system("bash -c '%s'" % rm_software_icon_delete)
            self.listWidget_3.clear()
            self.directory_9 = '/home/'+os.getlogin()+'/GamesForLinux/code_files/icon/'
            for self.item_3 in os.listdir(self.directory_9):  # для каждого файла в директории
                if self.item_3 != self.icons:
                    print(self.item_3)
                    icon='/home/'+os.getlogin()+'/GamesForLinux/code_files/img_icon/'+self.item_3
                    self.item_3 = QtWidgets.QListWidgetItem(self.item_3)
                    self.run = QIcon(icon)
                    self.item_3.setIcon(self.run)
                    self.listWidget.setIconSize(QtCore.QSize(40, 40))
                    self.listWidget_3.addItem(self.item_3)

    def winecfg(self):
        self.selectItem_3 = self.listWidget_2.currentItem().text()
        self.text7 = self.directory_14 + self.selectItem_3
        self.f_13 = self.text7
        self.f_13 = open(self.f_13, mode="r", encoding="utf_8")
        self.wine_ver = str(self.f_13.readlines()[0])
        self.f_13.close()
        self.wine_ver=self.wine_ver.replace("\n", "")
        print(self.wine_ver)
        try:
            self.selectItem_2 = self.listWidget_2.currentItem().text()
            self.f_2 = self.directory_7+ self.selectItem_2
            self.f_2 = open(self.f_2, mode="r", encoding="utf_8")
            s=str(self.f_2.readlines()[2])
            winecfg =  'export '+ '"'+self.wine_ver+'"'+' && '+s
            os.system("bash -c '%s'" % winecfg)
            print(winecfg)
        except AttributeError:
            error_1 = 'Выбери пути!'
            QMessageBox.question(self, 'Введено', error_1, QMessageBox.Ok, QMessageBox.Ok)
        except IndexError:
            error_2 = 'Выбери пути!'
            QMessageBox.question(self, 'Введено', error_2, QMessageBox.Ok, QMessageBox.Ok)

    def Winetricks_run(self):
        self.selectItem_3 = self.listWidget_2.currentItem().text()
        self.text7 = self.directory_14 + self.selectItem_3
        self.f_13 = self.text7
        self.f_13 = open(self.f_13, mode="r", encoding="utf_8")
        self.wine_ver = str(self.f_13.readlines()[0])
        self.f_13.close()
        self.wine_ver=self.wine_ver.replace("\n", "")
        print(self.wine_ver)
        try:
            self.selectItem = self.listWidget_2.currentItem().text()
            self.f = self.directory_7+ self.selectItem
            self.f = open(self.f, mode="r", encoding="utf_8")
            a=str(self.f.readlines()[1])
            run =  'export '+ '"'+self.wine_ver+'"'+' && '+a
            os.system("bash -c '%s'" % run)
            print(run)
        except AttributeError:
            error_3 = 'Выбери пути!'
            QMessageBox.question(self, 'Введено', error_3, QMessageBox.Ok, QMessageBox.Ok)
        except IndexError:
            error_4 = 'Выбери пути!'
            QMessageBox.question(self, 'Введено', error_4, QMessageBox.Ok, QMessageBox.Ok)
        update =  '/home/'+os.getlogin()+'/GamesForLinux/code_files/winetricks --self-update'
        os.system("bash -c '%s'" % update)

    def Selectexe(self):
        directory3 = QtWidgets.QFileDialog.getOpenFileName(self,"выберете утсановщик", "","Windows Files (*.exe)")[0]
        print(directory3)
        self.text3 = str(directory3)
        self.label_6.setText(self.text3)



    def install_file(self):
        if self.text2 == 'wine':
            if self.text and self.text2:
                self.cb=self.comboBox.currentText()
                install = 'WINEARCH='+self.cb+' WINEPREFIX='+'"'+self.text+'" '+self.text2+' winecfg &'
                os.system("bash -c '%s'" % install)
                print(install)
                install = 'префикс успешно сконфигурирован'
        if self.text2 != 'wine':
                self.cb=self.comboBox.currentText()
                install = 'WINEARCH='+self.cb+' WINEPREFIX='+'"'+self.text+'" '+self.text2+'/bin/wine'+' winecfg &'
                os.system("bash -c '%s'" % install)
                print(install)
                install = 'префикс успешно сконфигурирован'
            #msg = QMessageBox()
            #msg.setIcon(QMessageBox.Information)

            #msg.setWindowTitle("Информация")
            #msg.setText("\nпрефикс успешно сконфигурирован")

            #okButton = msg.addButton('Ок', QMessageBox.AcceptRole)
            #okButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(233, 15, 131, 255), stop:1 rgba(25, 206, 246, 255));")
            #msg.setStyleSheet("border-radius:5px;"
#"background-color: rgb(48, 48, 48);"
#"color: rgb(255, 255, 255);"
#"font:11pt;"
#"font-weight:900;")
            #msg.exec()
        if self.text == '':
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)

                    msg.setWindowTitle("Информация")
                    msg.setText("Error")
                    msg.setInformativeText("InformativeText")

                    okButton = msg.addButton('Окей', QMessageBox.AcceptRole)
                    okButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(233, 15, 131, 255), stop:1 rgba(25, 206, 246, 255));")
                    msg.setStyleSheet("border-radius:5px;"
"background-color: rgb(48, 48, 48);"
"color: rgb(255, 255, 255);")
                    msg.exec()
                    if msg.clickedButton() == okButton:
                        print("Yes")
                    else:
                        print("No")

    def lineEdit_5_update(self):
        self.selectItem_4 = self.listWidget_3.currentItem().text()
        self.text5 = self.lineEdit_5.text()
        f_9 = '/home/'+os.getlogin()+'/GamesForLinux/code_files/software_HUD/'+ self.selectItem_4
        f_9 = open(f_9, mode="w", encoding="utf_8")
        f_9.write(self.text5)
        f_9.close()
        print(self.text5)

    def open_icon(self):
        self.selectItem_4 = self.listWidget_3.currentItem().text()
        self.split_selectItem_4 = self.selectItem_4.split(' |')[0]
        print(self.split_selectItem_4)
        self.text7 = self.directory_14 + self.split_selectItem_4
        self.f_13 = self.text7
        self.f_13 = open(self.f_13, mode="r", encoding="utf_8")
        self.wine_ver = str(self.f_13.readlines()[0])
        self.f_13.close()
        self.wine_ver=self.wine_ver.replace("\n", "")
        print(self.wine_ver)
        self.text5 = self.lineEdit_5.text()
        xdg2 ='export '+self.wine_ver+' && ' +'export '+ self.text5 + ' && '+ self.directory_9 + '"'+self.selectItem_4 + '"'
        os.system("bash -c '%s'" % xdg2 + '&')
        print(xdg2)
        print(self.text5)

class downloadThread(QThread):
    download_proess_signal = pyqtSignal(int)
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


class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## ==> SET INITIAL PROGRESS BAR TO (0) ZERO
        self.progressBarValue(0)

        ## ==> REMOVE STANDARD TITLE BAR
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) # Remove title bar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # Set background to transparent

        ## ==> APPLY DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(255, 16, 72))

        self.ui.circularBg.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(10)

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## DEF TO LOANDING
    ########################################################################
    def progress (self):
        global counter
        global jumper
        value = counter

        # HTML TEXT PERCENTAGE
        htmlText = """<p><span style=" font-size:68pt;">{VALUE}</span><span style=" font-size:58pt; vertical-align:super;">%</span></p>"""

        # REPLACE VALUE
        newHtml = htmlText.replace("{VALUE}", str(jumper))

        if(value > jumper):
            # APPLY NEW PERCENTAGE TEXT
            self.ui.labelPercentage.setText(newHtml)
            jumper += 10

        # SET VALUE TO PROGRESS BAR
        # fix max value error if > than 100
        if value >= 100: value = 1.000
        self.progressBarValue(value)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()
            # SHOW MAIN WINDOW
            #self.fb = MyFileBrowser()
            #self.fb.show()
            #app = QApplication([])
            self.GamesForLinux = ExampleApp()  # Создаём объект класса ExampleApp
            self.GamesForLinux.show()# Показываем окно
            #app.exec()


            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 0.5

    ## DEF PROGRESS BAR VALUE
    ########################################################################
    def progressBarValue(self, value):

        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
        QFrame{
        	border-radius: 150px;
        	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 16, 72, 140), stop:{STOP_2} rgb(255, 16, 72));
        }
        """

        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0

        # GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        # APPLY STYLESHEET WITH NEW VALUES
        self.ui.circularProgress.setStyleSheet(newStylesheet)


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())  # и запускаем приложение
