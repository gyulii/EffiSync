# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'headBar.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLCDNumber, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)
import iconsDark_rc

class Ui_headbar(object):
    def setupUi(self, headbar):
        if not headbar.objectName():
            headbar.setObjectName(u"headbar")
        headbar.resize(1080, 61)
        self.gridLayout = QGridLayout(headbar)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.headBarFrame = QFrame(headbar)
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
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, -1)
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
        self.horizontalLayout.setContentsMargins(-1, 5, -1, 5)
        self.startBtn = QPushButton(self.startsoptBtnFrame)
        self.startBtn.setObjectName(u"startBtn")
        self.startBtn.setMinimumSize(QSize(91, 31))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
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
        icon = QIcon()
        icon.addFile(u":/iconsDark/icons/play.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.startBtn.setIcon(icon)

        self.horizontalLayout.addWidget(self.startBtn)

        self.stopBtn = QPushButton(self.startsoptBtnFrame)
        self.stopBtn.setObjectName(u"stopBtn")
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
        icon1 = QIcon()
        icon1.addFile(u":/iconsDark/icons/stop-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.stopBtn.setIcon(icon1)

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
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(12)
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


        self.gridLayout.addWidget(self.headBarFrame, 0, 0, 1, 1)


        self.retranslateUi(headbar)

        QMetaObject.connectSlotsByName(headbar)
    # setupUi

    def retranslateUi(self, headbar):
        headbar.setWindowTitle(QCoreApplication.translate("headbar", u"Form", None))
        self.startBtn.setText(QCoreApplication.translate("headbar", u"Start", None))
        self.stopBtn.setText(QCoreApplication.translate("headbar", u"Stop", None))
        self.user.setText(QCoreApplication.translate("headbar", u"User: u98o29", None))
    # retranslateUi

