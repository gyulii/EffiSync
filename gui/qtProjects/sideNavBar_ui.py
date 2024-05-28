# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sideNavBar.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import iconsDark_rc

class Ui_sideNavBar(object):
    def setupUi(self, sideNavBar):
        if not sideNavBar.objectName():
            sideNavBar.setObjectName(u"sideNavBar")
        sideNavBar.resize(313, 681)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(sideNavBar.sizePolicy().hasHeightForWidth())
        sideNavBar.setSizePolicy(sizePolicy)
        self.gridLayout_4 = QGridLayout(sideNavBar)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.sideBar = QWidget(sideNavBar)
        self.sideBar.setObjectName(u"sideBar")
        self.sideBar.setMinimumSize(QSize(221, 681))
        self.sideBar.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(0, 0, 27);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.sideBar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
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
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
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
        icon = QIcon()
        icon.addFile(u":/iconsDark/icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setCheckable(True)

        self.gridLayout.addWidget(self.menuBtn, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.menuBtnFrame)

        self.navigationBtnsFrame = QFrame(self.sideBar)
        self.navigationBtnsFrame.setObjectName(u"navigationBtnsFrame")
        self.navigationBtnsFrame.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"	margin:5px;\n"
"}")
        self.navigationBtnsFrame.setFrameShape(QFrame.StyledPanel)
        self.navigationBtnsFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.navigationBtnsFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
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
        icon1 = QIcon()
        icon1.addFile(u":/iconsDark/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon1)

        self.gridLayout_2.addWidget(self.homeBtn, 0, 0, 1, 1)

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
        icon2 = QIcon()
        icon2.addFile(u":/iconsDark/icons/code.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.developerBtn.setIcon(icon2)

        self.gridLayout_2.addWidget(self.developerBtn, 4, 0, 1, 1)

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
        icon3 = QIcon()
        icon3.addFile(u":/iconsDark/icons/clock.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.recordTimeBtn.setIcon(icon3)

        self.gridLayout_2.addWidget(self.recordTimeBtn, 1, 0, 1, 1)

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
        icon4 = QIcon()
        icon4.addFile(u":/iconsDark/icons/table.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.recordedTimesBtn.setIcon(icon4)

        self.gridLayout_2.addWidget(self.recordedTimesBtn, 2, 0, 1, 1)

        self.exportBtn = QPushButton(self.navigationBtnsFrame)
        self.exportBtn.setObjectName(u"exportBtn")
        self.exportBtn.setMinimumSize(QSize(181, 31))
        self.exportBtn.setFont(font)
        self.exportBtn.setStyleSheet(u"QPushButton{\n"
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
        icon5 = QIcon()
        icon5.addFile(u":/iconsDark/icons/external-link.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exportBtn.setIcon(icon5)

        self.gridLayout_2.addWidget(self.exportBtn, 3, 0, 1, 1)


        self.verticalLayout.addWidget(self.navigationBtnsFrame)

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
        icon6 = QIcon()
        icon6.addFile(u":/iconsDark/icons/power.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exitBtn.setIcon(icon6)

        self.gridLayout_3.addWidget(self.exitBtn, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.powerBtnFrame)


        self.gridLayout_4.addWidget(self.sideBar, 0, 1, 1, 1)

        self.sideBarMiniWidget = QWidget(sideNavBar)
        self.sideBarMiniWidget.setObjectName(u"sideBarMiniWidget")
        self.verticalLayout_2 = QVBoxLayout(self.sideBarMiniWidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
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
        self.recordTimeBtnMini.setIcon(icon3)

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
        self.recordedTimesBtnMini.setIcon(icon4)

        self.verticalLayout_29.addWidget(self.recordedTimesBtnMini)

        self.exportBtnMini = QPushButton(self.navigationBtnsFrameMini)
        self.exportBtnMini.setObjectName(u"exportBtnMini")
        self.exportBtnMini.setMinimumSize(QSize(31, 31))
        self.exportBtnMini.setMaximumSize(QSize(64, 16777215))
        self.exportBtnMini.setFont(font)
        self.exportBtnMini.setStyleSheet(u"QPushButton{\n"
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
        self.exportBtnMini.setIcon(icon5)

        self.verticalLayout_29.addWidget(self.exportBtnMini)

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
        self.developerBtnMini.setIcon(icon2)

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
        self.exitBtnMini.setIcon(icon6)

        self.verticalLayout_28.addWidget(self.exitBtnMini)


        self.verticalLayout_31.addWidget(self.powerBtnFrameMini)


        self.verticalLayout_2.addWidget(self.sideBarMini)


        self.gridLayout_4.addWidget(self.sideBarMiniWidget, 0, 0, 1, 1)


        self.retranslateUi(sideNavBar)
        self.menuBtnMini.clicked["bool"].connect(self.menuBtn.setChecked)
        self.menuBtn.toggled.connect(self.sideBarMini.setHidden)
        self.menuBtn.toggled.connect(self.sideBar.setVisible)

        QMetaObject.connectSlotsByName(sideNavBar)
    # setupUi

    def retranslateUi(self, sideNavBar):
        sideNavBar.setWindowTitle(QCoreApplication.translate("sideNavBar", u"Form", None))
        self.menuBtn.setText(QCoreApplication.translate("sideNavBar", u"Menu", None))
        self.homeBtn.setText(QCoreApplication.translate("sideNavBar", u"Home", None))
        self.developerBtn.setText(QCoreApplication.translate("sideNavBar", u"Developer", None))
        self.recordTimeBtn.setText(QCoreApplication.translate("sideNavBar", u"Record Time", None))
        self.recordedTimesBtn.setText(QCoreApplication.translate("sideNavBar", u"Recorded Times", None))
        self.exportBtn.setText(QCoreApplication.translate("sideNavBar", u"Export", None))
        self.exitBtn.setText(QCoreApplication.translate("sideNavBar", u"Exit", None))
        self.menuBtnMini.setText("")
        self.homeBtnMini.setText("")
        self.recordTimeBtnMini.setText("")
        self.recordedTimesBtnMini.setText("")
        self.exportBtnMini.setText("")
        self.developerBtnMini.setText("")
        self.exitBtnMini.setText("")
    # retranslateUi

