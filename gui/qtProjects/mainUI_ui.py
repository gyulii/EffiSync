# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUI.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QCalendarWidget,
    QComboBox, QDateEdit, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLCDNumber, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QTextBrowser,
    QTextEdit, QVBoxLayout, QWidget)
import iconsDark_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(1138, 681)
        MainWindow.setStyleSheet(u"background-color: rgb(18, 18, 18);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_7 = QGridLayout(self.centralwidget)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.sideBarMiniWidget = QWidget(self.centralwidget)
        self.sideBarMiniWidget.setObjectName(u"sideBarMiniWidget")
        self.sideBarMiniWidget.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_21 = QHBoxLayout(self.sideBarMiniWidget)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.sideBarMini = QWidget(self.sideBarMiniWidget)
        self.sideBarMini.setObjectName(u"sideBarMini")
        self.sideBarMini.setMinimumSize(QSize(0, 0))
        self.sideBarMini.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(0, 0, 27);\n"
"}")
        self.verticalLayout_31 = QVBoxLayout(self.sideBarMini)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.menuBtnFrameMini = QFrame(self.sideBarMini)
        self.menuBtnFrameMini.setObjectName(u"menuBtnFrameMini")
        self.menuBtnFrameMini.setStyleSheet(u"QFrame{\n"
"	border:none;\n"
"	margin:5px;\n"
"}")
        self.menuBtnFrameMini.setFrameShape(QFrame.StyledPanel)
        self.menuBtnFrameMini.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.menuBtnFrameMini)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.menuBtnMini = QPushButton(self.menuBtnFrameMini)
        self.menuBtnMini.setObjectName(u"menuBtnMini")
        self.menuBtnMini.setMinimumSize(QSize(31, 31))
        self.menuBtnMini.setMaximumSize(QSize(64, 16777215))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        self.menuBtnMini.setFont(font)
        self.menuBtnMini.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid  rgb(2, 20, 72);\n"
"	border-radius: 15px;\n"
"	color: rgb(177, 177, 177);\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(23, 32, 42);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(3, 1, 59)\n"
"}")
        icon = QIcon()
        icon.addFile(u":/iconsDark/icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtnMini.setIcon(icon)
        self.menuBtnMini.setCheckable(True)

        self.verticalLayout_30.addWidget(self.menuBtnMini)


        self.verticalLayout_31.addWidget(self.menuBtnFrameMini)

        self.navigationBtnsFrameMini = QFrame(self.sideBarMini)
        self.navigationBtnsFrameMini.setObjectName(u"navigationBtnsFrameMini")
        self.navigationBtnsFrameMini.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"	margin:5px;\n"
"}")
        self.navigationBtnsFrameMini.setFrameShape(QFrame.StyledPanel)
        self.navigationBtnsFrameMini.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.navigationBtnsFrameMini)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(6, -1, -1, -1)
        self.homeBtnMini = QPushButton(self.navigationBtnsFrameMini)
        self.homeBtnMini.setObjectName(u"homeBtnMini")
        self.homeBtnMini.setMinimumSize(QSize(31, 31))
        self.homeBtnMini.setMaximumSize(QSize(64, 16777215))
        self.homeBtnMini.setFont(font)
        self.homeBtnMini.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid  rgb(2, 20, 72);\n"
"	border-radius: 15px;\n"
"	color: rgb(177, 177, 177);\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(23, 32, 42);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(3, 1, 59)\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/iconsDark/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtnMini.setIcon(icon1)

        self.verticalLayout_29.addWidget(self.homeBtnMini)

        self.recordTimeBtnMini = QPushButton(self.navigationBtnsFrameMini)
        self.recordTimeBtnMini.setObjectName(u"recordTimeBtnMini")
        self.recordTimeBtnMini.setMinimumSize(QSize(31, 31))
        self.recordTimeBtnMini.setMaximumSize(QSize(64, 16777215))
        self.recordTimeBtnMini.setFont(font)
        self.recordTimeBtnMini.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid  rgb(2, 20, 72);\n"
"	border-radius: 15px;\n"
"	color: rgb(177, 177, 177);\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(23, 32, 42);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(3, 1, 59)\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/iconsDark/icons/clock.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.recordTimeBtnMini.setIcon(icon2)

        self.verticalLayout_29.addWidget(self.recordTimeBtnMini)

        self.recordedTimesBtnMini = QPushButton(self.navigationBtnsFrameMini)
        self.recordedTimesBtnMini.setObjectName(u"recordedTimesBtnMini")
        self.recordedTimesBtnMini.setMinimumSize(QSize(31, 31))
        self.recordedTimesBtnMini.setMaximumSize(QSize(64, 16777215))
        self.recordedTimesBtnMini.setFont(font)
        self.recordedTimesBtnMini.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid  rgb(2, 20, 72);\n"
"	border-radius: 15px;\n"
"	color: rgb(177, 177, 177);\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(23, 32, 42);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(3, 1, 59)\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/iconsDark/icons/table.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.recordedTimesBtnMini.setIcon(icon3)

        self.verticalLayout_29.addWidget(self.recordedTimesBtnMini)

        self.managerBtnMini = QPushButton(self.navigationBtnsFrameMini)
        self.managerBtnMini.setObjectName(u"managerBtnMini")
        self.managerBtnMini.setMinimumSize(QSize(31, 31))
        self.managerBtnMini.setMaximumSize(QSize(64, 16777215))
        self.managerBtnMini.setFont(font)
        self.managerBtnMini.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid  rgb(2, 20, 72);\n"
"	border-radius: 15px;\n"
"	color: rgb(177, 177, 177);\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(23, 32, 42);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(3, 1, 59)\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/iconsDark/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.managerBtnMini.setIcon(icon4)
        self.managerBtnMini.setCheckable(True)
        self.managerBtnMini.setChecked(False)

        self.verticalLayout_29.addWidget(self.managerBtnMini)

        self.managerWidgetMini = QWidget(self.navigationBtnsFrameMini)
        self.managerWidgetMini.setObjectName(u"managerWidgetMini")
        self.managerWidgetMini.setMinimumSize(QSize(0, 181))
        self.verticalLayout_17 = QVBoxLayout(self.managerWidgetMini)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(3, 0, 0, 0)
        self.employeeBtnFrameMini = QFrame(self.managerWidgetMini)
        self.employeeBtnFrameMini.setObjectName(u"employeeBtnFrameMini")
        self.employeeBtnFrameMini.setFrameShape(QFrame.StyledPanel)
        self.employeeBtnFrameMini.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.employeeBtnFrameMini)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.employeeBtnMini = QPushButton(self.employeeBtnFrameMini)
        self.employeeBtnMini.setObjectName(u"employeeBtnMini")
        self.employeeBtnMini.setMinimumSize(QSize(0, 26))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(12)
        self.employeeBtnMini.setFont(font1)
        self.employeeBtnMini.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid  rgb(2, 20, 72);\n"
"	border-radius: 13px;\n"
"	color: rgb(177, 177, 177);\n"
"	padding-left: 15px;\n"
"	padding-right: 15px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(23, 32, 42);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(3, 1, 59)\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/iconsDark/icons/users.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.employeeBtnMini.setIcon(icon5)

        self.horizontalLayout_17.addWidget(self.employeeBtnMini)


        self.verticalLayout_17.addWidget(self.employeeBtnFrameMini)

        self.projectsBtnFrameMini = QFrame(self.managerWidgetMini)
        self.projectsBtnFrameMini.setObjectName(u"projectsBtnFrameMini")
        self.projectsBtnFrameMini.setFrameShape(QFrame.StyledPanel)
        self.projectsBtnFrameMini.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.projectsBtnFrameMini)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.projectsBtnMini = QPushButton(self.projectsBtnFrameMini)
        self.projectsBtnMini.setObjectName(u"projectsBtnMini")
        self.projectsBtnMini.setMinimumSize(QSize(0, 26))
        self.projectsBtnMini.setFont(font1)
        self.projectsBtnMini.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid  rgb(2, 20, 72);\n"
"	border-radius: 13px;\n"
"	color: rgb(177, 177, 177);\n"
"	padding-left: 15px;\n"
"	padding-right: 15px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(23, 32, 42);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(3, 1, 59)\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/iconsDark/icons/folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.projectsBtnMini.setIcon(icon6)

        self.horizontalLayout_18.addWidget(self.projectsBtnMini)


        self.verticalLayout_17.addWidget(self.projectsBtnFrameMini)

        self.topicsBtnFrameMini = QFrame(self.managerWidgetMini)
        self.topicsBtnFrameMini.setObjectName(u"topicsBtnFrameMini")
        self.topicsBtnFrameMini.setFrameShape(QFrame.StyledPanel)
        self.topicsBtnFrameMini.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.topicsBtnFrameMini)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.topicsbtnMini = QPushButton(self.topicsBtnFrameMini)
        self.topicsbtnMini.setObjectName(u"topicsbtnMini")
        self.topicsbtnMini.setMinimumSize(QSize(0, 26))
        self.topicsbtnMini.setFont(font1)
        self.topicsbtnMini.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid  rgb(2, 20, 72);\n"
"	border-radius: 13px;\n"
"	color: rgb(177, 177, 177);\n"
"	padding-left: 15px;\n"
"	padding-right: 15px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(23, 32, 42);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(3, 1, 59)\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/iconsDark/icons/message-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.topicsbtnMini.setIcon(icon7)

        self.horizontalLayout_19.addWidget(self.topicsbtnMini)


        self.verticalLayout_17.addWidget(self.topicsBtnFrameMini)

        self.bookintextsBtnFrameMini = QFrame(self.managerWidgetMini)
        self.bookintextsBtnFrameMini.setObjectName(u"bookintextsBtnFrameMini")
        self.bookintextsBtnFrameMini.setFrameShape(QFrame.StyledPanel)
        self.bookintextsBtnFrameMini.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.bookintextsBtnFrameMini)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.bookingtextsBtnMini = QPushButton(self.bookintextsBtnFrameMini)
        self.bookingtextsBtnMini.setObjectName(u"bookingtextsBtnMini")
        self.bookingtextsBtnMini.setMinimumSize(QSize(0, 26))
        self.bookingtextsBtnMini.setFont(font1)
        self.bookingtextsBtnMini.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid  rgb(2, 20, 72);\n"
