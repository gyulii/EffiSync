# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confirmationDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_confirmationDialog(object):
    def setupUi(self, confirmationDialog):
        if not confirmationDialog.objectName():
            confirmationDialog.setObjectName(u"confirmationDialog")
        confirmationDialog.resize(361, 162)
        self.gridLayout_2 = QGridLayout(confirmationDialog)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.window = QFrame(confirmationDialog)
        self.window.setObjectName(u"window")
        self.window.setStyleSheet(u"background-color: rgb(7, 7, 7);")
        self.window.setFrameShape(QFrame.StyledPanel)
        self.window.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.window)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.labelFrame = QFrame(self.window)
        self.labelFrame.setObjectName(u"labelFrame")
        self.labelFrame.setFrameShape(QFrame.StyledPanel)
        self.labelFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.labelFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.labelFrame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(186, 186, 186);\n"
"")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.labelFrame)

        self.btnsFrame = QFrame(self.window)
        self.btnsFrame.setObjectName(u"btnsFrame")
        self.btnsFrame.setMaximumSize(QSize(351, 61))
        self.btnsFrame.setStyleSheet(u"QFrame{\n"
"	padding: 5px\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: rgb(179, 182, 186);\n"
"	border: 2px solid rgb(10, 10, 29);\n"
"	background-color: rgb(0, 0, 43);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(143, 145, 148);\n"
"	background-color: rgb(0, 0, 85);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	color: rgb(254, 254, 254);\n"
"	background-color: rgb(0, 0, 135);\n"
"}")
        self.btnsFrame.setFrameShape(QFrame.StyledPanel)
        self.btnsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.btnsFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(39, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.saveBtn = QPushButton(self.btnsFrame)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setMinimumSize(QSize(121, 31))
        self.saveBtn.setStyleSheet(u"background-color: rgb(36, 131, 31);")

        self.horizontalLayout.addWidget(self.saveBtn)

        self.horizontalSpacer_6 = QSpacerItem(38, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)

        self.discardBtn = QPushButton(self.btnsFrame)
        self.discardBtn.setObjectName(u"discardBtn")
        self.discardBtn.setMinimumSize(QSize(121, 31))
        self.discardBtn.setStyleSheet(u"background-color: rgb(135, 47, 13);")

        self.horizontalLayout.addWidget(self.discardBtn)

        self.horizontalSpacer_7 = QSpacerItem(39, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)


        self.verticalLayout.addWidget(self.btnsFrame)


        self.gridLayout_2.addWidget(self.window, 0, 0, 1, 1)


        self.retranslateUi(confirmationDialog)

        QMetaObject.connectSlotsByName(confirmationDialog)
    # setupUi

    def retranslateUi(self, confirmationDialog):
        confirmationDialog.setWindowTitle(QCoreApplication.translate("confirmationDialog", u"Dialog", None))
        self.label.setText("")
        self.saveBtn.setText(QCoreApplication.translate("confirmationDialog", u"Yes", None))
        self.discardBtn.setText(QCoreApplication.translate("confirmationDialog", u"No", None))
    # retranslateUi

