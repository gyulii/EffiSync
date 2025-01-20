from PySide6.QtWidgets import QWidget

from app.gui.baseClass.projectActions import Ui_projectActionBtns
from app.gui.extendedClass.projectModifyDialogControl import projectModifyDialogControl


class projectActionBtnControl(QWidget):

    rowNr = None

    def __init__(self):
        super().__init__()
        self.projectActionsBtn = Ui_projectActionBtns()
        self.projectActionsBtn.setupUi(self)
        self.projectActionsBtn.editBtn.clicked.connect(self.editBtnClicked)

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
        project = self.table.item(self.rowNr, 0).text()
        diag = projectModifyDialogControl(project)
        diag.setEditNth(self.editNth)
        diag.setRow(self.rowNr)
        diag.exec()