"	border-radius: 13px;\n"
"	color: rgb(177, 177, 177);\n"
"	padding-left: 15px;\n"
"	padding-right: 15px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(23, 32, 42);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(3, 1, 59)\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/iconsDark/icons/book-open.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bookingtextsBtnMini.setIcon(icon8)

        self.horizontalLayout_22.addWidget(self.bookingtextsBtnMini)


        self.verticalLayout_17.addWidget(self.bookintextsBtnFrameMini)

        self.exportBtnFrameMini = QFrame(self.managerWidgetMini)
        self.exportBtnFrameMini.setObjectName(u"exportBtnFrameMini")
        self.exportBtnFrameMini.setFrameShape(QFrame.StyledPanel)
        self.exportBtnFrameMini.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.exportBtnFrameMini)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.exportBtnMini = QPushButton(self.exportBtnFrameMini)
        self.exportBtnMini.setObjectName(u"exportBtnMini")
        self.exportBtnMini.setMinimumSize(QSize(0, 26))
        self.exportBtnMini.setFont(font1)
        self.exportBtnMini.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid  rgb(2, 20, 72);\n"
"	border-radius: 13px;\n"
"	color: rgb(177, 177, 177);\n"
"	padding-left: 15px;\n"
"	padding-right: 15px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(23, 32, 42);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(3, 1, 59)\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/iconsDark/icons/external-link.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exportBtnMini.setIcon(icon9)

        self.horizontalLayout_20.addWidget(self.exportBtnMini)


        self.verticalLayout_17.addWidget(self.exportBtnFrameMini)


        self.verticalLayout_29.addWidget(self.managerWidgetMini)

        self.developerBtnMini = QPushButton(self.navigationBtnsFrameMini)
        self.developerBtnMini.setObjectName(u"developerBtnMini")
        self.developerBtnMini.setMinimumSize(QSize(31, 31))
        self.developerBtnMini.setMaximumSize(QSize(64, 16777215))
        self.developerBtnMini.setFont(font)
        self.developerBtnMini.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid  rgb(2, 20, 72);\n"
"	border-radius: 15px;\n"
"	color: rgb(177, 177, 177);\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(23, 32, 42);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(3, 1, 59)\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/iconsDark/icons/code.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.developerBtnMini.setIcon(icon10)

        self.verticalLayout_29.addWidget(self.developerBtnMini)


        self.verticalLayout_31.addWidget(self.navigationBtnsFrameMini)

        self.powerBtnFrameMini = QFrame(self.sideBarMini)
        self.powerBtnFrameMini.setObjectName(u"powerBtnFrameMini")
        self.powerBtnFrameMini.setStyleSheet(u"QFrame{\n"
"	border:none;\n"
"	margin:5px;\n"
"}")
        self.powerBtnFrameMini.setFrameShape(QFrame.StyledPanel)
        self.powerBtnFrameMini.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.powerBtnFrameMini)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(9, 9, 9, 9)
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacer_6)

        self.exitBtnMini = QPushButton(self.powerBtnFrameMini)
        self.exitBtnMini.setObjectName(u"exitBtnMini")
        self.exitBtnMini.setMinimumSize(QSize(31, 31))
        self.exitBtnMini.setMaximumSize(QSize(64, 16777215))
        self.exitBtnMini.setFont(font)
        self.exitBtnMini.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid  rgb(2, 20, 72);\n"
"	border-radius: 15px;\n"
"	color: rgb(177, 177, 177);\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(23, 32, 42);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(3, 1, 59)\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/iconsDark/icons/power.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exitBtnMini.setIcon(icon11)

        self.verticalLayout_28.addWidget(self.exitBtnMini)


        self.verticalLayout_31.addWidget(self.powerBtnFrameMini)


        self.horizontalLayout_21.addWidget(self.sideBarMini)


        self.gridLayout_7.addWidget(self.sideBarMiniWidget, 0, 0, 2, 1)

        self.bodyFrame = QFrame(self.centralwidget)
        self.bodyFrame.setObjectName(u"bodyFrame")
        self.bodyFrame.setMinimumSize(QSize(791, 611))
        self.bodyFrame.setFrameShape(QFrame.StyledPanel)
        self.bodyFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.bodyFrame)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.bodyContentFrame = QFrame(self.bodyFrame)
        self.bodyContentFrame.setObjectName(u"bodyContentFrame")
        self.bodyContentFrame.setFrameShape(QFrame.StyledPanel)
        self.bodyContentFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.bodyContentFrame)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.bodyWidget = QStackedWidget(self.bodyContentFrame)
        self.bodyWidget.setObjectName(u"bodyWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bodyWidget.sizePolicy().hasHeightForWidth())
        self.bodyWidget.setSizePolicy(sizePolicy)
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        sizePolicy.setHeightForWidth(self.homePage.sizePolicy().hasHeightForWidth())
        self.homePage.setSizePolicy(sizePolicy)
        self.homePage.setMinimumSize(QSize(791, 541))
        self.bodyWidget.addWidget(self.homePage)
        self.recordTimePage = QWidget()
        self.recordTimePage.setObjectName(u"recordTimePage")
        sizePolicy.setHeightForWidth(self.recordTimePage.sizePolicy().hasHeightForWidth())
        self.recordTimePage.setSizePolicy(sizePolicy)
        self.recordTimePage.setMinimumSize(QSize(791, 541))
        self.recordTimePage.setStyleSheet(u"QLabel{\n"
"	color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"QComboBox{\n"
"	color: rgb(186, 186, 186);\n"
"}")
        self.verticalLayout_36 = QVBoxLayout(self.recordTimePage)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.recordTimePageFrame = QFrame(self.recordTimePage)
        self.recordTimePageFrame.setObjectName(u"recordTimePageFrame")
        self.recordTimePageFrame.setFrameShape(QFrame.StyledPanel)
        self.recordTimePageFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.recordTimePageFrame)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.recordTimePageTitleFrame = QFrame(self.recordTimePageFrame)
        self.recordTimePageTitleFrame.setObjectName(u"recordTimePageTitleFrame")
        self.recordTimePageTitleFrame.setFrameShape(QFrame.StyledPanel)
        self.recordTimePageTitleFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.recordTimePageTitleFrame)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.title = QLabel(self.recordTimePageTitleFrame)
        self.title.setObjectName(u"title")
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(26)
        self.title.setFont(font2)

        self.verticalLayout_33.addWidget(self.title)


        self.verticalLayout_35.addWidget(self.recordTimePageTitleFrame)

        self.recordTimeContentFrame = QFrame(self.recordTimePageFrame)
        self.recordTimeContentFrame.setObjectName(u"recordTimeContentFrame")
        self.recordTimeContentFrame.setStyleSheet(u"QComboBox{\n"
"	color: rgb(186, 186, 186);\n"
"}")
        self.recordTimeContentFrame.setFrameShape(QFrame.StyledPanel)
        self.recordTimeContentFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.recordTimeContentFrame)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(9, -1, -1, -1)
        self.recordTimeSettingFrame = QFrame(self.recordTimeContentFrame)
        self.recordTimeSettingFrame.setObjectName(u"recordTimeSettingFrame")
        self.recordTimeSettingFrame.setFrameShape(QFrame.StyledPanel)
        self.recordTimeSettingFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.recordTimeSettingFrame)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.projectFrame = QFrame(self.recordTimeSettingFrame)
        self.projectFrame.setObjectName(u"projectFrame")
        self.projectFrame.setFrameShape(QFrame.StyledPanel)
        self.projectFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.projectFrame)
        self.verticalLayout_26.setSpacing(9)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 9, 0)
        self.projectLabel = QLabel(self.projectFrame)
        self.projectLabel.setObjectName(u"projectLabel")
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setPointSize(16)
        self.projectLabel.setFont(font3)

        self.verticalLayout_26.addWidget(self.projectLabel)

        self.projectDropDownList = QComboBox(self.projectFrame)
        self.projectDropDownList.addItem("")
        self.projectDropDownList.addItem("")
        self.projectDropDownList.addItem("")
        self.projectDropDownList.addItem("")
        self.projectDropDownList.addItem("")
        self.projectDropDownList.setObjectName(u"projectDropDownList")
        self.projectDropDownList.setMinimumSize(QSize(160, 30))
        self.projectDropDownList.setFont(font3)
        self.projectDropDownList.setStyleSheet(u"color: rgb(186, 186, 186);")

        self.verticalLayout_26.addWidget(self.projectDropDownList)


        self.horizontalLayout_27.addWidget(self.projectFrame)

        self.topicFrame = QFrame(self.recordTimeSettingFrame)
        self.topicFrame.setObjectName(u"topicFrame")
        self.topicFrame.setFrameShape(QFrame.StyledPanel)
        self.topicFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.topicFrame)
        self.verticalLayout_27.setSpacing(9)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(9, 0, -1, 0)
        self.topicLabel = QLabel(self.topicFrame)
        self.topicLabel.setObjectName(u"topicLabel")
        self.topicLabel.setFont(font3)

        self.verticalLayout_27.addWidget(self.topicLabel)

        self.topicDropDownList = QComboBox(self.topicFrame)
        self.topicDropDownList.addItem("")
        self.topicDropDownList.addItem("")
        self.topicDropDownList.addItem("")
        self.topicDropDownList.addItem("")
        self.topicDropDownList.addItem("")
        self.topicDropDownList.setObjectName(u"topicDropDownList")
        self.topicDropDownList.setMinimumSize(QSize(160, 30))
        self.topicDropDownList.setFont(font3)
        self.topicDropDownList.setStyleSheet(u"color: rgb(186, 186, 186);")

        self.verticalLayout_27.addWidget(self.topicDropDownList)


        self.horizontalLayout_27.addWidget(self.topicFrame)

        self.bookingtextFrame = QFrame(self.recordTimeSettingFrame)
        self.bookingtextFrame.setObjectName(u"bookingtextFrame")
        self.bookingtextFrame.setFrameShape(QFrame.StyledPanel)
        self.bookingtextFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.bookingtextFrame)
        self.verticalLayout_32.setSpacing(9)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(-1, 0, -1, 0)
        self.bookingtextLabel = QLabel(self.bookingtextFrame)
        self.bookingtextLabel.setObjectName(u"bookingtextLabel")
        self.bookingtextLabel.setFont(font3)

        self.verticalLayout_32.addWidget(self.bookingtextLabel)

        self.bookingtextDropDownList = QComboBox(self.bookingtextFrame)
        self.bookingtextDropDownList.addItem("")
        self.bookingtextDropDownList.addItem("")
        self.bookingtextDropDownList.addItem("")
        self.bookingtextDropDownList.addItem("")
        self.bookingtextDropDownList.addItem("")
        self.bookingtextDropDownList.setObjectName(u"bookingtextDropDownList")
        self.bookingtextDropDownList.setMinimumSize(QSize(160, 30))
        self.bookingtextDropDownList.setFont(font3)
        self.bookingtextDropDownList.setStyleSheet(u"color: rgb(186, 186, 186);")

        self.verticalLayout_32.addWidget(self.bookingtextDropDownList)


        self.horizontalLayout_27.addWidget(self.bookingtextFrame)

        self.horizontalSpacer_7 = QSpacerItem(88, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_7)

        self.horizontalSpacer_8 = QSpacerItem(88, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_8)


        self.verticalLayout_34.addWidget(self.recordTimeSettingFrame)

        self.buttonsFrame = QFrame(self.recordTimeContentFrame)
        self.buttonsFrame.setObjectName(u"buttonsFrame")
        self.buttonsFrame.setFrameShape(QFrame.StyledPanel)
        self.buttonsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.buttonsFrame)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, -1, -1, -1)
        self.startBtn_2 = QPushButton(self.buttonsFrame)
        self.startBtn_2.setObjectName(u"startBtn_2")
        self.startBtn_2.setMinimumSize(QSize(91, 31))
        self.startBtn_2.setFont(font)
        self.startBtn_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid  rgb(2, 20, 72);\n"
