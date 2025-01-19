# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editTopic.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 119)
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.locationLabel = QLabel(Dialog)
        self.locationLabel.setObjectName(u"locationLabel")
        self.locationLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.locationLabel.setMargin(0)
        self.locationLabel.setIndent(10)

        self.verticalLayout.addWidget(self.locationLabel)

        self.topicLocation = QLineEdit(Dialog)
        self.topicLocation.setObjectName(u"topicLocation")

        self.verticalLayout.addWidget(self.topicLocation)

        self.wbsLabel = QLabel(Dialog)
        self.wbsLabel.setObjectName(u"wbsLabel")
        self.wbsLabel.setIndent(10)

        self.verticalLayout.addWidget(self.wbsLabel)

        self.topicWbs = QLineEdit(Dialog)
        self.topicWbs.setObjectName(u"topicWbs")

        self.verticalLayout.addWidget(self.topicWbs)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)
        self.buttonBox.setCenterButtons(True)

        self.horizontalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.locationLabel.setText(QCoreApplication.translate("Dialog", u"Country", None))
        self.wbsLabel.setText(QCoreApplication.translate("Dialog", u"Wbs", None))
    # retranslateUi

