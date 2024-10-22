# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginPopup.ui'
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
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from app.gui import iconsDark_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(371, 227)
        Dialog.setStyleSheet(u"*{\n"
"	background-color: rgb(7, 7, 7);\n"
"}\n"
"\n"
"QLabel{\n"
"	color:rgb(186, 186, 186);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color:rgb(186, 186, 186);\n"
"	background-color: rgb(100, 100, 100);\n"
"	padding-left: 2px;\n"
"	padding-right: 2px;\n"
"	border: 5px bold;\n"
"	border-color: rgb(2, 20, 72);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(44, 44, 44)\n"
"}\n"
"\n"
"QLineEdit{\n"
"	color: rgb(186, 186, 186);\n"
"}")
        self.gridLayout_3 = QGridLayout(Dialog)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.contentFrame = QFrame(Dialog)
        self.contentFrame.setObjectName(u"contentFrame")
        self.contentFrame.setFrameShape(QFrame.StyledPanel)
        self.contentFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.contentFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(4, 6, 9, -1)
        self.titleFrame = QFrame(self.contentFrame)
        self.titleFrame.setObjectName(u"titleFrame")
        self.titleFrame.setFrameShape(QFrame.StyledPanel)
        self.titleFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.titleFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.title = QLabel(self.titleFrame)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(16)
        self.title.setFont(font)
        self.title.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.title)

        self.infoMsg = QLabel(self.titleFrame)
        self.infoMsg.setObjectName(u"infoMsg")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(10)
        self.infoMsg.setFont(font1)

        self.verticalLayout_3.addWidget(self.infoMsg)


        self.gridLayout_2.addWidget(self.titleFrame, 0, 0, 1, 1)

        self.user_adminWidget = QWidget(self.contentFrame)
        self.user_adminWidget.setObjectName(u"user_adminWidget")
        self.horizontalLayout = QHBoxLayout(self.user_adminWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(25, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.asUserBtn = QPushButton(self.user_adminWidget)
        self.asUserBtn.setObjectName(u"asUserBtn")
        self.asUserBtn.setMinimumSize(QSize(75, 30))
        icon = QIcon()
        icon.addFile(u":/iconsDark/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.asUserBtn.setIcon(icon)

        self.horizontalLayout.addWidget(self.asUserBtn)

        self.horizontalSpacer = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.asAdminBtn = QPushButton(self.user_adminWidget)
        self.asAdminBtn.setObjectName(u"asAdminBtn")
        self.asAdminBtn.setMinimumSize(QSize(75, 30))
        self.asAdminBtn.setStyleSheet(u"padding: 5px;")
        icon1 = QIcon()
        icon1.addFile(u":/iconsDark/icons/key.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.asAdminBtn.setIcon(icon1)

        self.horizontalLayout.addWidget(self.asAdminBtn)

        self.horizontalSpacer_8 = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_8)

        self.exitBtn = QPushButton(self.user_adminWidget)
        self.exitBtn.setObjectName(u"exitBtn")
        self.exitBtn.setMinimumSize(QSize(75, 30))
        icon2 = QIcon()
        icon2.addFile(u":/iconsDark/icons/power.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exitBtn.setIcon(icon2)

        self.horizontalLayout.addWidget(self.exitBtn)

        self.horizontalSpacer_3 = QSpacerItem(25, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.gridLayout_2.addWidget(self.user_adminWidget, 1, 0, 1, 1)

        self.loginWidget = QWidget(self.contentFrame)
        self.loginWidget.setObjectName(u"loginWidget")
        self.gridLayout = QGridLayout(self.loginWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(8)
        self.gridLayout.setVerticalSpacing(3)
        self.gridLayout.setContentsMargins(9, 5, 9, 9)
        self.inputsLabelFrame = QFrame(self.loginWidget)
        self.inputsLabelFrame.setObjectName(u"inputsLabelFrame")
        self.inputsLabelFrame.setFrameShape(QFrame.StyledPanel)
        self.inputsLabelFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.inputsLabelFrame)
        self.verticalLayout.setSpacing(14)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 5, 16, 5)
        self.usernameLabel = QLabel(self.inputsLabelFrame)
        self.usernameLabel.setObjectName(u"usernameLabel")
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(12)
        self.usernameLabel.setFont(font2)

        self.verticalLayout.addWidget(self.usernameLabel)

        self.passwordLabel = QLabel(self.inputsLabelFrame)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setFont(font2)

        self.verticalLayout.addWidget(self.passwordLabel)


        self.gridLayout.addWidget(self.inputsLabelFrame, 0, 0, 1, 1)

        self.inputsFrame = QFrame(self.loginWidget)
        self.inputsFrame.setObjectName(u"inputsFrame")
        self.inputsFrame.setFrameShape(QFrame.StyledPanel)
        self.inputsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.inputsFrame)
        self.verticalLayout_2.setSpacing(14)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 5, 0, 5)
        self.userNameInput = QLineEdit(self.inputsFrame)
        self.userNameInput.setObjectName(u"userNameInput")
        self.userNameInput.setFont(font2)
        self.userNameInput.setStyleSheet(u"")
        self.userNameInput.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_2.addWidget(self.userNameInput)

        self.passwordInput = QLineEdit(self.inputsFrame)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setFont(font2)
        self.passwordInput.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.passwordInput)


        self.gridLayout.addWidget(self.inputsFrame, 0, 1, 1, 1)

        self.buttonsFrame = QFrame(self.loginWidget)
        self.buttonsFrame.setObjectName(u"buttonsFrame")
        self.buttonsFrame.setFrameShape(QFrame.StyledPanel)
        self.buttonsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.buttonsFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_4 = QSpacerItem(59, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.loginBtn = QPushButton(self.buttonsFrame)
        self.loginBtn.setObjectName(u"loginBtn")
        self.loginBtn.setMinimumSize(QSize(75, 30))
        self.loginBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 140, 5);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(0, 95, 5);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/iconsDark/icons/log-in.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.loginBtn.setIcon(icon3)

        self.horizontalLayout_3.addWidget(self.loginBtn)

        self.horizontalSpacer_5 = QSpacerItem(59, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.cancelBtn = QPushButton(self.buttonsFrame)
        self.cancelBtn.setObjectName(u"cancelBtn")
        self.cancelBtn.setMinimumSize(QSize(75, 30))
        self.cancelBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(170, 0 , 5);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(125, 0, 5);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/iconsDark/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cancelBtn.setIcon(icon4)

        self.horizontalLayout_3.addWidget(self.cancelBtn)

        self.horizontalSpacer_6 = QSpacerItem(59, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.gridLayout.addWidget(self.buttonsFrame, 1, 0, 1, 2)


        self.gridLayout_2.addWidget(self.loginWidget, 2, 0, 1, 1)


        self.gridLayout_3.addWidget(self.contentFrame, 0, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.exitBtn.clicked.connect(Dialog.close)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.title.setText(QCoreApplication.translate("Dialog", u"Lorem ipsum dolor sit amet, consectetur", None))
        self.infoMsg.setText("")
        self.asUserBtn.setText(QCoreApplication.translate("Dialog", u"As User", None))
        self.asAdminBtn.setText(QCoreApplication.translate("Dialog", u"As Manager", None))
        self.exitBtn.setText(QCoreApplication.translate("Dialog", u"Exit", None))
        self.usernameLabel.setText(QCoreApplication.translate("Dialog", u"User name:", None))
        self.passwordLabel.setText(QCoreApplication.translate("Dialog", u"Password:", None))
        self.userNameInput.setText("")
        self.loginBtn.setText(QCoreApplication.translate("Dialog", u"Log in", None))
        self.cancelBtn.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