"	border-radius: 15px;\n"
"	color: rgb(177, 177, 177);\n"
"	padding-left: 6px;\n"
"	padding-right: 2px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(23, 32, 42);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(3, 1, 59)\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/iconsDark/icons/play.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.startBtn_2.setIcon(icon12)

        self.horizontalLayout_28.addWidget(self.startBtn_2)

        self.stopBtn_2 = QPushButton(self.buttonsFrame)
        self.stopBtn_2.setObjectName(u"stopBtn_2")
        self.stopBtn_2.setEnabled(False)
        self.stopBtn_2.setMinimumSize(QSize(91, 31))
        self.stopBtn_2.setFont(font)
        self.stopBtn_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid  rgb(2, 20, 72);\n"
"	border-radius: 15px;\n"
"	color: rgb(177, 177, 177);\n"
"	padding-left: 6px;\n"
"	padding-right: 2px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(23, 32, 42);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(3, 1, 59)\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/iconsDark/icons/stop-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.stopBtn_2.setIcon(icon13)

        self.horizontalLayout_28.addWidget(self.stopBtn_2)

        self.horizontalSpacer_12 = QSpacerItem(270, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_12)

        self.horizontalSpacer_13 = QSpacerItem(270, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_13)


        self.verticalLayout_34.addWidget(self.buttonsFrame)

        self.verticalSpacer_3 = QSpacerItem(20, 89, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_34.addItem(self.verticalSpacer_3)

        self.verticalSpacer_4 = QSpacerItem(20, 89, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_34.addItem(self.verticalSpacer_4)

        self.verticalSpacer_5 = QSpacerItem(20, 89, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_34.addItem(self.verticalSpacer_5)


        self.verticalLayout_35.addWidget(self.recordTimeContentFrame)


        self.verticalLayout_36.addWidget(self.recordTimePageFrame)

        self.bodyWidget.addWidget(self.recordTimePage)
        self.recordedTimePage = QWidget()
        self.recordedTimePage.setObjectName(u"recordedTimePage")
        sizePolicy.setHeightForWidth(self.recordedTimePage.sizePolicy().hasHeightForWidth())
        self.recordedTimePage.setSizePolicy(sizePolicy)
        self.recordedTimePage.setMinimumSize(QSize(791, 541))
        self.gridLayout_10 = QGridLayout(self.recordedTimePage)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.recordedTimePageFrame = QFrame(self.recordedTimePage)
        self.recordedTimePageFrame.setObjectName(u"recordedTimePageFrame")
        self.recordedTimePageFrame.setMinimumSize(QSize(781, 541))
        self.recordedTimePageFrame.setFrameShape(QFrame.StyledPanel)
        self.recordedTimePageFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.recordedTimePageFrame)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(9, 9, -1, -1)
        self.recordedTimeTitleFrame = QFrame(self.recordedTimePageFrame)
        self.recordedTimeTitleFrame.setObjectName(u"recordedTimeTitleFrame")
        sizePolicy.setHeightForWidth(self.recordedTimeTitleFrame.sizePolicy().hasHeightForWidth())
        self.recordedTimeTitleFrame.setSizePolicy(sizePolicy)
        self.recordedTimeTitleFrame.setMaximumSize(QSize(16777215, 75))
        self.recordedTimeTitleFrame.setStyleSheet(u"color: rgb(186, 186, 186);")
        self.recordedTimeTitleFrame.setFrameShape(QFrame.StyledPanel)
        self.recordedTimeTitleFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.recordedTimeTitleFrame)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.recordedTimeTitle = QLabel(self.recordedTimeTitleFrame)
        self.recordedTimeTitle.setObjectName(u"recordedTimeTitle")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.recordedTimeTitle.sizePolicy().hasHeightForWidth())
        self.recordedTimeTitle.setSizePolicy(sizePolicy1)
        self.recordedTimeTitle.setFont(font2)

        self.horizontalLayout_29.addWidget(self.recordedTimeTitle)

        self.horizontalSpacer_9 = QSpacerItem(89, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_9)

        self.horizontalSpacer_10 = QSpacerItem(90, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_10)

        self.horizontalSpacer_11 = QSpacerItem(89, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_11)

        self.lockAllBtn = QPushButton(self.recordedTimeTitleFrame)
        self.lockAllBtn.setObjectName(u"lockAllBtn")
        self.lockAllBtn.setEnabled(False)
        self.lockAllBtn.setMinimumSize(QSize(105, 31))
        self.lockAllBtn.setFont(font)
        self.lockAllBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid  rgb(2, 20, 72);\n"
"	border-radius: 15px;\n"
"	color: rgb(177, 177, 177);\n"
"	padding-left: 6px;\n"
"	padding-right: 2px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(23, 32, 42);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(3, 1, 59)\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/iconsDark/icons/unlock.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon14.addFile(u":/iconsDark/icons/lock.svg", QSize(), QIcon.Active, QIcon.On)
        icon14.addFile(u":/iconsDark/icons/lock.svg", QSize(), QIcon.Selected, QIcon.On)
        self.lockAllBtn.setIcon(icon14)
        self.lockAllBtn.setCheckable(True)

        self.horizontalLayout_29.addWidget(self.lockAllBtn)

        self.sendAllBtn = QPushButton(self.recordedTimeTitleFrame)
        self.sendAllBtn.setObjectName(u"sendAllBtn")
        self.sendAllBtn.setEnabled(False)
        self.sendAllBtn.setMinimumSize(QSize(105, 31))
        self.sendAllBtn.setFont(font)
        self.sendAllBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid  rgb(2, 20, 72);\n"
"	border-radius: 15px;\n"
"	color: rgb(177, 177, 177);\n"
"	padding-left: 6px;\n"
"	padding-right: 2px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(23, 32, 42);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(3, 1, 59)\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u":/iconsDark/icons/send.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sendAllBtn.setIcon(icon15)

        self.horizontalLayout_29.addWidget(self.sendAllBtn)

        self.horizontalSpacer_14 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_14)


        self.verticalLayout_13.addWidget(self.recordedTimeTitleFrame)

        self.recordedTimeContentFrame = QFrame(self.recordedTimePageFrame)
        self.recordedTimeContentFrame.setObjectName(u"recordedTimeContentFrame")
        sizePolicy.setHeightForWidth(self.recordedTimeContentFrame.sizePolicy().hasHeightForWidth())
        self.recordedTimeContentFrame.setSizePolicy(sizePolicy)
        self.recordedTimeContentFrame.setFrameShape(QFrame.StyledPanel)
        self.recordedTimeContentFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.recordedTimeContentFrame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(12, -1, 13, -1)
        self.recordedTimesTable = QTableWidget(self.recordedTimeContentFrame)
        if (self.recordedTimesTable.columnCount() < 7):
            self.recordedTimesTable.setColumnCount(7)
        self.recordedTimesTable.setObjectName(u"recordedTimesTable")
        self.recordedTimesTable.setMinimumSize(QSize(748, 435))
        self.recordedTimesTable.setStyleSheet(u"QTableWidget{\n"
"	alternate-background-color: rgb(1, 65, 63);\n"
"	color: rgb(186, 186, 186);\n"
"}")
        self.recordedTimesTable.setFrameShape(QFrame.StyledPanel)
        self.recordedTimesTable.setFrameShadow(QFrame.Sunken)
        self.recordedTimesTable.setLineWidth(3)
        self.recordedTimesTable.setMidLineWidth(0)
        self.recordedTimesTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.recordedTimesTable.setAlternatingRowColors(True)
        self.recordedTimesTable.setShowGrid(True)
        self.recordedTimesTable.setWordWrap(True)
        self.recordedTimesTable.setCornerButtonEnabled(False)
        self.recordedTimesTable.setRowCount(0)
        self.recordedTimesTable.setColumnCount(7)
        self.recordedTimesTable.verticalHeader().setVisible(False)

        self.verticalLayout_12.addWidget(self.recordedTimesTable)


        self.verticalLayout_13.addWidget(self.recordedTimeContentFrame)


        self.gridLayout_10.addWidget(self.recordedTimePageFrame, 0, 0, 1, 1)

        self.bodyWidget.addWidget(self.recordedTimePage)
        self.employeePage = QWidget()
        self.employeePage.setObjectName(u"employeePage")
        self.gridLayout_2 = QGridLayout(self.employeePage)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.employeesPageFrame = QFrame(self.employeePage)
        self.employeesPageFrame.setObjectName(u"employeesPageFrame")
        self.employeesPageFrame.setMinimumSize(QSize(781, 541))
        self.employeesPageFrame.setFrameShape(QFrame.StyledPanel)
        self.employeesPageFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.employeesPageFrame)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(9, 9, -1, -1)
        self.employeesTitleFrame = QFrame(self.employeesPageFrame)
        self.employeesTitleFrame.setObjectName(u"employeesTitleFrame")
        sizePolicy.setHeightForWidth(self.employeesTitleFrame.sizePolicy().hasHeightForWidth())
        self.employeesTitleFrame.setSizePolicy(sizePolicy)
        self.employeesTitleFrame.setMaximumSize(QSize(16777215, 150))
        self.employeesTitleFrame.setStyleSheet(u"color: rgb(186, 186, 186);")
        self.employeesTitleFrame.setFrameShape(QFrame.StyledPanel)
        self.employeesTitleFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.employeesTitleFrame)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(16, 0, 16, 0)
        self.employeesTitle = QLabel(self.employeesTitleFrame)
        self.employeesTitle.setObjectName(u"employeesTitle")
        sizePolicy1.setHeightForWidth(self.employeesTitle.sizePolicy().hasHeightForWidth())
        self.employeesTitle.setSizePolicy(sizePolicy1)
        self.employeesTitle.setFont(font2)

        self.horizontalLayout_23.addWidget(self.employeesTitle)

        self.addNewEmployeeBtn = QPushButton(self.employeesTitleFrame)
        self.addNewEmployeeBtn.setObjectName(u"addNewEmployeeBtn")
        self.addNewEmployeeBtn.setMinimumSize(QSize(0, 31))
        self.addNewEmployeeBtn.setFont(font)
        self.addNewEmployeeBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid  rgb(2, 20, 72);\n"
