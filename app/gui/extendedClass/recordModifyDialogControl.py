import datetime

from PySide6.QtWidgets import QDialog, QTableWidget, QTableWidgetItem
from PySide6.QtCore import Qt, QTime, QDate

from app.db.database_handler import DatabaseHandler
from app.gui.baseClass.recordModifyDialog import Ui_modifyRecord

class recordModifyDialogControl(QDialog):
    project = None
    date = QDate()
    total = QTime()
    db = DatabaseHandler()

    table = None
    rowNr = None
    log = None

    def __init__(self, total=None, date=None, project=None, wbs=None):
        super().__init__()
        self.diag = Ui_modifyRecord()
        self.diag.setupUi(self)

        if total is not None and date is not None and project is not None and wbs is not None:
            self.total = QTime().fromMSecsSinceStartOfDay(float(total)*1000*3600)
            self.date = QDate().fromString(date, "yyyy-MM-dd")
            self.project = project
            self.wbs = wbs

            self.setupFields()

        self.diag.saveBtn.clicked.connect(self.save)
        self.diag.discardBtn.clicked.connect(self.close)
        self.diag.projectList.currentIndexChanged.connect(self.updateProject)
        self.diag.workDate.dateChanged.connect(self.updateDate)
        self.diag.totalTime.timeChanged.connect(self.updateTotal)

    def setTable(self, table):
        self.table = table

    def setRow(self, nr):
        self.rowNr = nr

    def setLog(self, log):
        self.log = log

    def setProject(self, project):
        self.project = project

    def setStart(self, start):
        self.start = start

    def setEnd(self, end):
        self.end = end

    def setEditNth(self, editNth):
        self.editNth = editNth

    def setDB(self, db):
        self.db = db

    def getProject(self):
        return self.project

    def getStart(self):
        return self.start

    def getEnd(self):
        return self.end

    def setupFields(self):
        self.diag.projectList.clear()
        self.diag.projectList.addItems(self.db.read_all_booking_names())
        self.diag.totalTime.setTime(self.total)
        self.diag.workDate.setDate(self.date)

        prjIdx = self.diag.projectList.findText(self.project)
        # if project is not in the list, exception handling should be added
        self.diag.projectList.setCurrentIndex(prjIdx)

    def updateProject(self, projectIndex):
        self.project = self.diag.projectList.currentText()

    def updateDate(self, date):
        self.date = date

    def updateTotal(self, total):
        self.total = total

    def save(self):
        # data validity check needed
        # db update
        self.editNth(self.rowNr, self.project, self.wbs, datetime.date.fromisoformat(self.date.toString("yyyy-MM-dd")), self.total.msecsSinceStartOfDay()/3600000)

        self.close()