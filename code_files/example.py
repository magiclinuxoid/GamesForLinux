# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(619, 532)
        MainWindow.setStyleSheet("background-color: rgb(71, 71, 71);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setMinimumSize(QtCore.QSize(100, 50))
        self.tabWidget.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("QTabBar::tab:selected{\n"
"background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QTabBar::tab:hover {}\n"
"QTabBar{\n"
"background-color:rgb(8, 148, 255);\n"
"border-top-left-radius: 8px;\n"
"border-bottom-left-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QToolButton{\n"
"background-color: transparent;\n"
"border:none;\n"
"font:  11pt;\n"
"font-weight:900;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QTabWidget{\n"
"background-color: rgb(48, 48, 48);\n"
"}\n"
"QTabBar::tab {\n"
"    border-top-left-radius: 8px;\n"
"    border-bottom-left-radius: 8px;\n"
"    min-height: 6ex;\n"
"    padding: 11px;\n"
"    border:10px;\n"
"    font:  11pt;\n"
"}\n"
"\n"
"")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setIconSize(QtCore.QSize(35, 40))
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("background-color: rgb(48, 48, 48);")
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.listWidget = QtWidgets.QListWidget(self.tab)
        self.listWidget.setStyleSheet("QListWidget{\n"
"font:11pt;\n"
"font-weight:900;\n"
"border:none;\n"
"}\n"
"QListWidget::item::selected{\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(233, 15, 131, 255), stop:1 rgba(25, 206, 246, 255));\n"
"}\n"
"")
        self.listWidget.setViewMode(QtWidgets.QListView.IconMode)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_4.addWidget(self.listWidget, 1, 0, 2, 1)
        self.Installscript = QtWidgets.QToolButton(self.tab)
        self.Installscript.setObjectName("Installscript")
        self.gridLayout_4.addWidget(self.Installscript, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 399, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 2, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setMinimumSize(QtCore.QSize(15, 5))
        self.comboBox_2.setStyleSheet("QScrollBar:vertical {\n"
"background-color: #0894FF;\n"
"width: 20px;\n"
"margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"border-radius: 10px;\n"
"background: #18E8FD;\n"
"min-height: 48px;\n"
"}\n"
"\n"
"/* This remvoes the bottom button by setting the height to 0px */\n"
"QScrollBar::add-line:vertical {\n"
"height: 0px;\n"
"subcontrol-position: bottom;\n"
"subcontrol-origin: margin;\n"
"}\n"
"\n"
"/* This remvoes the top button by setting the height to 0px */\n"
"QScrollBar::sub-line:vertical {\n"
"height: 0px;\n"
"subcontrol-position: top;\n"
"subcontrol-origin: margin;\n"
"}\n"
"\n"
"/* need this to get rid of crosshatching on scrollbar background */\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"background: none;\n"
"}\n"
"QComboBox{\n"
"border-width: 1px;        \n"
"border-style: solid;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(8, 148, 255, 255), stop:1 rgba(24, 232, 253, 255));\n"
"border-radius:5px;\n"
"border:none;\n"
"font:11pt;\n"
"font-weight:900;\n"
"padding:5px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"background-color: transparent;\n"
"    color:                      rgb(255, 255, 255);\n"
"    font-weight:            bold;\n"
"    padding:                    0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
" padding-right: 10px;\n"
"image: url(:/newPrefix/img/arrow-216-16.png);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0          rgba(24, 234, 253, 255), stop:0.75 rgba(8, 148, 255, 255));\n"
"border-radius:5px;\n"
"border:none;\n"
"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(44, 206, 255);\n"
"}")
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setMaxVisibleItems(15)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox_2)
        self.gridLayout_4.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.createprefix = QtWidgets.QWidget()
        self.createprefix.setStyleSheet("background-color: rgb(48, 48, 48);")
        self.createprefix.setObjectName("createprefix")
        self.gridLayout = QtWidgets.QGridLayout(self.createprefix)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 8, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.createprefix)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"border-width: 2px;        \n"