"	border-radius: 15px;\n"
"	color: rgb(177, 177, 177);\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(23, 32, 42);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(3, 1, 59)\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u":/iconsDark/icons/user-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addNewEmployeeBtn.setIcon(icon16)

        self.horizontalLayout_23.addWidget(self.addNewEmployeeBtn)


        self.verticalLayout_18.addWidget(self.employeesTitleFrame)

        self.employeesContentFrame = QFrame(self.employeesPageFrame)
        self.employeesContentFrame.setObjectName(u"employeesContentFrame")
        sizePolicy.setHeightForWidth(self.employeesContentFrame.sizePolicy().hasHeightForWidth())
        self.employeesContentFrame.setSizePolicy(sizePolicy)
        self.employeesContentFrame.setFrameShape(QFrame.StyledPanel)
        self.employeesContentFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.employeesContentFrame)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(12, -1, 13, -1)
        self.employeesTable = QTableWidget(self.employeesContentFrame)
        if (self.employeesTable.columnCount() < 7):
            self.employeesTable.setColumnCount(7)
        self.employeesTable.setObjectName(u"employeesTable")
        self.employeesTable.setMinimumSize(QSize(748, 431))
        self.employeesTable.setStyleSheet(u"QTableWidget{\n"
"	alternate-background-color: rgb(1, 65, 63);\n"
"	color: rgb(186, 186, 186);\n"
"}")
        self.employeesTable.setFrameShape(QFrame.StyledPanel)
        self.employeesTable.setFrameShadow(QFrame.Sunken)
        self.employeesTable.setLineWidth(3)
        self.employeesTable.setMidLineWidth(0)
        self.employeesTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.employeesTable.setAlternatingRowColors(True)
        self.employeesTable.setShowGrid(True)
        self.employeesTable.setWordWrap(True)
        self.employeesTable.setCornerButtonEnabled(False)
        self.employeesTable.setRowCount(0)
        self.employeesTable.setColumnCount(7)
        self.employeesTable.verticalHeader().setVisible(False)

        self.verticalLayout_20.addWidget(self.employeesTable)


        self.verticalLayout_18.addWidget(self.employeesContentFrame)


        self.gridLayout_2.addWidget(self.employeesPageFrame, 0, 0, 1, 1)

        self.bodyWidget.addWidget(self.employeePage)
        self.projectsPage = QWidget()
        self.projectsPage.setObjectName(u"projectsPage")
        self.gridLayout_11 = QGridLayout(self.projectsPage)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.projectsPageFrame = QFrame(self.projectsPage)
        self.projectsPageFrame.setObjectName(u"projectsPageFrame")
        self.projectsPageFrame.setMinimumSize(QSize(781, 541))
        self.projectsPageFrame.setFrameShape(QFrame.StyledPanel)
        self.projectsPageFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.projectsPageFrame)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(9, 9, -1, -1)
        self.projectsTitleFrame = QFrame(self.projectsPageFrame)
        self.projectsTitleFrame.setObjectName(u"projectsTitleFrame")
        sizePolicy.setHeightForWidth(self.projectsTitleFrame.sizePolicy().hasHeightForWidth())
        self.projectsTitleFrame.setSizePolicy(sizePolicy)
        self.projectsTitleFrame.setMaximumSize(QSize(16777215, 150))
        self.projectsTitleFrame.setStyleSheet(u"color: rgb(186, 186, 186);")
        self.projectsTitleFrame.setFrameShape(QFrame.StyledPanel)
        self.projectsTitleFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.projectsTitleFrame)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(16, 0, 16, 0)
        self.projectsTitle = QLabel(self.projectsTitleFrame)
        self.projectsTitle.setObjectName(u"projectsTitle")
        sizePolicy1.setHeightForWidth(self.projectsTitle.sizePolicy().hasHeightForWidth())
        self.projectsTitle.setSizePolicy(sizePolicy1)
        self.projectsTitle.setFont(font2)

        self.horizontalLayout_24.addWidget(self.projectsTitle)

        self.addNewProjectBtn = QPushButton(self.projectsTitleFrame)
        self.addNewProjectBtn.setObjectName(u"addNewProjectBtn")
        self.addNewProjectBtn.setMinimumSize(QSize(0, 31))
        self.addNewProjectBtn.setFont(font)
        self.addNewProjectBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid  rgb(2, 20, 72);\n"
"	border-radius: 15px;\n"
"	color: rgb(177, 177, 177);\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(23, 32, 42);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(3, 1, 59)\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u":/iconsDark/icons/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addNewProjectBtn.setIcon(icon17)

        self.horizontalLayout_24.addWidget(self.addNewProjectBtn)


        self.verticalLayout_19.addWidget(self.projectsTitleFrame)

        self.projectsContentFrame = QFrame(self.projectsPageFrame)
        self.projectsContentFrame.setObjectName(u"projectsContentFrame")
        sizePolicy.setHeightForWidth(self.projectsContentFrame.sizePolicy().hasHeightForWidth())
        self.projectsContentFrame.setSizePolicy(sizePolicy)
        self.projectsContentFrame.setFrameShape(QFrame.StyledPanel)
        self.projectsContentFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.projectsContentFrame)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(12, -1, 13, -1)
        self.projectsTable = QTableWidget(self.projectsContentFrame)
        if (self.projectsTable.columnCount() < 7):
            self.projectsTable.setColumnCount(7)
        self.projectsTable.setObjectName(u"projectsTable")
        self.projectsTable.setMinimumSize(QSize(748, 431))
        self.projectsTable.setStyleSheet(u"QTableWidget{\n"
"	alternate-background-color: rgb(1, 65, 63);\n"
"	color: rgb(186, 186, 186);\n"
"}")
        self.projectsTable.setFrameShape(QFrame.StyledPanel)
        self.projectsTable.setFrameShadow(QFrame.Sunken)
        self.projectsTable.setLineWidth(3)
        self.projectsTable.setMidLineWidth(0)
        self.projectsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.projectsTable.setAlternatingRowColors(True)
        self.projectsTable.setShowGrid(True)
        self.projectsTable.setWordWrap(True)
        self.projectsTable.setCornerButtonEnabled(False)
        self.projectsTable.setRowCount(0)
        self.projectsTable.setColumnCount(7)
        self.projectsTable.verticalHeader().setVisible(False)

        self.verticalLayout_21.addWidget(self.projectsTable)


        self.verticalLayout_19.addWidget(self.projectsContentFrame)


        self.gridLayout_11.addWidget(self.projectsPageFrame, 0, 0, 1, 1)

        self.bodyWidget.addWidget(self.projectsPage)
        self.topicsPage = QWidget()
        self.topicsPage.setObjectName(u"topicsPage")
        self.gridLayout_12 = QGridLayout(self.topicsPage)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.topicsPageFrame = QFrame(self.topicsPage)
        self.topicsPageFrame.setObjectName(u"topicsPageFrame")
        self.topicsPageFrame.setMinimumSize(QSize(781, 541))
        self.topicsPageFrame.setFrameShape(QFrame.StyledPanel)
        self.topicsPageFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.topicsPageFrame)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(9, 9, -1, -1)
        self.topicsTitleFrame = QFrame(self.topicsPageFrame)
        self.topicsTitleFrame.setObjectName(u"topicsTitleFrame")
        sizePolicy.setHeightForWidth(self.topicsTitleFrame.sizePolicy().hasHeightForWidth())
        self.topicsTitleFrame.setSizePolicy(sizePolicy)
        self.topicsTitleFrame.setMaximumSize(QSize(16777215, 150))
        self.topicsTitleFrame.setStyleSheet(u"color: rgb(186, 186, 186);")
        self.topicsTitleFrame.setFrameShape(QFrame.StyledPanel)
        self.topicsTitleFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.topicsTitleFrame)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(16, 0, 16, 0)
        self.topicTitle = QLabel(self.topicsTitleFrame)
        self.topicTitle.setObjectName(u"topicTitle")
        sizePolicy1.setHeightForWidth(self.topicTitle.sizePolicy().hasHeightForWidth())
        self.topicTitle.setSizePolicy(sizePolicy1)
        self.topicTitle.setFont(font2)

        self.horizontalLayout_25.addWidget(self.topicTitle)

        self.addNewTopicBtn = QPushButton(self.topicsTitleFrame)
        self.addNewTopicBtn.setObjectName(u"addNewTopicBtn")
        self.addNewTopicBtn.setMinimumSize(QSize(0, 31))
        self.addNewTopicBtn.setFont(font)
        self.addNewTopicBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid  rgb(2, 20, 72);\n"
