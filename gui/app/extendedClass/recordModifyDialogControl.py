from recordModifyDialog import Ui_modifyRecord
from PySide6.QtWidgets import QDialog, QTableWidget, QTableWidgetItem
from PySide6.QtCore import Qt, QTime

class recordModifyDialogControl(QDialog):
    project = None
    start = QTime()
    end = QTime()
    total = QTime()

    table = None
    rowNr = None
    log = None

    def __init__(self, start=None, end=None, project=None):
        super().__init__()
        self.diag = Ui_modifyRecord()
        self.diag.setupUi(self)

        if start is not None and end is not None and project is not None:
            self.start = QTime().fromString(start, "hh:mm")
            self.end = QTime().fromString(end,"hh:mm")
            self.calcTotal()

            self.project = project

            self.setupFields()

        self.diag.saveBtn.clicked.connect(self.save)
        self.diag.discardBtn.clicked.connect(self.close)
        self.diag.startTime.timeChanged.connect(self.updateTotal)
        self.diag.endTime.timeChanged.connect(self.updateTotal)
        self.diag.projectList.currentIndexChanged.connect(self.updateProject)

    def setTable(self, table):
        self.table = table

    def setRow(self, nr):
        self.rowNr = nr

    def setLog(self, log):
        self.log = log

    def setProject(self, project):
        self.project = project

    def setSatrt(self, start):
        self.start = start

    def setEnd(self, end):
        self.end = end

    def calcTotal(self):
        self.total = QTime.fromMSecsSinceStartOfDay(self.start.secsTo(self.end)*1000)

    def getProject(self):
        return self.project

    def getSatrt(self):
        return self.start

    def getEnd(self):
        return self.end

    def setupFields(self):
        self.diag.startTime.setTime(self.start)
        self.diag.endTime.setTime(self.end)
        self.diag.totalTime.setTime(self.total)

        prjIdx = self.diag.projectList.findText(self.project)
        self.diag.projectList.setCurrentIndex(prjIdx)

    def updateProject(self, projectIndex):
        self.project = self.diag.projectList.currentText()

    def updateTotal(self):
        self.start = self.diag.startTime.time()
        self.end = self.diag.endTime.time()
        self.calcTotal()
        self.diag.totalTime.setTime(self.total)

    def save(self):
        # data validity check needed

        self.table.setItem(self.rowNr, 2, QTableWidgetItem(self.project))
        self.table.setItem(self.rowNr, 3, QTableWidgetItem(self.start.toString("hh:mm")))
        self.table.setItem(self.rowNr, 4, QTableWidgetItem(self.end.toString("hh:mm")))
        self.table.setItem(self.rowNr, 5, QTableWidgetItem(self.total.toString("hh:mm")))

        self.close()