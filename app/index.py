import datetime
import getpass
import pickle
from threading import Timer

from PySide6.QtWidgets import QCheckBox, QHBoxLayout
from PySide6.QtCore import Qt, QDateTime, QTime, QSize
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView, QWidget, QFrame
from pandas.io.common import file_exists

from app.db.database_handler import DatabaseHandler
from app.gui import Ui_MainWindow, loginPopupControl, recordActionBtnControl, confirmationDialogControl, projectActionBtnControl
from app.gui.extendedClass.projectModifyDialogControl import projectModifyDialogControl
from app.gui.extendedClass.topicActionsBtnControl import topicActionBtnControl
from app.gui.extendedClass.topicModifyDialogControl import topicModifyDialogControl
from app.network.network_client import RelayClient
from app.network.network_manager import RelayManager
from app.sapi.sap_handler import EssDriver


class myApp(QMainWindow, Ui_MainWindow):

    timerThread = None
    pollingThread = None
    blink = False
    userID = None
    lastChange = None
    timeTables = None

    def __init__(self, type=None):
        super().__init__()

        self.setupUi(self)
        self.db=DatabaseHandler()
        self.effiLog("Open the UI.")

        self.driver = EssDriver()
        self.relay = RelayClient() if type != "Manager" else RelayManager()

        self.userID = getpass.getuser()
        if file_exists("lastChange.p"):
            f = open("lastChange.p", "rb")
        else: f = None
        if f is not None and f.readable():
            self.lastChange = pickle.load(f)
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
        else:
            self.retrieveProjectsTopics()

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
        self.loadTimeTable()
        
        if type == "Manager":
            self.topicsTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.employeesTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.projectsTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.bookingtextsTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.bookingtextsBtnFrame.hide()
            self.employeeBtnFrame.hide()
            self.bookintextsBtnFrameMini.hide()
            self.employeeBtnFrameMini.hide()
            self.managerWidgetMini.setMinimumSize(QSize(0, 100))
            self.managerWidget.setMinimumSize(QSize(0, 100))
            self.loadTopicsTable()
            self.loadProjectsTable()
            self.addNewProjectBtn.clicked.connect(self.addNewProject)
            self.addNewTopicBtn.clicked.connect(self.addNewTopic)
            self.syncTopicsBtn.clicked.connect(self.sendProjectsTopics)
            self.syncProjectsBtn.clicked.connect(self.sendProjectsTopics)

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


    def retrieveProjectsTopics(self):
        current = self.relay.sync_projects_topics(self.lastChange)
        if current[0]:
            self.lastChange = current[1].get("time")
            projects = current[1].get("projects")
            topics = current[1].get("topics")
            self.db.sync_tables(projects, topics)
            self.loadProjectsTable()
            self.updateProjectList()
            self.loadTopicsTable()
            self.updateLocationList()
            self.loadTimeTable()

        self.pollingThread = Timer(600, self.retrieveProjectsTopics)
        self.pollingThread.start()

    def sendProjectsTopics(self):
        projs = self.db.read_all_projects()
        topics = self.db.read_all_locations()
        self.relay.sync_manager([proj.to_dict() for proj in projs], [topic.to_dict() for topic in topics])

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
        projects = self.db.read_active_booking_names()
        self.projectDropDownList.clear()
        self.projectDropDownList.addItems(projects)

    def updateLocationList(self):
        locations = self.db.read_active_location_names()
        self.topicDropDownList.clear()
        self.topicDropDownList.addItems(locations)

    def loadTopicsTable(self):
        self.topics = self.db.read_all_locations()
        #clear the table
        self.topicsTable.setRowCount(0)
        #set columns
        header = ["Country","WBS","Active","Actions"]
        self.topicsTable.setColumnCount(4)
        self.topicsTable.setHorizontalHeaderLabels(header)
        self.topicsTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for i in range(len(self.topics)):
            self.topicsTable.insertRow(i)
            self.topicsTable.setItem(i, 0, QTableWidgetItem(str(self.topics[i].country)))
            self.topicsTable.setItem(i, 1, QTableWidgetItem(str(self.topics[i].wbs)))
            checkboxWidget = QFrame()
            checkboxLayout = QHBoxLayout(checkboxWidget)
            checkbox = QCheckBox(checkboxWidget)
            checkbox.setChecked(self.topics[i].active)
            checkbox.stateChanged.connect(lambda state, j=i: self.changeTopicState(j, state))
            checkboxLayout.addWidget(checkbox)
            self.topicsTable.setCellWidget(i, 2, checkboxWidget)
            actionBtn = topicActionBtnControl()
            actionBtn.setRowNr(i)
            actionBtn.setTable(self.topicsTable)
            actionBtn.setLog(self.miniLog)
            actionBtn.setLogField(self.userLog)
            actionBtn.setDBActions(self.editNthTopic)
            actionBtn.topicActionsBtn.editBtn.setEnabled(True)
            self.topicsTable.setCellWidget(i, 3, actionBtn)


    def addNewTopic(self):
        diag = topicModifyDialogControl()
        diag.setEditNth(self.createTopic)
        diag.exec()

    def createTopic(self, row, country, wbs):
        self.db.create_location(self.db.Location(country=country, wbs=wbs))
        self.loadTopicsTable()
        self.updateLocationList()

    def changeTopicState(self, row, state):
        topic = self.topics[row]
        if state:
            self.db.activate_location(topic)
        else:
            self.db.archive_location(topic)
        self.loadTopicsTable()
        self.updateLocationList()

    def editNthTopic(self, row, country, wbs):
        self.db.update_location(self.topics[row], self.db.Location(country=country, wbs=wbs))
        self.loadTopicsTable()
        self.updateLocationList()

    def loadProjectsTable(self):
        self.projects = self.db.read_all_projects()
        #clear the table
        self.projectsTable.setRowCount(0)
        #set columns
        header = ["Project","Active","Actions"]
        self.projectsTable.setColumnCount(3)
        self.projectsTable.setHorizontalHeaderLabels(header)
        self.projectsTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for i in range(len(self.projects)):
            self.projectsTable.insertRow(i)
            self.projectsTable.setItem(i, 0, QTableWidgetItem(str(self.projects[i].name)))
            checkboxWidget = QFrame()
            checkboxLayout = QHBoxLayout(checkboxWidget)
            checkbox = QCheckBox(checkboxWidget)
            checkbox.setChecked(self.projects[i].active)
            checkbox.stateChanged.connect(lambda state, j=i: self.changeProjectState(j, state))
            checkboxLayout.addWidget(checkbox)
            self.projectsTable.setCellWidget(i, 1, checkboxWidget)
            actionBtn = projectActionBtnControl()
            actionBtn.setRowNr(i)
            actionBtn.setTable(self.projectsTable)
            actionBtn.setLog(self.miniLog)
            actionBtn.setLogField(self.userLog)
            actionBtn.setDBActions(self.editNthProject)

            actionBtn.projectActionsBtn.editBtn.setEnabled(True)

            self.projectsTable.setCellWidget(i, 2, actionBtn)


    def addNewProject(self):
        diag = projectModifyDialogControl()
        diag.setEditNth(self.createProject)
        diag.exec()

    def createProject(self, row, project):
        self.db.create_booking_item(self.db.BookingItem(name=project))
        self.loadProjectsTable()
        self.updateProjectList()

    def changeProjectState(self, row, state):
        proj = self.projects[row]
        if state:
            self.db.activate_booking_item(proj)
        else:
            self.db.archive_booking_item(proj)
        self.loadProjectsTable()
        self.updateProjectList()

    def editNthProject(self, row, project):
        self.db.update_booking_item(self.projects[row],self.db.BookingItem(name=project, active=self.projects[row].active))
        self.loadProjectsTable()
        self.updateProjectList()

    def loadTimeTable(self):
        self.timeTables = self.db.read_active_time_table_items()
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
            actionBtns.setDBActions(self.delNthRow, self.editNthRow, self.archiveNthRow)
            actionBtns.setServices(self.driver, self.relay)

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

    def archiveNthRow(self, row):
        self.db.archive_time_table_item(self.timeTables[row])
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
                recBtn.sendRecord()
                self.miniLog("All records are sent...", "INFO")
            #self.driver.execute_booking() #should be uncommented when not on outside machine
            self.relay.send_queue()

    def closeEvent(self, event):
        dialog = confirmationDialogControl("Are you sure to want to exit from the app?")
        dialog.exec()

        if dialog.action:
            self.timerThread.cancel()
            self.pollingThread.cancel() if self.pollingThread is not None else None
            pickle.dump(self.lastChange, open("lastChange.p", "wb"))
            event.accept()
        else:
            event.ignore()