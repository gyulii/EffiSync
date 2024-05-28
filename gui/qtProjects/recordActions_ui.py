# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recordActions.ui'
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
    QPushButton, QSizePolicy, QWidget)
import iconsDark_rc

class Ui_recordActionButtons(object):
    def setupUi(self, recordActionButtons):
        if not recordActionButtons.objectName():
            recordActionButtons.setObjectName(u"recordActionButtons")
        recordActionButtons.resize(128, 33)
        self.gridLayout = QGridLayout(recordActionButtons)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(recordActionButtons)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-color: transparent;\n"
"	margin: 1px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(1, 2, 1, 2)
        self.editBtn = QPushButton(self.frame)
        self.editBtn.setObjectName(u"editBtn")
        self.editBtn.setMinimumSize(QSize(23, 23))
        self.editBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid  rgb(2, 20, 72);\n"
"	border-radius:10px;\n"
"	color: rgb(177, 177, 177);\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(23, 32, 42);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(3, 1, 59)\n"
"}")
        icon = QIcon()
        icon.addFile(u":/iconsDark/icons/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.editBtn.setIcon(icon)

        self.horizontalLayout.addWidget(self.editBtn)

        self.deleteBtn = QPushButton(self.frame)
        self.deleteBtn.setObjectName(u"deleteBtn")
        self.deleteBtn.setMinimumSize(QSize(23, 23))
        self.deleteBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid  rgb(2, 20, 72);\n"
"	border-radius:10px;\n"
"	color: rgb(177, 177, 177);\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(23, 32, 42);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(3, 1, 59)\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/iconsDark/icons/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteBtn.setIcon(icon1)

        self.horizontalLayout.addWidget(self.deleteBtn)

        self.freezeBtn = QPushButton(self.frame)
        self.freezeBtn.setObjectName(u"freezeBtn")
        self.freezeBtn.setMinimumSize(QSize(23, 23))
        self.freezeBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid  rgb(2, 20, 72);\n"
"	border-radius:10px;\n"
"	color: rgb(177, 177, 177);\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(23, 32, 42);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(3, 1, 59)\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/iconsDark/icons/unlock.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/iconsDark/icons/lock.svg", QSize(), QIcon.Active, QIcon.On)
        icon2.addFile(u":/iconsDark/icons/lock.svg", QSize(), QIcon.Selected, QIcon.On)
        self.freezeBtn.setIcon(icon2)
        self.freezeBtn.setCheckable(True)

        self.horizontalLayout.addWidget(self.freezeBtn)

        self.sendBtn = QPushButton(self.frame)
        self.sendBtn.setObjectName(u"sendBtn")
        self.sendBtn.setMinimumSize(QSize(23, 23))
        self.sendBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(44, 44, 44);\n"
"	border: 2px solid  rgb(2, 20, 72);\n"
"	border-radius:10px;\n"
"	color: rgb(177, 177, 177);\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(23, 32, 42);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(3, 1, 59)\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/iconsDark/icons/send.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sendBtn.setIcon(icon3)
        self.sendBtn.setCheckable(True)

        self.horizontalLayout.addWidget(self.sendBtn)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(recordActionButtons)
        self.freezeBtn.clicked["bool"].connect(self.deleteBtn.setDisabled)
        self.freezeBtn.clicked["bool"].connect(self.editBtn.setDisabled)
        self.sendBtn.toggled.connect(self.editBtn.setDisabled)
        self.sendBtn.toggled.connect(self.deleteBtn.setDisabled)
        self.sendBtn.toggled.connect(self.freezeBtn.setDisabled)
        self.sendBtn.toggled.connect(self.sendBtn.setDisabled)

        QMetaObject.connectSlotsByName(recordActionButtons)
    # setupUi

    def retranslateUi(self, recordActionButtons):
        recordActionButtons.setWindowTitle(QCoreApplication.translate("recordActionButtons", u"Form", None))
        self.editBtn.setText("")
        self.deleteBtn.setText("")
        self.freezeBtn.setText("")
        self.sendBtn.setText("")
    # retranslateUi

