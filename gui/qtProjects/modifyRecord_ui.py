# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modifyRecord.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDialog,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTimeEdit,
    QVBoxLayout, QWidget)

class Ui_modifyRecord(object):
    def setupUi(self, modifyRecord):
        if not modifyRecord.objectName():
            modifyRecord.setObjectName(u"modifyRecord")
        modifyRecord.resize(351, 364)
        self.gridLayout = QGridLayout(modifyRecord)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(modifyRecord)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(7, 7, 7);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.projectFrame = QFrame(self.frame)
        self.projectFrame.setObjectName(u"projectFrame")
        self.projectFrame.setStyleSheet(u"color: rgb(186, 186, 186);")
        self.projectFrame.setFrameShape(QFrame.StyledPanel)
        self.projectFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.projectFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.projectLabel = QLabel(self.projectFrame)
        self.projectLabel.setObjectName(u"projectLabel")
        self.projectLabel.setMinimumSize(QSize(0, 31))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(18)
        self.projectLabel.setFont(font)

        self.horizontalLayout.addWidget(self.projectLabel)

        self.projectList = QComboBox(self.projectFrame)
        self.projectList.addItem("")
        self.projectList.addItem("")
        self.projectList.addItem("")
        self.projectList.addItem("")
        self.projectList.addItem("")
        self.projectList.addItem("")
        self.projectList.setObjectName(u"projectList")
        self.projectList.setMinimumSize(QSize(190, 31))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(16)
        self.projectList.setFont(font1)

        self.horizontalLayout.addWidget(self.projectList)

        self.horizontalSpacer = QSpacerItem(25, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.projectFrame)

        self.startFrame = QFrame(self.frame)
        self.startFrame.setObjectName(u"startFrame")
        self.startFrame.setStyleSheet(u"color: rgb(186, 186, 186);")
        self.startFrame.setFrameShape(QFrame.StyledPanel)
        self.startFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.startFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.startLabel = QLabel(self.startFrame)
        self.startLabel.setObjectName(u"startLabel")
        self.startLabel.setMinimumSize(QSize(0, 31))
        self.startLabel.setFont(font)

        self.horizontalLayout_2.addWidget(self.startLabel)

        self.startTime = QTimeEdit(self.startFrame)
        self.startTime.setObjectName(u"startTime")
        self.startTime.setMinimumSize(QSize(190, 31))
        self.startTime.setFont(font1)

        self.horizontalLayout_2.addWidget(self.startTime)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.startFrame)

        self.endFrame = QFrame(self.frame)
        self.endFrame.setObjectName(u"endFrame")
        self.endFrame.setStyleSheet(u"color: rgb(186, 186, 186);")
        self.endFrame.setFrameShape(QFrame.StyledPanel)
        self.endFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.endFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.endLabel = QLabel(self.endFrame)
        self.endLabel.setObjectName(u"endLabel")
        self.endLabel.setMinimumSize(QSize(0, 31))
        self.endLabel.setFont(font)

        self.horizontalLayout_3.addWidget(self.endLabel)

        self.endTime = QTimeEdit(self.endFrame)
        self.endTime.setObjectName(u"endTime")
        self.endTime.setMinimumSize(QSize(190, 31))
        self.endTime.setFont(font1)

        self.horizontalLayout_3.addWidget(self.endTime)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addWidget(self.endFrame)

        self.totalFrame = QFrame(self.frame)
        self.totalFrame.setObjectName(u"totalFrame")
        self.totalFrame.setStyleSheet(u"color: rgb(186, 186, 186);")
        self.totalFrame.setFrameShape(QFrame.StyledPanel)
        self.totalFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.totalFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.totalLabel = QLabel(self.totalFrame)
        self.totalLabel.setObjectName(u"totalLabel")
        self.totalLabel.setMinimumSize(QSize(0, 31))
        self.totalLabel.setFont(font)

        self.horizontalLayout_4.addWidget(self.totalLabel)

        self.totalTime = QTimeEdit(self.totalFrame)
        self.totalTime.setObjectName(u"totalTime")
        self.totalTime.setMinimumSize(QSize(190, 31))
        self.totalTime.setFont(font1)
        self.totalTime.setReadOnly(True)
        self.totalTime.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.horizontalLayout_4.addWidget(self.totalTime)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.totalFrame)

        self.verticalSpacer = QSpacerItem(20, 64, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btnsFrame = QFrame(self.frame)
        self.btnsFrame.setObjectName(u"btnsFrame")
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
        self.horizontalLayout_5 = QHBoxLayout(self.btnsFrame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(39, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.saveBtn = QPushButton(self.btnsFrame)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setMinimumSize(QSize(121, 31))
        self.saveBtn.setStyleSheet(u"background-color: rgb(36, 131, 31);")

        self.horizontalLayout_5.addWidget(self.saveBtn)

        self.horizontalSpacer_6 = QSpacerItem(38, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.discardBtn = QPushButton(self.btnsFrame)
        self.discardBtn.setObjectName(u"discardBtn")
        self.discardBtn.setMinimumSize(QSize(121, 31))
        self.discardBtn.setStyleSheet(u"background-color: rgb(135, 47, 13);")

        self.horizontalLayout_5.addWidget(self.discardBtn)

        self.horizontalSpacer_7 = QSpacerItem(39, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)


        self.verticalLayout.addWidget(self.btnsFrame)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(modifyRecord)

        QMetaObject.connectSlotsByName(modifyRecord)
    # setupUi

    def retranslateUi(self, modifyRecord):
        modifyRecord.setWindowTitle(QCoreApplication.translate("modifyRecord", u"Dialog", None))
        self.projectLabel.setText(QCoreApplication.translate("modifyRecord", u"Project: ", None))
        self.projectList.setItemText(0, QCoreApplication.translate("modifyRecord", u"Project1", None))
        self.projectList.setItemText(1, QCoreApplication.translate("modifyRecord", u"Project2", None))
        self.projectList.setItemText(2, QCoreApplication.translate("modifyRecord", u"Project3", None))
        self.projectList.setItemText(3, QCoreApplication.translate("modifyRecord", u"Project4", None))
        self.projectList.setItemText(4, QCoreApplication.translate("modifyRecord", u"Project5", None))
        self.projectList.setItemText(5, QCoreApplication.translate("modifyRecord", u"Project6", None))

        self.startLabel.setText(QCoreApplication.translate("modifyRecord", u"Start:     ", None))
        self.endLabel.setText(QCoreApplication.translate("modifyRecord", u"End:      ", None))
        self.totalLabel.setText(QCoreApplication.translate("modifyRecord", u"Total:    ", None))
        self.saveBtn.setText(QCoreApplication.translate("modifyRecord", u"Save", None))
        self.discardBtn.setText(QCoreApplication.translate("modifyRecord", u"Discard", None))
    # retranslateUi

