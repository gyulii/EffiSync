# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'controlPane.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QWidget)
import iconsDark_rc

class Ui_controlPane(object):
    def setupUi(self, controlPane):
        if not controlPane.objectName():
            controlPane.setObjectName(u"controlPane")
        controlPane.resize(1081, 27)
        self.gridLayout = QGridLayout(controlPane)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(controlPane)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 66);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(956, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.buttons = QFrame(self.frame)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setMinimumSize(QSize(120, 25))
        self.buttons.setMaximumSize(QSize(120, 25))
        self.buttons.setFrameShape(QFrame.StyledPanel)
        self.buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.buttons)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.minimizeBtn = QPushButton(self.buttons)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        self.minimizeBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 66);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 0, 105);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/iconsDark/icons/chevron-down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon)

        self.horizontalLayout.addWidget(self.minimizeBtn)

        self.maximizeBtn = QPushButton(self.buttons)
        self.maximizeBtn.setObjectName(u"maximizeBtn")
        self.maximizeBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 66);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 0, 105);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/iconsDark/icons/chevron-up.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeBtn.setIcon(icon1)

        self.horizontalLayout.addWidget(self.maximizeBtn)

        self.closeBtn = QPushButton(self.buttons)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(140, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(165, 0, 0);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/iconsDark/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon2)

        self.horizontalLayout.addWidget(self.closeBtn)


        self.horizontalLayout_2.addWidget(self.buttons)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(controlPane)

        QMetaObject.connectSlotsByName(controlPane)
    # setupUi

    def retranslateUi(self, controlPane):
        controlPane.setWindowTitle(QCoreApplication.translate("controlPane", u"Form", None))
        self.minimizeBtn.setText("")
        self.maximizeBtn.setText("")
        self.closeBtn.setText("")
    # retranslateUi

