# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(930, 608)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"\n"
"\n"
"QWidget {	\n"
"	background-color: rgb(36,41,62);\n"
"	border: 0px solid rgb(44, 49, 58);\n"
"	color: rgb(255, 255, 255);   /* White text */\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"\n"
"QPushButton {	\n"
"	background-color: rgb(142,187,255);\n"
"	color: rgb(255, 255, 255);   /* White text */\n"
"	font: 10pt \"Segoe UI\";\n"
"    border: 2px solid  rgb(142,187,255); \n"
"    border-radius: 10px; \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(99,130,178);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(235,167,95); \n"
"    border: 2px solid #4A4A4A; \n"
"}\n"
"\n"
"\n"
"#topRight QPushButton {\n"
"	background-color: rgb(29,39,53);\n"
"	color: rgb(255, 255, 255);   /* White text */\n"
"    border: 1px solid  rgb(142,187,255); \n"
"    border-radius: 10px; \n"
"}\n"
"\n"
"\n"
"\n"
"#stackedWidget{\n"
"	background-color: rgb(29,39,53);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"#sidepanel{\n"
"	background-color: rgb(29,39,53);\n"
"    border: 3px solid  rgb(29,39,53"
                        ");\n"
"    border-radius: 15px; \n"
"	margin-right: 5px; \n"
"	margin-left: 0px; \n"
"	margin-top: 5px; \n"
"	margin-bottom: 5px;\n"
"}\n"
"\n"
"QTableWidget {	\n"
"	background-color: rgb(29,39,53);\n"
"	padding: 5px;\n"
"	border-radius: 5px;\n"
"	gridline-color: #878E95;\n"
"    color: rgb(255,255,255);\n"
"}\n"
"\n"
"QTableWidget::item{\n"
"	border-color: none;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	gridline-color: rgb(255, 255, 255);\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(235,167,95);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 5px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QTableWidget QTableCornerButton::section {\n"
"    border: none;\n"
"	background-color: rgb(29,3"
                        "9,53);\n"