"border-style: solid;\n"
"border-top-left-radius: 22px;\n"
"border-bottom-left-radius: 22px;\n"
"border-color: transparent;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(255, 129, 25, 255), stop:1 rgba(255, 0, 0, 255));\n"
"font:11pt;\n"
"font-weight:900;\n"
"padding:12px;\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.lineEdit.setMaxLength(32767)
        self.lineEdit.setFrame(False)
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.Addbase = QtWidgets.QToolButton(self.createprefix)
        self.Addbase.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Addbase.sizePolicy().hasHeightForWidth())
        self.Addbase.setSizePolicy(sizePolicy)
        self.Addbase.setStyleSheet("QToolButton{\n"
"border-top-right-radius: 22px;\n"
"border-bottom-right-radius: 22px;\n"
"background-color:rgb(255, 0, 0);\n"
"}")
        self.Addbase.setIconSize(QtCore.QSize(40, 40))
        self.Addbase.setCheckable(True)
        self.Addbase.setChecked(False)
        self.Addbase.setAutoRepeat(False)
        self.Addbase.setAutoExclusive(True)
        self.Addbase.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.Addbase.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.Addbase.setAutoRaise(False)
        self.Addbase.setObjectName("Addbase")
        self.horizontalLayout.addWidget(self.Addbase)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Createprefix = QtWidgets.QToolButton(self.createprefix)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Createprefix.sizePolicy().hasHeightForWidth())
        self.Createprefix.setSizePolicy(sizePolicy)
        self.Createprefix.setMinimumSize(QtCore.QSize(0, 70))
        self.Createprefix.setStyleSheet("QToolButton::checked{\n"
"border-radius:5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(8, 148, 255, 255), stop:1 rgba(24, 232, 253, 255));\n"
"}")
        self.Createprefix.setIconSize(QtCore.QSize(40, 40))
        self.Createprefix.setCheckable(True)
        self.Createprefix.setChecked(False)
        self.Createprefix.setAutoExclusive(True)
        self.Createprefix.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.Createprefix.setObjectName("Createprefix")
        self.horizontalLayout_2.addWidget(self.Createprefix)
        self.Selectwine = QtWidgets.QToolButton(self.createprefix)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Selectwine.sizePolicy().hasHeightForWidth())
        self.Selectwine.setSizePolicy(sizePolicy)
        self.Selectwine.setStyleSheet("QToolButton::checked{\n"
"border-radius:5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(8, 148, 255, 255), stop:1 rgba(24, 232, 253, 255));\n"
"}")
        self.Selectwine.setIconSize(QtCore.QSize(40, 40))
        self.Selectwine.setCheckable(True)
        self.Selectwine.setChecked(False)
        self.Selectwine.setAutoExclusive(True)
        self.Selectwine.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.Selectwine.setObjectName("Selectwine")
        self.horizontalLayout_2.addWidget(self.Selectwine)
        self.comboBox = QtWidgets.QComboBox(self.createprefix)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet("QComboBox{\n"
"border-width: 1px;        \n"
"border-style: solid;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(255, 129, 25, 255), stop:1 rgba(255, 0, 0, 255));\n"
"border-radius:5px;\n"
"border:none;\n"
"font:11pt;\n"
"font-weight:900;\n"
"padding:5px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"background-color: transparent;\n"
"    color:                      rgb(255, 255, 255);\n"
"    font-weight:            bold;\n"
"    padding:                    0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
" padding-right: 10px;\n"
"image: url(:/newPrefix/img/arrow-216-16.png);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0          rgba(24, 234, 253, 255), stop:0.75 rgba(8, 148, 255, 255));\n"
"border-radius:5px;\n"
"border:none;\n"
"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(44, 206, 255);\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox, 0, QtCore.Qt.AlignHCenter)
        self.Prefixload = QtWidgets.QToolButton(self.createprefix)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Prefixload.sizePolicy().hasHeightForWidth())
        self.Prefixload.setSizePolicy(sizePolicy)
        self.Prefixload.setStyleSheet("QToolButton::checked{\n"
"border-radius:5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(8, 148, 255, 255), stop:1 rgba(24, 232, 253, 255));\n"
"}")
        self.Prefixload.setIconSize(QtCore.QSize(40, 40))
        self.Prefixload.setCheckable(True)
        self.Prefixload.setChecked(False)
        self.Prefixload.setAutoExclusive(True)
        self.Prefixload.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.Prefixload.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.Prefixload.setObjectName("Prefixload")
        self.horizontalLayout_2.addWidget(self.Prefixload)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.createprefix)
        self.label_3.setStyleSheet("border-width: 1px;        \n"
"border-style: solid;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(24, 234, 253, 255), stop:0.75 rgba(8, 148, 255, 255));\n"
"border-radius:5px;\n"
"border:none;\n"
"font:11pt;\n"
"font-weight:900;\n"
"padding:1px;\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label = QtWidgets.QLabel(self.createprefix)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_4 = QtWidgets.QLabel(self.createprefix)
        self.label_4.setStyleSheet("border-width: 1px;        \n"
"border-style: solid;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(24, 234, 253, 255), stop:0.75 rgba(8, 148, 255, 255));\n"
"border-radius:5px;\n"
"border:none;\n"
"font:11pt;\n"
"font-weight:900;\n"
"padding:1px;\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_2 = QtWidgets.QLabel(self.createprefix)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.gridLayout.addLayout(self.verticalLayout, 7, 0, 1, 1)
        self.tabWidget.addTab(self.createprefix, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setMouseTracking(False)
        self.tab_2.setAutoFillBackground(False)
        self.tab_2.setStyleSheet("background-color: rgb(48, 48, 48);")
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.listWidget_2 = QtWidgets.QListWidget(self.tab_2)
        self.listWidget_2.setStyleSheet("QListWidget{\n"
"font:11pt;\n"
"font-weight:900;\n"
"border:none;\n"
"}\n"
"QListWidget::item::selected{\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(233, 15, 131, 255), stop:1 rgba(25, 206, 246, 255));\n"
"}\n"
"")
        self.listWidget_2.setViewMode(QtWidgets.QListView.IconMode)
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout_3.addWidget(self.listWidget_2, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.selectexe = QtWidgets.QToolButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectexe.sizePolicy().hasHeightForWidth())
        self.selectexe.setSizePolicy(sizePolicy)
        self.selectexe.setMinimumSize(QtCore.QSize(0, 40))
        self.selectexe.setObjectName("selectexe")
        self.verticalLayout_5.addWidget(self.selectexe)
        self.installexe = QtWidgets.QToolButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.installexe.sizePolicy().hasHeightForWidth())
        self.installexe.setSizePolicy(sizePolicy)
        self.installexe.setMinimumSize(QtCore.QSize(0, 40))
        self.installexe.setObjectName("installexe")
        self.verticalLayout_5.addWidget(self.installexe)
        self.deleteitem = QtWidgets.QToolButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteitem.sizePolicy().hasHeightForWidth())
        self.deleteitem.setSizePolicy(sizePolicy)
        self.deleteitem.setMinimumSize(QtCore.QSize(0, 40))
        self.deleteitem.setObjectName("deleteitem")
        self.verticalLayout_5.addWidget(self.deleteitem)
        self.Winetricks = QtWidgets.QToolButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Winetricks.sizePolicy().hasHeightForWidth())
        self.Winetricks.setSizePolicy(sizePolicy)
        self.Winetricks.setMinimumSize(QtCore.QSize(0, 40))
        self.Winetricks.setObjectName("Winetricks")
        self.verticalLayout_5.addWidget(self.Winetricks)
        self.WineCfg = QtWidgets.QToolButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WineCfg.sizePolicy().hasHeightForWidth())
        self.WineCfg.setSizePolicy(sizePolicy)
        self.WineCfg.setMinimumSize(QtCore.QSize(0, 40))
        self.WineCfg.setObjectName("WineCfg")
        self.verticalLayout_5.addWidget(self.WineCfg)
        self.toolButton_6 = QtWidgets.QToolButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_6.sizePolicy().hasHeightForWidth())
        self.toolButton_6.setSizePolicy(sizePolicy)
        self.toolButton_6.setMinimumSize(QtCore.QSize(0, 40))
        self.toolButton_6.setObjectName("toolButton_6")
        self.verticalLayout_5.addWidget(self.toolButton_6)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.gridLayout_6.addLayout(self.verticalLayout_5, 0, 3, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_3.sizePolicy().hasHeightForWidth())
        self.tab_3.setSizePolicy(sizePolicy)
        self.tab_3.setMaximumSize(QtCore.QSize(560, 489))
        self.tab_3.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tab_3.setStyleSheet("background-color: rgb(48, 48, 48);")
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_3.setObjectName("comboBox_3")
        self.verticalLayout_3.addWidget(self.comboBox_3)
        self.gridLayout_5.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionrty = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("folder")
        self.actionrty.setIcon(icon)
        self.actionrty.setObjectName("actionrty")
        self.actionEnglish = QtWidgets.QAction(MainWindow)
        self.actionEnglish.setObjectName("actionEnglish")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.comboBox_2.setCurrentIndex(0)
        self.comboBox.setCurrentIndex(0)
        self.tabWidget.currentChanged['int'].connect(self.Addbase.hide)
        self.Prefixload.clicked.connect(self.Addbase.show)
        self.tabWidget.currentChanged['int'].connect(self.lineEdit.hide)
        self.Prefixload.clicked.connect(self.lineEdit.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.selectexe, self.installexe)
        MainWindow.setTabOrder(self.installexe, self.comboBox)
        MainWindow.setTabOrder(self.comboBox, self.Prefixload)
        MainWindow.setTabOrder(self.Prefixload, self.listWidget_2)
        MainWindow.setTabOrder(self.listWidget_2, self.Createprefix)
        MainWindow.setTabOrder(self.Createprefix, self.Selectwine)
        MainWindow.setTabOrder(self.Selectwine, self.deleteitem)
        MainWindow.setTabOrder(self.deleteitem, self.Winetricks)
        MainWindow.setTabOrder(self.Winetricks, self.WineCfg)
        MainWindow.setTabOrder(self.WineCfg, self.toolButton_6)
        MainWindow.setTabOrder(self.toolButton_6, self.Installscript)
        MainWindow.setTabOrder(self.Installscript, self.comboBox_2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Installscript.setText(_translate("MainWindow", "Установка"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "New Item"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "New Item"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "New Item"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "New Item"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "New Item"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "New Item"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "New Item"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "   Библиотека   "))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Введите название"))
        self.Addbase.setText(_translate("MainWindow", "Добавить в базу  \n"
"   префиксов    "))
        self.Createprefix.setText(_translate("MainWindow", "Создать и выбрать\n"
" префикс"))
        self.Selectwine.setText(_translate("MainWindow", "Выбрать wine"))
        self.comboBox.setCurrentText(_translate("MainWindow", "win64"))
        self.comboBox.setItemText(0, _translate("MainWindow", "win64"))
        self.comboBox.setItemText(1, _translate("MainWindow", "win32"))
        self.Prefixload.setText(_translate("MainWindow", "сконфигурировать \n"
"префикс"))
        self.label_3.setText(_translate("MainWindow", "Путь к префиксу:"))
        self.label_4.setText(_translate("MainWindow", "Путь к wine:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.createprefix), _translate("MainWindow", "  Создание  "))
        self.listWidget_2.setSortingEnabled(False)
        self.selectexe.setText(_translate("MainWindow", "Выбрать .exe"))
        self.installexe.setText(_translate("MainWindow", "Установка"))
        self.deleteitem.setText(_translate("MainWindow", "Удалить"))
        self.Winetricks.setText(_translate("MainWindow", "Winetricks"))
        self.WineCfg.setText(_translate("MainWindow", "Winecfg"))
        self.toolButton_6.setText(_translate("MainWindow", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "  Префиксы  "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "  Настройки  "))
        self.actionrty.setText(_translate("MainWindow", "rty"))
        self.actionrty.setShortcut(_translate("MainWindow", "Backspace"))
        self.actionEnglish.setText(_translate("MainWindow", "English"))
        self.action_2.setText(_translate("MainWindow", "Русский"))
import resource_rc