"	border-radius: 15px;\n"
"	color: rgb(177, 177, 177);\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(23, 32, 42);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(3, 1, 59)\n"
"}")
        self.addNewTopicBtn.setIcon(icon17)

        self.horizontalLayout_25.addWidget(self.addNewTopicBtn)


        self.verticalLayout_22.addWidget(self.topicsTitleFrame)

        self.topicsContentFrame = QFrame(self.topicsPageFrame)
        self.topicsContentFrame.setObjectName(u"topicsContentFrame")
        sizePolicy.setHeightForWidth(self.topicsContentFrame.sizePolicy().hasHeightForWidth())
        self.topicsContentFrame.setSizePolicy(sizePolicy)
        self.topicsContentFrame.setFrameShape(QFrame.StyledPanel)
        self.topicsContentFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.topicsContentFrame)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(12, -1, 13, -1)
        self.topicsTable = QTableWidget(self.topicsContentFrame)
        if (self.topicsTable.columnCount() < 7):
            self.topicsTable.setColumnCount(7)
        self.topicsTable.setObjectName(u"topicsTable")
        self.topicsTable.setMinimumSize(QSize(748, 431))
        self.topicsTable.setStyleSheet(u"QTableWidget{\n"
"	alternate-background-color: rgb(1, 65, 63);\n"
"	color: rgb(186, 186, 186);\n"
"}")
        self.topicsTable.setFrameShape(QFrame.StyledPanel)
        self.topicsTable.setFrameShadow(QFrame.Sunken)
        self.topicsTable.setLineWidth(3)
        self.topicsTable.setMidLineWidth(0)
        self.topicsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.topicsTable.setAlternatingRowColors(True)
        self.topicsTable.setShowGrid(True)
        self.topicsTable.setWordWrap(True)
        self.topicsTable.setCornerButtonEnabled(False)
        self.topicsTable.setRowCount(0)
        self.topicsTable.setColumnCount(7)
        self.topicsTable.verticalHeader().setVisible(False)

        self.verticalLayout_23.addWidget(self.topicsTable)


        self.verticalLayout_22.addWidget(self.topicsContentFrame)


        self.gridLayout_12.addWidget(self.topicsPageFrame, 0, 0, 1, 1)

        self.bodyWidget.addWidget(self.topicsPage)
        self.bookingtextsPage = QWidget()
        self.bookingtextsPage.setObjectName(u"bookingtextsPage")
        self.gridLayout_13 = QGridLayout(self.bookingtextsPage)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.bookingtextsPageFrame = QFrame(self.bookingtextsPage)
        self.bookingtextsPageFrame.setObjectName(u"bookingtextsPageFrame")
        self.bookingtextsPageFrame.setMinimumSize(QSize(781, 541))
        self.bookingtextsPageFrame.setFrameShape(QFrame.StyledPanel)
        self.bookingtextsPageFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.bookingtextsPageFrame)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(9, 9, -1, -1)
        self.bookingtextsTitleFrame = QFrame(self.bookingtextsPageFrame)
        self.bookingtextsTitleFrame.setObjectName(u"bookingtextsTitleFrame")
        sizePolicy.setHeightForWidth(self.bookingtextsTitleFrame.sizePolicy().hasHeightForWidth())
        self.bookingtextsTitleFrame.setSizePolicy(sizePolicy)
        self.bookingtextsTitleFrame.setMaximumSize(QSize(16777215, 150))
        self.bookingtextsTitleFrame.setStyleSheet(u"color: rgb(186, 186, 186);")
        self.bookingtextsTitleFrame.setFrameShape(QFrame.StyledPanel)
        self.bookingtextsTitleFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.bookingtextsTitleFrame)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(16, 0, 16, 0)
        self.bookingtextsTitle = QLabel(self.bookingtextsTitleFrame)
        self.bookingtextsTitle.setObjectName(u"bookingtextsTitle")
        sizePolicy1.setHeightForWidth(self.bookingtextsTitle.sizePolicy().hasHeightForWidth())
        self.bookingtextsTitle.setSizePolicy(sizePolicy1)
        self.bookingtextsTitle.setFont(font2)

        self.horizontalLayout_26.addWidget(self.bookingtextsTitle)

        self.addNewBookingtextsBtn = QPushButton(self.bookingtextsTitleFrame)
        self.addNewBookingtextsBtn.setObjectName(u"addNewBookingtextsBtn")
        self.addNewBookingtextsBtn.setMinimumSize(QSize(0, 31))
        self.addNewBookingtextsBtn.setFont(font)
        self.addNewBookingtextsBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid  rgb(2, 20, 72);\n"
"	border-radius: 15px;\n"
"	color: rgb(177, 177, 177);\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(23, 32, 42);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(3, 1, 59)\n"
"}")
        self.addNewBookingtextsBtn.setIcon(icon17)

        self.horizontalLayout_26.addWidget(self.addNewBookingtextsBtn)


        self.verticalLayout_24.addWidget(self.bookingtextsTitleFrame)

        self.bookingtextsContentFrame = QFrame(self.bookingtextsPageFrame)
        self.bookingtextsContentFrame.setObjectName(u"bookingtextsContentFrame")
        sizePolicy.setHeightForWidth(self.bookingtextsContentFrame.sizePolicy().hasHeightForWidth())
        self.bookingtextsContentFrame.setSizePolicy(sizePolicy)
        self.bookingtextsContentFrame.setFrameShape(QFrame.StyledPanel)
        self.bookingtextsContentFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.bookingtextsContentFrame)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(12, -1, 13, -1)
        self.bookingtextsTable = QTableWidget(self.bookingtextsContentFrame)
        if (self.bookingtextsTable.columnCount() < 7):
            self.bookingtextsTable.setColumnCount(7)
        self.bookingtextsTable.setObjectName(u"bookingtextsTable")
        self.bookingtextsTable.setMinimumSize(QSize(748, 431))
        self.bookingtextsTable.setStyleSheet(u"QTableWidget{\n"
"	alternate-background-color: rgb(1, 65, 63);\n"
"	color: rgb(186, 186, 186);\n"
"}")
        self.bookingtextsTable.setFrameShape(QFrame.StyledPanel)
        self.bookingtextsTable.setFrameShadow(QFrame.Sunken)
        self.bookingtextsTable.setLineWidth(3)
        self.bookingtextsTable.setMidLineWidth(0)
        self.bookingtextsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.bookingtextsTable.setAlternatingRowColors(True)
        self.bookingtextsTable.setShowGrid(True)
        self.bookingtextsTable.setWordWrap(True)
        self.bookingtextsTable.setCornerButtonEnabled(False)
        self.bookingtextsTable.setRowCount(0)
        self.bookingtextsTable.setColumnCount(7)
        self.bookingtextsTable.verticalHeader().setVisible(False)

        self.verticalLayout_25.addWidget(self.bookingtextsTable)


        self.verticalLayout_24.addWidget(self.bookingtextsContentFrame)


        self.gridLayout_13.addWidget(self.bookingtextsPageFrame, 0, 0, 1, 1)

        self.bodyWidget.addWidget(self.bookingtextsPage)
        self.exportPage = QWidget()
        self.exportPage.setObjectName(u"exportPage")
        sizePolicy.setHeightForWidth(self.exportPage.sizePolicy().hasHeightForWidth())
        self.exportPage.setSizePolicy(sizePolicy)
        self.exportPage.setMinimumSize(QSize(791, 541))
        self.exportPage.setStyleSheet(u"color: rgb(186, 186, 186);")
        self.gridLayout_9 = QGridLayout(self.exportPage)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.exportPageFrame = QFrame(self.exportPage)
        self.exportPageFrame.setObjectName(u"exportPageFrame")
        self.exportPageFrame.setMinimumSize(QSize(781, 541))
        self.exportPageFrame.setFrameShape(QFrame.StyledPanel)
        self.exportPageFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.exportPageFrame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.exportTitleFrame = QFrame(self.exportPageFrame)
        self.exportTitleFrame.setObjectName(u"exportTitleFrame")
        self.exportTitleFrame.setMaximumSize(QSize(16777215, 150))
        self.exportTitleFrame.setFrameShape(QFrame.StyledPanel)
        self.exportTitleFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.exportTitleFrame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.exportPageTitle = QLabel(self.exportTitleFrame)
        self.exportPageTitle.setObjectName(u"exportPageTitle")
        self.exportPageTitle.setFont(font2)

        self.gridLayout_6.addWidget(self.exportPageTitle, 0, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.exportTitleFrame)

        self.exportContentFrame = QFrame(self.exportPageFrame)
        self.exportContentFrame.setObjectName(u"exportContentFrame")
        self.exportContentFrame.setFrameShape(QFrame.StyledPanel)
        self.exportContentFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.exportContentFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.optionsFrame_2 = QFrame(self.exportContentFrame)
        self.optionsFrame_2.setObjectName(u"optionsFrame_2")
        self.optionsFrame_2.setFrameShape(QFrame.StyledPanel)
        self.optionsFrame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.optionsFrame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.settingFrame = QFrame(self.optionsFrame_2)
        self.settingFrame.setObjectName(u"settingFrame")
        self.settingFrame.setFrameShape(QFrame.StyledPanel)
        self.settingFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.settingFrame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.fromFrame = QFrame(self.settingFrame)
        self.fromFrame.setObjectName(u"fromFrame")
        self.fromFrame.setFrameShape(QFrame.StyledPanel)
        self.fromFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.fromFrame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.fromDateFrame = QFrame(self.fromFrame)
        self.fromDateFrame.setObjectName(u"fromDateFrame")
        self.fromDateFrame.setFrameShape(QFrame.StyledPanel)
        self.fromDateFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.fromDateFrame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label = QLabel(self.fromDateFrame)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout_6.addWidget(self.label)

        self.fromLabel = QDateEdit(self.fromDateFrame)
        self.fromLabel.setObjectName(u"fromLabel")
        self.fromLabel.setFont(font)
        self.fromLabel.setReadOnly(True)
        self.fromLabel.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.horizontalLayout_6.addWidget(self.fromLabel)


        self.verticalLayout_6.addWidget(self.fromDateFrame)

        self.fromDateBtn = QPushButton(self.fromFrame)
        self.fromDateBtn.setObjectName(u"fromDateBtn")
        self.fromDateBtn.setMinimumSize(QSize(91, 31))
        self.fromDateBtn.setFont(font)
        self.fromDateBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid  rgb(2, 20, 72);\n"
"	border-radius: 15px;\n"
"	color: rgb(177, 177, 177);\n"
"	padding-left: 6px;\n"
"	padding-right: 2px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(23, 32, 42);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(3, 1, 59)\n"
"}")
        self.fromDateBtn.setCheckable(True)

        self.verticalLayout_6.addWidget(self.fromDateBtn)


        self.horizontalLayout_9.addWidget(self.fromFrame)

        self.toFrame = QFrame(self.settingFrame)
        self.toFrame.setObjectName(u"toFrame")
        self.toFrame.setFrameShape(QFrame.StyledPanel)
        self.toFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.toFrame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.toDateFrame = QFrame(self.toFrame)
        self.toDateFrame.setObjectName(u"toDateFrame")
        self.toDateFrame.setFrameShape(QFrame.StyledPanel)
        self.toDateFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.toDateFrame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.toLabel = QLabel(self.toDateFrame)
        self.toLabel.setObjectName(u"toLabel")
        self.toLabel.setFont(font)

        self.horizontalLayout_7.addWidget(self.toLabel)

        self.toDate = QDateEdit(self.toDateFrame)
        self.toDate.setObjectName(u"toDate")
        self.toDate.setFont(font)
        self.toDate.setReadOnly(True)
        self.toDate.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.horizontalLayout_7.addWidget(self.toDate)


        self.verticalLayout_7.addWidget(self.toDateFrame)

        self.toDateBtn = QPushButton(self.toFrame)
        self.toDateBtn.setObjectName(u"toDateBtn")
        self.toDateBtn.setMinimumSize(QSize(91, 31))
        self.toDateBtn.setFont(font)
        self.toDateBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid  rgb(2, 20, 72);\n"
