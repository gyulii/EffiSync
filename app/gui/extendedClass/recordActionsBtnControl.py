import venv
from datetime import datetime

import requests
from PySide6.QtWidgets import QWidget, QTableWidgetItem
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt

from app.db.database_handler import DatabaseHandler
from app.gui.extendedClass.recordModifyDialogControl import recordModifyDialogControl
from app.gui.baseClass.recordActions import Ui_recordActionButtons
from app.gui.extendedClass.confirmationDialogControl import confirmationDialogControl
from app.booking import BookingItem
import os

class recordActionBtnControl(QWidget):

    rowNr = None
    table = None
    logField = None
    log = None

    def __init__(self):
        super().__init__()
        self.recAcBtns = Ui_recordActionButtons()
        self.recAcBtns.setupUi(self)

        self.recAcBtns.editBtn.clicked.connect(self.editRecord)
        self.recAcBtns.deleteBtn.clicked.connect(self.deleteRecord)
        self.recAcBtns.freezeBtn.clicked.connect(self.freezeRecord)
        self.recAcBtns.sendBtn.clicked.connect(self.sendRecord)

    def setRowNr(self,num):
        self.rowNr = num

    def setTable (self, table):
        self.table = table

    def setlogField(self, field):
        self.logField = field
        self.log("Új sor hozzáadva", "WARNING")

    def setLog(self, log):
        self.log = log

    def setDelNth(self, delNth):
        self.delNth = delNth

    def setEditNth(self, editNth):
        self.editNth = editNth

    def setDriver(self, driver):
        self.driver = driver

    def editRecord(self):
        project = self.table.item(self.rowNr, 2).text()
        date = self.table.item(self.rowNr, 4).text()
        total = self.table.item(self.rowNr, 5).text()
        wbs = self.table.item(self.rowNr, 3).text()
        
        diag = recordModifyDialogControl(total, date, project, wbs)
        diag.setEditNth(self.editNth)
        diag.setTable(self.table)
        diag.setRow(self.rowNr)
        diag.setLog(self.log)
        diag.exec()
        self.log(f"The edit button for row: {self.rowNr} is pressed", "INFO")

    def deleteRecord(self):
        dialog = confirmationDialogControl(f"Are you sure to want to delete the {self.rowNr}. record?")
        dialog.exec()

        self.log(f"The delete button for row: {self.rowNr} is pressed", "ERROR")
        if dialog.action:
            self.delNth(self.rowNr)

    def freezeRecord(self):
        if self.recAcBtns.freezeBtn.isChecked():
            self.log(f"The record: {self.rowNr} is freezed", "INFO")
        else:
            self.log(f"The record: {self.rowNr} is unfreezed", "INFO")

    def sendRecord(self):
        if self.recAcBtns.freezeBtn.isChecked():
            #SAPI
            record = BookingItem(self.table.item(self.rowNr, 2).text(), float(self.table.item(self.rowNr, 5).text()), self.table.item(self.rowNr, 3).text())
            #is this fine without the date?
            self.driver.add_booking_item_to_queue(record)

            #Manager - relay server
            data = {
                "wbs": self.table.item(self.rowNr, 3).text(),
                "project": self.table.item(self.rowNr, 2).text(),
                "day": datetime.strptime(self.table.item(self.rowNr, 4).text(), "%Y.%m.%d"),
                "hours": float(self.table.item(self.rowNr, 5).text())
            }
            url = os.environ["RELAY_URL"]
            response = requests.post(url, json=data, verify=False)
            self.log(f"{response.text} sent to manager", "INFO")

            self.log(f"The {self.rowNr} record is sent to server. The {self.rowNr} record is freezed, the action buttons are disabled", "INFO")
            self.recAcBtns.sendBtn.setDisabled(True)
            self.recAcBtns.freezeBtn.setDisabled(True)
            self.recAcBtns.editBtn.setDisabled(True)
            self.recAcBtns.deleteBtn.setDisabled(True)
        else:
            self.log(f"The {self.rowNr} record is not freezed. Freeze the record first and after that send it.", "WARNING")
            self.recAcBtns.sendBtn.setEnabled(True)
            self.recAcBtns.freezeBtn.setEnabled(True)
            self.recAcBtns.editBtn.setEnabled(True)
            self.recAcBtns.deleteBtn.setEnabled(True)
