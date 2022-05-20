import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QFileInfo
from PyQt5.QtCore import Qt
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QMovie)
from PyQt5.QtWidgets import *
import theme # Это наш конвертированный файл дизайна
from theme import Ui_MainWindow
import os

class QCustomQWidget (QtWidgets.QWidget):                       # QtWidgets
    def __init__ (self, parent = None):
        super(QCustomQWidget, self).__init__(parent)
        self.textQVBoxLayout = QtWidgets.QVBoxLayout()          # QtWidgets
        self.textUpQLabel    = QtWidgets.QLabel()               # QtWidgets
        self.textDownQLabel  = QtWidgets.QLabel()               # QtWidgets
        self.textQVBoxLayout.addWidget(self.textUpQLabel)
        self.textQVBoxLayout.addWidget(self.textDownQLabel)
        self.allQHBoxLayout  = QtWidgets.QHBoxLayout()          # QtWidgets
        self.iconQLabel      = QtWidgets.QLabel()               # QtWidgets
        self.allQHBoxLayout.addWidget(self.iconQLabel, 0)
        self.toolButton_10 = QtWidgets.QToolButton()

        self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1)
        self.allQHBoxLayout.addWidget(self.toolButton_10,alignment=QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        self.setLayout(self.allQHBoxLayout)
        #setStyleSheet
        #self.textUpQLabel.setStyleSheet('''
            #color: rgb(0, 0, 255);
        #''')
        #self.textDownQLabel.setStyleSheet('''
            #color: rgb(255, 0, 0);
        #''')

    def setTextUp (self, text):
        self.textUpQLabel.setText(text)

    #def setTextDown (self, text):
        #self.textDownQLabel.setText(text)

    #def setIcon (self, imagePath):
        #self.iconQLabel.setPixmap(QtGui.QPixmap(imagePath).scaled(60, 60))   # + .scaled(60, 60

class QMainWindow (QtWidgets.QMainWindow,theme.Ui_MainWindow):                            # QtWidgets
    def __init__(self):
        super().__init__()
        self.directory_9 = '/home/'+os.getlogin()+'/GamesForLinux/code_files/icon'
        # Create QListWidget
        self.myQListWidget = QtWidgets.QListWidget()                     # QtWidgets
        for self.item in os.listdir(self.directory_9):
            # Create QCustomQWidget
            myQCustomQWidget = QCustomQWidget()
            myQCustomQWidget.setTextUp(self.item)
            # Create QListWidgetItem
            myQListWidgetItem = QtWidgets.QListWidgetItem(self.myQListWidget)  # QtWidgets
            # Set size hint
            myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
            # Add QListWidgetItem into QListWidget
            self.myQListWidget.addItem(myQListWidgetItem)
            self.myQListWidget.setItemWidget(myQListWidgetItem, myQCustomQWidget)
        self.setCentralWidget(self.myQListWidget)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])                                           # QtWidgets
    window = QMainWindow()
    window.show()
    sys.exit(app.exec_())