"	border-radius: 15px;\n"
"	color: rgb(177, 177, 177);\n"
"	padding-left: 6px;\n"
"	padding-right: 2px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(23, 32, 42);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(3, 1, 59)\n"
"}")
        self.toDateBtn.setCheckable(True)

        self.verticalLayout_7.addWidget(self.toDateBtn)


        self.horizontalLayout_9.addWidget(self.toFrame)

        self.optionsFrame = QFrame(self.settingFrame)
        self.optionsFrame.setObjectName(u"optionsFrame")
        self.optionsFrame.setFrameShape(QFrame.StyledPanel)
        self.optionsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.optionsFrame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.optionsLabelFrame = QFrame(self.optionsFrame)
        self.optionsLabelFrame.setObjectName(u"optionsLabelFrame")
        self.optionsLabelFrame.setFrameShape(QFrame.StyledPanel)
        self.optionsLabelFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.optionsLabelFrame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, -1, -1, -1)
        self.optionsLabel = QLabel(self.optionsLabelFrame)
        self.optionsLabel.setObjectName(u"optionsLabel")
        self.optionsLabel.setFont(font)

        self.horizontalLayout_8.addWidget(self.optionsLabel)


        self.verticalLayout_8.addWidget(self.optionsLabelFrame)

        self.optionList = QComboBox(self.optionsFrame)
        self.optionList.addItem("")
        self.optionList.addItem("")
        self.optionList.addItem("")
        self.optionList.addItem("")
        self.optionList.addItem("")
        self.optionList.addItem("")
        self.optionList.setObjectName(u"optionList")
        self.optionList.setMinimumSize(QSize(161, 31))
        self.optionList.setFont(font1)

        self.verticalLayout_8.addWidget(self.optionList)


        self.horizontalLayout_9.addWidget(self.optionsFrame)


        self.verticalLayout_4.addWidget(self.settingFrame)

        self.calendarFrame = QFrame(self.optionsFrame_2)
        self.calendarFrame.setObjectName(u"calendarFrame")
        self.calendarFrame.setFrameShape(QFrame.StyledPanel)
        self.calendarFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.calendarFrame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.fromCalendar = QCalendarWidget(self.calendarFrame)
        self.fromCalendar.setObjectName(u"fromCalendar")
        self.fromCalendar.setEnabled(True)
        self.fromCalendar.setToolTipDuration(-1)
        self.fromCalendar.setGridVisible(True)

        self.horizontalLayout_10.addWidget(self.fromCalendar)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_4)

        self.toCalendar = QCalendarWidget(self.calendarFrame)
        self.toCalendar.setObjectName(u"toCalendar")
        self.toCalendar.setEnabled(True)
        self.toCalendar.setToolTipDuration(-1)
        self.toCalendar.setGridVisible(True)

        self.horizontalLayout_10.addWidget(self.toCalendar)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_6)


        self.verticalLayout_4.addWidget(self.calendarFrame)


        self.verticalLayout_5.addWidget(self.optionsFrame_2)

        self.verticalSpacer_2 = QSpacerItem(20, 113, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.exportBtnFrame = QFrame(self.exportContentFrame)
        self.exportBtnFrame.setObjectName(u"exportBtnFrame")
        self.exportBtnFrame.setFrameShape(QFrame.StyledPanel)
        self.exportBtnFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.exportBtnFrame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(261, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.exportDataBtn = QPushButton(self.exportBtnFrame)
        self.exportDataBtn.setObjectName(u"exportDataBtn")
        self.exportDataBtn.setMinimumSize(QSize(181, 31))
        self.exportDataBtn.setFont(font)
        self.exportDataBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid  rgb(2, 20, 72);\n"
"	border-radius: 15px;\n"
"	color: rgb(177, 177, 177);\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	text-align: center;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(23, 32, 42);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(3, 1, 59)\n"
"}")
        self.exportDataBtn.setIcon(icon9)

        self.horizontalLayout_5.addWidget(self.exportDataBtn)

        self.horizontalSpacer_5 = QSpacerItem(261, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)


        self.verticalLayout_5.addWidget(self.exportBtnFrame)


        self.verticalLayout_9.addWidget(self.exportContentFrame)


        self.gridLayout_9.addWidget(self.exportPageFrame, 0, 0, 1, 1)

        self.bodyWidget.addWidget(self.exportPage)
        self.developerPage = QWidget()
        self.developerPage.setObjectName(u"developerPage")
        sizePolicy.setHeightForWidth(self.developerPage.sizePolicy().hasHeightForWidth())
        self.developerPage.setSizePolicy(sizePolicy)
        self.developerPage.setMinimumSize(QSize(791, 541))
        font4 = QFont()
        font4.setFamilies([u"Times New Roman"])
        font4.setPointSize(24)
        self.developerPage.setFont(font4)
        self.developerPage.setStyleSheet(u"color: rgb(186, 186, 186);")
        self.gridLayout_8 = QGridLayout(self.developerPage)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.developerPageFrame = QFrame(self.developerPage)
        self.developerPageFrame.setObjectName(u"developerPageFrame")
        self.developerPageFrame.setMinimumSize(QSize(781, 541))
        self.developerPageFrame.setFrameShape(QFrame.StyledPanel)
        self.developerPageFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.developerPageFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.titleFrame = QFrame(self.developerPageFrame)
        self.titleFrame.setObjectName(u"titleFrame")
        self.titleFrame.setMaximumSize(QSize(16777215, 150))
        self.titleFrame.setFrameShape(QFrame.StyledPanel)
        self.titleFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.titleFrame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.developerPageTitle = QLabel(self.titleFrame)
        self.developerPageTitle.setObjectName(u"developerPageTitle")
        self.developerPageTitle.setFont(font2)

        self.gridLayout_4.addWidget(self.developerPageTitle, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.titleFrame)

        self.contentFrame = QFrame(self.developerPageFrame)
        self.contentFrame.setObjectName(u"contentFrame")
        self.contentFrame.setFrameShape(QFrame.StyledPanel)
        self.contentFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.textBrowser = QTextBrowser(self.contentFrame)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_2.addWidget(self.textBrowser)


        self.verticalLayout_3.addWidget(self.contentFrame)


        self.gridLayout_8.addWidget(self.developerPageFrame, 0, 0, 1, 1)

        self.bodyWidget.addWidget(self.developerPage)

        self.verticalLayout_14.addWidget(self.bodyWidget)


        self.gridLayout_5.addWidget(self.bodyContentFrame, 0, 0, 1, 1)

        self.userLogFrame = QFrame(self.bodyFrame)
        self.userLogFrame.setObjectName(u"userLogFrame")
        self.userLogFrame.setMaximumSize(QSize(16777215, 150))
        self.userLogFrame.setFrameShape(QFrame.StyledPanel)
        self.userLogFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.userLogFrame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(20, -1, 20, -1)
        self.userLog = QTextEdit(self.userLogFrame)
        self.userLog.setObjectName(u"userLog")
        self.userLog.setStyleSheet(u"color: rgb(186, 186, 186);")

        self.horizontalLayout_11.addWidget(self.userLog)


        self.gridLayout_5.addWidget(self.userLogFrame, 1, 0, 1, 1)


        self.gridLayout_7.addWidget(self.bodyFrame, 1, 2, 1, 1)

        self.headBarFrame = QFrame(self.centralwidget)
        self.headBarFrame.setObjectName(u"headBarFrame")
        self.headBarFrame.setMinimumSize(QSize(801, 61))
        self.headBarFrame.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-color: rgb(0, 0, 27);\n"
"}")
        self.headBarFrame.setFrameShape(QFrame.StyledPanel)
        self.headBarFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.headBarFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 4, 0, 9)
        self.startsoptBtnFrame = QFrame(self.headBarFrame)
        self.startsoptBtnFrame.setObjectName(u"startsoptBtnFrame")
        self.startsoptBtnFrame.setStyleSheet(u"QFrame{\n"
"	border:none;\n"
"	margin:3px;\n"
"}")
        self.startsoptBtnFrame.setFrameShape(QFrame.StyledPanel)
        self.startsoptBtnFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.startsoptBtnFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 5, -1, 6)
        self.startBtn = QPushButton(self.startsoptBtnFrame)
        self.startBtn.setObjectName(u"startBtn")
        self.startBtn.setMinimumSize(QSize(91, 31))
        self.startBtn.setFont(font)
        self.startBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid  rgb(2, 20, 72);\n"
"	border-radius: 15px;\n"
"	color: rgb(177, 177, 177);\n"
"	padding-left: 6px;\n"
"	padding-right: 2px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(23, 32, 42);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(3, 1, 59)\n"
"}")
        self.startBtn.setIcon(icon12)

        self.horizontalLayout.addWidget(self.startBtn)

        self.stopBtn = QPushButton(self.startsoptBtnFrame)
        self.stopBtn.setObjectName(u"stopBtn")
        self.stopBtn.setEnabled(False)
        self.stopBtn.setMinimumSize(QSize(91, 31))
        self.stopBtn.setFont(font)
        self.stopBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid  rgb(2, 20, 72);\n"
