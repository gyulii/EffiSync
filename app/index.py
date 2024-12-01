import sys
import getpass
from threading import Timer
from PySide6.QtCore import Qt, QDateTime, QTime, QPoint
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QTableWidgetItem, QMessageBox, QDialog, QHeaderView
from PySide6.QtGui import QColor

import datetime


from app.gui import Ui_MainWindow, loginPopupControl, recordActionBtnControl, confirmationDialogControl
from app.db.database_handler import DatabaseHandler, mock_data


class myApp(QMainWindow, Ui_MainWindow):

    timerThread = None
    blink = False
    userID = None

    def __init__(self, type=None):
        super().__init__()
        self.setupUi(self)
        self.db=DatabaseHandler()
        self.effiLog("Open the UI.")

        self.userID = getpass.getuser()

        self.loadInitUI(type)

        self.homeBtn.clicked.connect(self.switchToHomePage)
        self.recordTimeBtn.clicked.connect(self.switchToRecordTimePage)
        self.recordedTimesBtn.clicked.connect(self.switchToRecordedTimesPage)
        self.developerBtn.clicked.connect(self.switchToDeveloperPage)

        if type == "Manager":
            self.employeeBtn.clicked.connect(self.switchToEmployeesPage)
            self.projectsBtn.clicked.connect(self.switchToProjectsPage)
            self.topicsBtn.clicked.connect(self.switchToTopicsPage)
            self.bookingtextsBtn.clicked.connect(self.switchToBookintextsPage)
            self.exportBtn.clicked.connect(self.switchToExportPage)

        self.updateDateTime()

        self.fromDateBtn.clicked.connect(self.showHideFromCalendar)
        self.toDateBtn.clicked.connect(self.showHideToCalendar)
        self.startBtn.clicked.connect(self.startBtnAction)
        self.startBtn_2.clicked.connect(self.startBtnAction)
        self.stopBtn.clicked.connect(self.stopBtnAction)
        self.stopBtn_2.clicked.connect(self.stopBtnAction)
        self.lockAllBtn.clicked.connect(self.lockAllBtnAction)
        self.sendAllBtn.clicked.connect(self.sendAll)

    def loadInitUI(self, type):
        self.user.setText(f"User: {self.userID}")

        self.fromCalendar.hide()
        self.toCalendar.hide()

        self.effiLog("The UI initially outlook is loaded in.")

        if type == "User":
            self.managerBtn.hide()
            self.managerBtnMini.hide()

        self.sideBar.hide()
        self.managerWidget.hide()
        self.managerWidgetMini.hide()

        #mock_data()
        self.updateProjectList()
        self.updateLocationList()
        self.bookingtextFrame.hide()

        self.bodyWidget.setCurrentIndex(0)

        # header = ["#","User","Project","Start","End","Total","Actions"]
        # self.recordedTimesTable.setColumnCount(7)
        # self.recordedTimesTable.setHorizontalHeaderLabels(header)
        # self.recordedTimesTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.loadTimeTable()
        
        if type == "Manager":
            self.topicsTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.employeesTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.projectsTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.bookingtextsTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def switchToHomePage(self):
        self.bodyWidget.setCurrentIndex(0)
        self.effiLog("Switch to Home page.")

    def switchToRecordTimePage(self):
        self.bodyWidget.setCurrentIndex(1)
        self.effiLog("Switch to Record Time page.")

    def switchToRecordedTimesPage(self):
        self.bodyWidget.setCurrentIndex(2)
        self.effiLog("Switch to Recorded Time page.")

    def switchToEmployeesPage(self):
        self.bodyWidget.setCurrentIndex(3)
        self.effiLog("Switch to Employees page.")

    def switchToProjectsPage(self):
        self.bodyWidget.setCurrentIndex(4)
        self.effiLog("Switch to Projects page.")

    def switchToTopicsPage(self):
        self.bodyWidget.setCurrentIndex(5)
        self.effiLog("Switch to Topics page.")

    def switchToBookintextsPage(self):
        self.bodyWidget.setCurrentIndex(6)
        self.effiLog("Switch to Booking texts page.")

    def switchToExportPage(self):
        self.bodyWidget.setCurrentIndex(7)
        self.effiLog("Switch to Export page.")

    def switchToDeveloperPage(self):
        dialog = loginPopupControl()
        dialog.exec()

        if dialog.auth:
            self.bodyWidget.setCurrentIndex(8)
            self.effiLog("The login was successfully...Switch to Developer page.")

    def updateDateTime(self):
        self.timerThread = Timer(1, self.updateDateTime)
        self.timerThread.start()

        date = QDateTime.currentDateTime().date()
        time = QDateTime.currentDateTime().time()
        
        if self.blink:
            self.timeLCD.display(time.toString("hh mm"))
            self.blink = False
        else:
            self.timeLCD.display(time.toString("hh:mm"))
            self.blink = True

        self.dateLCD.display(date.toString("yyyy.MM.dd."))

    def showHideFromCalendar(self, checked):
        if checked:
            self.fromDateBtn.setText("Close Calendar")
            self.toDateBtn.setText("Open Calendar")
            self.toDateBtn.setChecked(False)
            self.toCalendar.hide()
            self.fromCalendar.show()
            self.effiLog("The From date calendar is opened.")
        elif not checked:
            self.fromDateBtn.setText("Open Calendar")
            self.fromCalendar.hide()
            self.effiLog("The From date calendar is closed.")

    def showHideToCalendar(self, checked):
        if checked:
            self.toDateBtn.setText("Close Calendar")
            self.fromDateBtn.setText("Open Calendar")
            self.fromDateBtn.setChecked(False)
            self.fromCalendar.hide()
            self.toCalendar.show()
            self.effiLog("The To date calendar is opened.")
        elif not checked:
            self.toDateBtn.setText("Open Calendar")
            self.toCalendar.hide()
            self.effiLog("The To date calendar is closed.")

    def effiLog(self, text):
        time = datetime.datetime.now()
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        newRow = "<" + timestamp + ">: " + text
        curtext = self.textBrowser.toPlainText()
        log = curtext + newRow + "\n"
        self.textBrowser.setText(log)

    def miniLog(self, msg, state):
        time = datetime.datetime.now()
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        self.effiLog(msg)

        if state == "INFO":
            self.userLog.setTextColor(QColor("#bababa"))
            log = "<" + timestamp + "> INFO: " + msg + "\n"
            self.userLog.setText(log)
        elif state == "WARNING":
            self.userLog.setTextColor(QColor("#ffff00"))
            log = "<" + timestamp + "> WARNING: " + msg + "\n"
            self.userLog.setText(log)
        elif state == "ERROR":
            self.userLog.setTextColor(QColor("#ff0000"))
            log = "<" + timestamp + "> ERROR: " + msg + "\n"
            self.userLog.setText(log)

    def updateProjectList(self):
        projects = self.db.read_all_booking_names()
        self.projectDropDownList.clear()
        self.projectDropDownList.addItems(projects)

    def updateLocationList(self):
        locations = self.db.read_all_location_names()
        self.topicDropDownList.clear()
        self.topicDropDownList.addItems(locations)

    def loadTimeTable(self):
        # WIP
        self.timeTables = self.db.read_all_time_table_items()
        #clear the table
        self.recordedTimesTable.setRowCount(0)
        #set columns
        header = ["#","User","Project","Topic","Date","TimeElapsed","Actions"]
        self.recordedTimesTable.setColumnCount(7)
        self.recordedTimesTable.setHorizontalHeaderLabels(header)
        self.recordedTimesTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        for i in range(len(self.timeTables)):
            self.recordedTimesTable.insertRow(i)
            self.recordedTimesTable.setItem(i, 0, QTableWidgetItem(str(i+1)))
            self.recordedTimesTable.setItem(i, 1, QTableWidgetItem(str(self.userID)))
            self.recordedTimesTable.setItem(i, 2, QTableWidgetItem(str(self.timeTables[i].booking_item.name)))
            self.recordedTimesTable.setItem(i, 3, QTableWidgetItem(str(self.timeTables[i].location.wbs)))
            self.recordedTimesTable.setItem(i, 4, QTableWidgetItem(str(self.timeTables[i].date)))
            self.recordedTimesTable.setItem(i, 5, QTableWidgetItem(str(self.timeTables[i].hours)))

            actionBtns = recordActionBtnControl()
            actionBtns.setLog(self.miniLog)
            actionBtns.setRowNr(i)
            actionBtns.setTable(self.recordedTimesTable)
            actionBtns.setlogField(self.userLog)
            actionBtns.setDelNth(self.delNthRow)
            actionBtns.setEditNth(self.editNthRow)

            actionBtns.recAcBtns.editBtn.setEnabled(True)
            actionBtns.recAcBtns.freezeBtn.setEnabled(True)
            actionBtns.recAcBtns.deleteBtn.setEnabled(True)
            actionBtns.recAcBtns.sendBtn.setEnabled(True)

            self.recordedTimesTable.setCellWidget(i, 6, actionBtns)
        self.lockAllBtn.setEnabled(True)
        self.sendAllBtn.setEnabled(True)

    def delNthRow(self, row):
        self.db.delete_time_table_item(self.timeTables[row])
        self.loadTimeTable()

    def editNthRow(self, row, project, wbs, date, hours):
        self.db.update_time_table_item(self.timeTables[row], self.db.TimeTable(hours=hours, booking_item=self.db.BookingItem(name=project), location=self.db.Location(wbs=wbs), date=date))
        self.loadTimeTable()

    def startBtnActionDemo(self):
        rowNr = self.recordedTimesTable.rowCount()
        self.recordedTimesTable.insertRow(rowNr)

        self.recordedTimesTable.setItem(rowNr, 0, QTableWidgetItem(str(rowNr+1)))
        
        item = self.recordedTimesTable.item(rowNr, 0)
        item.setTextAlignment(Qt.AlignCenter)
        
        self.recordedTimesTable.setItem(rowNr, 1, QTableWidgetItem("u98029"))
        self.recordedTimesTable.setItem(rowNr, 2, QTableWidgetItem("Project3"))

        startDate = "12:45"
        endDate = "16:30"
        formatstring = "hh:mm"

        start = QTime.fromString(startDate, formatstring)
        end = QTime.fromString(endDate, formatstring)

        self.recordedTimesTable.setItem(rowNr, 3, QTableWidgetItem(start.toString(formatstring)))
        self.recordedTimesTable.setItem(rowNr, 4, QTableWidgetItem(end.toString(formatstring)))

        elips = start.secsTo(end)
        total = QTime.fromMSecsSinceStartOfDay(elips*1000)
        self.recordedTimesTable.setItem(rowNr, 5, QTableWidgetItem(total.toString(formatstring)))

        actionBtns = recordActionBtnControl()
        actionBtns.setLog(self.miniLog)
        actionBtns.setRowNr(rowNr)
        actionBtns.setTable(self.recordedTimesTable)
        actionBtns.setlogField(self.userLog)

        self.recordedTimesTable.setCellWidget(rowNr, 6, actionBtns)

    def startBtnAction(self):
        self.currentProject = self.db.BookingItem(name=self.projectDropDownList.currentText())
        self.currentLocation = self.db.Location(country=self.topicDropDownList.currentText())
        self.date = datetime.date.today()
        self.startTime = datetime.datetime.now()

        self.startBtn.setDisabled(True)
        self.startBtn_2.setDisabled(True)
        self.stopBtn.setEnabled(True)
        self.stopBtn_2.setEnabled(True)

        #Will remove this when data is loaded from the database
        # rowNr = self.recordedTimesTable.rowCount()
        # self.recordedTimesTable.insertRow(rowNr)
        #
        # self.recordedTimesTable.setItem(rowNr, 0, QTableWidgetItem(str(rowNr+1)))
        #
        # item = self.recordedTimesTable.item(rowNr, 0)
        # item.setTextAlignment(Qt.AlignCenter)
        #
        # self.recordedTimesTable.setItem(rowNr, 1, QTableWidgetItem(str(self.userID)))
        # self.recordedTimesTable.setItem(rowNr, 2, QTableWidgetItem(str(self.projectDropDownList.currentText())))
        #
        # startTime = QDateTime.currentDateTime().time().toString("hh:mm")
        #
        # self.recordedTimesTable.setItem(rowNr, 3, QTableWidgetItem(startTime))
        #
        # actionBtns = recordActionBtnControl()
        # actionBtns.setLog(self.miniLog)
        # actionBtns.setRowNr(rowNr)
        # actionBtns.setTable(self.recordedTimesTable)
        # actionBtns.setlogField(self.userLog)
        #
        # actionBtns.recAcBtns.editBtn.setDisabled(True)
        # actionBtns.recAcBtns.freezeBtn.setDisabled(True)
        # actionBtns.recAcBtns.deleteBtn.setDisabled(True)
        # actionBtns.recAcBtns.sendBtn.setDisabled(True)
        #
        # self.recordedTimesTable.setCellWidget(rowNr, 6, actionBtns)
        #
        # self.sendAllBtn.setDisabled(True)
        # self.lockAllBtn.setDisabled(True)

    def stopBtnAction(self):
        stopTime = datetime.datetime.now()
        deltaTime = (stopTime - self.startTime).seconds / 3600
        self.db.create_time_table_item(self.db.TimeTable(hours=deltaTime, booking_item=self.currentProject, location=self.currentLocation, date=self.date))
        #update the table
        self.loadTimeTable()

        self.startBtn.setEnabled(True)
        self.startBtn_2.setEnabled(True)
        self.stopBtn.setDisabled(True)
        self.stopBtn_2.setDisabled(True)

        #Will remove this when data is loaded from the database
        # rowNr = self.recordedTimesTable.rowCount() - 1
        #
        # endTime = QDateTime.currentDateTime().time().toString("hh:mm")
        # self.recordedTimesTable.setItem(rowNr, 4, QTableWidgetItem(endTime))
        #
        # startTime = self.recordedTimesTable.item(rowNr, 3).text()
        #
        # start = QTime.fromString(startTime, "hh:mm")
        # end = QTime.fromString(endTime, "hh:mm")
        #
        # elips = start.secsTo(end)
        # total = QTime.fromMSecsSinceStartOfDay(elips*1000)
        # self.recordedTimesTable.setItem(rowNr, 5, QTableWidgetItem(total.toString("hh:mm")))
        #
        # actionBtns = self.recordedTimesTable.cellWidget(rowNr, 6)
        #
        # actionBtns.recAcBtns.editBtn.setEnabled(True)
        # actionBtns.recAcBtns.freezeBtn.setEnabled(True)
        # actionBtns.recAcBtns.deleteBtn.setEnabled(True)
        # actionBtns.recAcBtns.sendBtn.setEnabled(True)
        #
        # self.lockAllBtn.setEnabled(True)
        # self.sendAllBtn.setEnabled(True)

    def lockAllBtnAction(self):
        rowNr = self.recordedTimesTable.rowCount()

        if self.lockAllBtn.isChecked():
            for i in range(0, rowNr):
                recBtn = self.recordedTimesTable.cellWidget(i, 6)
                if not recBtn.recAcBtns.freezeBtn.isChecked():
                    recBtn.recAcBtns.freezeBtn.click()
            
            self.lockAllBtn.setText("Unlock all")
            self.miniLog("All records are freezed (locked)...", "INFO")
        else:
            for i in range(0, rowNr):
                recBtn = self.recordedTimesTable.cellWidget(i, 6)
                if recBtn.recAcBtns.freezeBtn.isChecked():
                    recBtn.recAcBtns.freezeBtn.click()

            self.lockAllBtn.setText("Lock all")
            self.miniLog("All records are unfreezed (unlocked)...", "INFO")

    def sendAll(self):
        rowNr = self.recordedTimesTable.rowCount()
        isAllFreezed = False

        # check all records if any of them is not freezed
        for i in range(0, rowNr):
            state = self.recordedTimesTable.cellWidget(i,6).recAcBtns.freezeBtn.isChecked()

            if not state:
                isAllFreezed = False
                self.miniLog("Please lock all records before you send all to the manager...", "WARNING")
                break
            else:
                isAllFreezed = True

        if isAllFreezed:
            for i in range(0, rowNr):
                recBtn = self.recordedTimesTable.cellWidget(i, 6)
                recBtn.recAcBtns.sendBtn.click()
                self.miniLog("All records are sent...", "INFO")

    def closeEvent(self, event):
        dialog = confirmationDialogControl("Are you sure to want to exit from the app?")
        dialog.exec()

        if dialog.action:
            self.timerThread.cancel()
            event.accept()
        else:
            event.ignore()