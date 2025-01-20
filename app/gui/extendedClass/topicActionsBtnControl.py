from PySide6.QtWidgets import QWidget

from app.gui.baseClass.projectActions import Ui_projectActionBtns
from app.gui.extendedClass.topicModifyDialogControl import topicModifyDialogControl


class topicActionBtnControl(QWidget):

    rowNr = None

    def __init__(self):
        super().__init__()
        self.topicActionsBtn = Ui_projectActionBtns()
        self.topicActionsBtn.setupUi(self)
        self.topicActionsBtn.editBtn.clicked.connect(self.editBtnClicked)

    def setRowNr(self, num):
        self.rowNr = num

    def setTable(self, table):
        self.table = table

    def setLogField(self, field):
        self.logField = field
        self.log("Új sor hozzáadva", "WARNING")

    def setLog(self, log):
        self.log = log

    def setDBActions(self, editNth):
        self.editNth = editNth

    def editBtnClicked(self):
        topic = self.table.item(self.rowNr, 0).text()
        wbs = self.table.item(self.rowNr, 1).text()
        diag = topicModifyDialogControl(topic, wbs)
        diag.setEditNth(self.editNth)
        diag.setRow(self.rowNr)
        diag.exec()