"	border-radius: 15px;\n"
"	color: rgb(177, 177, 177);\n"
"	padding-left: 6px;\n"
"	padding-right: 2px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(23, 32, 42);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(3, 1, 59)\n"
"}")
        self.stopBtn.setIcon(icon13)

        self.horizontalLayout.addWidget(self.stopBtn)


        self.horizontalLayout_4.addWidget(self.startsoptBtnFrame)

        self.horizontalSpacer = QSpacerItem(57, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.frame = QFrame(self.headBarFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"	border:none;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.dateLCD = QLCDNumber(self.frame)
        self.dateLCD.setObjectName(u"dateLCD")
        self.dateLCD.setMinimumSize(QSize(171, 31))
        self.dateLCD.setSmallDecimalPoint(False)
        self.dateLCD.setDigitCount(11)
        self.dateLCD.setSegmentStyle(QLCDNumber.Filled)
        self.dateLCD.setProperty("value", 2024.000000000000000)
        self.dateLCD.setProperty("intValue", 2024)

        self.horizontalLayout_2.addWidget(self.dateLCD)

        self.timeLCD = QLCDNumber(self.frame)
        self.timeLCD.setObjectName(u"timeLCD")
        self.timeLCD.setMinimumSize(QSize(75, 31))
        self.timeLCD.setStyleSheet(u"QFrame{\n"
"	border:none;\n"
"}")
        self.timeLCD.setProperty("value", 16.210000000000001)

        self.horizontalLayout_2.addWidget(self.timeLCD)

        self.timeLCD.raise_()
        self.dateLCD.raise_()

        self.horizontalLayout_4.addWidget(self.frame)

        self.horizontalSpacer_2 = QSpacerItem(58, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.userFrame = QFrame(self.headBarFrame)
        self.userFrame.setObjectName(u"userFrame")
        self.userFrame.setStyleSheet(u"QFrame{\n"
"	border:none;\n"
"}")
        self.userFrame.setFrameShape(QFrame.StyledPanel)
        self.userFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.userFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 5, -1, 5)
        self.user = QLabel(self.userFrame)
        self.user.setObjectName(u"user")
        self.user.setMinimumSize(QSize(131, 31))
        self.user.setFont(font1)
        self.user.setStyleSheet(u"QLabel{\n"
"	color: rgb(186, 186, 186);\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid rgb(2, 20, 72);\n"
"	border-radius: 10px;\n"
"	padding-left: 10px;\n"
"	padding-right: 19px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.user)


        self.horizontalLayout_4.addWidget(self.userFrame)


        self.gridLayout_7.addWidget(self.headBarFrame, 0, 2, 1, 1)

        self.sideBarWidget = QWidget(self.centralwidget)
        self.sideBarWidget.setObjectName(u"sideBarWidget")
        self.verticalLayout_16 = QVBoxLayout(self.sideBarWidget)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.sideBar = QWidget(self.sideBarWidget)
        self.sideBar.setObjectName(u"sideBar")
        self.sideBar.setMinimumSize(QSize(221, 681))
        self.sideBar.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(0, 0, 27);\n"
"}")
        self.verticalLayout_15 = QVBoxLayout(self.sideBar)
        self.verticalLayout_15.setSpacing(6)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 14, 0)
        self.menuBtnFrame = QFrame(self.sideBar)
        self.menuBtnFrame.setObjectName(u"menuBtnFrame")
        self.menuBtnFrame.setStyleSheet(u"QFrame{\n"
"	border:none;\n"
"	margin:5px;\n"
"}")
        self.menuBtnFrame.setFrameShape(QFrame.StyledPanel)
        self.menuBtnFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.menuBtnFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.menuBtn = QPushButton(self.menuBtnFrame)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setMinimumSize(QSize(181, 31))
        self.menuBtn.setFont(font)
        self.menuBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid  rgb(2, 20, 72);\n"
"	border-radius: 15px;\n"
"	color: rgb(177, 177, 177);\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(23, 32, 42);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(3, 1, 59)\n"
"}")
        self.menuBtn.setIcon(icon)
        self.menuBtn.setCheckable(True)

        self.gridLayout.addWidget(self.menuBtn, 0, 0, 1, 1)


        self.verticalLayout_15.addWidget(self.menuBtnFrame)

        self.navigationBtnsFrame = QFrame(self.sideBar)
        self.navigationBtnsFrame.setObjectName(u"navigationBtnsFrame")
        self.navigationBtnsFrame.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"	margin:5px;\n"
"}")
        self.navigationBtnsFrame.setFrameShape(QFrame.StyledPanel)
        self.navigationBtnsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.navigationBtnsFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, -1, -1, -1)
        self.homeBtn = QPushButton(self.navigationBtnsFrame)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setMinimumSize(QSize(181, 31))
        self.homeBtn.setFont(font)
        self.homeBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid  rgb(2, 20, 72);\n"
"	border-radius: 15px;\n"
"	color: rgb(177, 177, 177);\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(23, 32, 42);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(3, 1, 59)\n"
"}")
        self.homeBtn.setIcon(icon1)

        self.verticalLayout.addWidget(self.homeBtn)

        self.recordTimeBtn = QPushButton(self.navigationBtnsFrame)
        self.recordTimeBtn.setObjectName(u"recordTimeBtn")
        self.recordTimeBtn.setMinimumSize(QSize(181, 31))
        self.recordTimeBtn.setFont(font)
        self.recordTimeBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid  rgb(2, 20, 72);\n"
"	border-radius: 15px;\n"
"	color: rgb(177, 177, 177);\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(23, 32, 42);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(3, 1, 59)\n"
"}")
        self.recordTimeBtn.setIcon(icon2)

        self.verticalLayout.addWidget(self.recordTimeBtn)

        self.recordedTimesBtn = QPushButton(self.navigationBtnsFrame)
        self.recordedTimesBtn.setObjectName(u"recordedTimesBtn")
        self.recordedTimesBtn.setMinimumSize(QSize(181, 31))
        self.recordedTimesBtn.setFont(font)
        self.recordedTimesBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid  rgb(2, 20, 72);\n"
"	border-radius: 15px;\n"
"	color: rgb(177, 177, 177);\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(23, 32, 42);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(3, 1, 59)\n"
"}")
        self.recordedTimesBtn.setIcon(icon3)

        self.verticalLayout.addWidget(self.recordedTimesBtn)

        self.managerBtn = QPushButton(self.navigationBtnsFrame)
        self.managerBtn.setObjectName(u"managerBtn")
        self.managerBtn.setMinimumSize(QSize(181, 31))
        self.managerBtn.setFont(font)
        self.managerBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid  rgb(2, 20, 72);\n"
"	border-radius: 15px;\n"
"	color: rgb(177, 177, 177);\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(23, 32, 42);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(3, 1, 59)\n"
"}")
        self.managerBtn.setIcon(icon4)
        self.managerBtn.setCheckable(True)
        self.managerBtn.setChecked(False)

        self.verticalLayout.addWidget(self.managerBtn)

        self.managerWidget = QWidget(self.navigationBtnsFrame)
        self.managerWidget.setObjectName(u"managerWidget")
        self.managerWidget.setMinimumSize(QSize(151, 181))
        self.verticalLayout_10 = QVBoxLayout(self.managerWidget)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(9, 0, 0, 0)
        self.employeeBtnFrame = QFrame(self.managerWidget)
        self.employeeBtnFrame.setObjectName(u"employeeBtnFrame")
        self.employeeBtnFrame.setFrameShape(QFrame.StyledPanel)
        self.employeeBtnFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.employeeBtnFrame)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.employeeBtn = QPushButton(self.employeeBtnFrame)
        self.employeeBtn.setObjectName(u"employeeBtn")
        self.employeeBtn.setMinimumSize(QSize(0, 26))
        self.employeeBtn.setFont(font1)
        self.employeeBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid  rgb(2, 20, 72);\n"
"	border-radius: 13px;\n"
"	color: rgb(177, 177, 177);\n"
"	padding-left: 15px;\n"
"	padding-right: 15px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(23, 32, 42);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(3, 1, 59)\n"
"}")
        self.employeeBtn.setIcon(icon5)

        self.horizontalLayout_12.addWidget(self.employeeBtn)


        self.verticalLayout_10.addWidget(self.employeeBtnFrame)

        self.projectsBtnFrame = QFrame(self.managerWidget)
        self.projectsBtnFrame.setObjectName(u"projectsBtnFrame")
        self.projectsBtnFrame.setFrameShape(QFrame.StyledPanel)
        self.projectsBtnFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.projectsBtnFrame)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.projectsBtn = QPushButton(self.projectsBtnFrame)
        self.projectsBtn.setObjectName(u"projectsBtn")
        self.projectsBtn.setMinimumSize(QSize(0, 26))
        self.projectsBtn.setFont(font1)
        self.projectsBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid  rgb(2, 20, 72);\n"
"	border-radius: 13px;\n"
"	color: rgb(177, 177, 177);\n"
"	padding-left: 15px;\n"
"	padding-right: 15px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(23, 32, 42);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(3, 1, 59)\n"
"}")
        self.projectsBtn.setIcon(icon6)

        self.horizontalLayout_13.addWidget(self.projectsBtn)


        self.verticalLayout_10.addWidget(self.projectsBtnFrame)

        self.topicsBtnFrame = QFrame(self.managerWidget)
        self.topicsBtnFrame.setObjectName(u"topicsBtnFrame")
        self.topicsBtnFrame.setFrameShape(QFrame.StyledPanel)
        self.topicsBtnFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.topicsBtnFrame)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.topicsBtn = QPushButton(self.topicsBtnFrame)
        self.topicsBtn.setObjectName(u"topicsBtn")
        self.topicsBtn.setMinimumSize(QSize(0, 26))
        self.topicsBtn.setFont(font1)
        self.topicsBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid  rgb(2, 20, 72);\n"
"	border-radius: 13px;\n"
"	color: rgb(177, 177, 177);\n"
"	padding-left: 15px;\n"
"	padding-right: 15px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(23, 32, 42);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(3, 1, 59)\n"
"}")
        self.topicsBtn.setIcon(icon7)

        self.horizontalLayout_14.addWidget(self.topicsBtn)


        self.verticalLayout_10.addWidget(self.topicsBtnFrame)

        self.bookingtextsBtnFrame = QFrame(self.managerWidget)
        self.bookingtextsBtnFrame.setObjectName(u"bookingtextsBtnFrame")
        self.bookingtextsBtnFrame.setFrameShape(QFrame.StyledPanel)
        self.bookingtextsBtnFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.bookingtextsBtnFrame)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.bookingtextsBtn = QPushButton(self.bookingtextsBtnFrame)
        self.bookingtextsBtn.setObjectName(u"bookingtextsBtn")
        self.bookingtextsBtn.setMinimumSize(QSize(0, 26))
        self.bookingtextsBtn.setFont(font1)
        self.bookingtextsBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid  rgb(2, 20, 72);\n"
"	border-radius: 13px;\n"
"	color: rgb(177, 177, 177);\n"
"	padding-left: 15px;\n"
"	padding-right: 15px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(23, 32, 42);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(3, 1, 59)\n"
"}")
        self.bookingtextsBtn.setIcon(icon8)

        self.horizontalLayout_15.addWidget(self.bookingtextsBtn)


        self.verticalLayout_10.addWidget(self.bookingtextsBtnFrame)

        self.exportBttnFrame = QFrame(self.managerWidget)
        self.exportBttnFrame.setObjectName(u"exportBttnFrame")
        self.exportBttnFrame.setFrameShape(QFrame.StyledPanel)
        self.exportBttnFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.exportBttnFrame)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.exportBtn = QPushButton(self.exportBttnFrame)
        self.exportBtn.setObjectName(u"exportBtn")
        self.exportBtn.setMinimumSize(QSize(0, 26))
        self.exportBtn.setFont(font1)
        self.exportBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid  rgb(2, 20, 72);\n"