"	padding: 3px;\n"
"    border-top-left-radius: 5px;\n"
"}\n"
"\n"
"#widget{\n"
"	background-color: rgb(29,39,53);\n"
"}\n"
"\n"
"QHeaderView {\n"
"    background-color:  rgb(29,39,53);\n"
"}\n"
"\n"
"#widget_2 {\n"
"	background-color: rgb(29,39,53);\n"
"	color: rgb(255, 255, 255);   /* White text */\n"
"    border: 10px solid  rgb(29,39,53);\n"
"    border-radius: 5px; \n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.horizontalLayout_7 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setSpacing(1)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.backgroundwidget = QWidget(self.centralwidget)
        self.backgroundwidget.setObjectName(u"backgroundwidget")
        self.verticalLayout_10 = QVBoxLayout(self.backgroundwidget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(3, 0, 0, 0)
        self.main_container = QWidget(self.backgroundwidget)
        self.main_container.setObjectName(u"main_container")
        self.horizontalLayout_8 = QHBoxLayout(self.main_container)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.sidepanel = QWidget(self.main_container)
        self.sidepanel.setObjectName(u"sidepanel")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidepanel.sizePolicy().hasHeightForWidth())
        self.sidepanel.setSizePolicy(sizePolicy)
        self.sidepanel.setFocusPolicy(Qt.NoFocus)
        self.sidepanel.setAutoFillBackground(False)
        self.gridLayout = QGridLayout(self.sidepanel)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(4)
        self.gridLayout.setContentsMargins(15, 15, 15, 9)
        self.verticalSpacer_2 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.textEdit = QTextEdit(self.sidepanel)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy1)
        self.textEdit.setMinimumSize(QSize(0, 50))
        self.textEdit.setMaximumSize(QSize(150, 50))

        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.ButtonCopyPageSelect = QPushButton(self.sidepanel)
        self.ButtonCopyPageSelect.setObjectName(u"ButtonCopyPageSelect")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ButtonCopyPageSelect.sizePolicy().hasHeightForWidth())
        self.ButtonCopyPageSelect.setSizePolicy(sizePolicy2)
        self.ButtonCopyPageSelect.setMinimumSize(QSize(120, 25))

        self.gridLayout.addWidget(self.ButtonCopyPageSelect, 3, 0, 1, 1, Qt.AlignHCenter)

        self.ButtonExit = QPushButton(self.sidepanel)
        self.ButtonExit.setObjectName(u"ButtonExit")
        self.ButtonExit.setMinimumSize(QSize(120, 25))
        self.ButtonExit.setMaximumSize(QSize(120, 25))

        self.gridLayout.addWidget(self.ButtonExit, 5, 0, 1, 1, Qt.AlignHCenter)


        self.horizontalLayout_8.addWidget(self.sidepanel)

        self.main_body = QWidget(self.main_container)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setMinimumSize(QSize(0, 0))
        self.verticalLayout_7 = QVBoxLayout(self.main_body)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 5, 0, 0)
        self.topPart = QWidget(self.main_body)
        self.topPart.setObjectName(u"topPart")
        self.topPart.setMinimumSize(QSize(0, 50))
        self.topPart.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_2 = QHBoxLayout(self.topPart)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, 5, 15)
        self.topLeft = QWidget(self.topPart)
        self.topLeft.setObjectName(u"topLeft")
        self.verticalLayout_6 = QVBoxLayout(self.topLeft)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")

        self.horizontalLayout_2.addWidget(self.topLeft)

        self.topMiddle = QWidget(self.topPart)
        self.topMiddle.setObjectName(u"topMiddle")
        self.horizontalLayout_5 = QHBoxLayout(self.topMiddle)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.label = QLabel(self.topMiddle)
        self.label.setObjectName(u"label")

        self.horizontalLayout_5.addWidget(self.label)

        self.lineEdit = QLineEdit(self.topMiddle)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.lineEdit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_2.addWidget(self.topMiddle)

        self.topRight = QWidget(self.topPart)
        self.topRight.setObjectName(u"topRight")
        self.topRight.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_4 = QHBoxLayout(self.topRight)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 14)
        self.ButtonMinimalize = QPushButton(self.topRight)
        self.ButtonMinimalize.setObjectName(u"ButtonMinimalize")
        self.ButtonMinimalize.setMinimumSize(QSize(25, 25))
        self.ButtonMinimalize.setMaximumSize(QSize(25, 25))
        icon = QIcon()
        icon.addFile(u":/icons/resources/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ButtonMinimalize.setIcon(icon)
        self.ButtonMinimalize.setCheckable(False)

        self.horizontalLayout_4.addWidget(self.ButtonMinimalize)

        self.ButtonChangeWindowSize = QPushButton(self.topRight)
        self.ButtonChangeWindowSize.setObjectName(u"ButtonChangeWindowSize")
        self.ButtonChangeWindowSize.setMinimumSize(QSize(25, 25))
        self.ButtonChangeWindowSize.setMaximumSize(QSize(25, 25))
        icon1 = QIcon()
        icon1.addFile(u":/icons/resources/icons/icon_restore.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ButtonChangeWindowSize.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.ButtonChangeWindowSize)

        self.ButtonExitTop = QPushButton(self.topRight)
        self.ButtonExitTop.setObjectName(u"ButtonExitTop")
        self.ButtonExitTop.setMinimumSize(QSize(25, 25))
        self.ButtonExitTop.setMaximumSize(QSize(25, 25))
        icon2 = QIcon()
        icon2.addFile(u":/icons/resources/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ButtonExitTop.setIcon(icon2)

        self.horizontalLayout_4.addWidget(self.ButtonExitTop)


        self.horizontalLayout_2.addWidget(self.topRight, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.topPart)

        self.bottomPart = QWidget(self.main_body)
        self.bottomPart.setObjectName(u"bottomPart")
        self.horizontalLayout_3 = QHBoxLayout(self.bottomPart)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.mainpanel = QWidget(self.bottomPart)
        self.mainpanel.setObjectName(u"mainpanel")
        self.horizontalLayout = QHBoxLayout(self.mainpanel)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackedWidget = QStackedWidget(self.mainpanel)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.PageBooking = QWidget()
        self.PageBooking.setObjectName(u"PageBooking")
        self.gridLayout_3 = QGridLayout(self.PageBooking)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget = QWidget(self.PageBooking)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 0, 10, -1)
        self.tableWidget = QTableWidget(self.widget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 2):
            self.tableWidget.setRowCount(2)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMaximumSize(QSize(16777215, 200))
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.widget_2.setMaximumSize(QSize(50000, 50000))
        self.horizontalLayout_9 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy3)
        self.pushButton_2.setMinimumSize(QSize(0, 27))

        self.horizontalLayout_9.addWidget(self.pushButton_2, 0, Qt.AlignTop)

        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy3.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy3)
        self.pushButton.setMinimumSize(QSize(200, 27))

        self.horizontalLayout_9.addWidget(self.pushButton, 0, Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.widget_2)


        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.PageBooking)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout = QVBoxLayout(self.page_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.page_2_main_widget = QWidget(self.page_2)
        self.page_2_main_widget.setObjectName(u"page_2_main_widget")
        self.verticalLayout_5 = QVBoxLayout(self.page_2_main_widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, -1, -1, 0)

        self.verticalLayout.addWidget(self.page_2_main_widget)

        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.horizontalLayout_3.addWidget(self.mainpanel)


        self.verticalLayout_7.addWidget(self.bottomPart)

        self.footer = QWidget(self.main_body)
        self.footer.setObjectName(u"footer")
        self.horizontalLayout_6 = QHBoxLayout(self.footer)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.label_6 = QLabel(self.footer)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)


        self.verticalLayout_7.addWidget(self.footer)


        self.horizontalLayout_8.addWidget(self.main_body)


        self.verticalLayout_10.addWidget(self.main_container)


        self.horizontalLayout_7.addWidget(self.backgroundwidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Place for logo or for </p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">something else</p></body></html>", None))
        self.ButtonCopyPageSelect.setText(QCoreApplication.translate("MainWindow", u"Time tracker", None))
        self.ButtonExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.label.setText("")
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Welcome to EffiSync", None))
        self.ButtonMinimalize.setText("")
        self.ButtonChangeWindowSize.setText("")
        self.ButtonExitTop.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Booking number", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Time spent today", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Time spent overall", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Start/Stop", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"n1", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"n2", None));
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Book hours to ESS", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Stop current timer", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Version Pre-Alpha", None))
    # retranslateUi

