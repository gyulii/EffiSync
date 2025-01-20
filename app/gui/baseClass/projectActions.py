# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modifyProject.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
    QSizePolicy, QWidget)
#import iconsDark_rc
import app.gui.iconsDark_rc

class Ui_projectActionBtns(object):
    def setupUi(self, projectActionBtns):
        if not projectActionBtns.objectName():
            projectActionBtns.setObjectName(u"projectActionBtns")
        projectActionBtns.resize(168, 33)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(projectActionBtns.sizePolicy().hasHeightForWidth())
        projectActionBtns.setSizePolicy(sizePolicy)
        projectActionBtns.setMinimumSize(QSize(50, 0))
        projectActionBtns.setMaximumSize(QSize(16777215, 16777215))
        self.frame = QFrame(projectActionBtns)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 47, 33))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-color: transparent;\n"
"	margin: 1px;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(1, 2, 1, 2)
        self.editBtn = QPushButton(self.frame)
        self.editBtn.setObjectName(u"editBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.editBtn.sizePolicy().hasHeightForWidth())
        self.editBtn.setSizePolicy(sizePolicy2)
        self.editBtn.setMinimumSize(QSize(40, 23))
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
        icon.addFile(u":/iconsDark/icons/edit.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.editBtn.setIcon(icon)

        self.horizontalLayout.addWidget(self.editBtn)


        self.retranslateUi(projectActionBtns)

        QMetaObject.connectSlotsByName(projectActionBtns)
    # setupUi

    def retranslateUi(self, projectActionBtns):
        projectActionBtns.setWindowTitle(QCoreApplication.translate("projectActionBtns", u"Form", None))
        self.editBtn.setText("")
    # retranslateUi