"	border-radius: 13px;\n"
"	color: rgb(177, 177, 177);\n"
"	padding-left: 15px;\n"
"	padding-right: 15px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(23, 32, 42);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(3, 1, 59)\n"
"}")
        self.exportBtn.setIcon(icon9)

        self.horizontalLayout_16.addWidget(self.exportBtn)


        self.verticalLayout_10.addWidget(self.exportBttnFrame)


        self.verticalLayout.addWidget(self.managerWidget)

        self.developerBtn = QPushButton(self.navigationBtnsFrame)
        self.developerBtn.setObjectName(u"developerBtn")
        self.developerBtn.setMinimumSize(QSize(181, 31))
        self.developerBtn.setFont(font)
        self.developerBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid  rgb(2, 20, 72);\n"
"	border-radius: 15px;\n"
"	color: rgb(177, 177, 177);\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(23, 32, 42);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(3, 1, 59)\n"
"}")
        self.developerBtn.setIcon(icon10)

        self.verticalLayout.addWidget(self.developerBtn)


        self.verticalLayout_15.addWidget(self.navigationBtnsFrame)

        self.powerBtnFrame = QFrame(self.sideBar)
        self.powerBtnFrame.setObjectName(u"powerBtnFrame")
        self.powerBtnFrame.setStyleSheet(u"QFrame{\n"
"	border:none;\n"
"	margin:5px;\n"
"}")
        self.powerBtnFrame.setFrameShape(QFrame.StyledPanel)
        self.powerBtnFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.powerBtnFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.exitBtn = QPushButton(self.powerBtnFrame)
        self.exitBtn.setObjectName(u"exitBtn")
        self.exitBtn.setMinimumSize(QSize(181, 31))
        self.exitBtn.setFont(font)
        self.exitBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid  rgb(2, 20, 72);\n"
"	border-radius: 15px;\n"
"	color: rgb(177, 177, 177);\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(23, 32, 42);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(3, 1, 59)\n"
"}")
        self.exitBtn.setIcon(icon11)

        self.gridLayout_3.addWidget(self.exitBtn, 1, 0, 1, 1)


        self.verticalLayout_15.addWidget(self.powerBtnFrame)


        self.verticalLayout_16.addWidget(self.sideBar)


        self.gridLayout_7.addWidget(self.sideBarWidget, 0, 1, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.bodyFrame.raise_()
        self.headBarFrame.raise_()
        self.sideBarMiniWidget.raise_()
        self.sideBarWidget.raise_()

        self.retranslateUi(MainWindow)
        self.fromCalendar.clicked.connect(self.fromLabel.setDate)
        self.toCalendar.clicked.connect(self.toDate.setDate)
        self.menuBtnMini.clicked["bool"].connect(self.sideBarMini.setHidden)
        self.recordedTimesBtnMini.clicked.connect(self.recordedTimesBtn.click)
        self.menuBtn.clicked.connect(self.menuBtnMini.click)
        self.menuBtnMini.clicked["bool"].connect(self.sideBar.setVisible)
        self.managerBtnMini.clicked.connect(self.managerBtn.click)
        self.developerBtnMini.clicked.connect(self.developerBtn.click)
        self.homeBtnMini.clicked.connect(self.homeBtn.click)
        self.recordTimeBtnMini.clicked.connect(self.recordTimeBtn.click)
        self.exitBtn.clicked.connect(MainWindow.close)
        self.exitBtnMini.clicked.connect(self.exitBtn.click)
        self.managerBtn.clicked["bool"].connect(self.managerWidget.setVisible)
        self.managerBtnMini.clicked["bool"].connect(self.managerWidgetMini.setVisible)
        self.managerBtnMini.clicked["bool"].connect(self.managerWidget.setVisible)
        self.managerBtn.clicked["bool"].connect(self.managerWidgetMini.setVisible)
        self.managerBtn.clicked["bool"].connect(self.managerBtnMini.setChecked)
        self.employeeBtnMini.clicked.connect(self.employeeBtn.click)
        self.projectsBtnMini.clicked.connect(self.projectsBtn.click)
        self.topicsbtnMini.clicked.connect(self.topicsBtn.click)
        self.bookingtextsBtnMini.clicked.connect(self.bookingtextsBtn.click)
        self.exportBtnMini.clicked.connect(self.exportBtn.click)

        self.bodyWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuBtnMini.setText("")
        self.homeBtnMini.setText("")
        self.recordTimeBtnMini.setText("")
        self.recordedTimesBtnMini.setText("")
        self.managerBtnMini.setText("")
        self.employeeBtnMini.setText("")
        self.projectsBtnMini.setText("")
        self.topicsbtnMini.setText("")
        self.bookingtextsBtnMini.setText("")
        self.exportBtnMini.setText("")
        self.developerBtnMini.setText("")
        self.exitBtnMini.setText("")
        self.title.setText(QCoreApplication.translate("MainWindow", u"Record Time", None))
        self.projectLabel.setText(QCoreApplication.translate("MainWindow", u"Project", None))
        self.projectDropDownList.setItemText(0, QCoreApplication.translate("MainWindow", u"Project1", None))
        self.projectDropDownList.setItemText(1, QCoreApplication.translate("MainWindow", u"Project2", None))
        self.projectDropDownList.setItemText(2, QCoreApplication.translate("MainWindow", u"Project3", None))
        self.projectDropDownList.setItemText(3, QCoreApplication.translate("MainWindow", u"Project4", None))
        self.projectDropDownList.setItemText(4, QCoreApplication.translate("MainWindow", u"Project5", None))

        self.topicLabel.setText(QCoreApplication.translate("MainWindow", u"Topic", None))
        self.topicDropDownList.setItemText(0, QCoreApplication.translate("MainWindow", u"Topic1", None))
        self.topicDropDownList.setItemText(1, QCoreApplication.translate("MainWindow", u"Topic2", None))
        self.topicDropDownList.setItemText(2, QCoreApplication.translate("MainWindow", u"Topic3", None))
        self.topicDropDownList.setItemText(3, QCoreApplication.translate("MainWindow", u"Topic4", None))
        self.topicDropDownList.setItemText(4, QCoreApplication.translate("MainWindow", u"Topic5", None))

        self.bookingtextLabel.setText(QCoreApplication.translate("MainWindow", u"Booking text", None))
        self.bookingtextDropDownList.setItemText(0, QCoreApplication.translate("MainWindow", u"Booking Text 1", None))
        self.bookingtextDropDownList.setItemText(1, QCoreApplication.translate("MainWindow", u"Booking Text 2", None))
        self.bookingtextDropDownList.setItemText(2, QCoreApplication.translate("MainWindow", u"Booking Text 3", None))
        self.bookingtextDropDownList.setItemText(3, QCoreApplication.translate("MainWindow", u"Booking Text 4", None))
        self.bookingtextDropDownList.setItemText(4, QCoreApplication.translate("MainWindow", u"Booking Text 5", None))

        self.startBtn_2.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.stopBtn_2.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.recordedTimeTitle.setText(QCoreApplication.translate("MainWindow", u"Recorded Times", None))
        self.lockAllBtn.setText(QCoreApplication.translate("MainWindow", u"Lock All", None))
        self.sendAllBtn.setText(QCoreApplication.translate("MainWindow", u"Send All", None))
        self.employeesTitle.setText(QCoreApplication.translate("MainWindow", u"Employees", None))
        self.addNewEmployeeBtn.setText(QCoreApplication.translate("MainWindow", u"Add new employee", None))
        self.projectsTitle.setText(QCoreApplication.translate("MainWindow", u"Projects", None))
        self.addNewProjectBtn.setText(QCoreApplication.translate("MainWindow", u"Add new project", None))
        self.topicTitle.setText(QCoreApplication.translate("MainWindow", u"Topics", None))
        self.addNewTopicBtn.setText(QCoreApplication.translate("MainWindow", u"Add new topic", None))
        self.bookingtextsTitle.setText(QCoreApplication.translate("MainWindow", u"Booking texts", None))
        self.addNewBookingtextsBtn.setText(QCoreApplication.translate("MainWindow", u"Add new booking text", None))
        self.exportPageTitle.setText(QCoreApplication.translate("MainWindow", u"What do you want to export?", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"From:", None))
        self.fromDateBtn.setText(QCoreApplication.translate("MainWindow", u"Open Calendar", None))
        self.toLabel.setText(QCoreApplication.translate("MainWindow", u"To:", None))
        self.toDateBtn.setText(QCoreApplication.translate("MainWindow", u"Open Calendar", None))
        self.optionsLabel.setText(QCoreApplication.translate("MainWindow", u"Filters:", None))
        self.optionList.setItemText(0, QCoreApplication.translate("MainWindow", u"Filter1", None))
        self.optionList.setItemText(1, QCoreApplication.translate("MainWindow", u"Filter2", None))
        self.optionList.setItemText(2, QCoreApplication.translate("MainWindow", u"Filter3", None))
        self.optionList.setItemText(3, QCoreApplication.translate("MainWindow", u"Filter4", None))
        self.optionList.setItemText(4, QCoreApplication.translate("MainWindow", u"Filter5", None))
        self.optionList.setItemText(5, QCoreApplication.translate("MainWindow", u"Filter6", None))

        self.exportDataBtn.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.developerPageTitle.setText(QCoreApplication.translate("MainWindow", u"Log", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.startBtn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.stopBtn.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.user.setText(QCoreApplication.translate("MainWindow", u"User: u98o29", None))
        self.menuBtn.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.recordTimeBtn.setText(QCoreApplication.translate("MainWindow", u"Record Time", None))
        self.recordedTimesBtn.setText(QCoreApplication.translate("MainWindow", u"Recorded Times", None))
        self.managerBtn.setText(QCoreApplication.translate("MainWindow", u"Manager", None))
        self.employeeBtn.setText(QCoreApplication.translate("MainWindow", u"Employee", None))
        self.projectsBtn.setText(QCoreApplication.translate("MainWindow", u"Projects", None))
        self.topicsBtn.setText(QCoreApplication.translate("MainWindow", u"Topics", None))
        self.bookingtextsBtn.setText(QCoreApplication.translate("MainWindow", u"Booking Texts", None))
        self.exportBtn.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.developerBtn.setText(QCoreApplication.translate("MainWindow", u"Developer", None))
        self.exitBtn.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

