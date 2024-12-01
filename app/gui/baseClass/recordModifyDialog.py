# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modifyRecord.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QDialog, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTimeEdit, QVBoxLayout, QWidget)

class Ui_modifyRecord(object):
    def setupUi(self, modifyRecord):
        if not modifyRecord.objectName():
            modifyRecord.setObjectName(u"modifyRecord")
        modifyRecord.resize(351, 302)
        self.gridLayout = QGridLayout(modifyRecord)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(modifyRecord)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(7, 7, 7);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.projectFrame = QFrame(self.frame)
        self.projectFrame.setObjectName(u"projectFrame")
        self.projectFrame.setStyleSheet(u"color: rgb(186, 186, 186);")
        self.projectFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.projectFrame.setFrameShadow(QFrame.Shadow.Raised)
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

        self.horizontalSpacer = QSpacerItem(25, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.projectFrame)

        self.dateFrame = QFrame(self.frame)
        self.dateFrame.setObjectName(u"dateFrame")
        self.dateFrame.setStyleSheet(u"color: rgb(186, 186, 186);")
        self.dateFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.dateFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.dateFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.dateLabel = QLabel(self.dateFrame)
        self.dateLabel.setObjectName(u"dateLabel")
        self.dateLabel.setMinimumSize(QSize(0, 31))
        self.dateLabel.setFont(font)

        self.horizontalLayout_3.addWidget(self.dateLabel)

        self.workDate = QDateEdit(self.dateFrame)
        self.workDate.setObjectName(u"workDate")
        self.workDate.setMinimumSize(QSize(190, 31))
        self.workDate.setFont(font1)
        self.workDate.setDate(QDate(2000, 1, 1))

        self.horizontalLayout_3.addWidget(self.workDate)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addWidget(self.dateFrame)

        self.timeFrame = QFrame(self.frame)
        self.timeFrame.setObjectName(u"timeFrame")
        self.timeFrame.setStyleSheet(u"color: rgb(186, 186, 186);")
        self.timeFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.timeFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.timeFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.timeLabel = QLabel(self.timeFrame)
        self.timeLabel.setObjectName(u"timeLabel")
        self.timeLabel.setEnabled(True)
        self.timeLabel.setMinimumSize(QSize(0, 31))
        self.timeLabel.setFont(font)

        self.horizontalLayout_4.addWidget(self.timeLabel)

        self.totalTime = QTimeEdit(self.timeFrame)
        self.totalTime.setObjectName(u"totalTime")
        self.totalTime.setMinimumSize(QSize(190, 31))
        self.totalTime.setFont(font1)
        self.totalTime.setReadOnly(False)
        self.totalTime.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)

        self.horizontalLayout_4.addWidget(self.totalTime)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.timeFrame)

        self.verticalSpacer = QSpacerItem(20, 64, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

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
        self.btnsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.btnsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.btnsFrame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(39, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.saveBtn = QPushButton(self.btnsFrame)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setMinimumSize(QSize(121, 31))
        self.saveBtn.setStyleSheet(u"background-color: rgb(36, 131, 31);")

        self.horizontalLayout_5.addWidget(self.saveBtn)

        self.horizontalSpacer_6 = QSpacerItem(38, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.discardBtn = QPushButton(self.btnsFrame)
        self.discardBtn.setObjectName(u"discardBtn")
        self.discardBtn.setMinimumSize(QSize(121, 31))
        self.discardBtn.setStyleSheet(u"background-color: rgb(135, 47, 13);")

        self.horizontalLayout_5.addWidget(self.discardBtn)

        self.horizontalSpacer_7 = QSpacerItem(39, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

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

        self.dateLabel.setText(QCoreApplication.translate("modifyRecord", u"Date:     ", None))
        self.workDate.setDisplayFormat(QCoreApplication.translate("modifyRecord", u"yyyy/MM/dd", None))
        self.timeLabel.setText(QCoreApplication.translate("modifyRecord", u"Time:     ", None))
        self.saveBtn.setText(QCoreApplication.translate("modifyRecord", u"Save", None))
        self.discardBtn.setText(QCoreApplication.translate("modifyRecord", u"Discard", None))
    # retranslateUi

