from PySide6.QtWidgets import QDialog

from app.gui.baseClass.projectModifyDialog import Ui_Dialog


class projectModifyDialogControl(QDialog):
    project = None
    row = None

    def __init__(self, project=None):
        super().__init__()
        self.diag = Ui_Dialog()
        self.diag.setupUi(self)

        if project is not None:
            self.project = project
            self.diag.projectName.setText(project)

        self.diag.projectName.textChanged.connect(self.updateProject)
        self.diag.buttonBox.accepted.connect(self.save)
        self.diag.buttonBox.rejected.connect(self.close)

    def setRow(self, row):
        self.row = row

    def setEditNth(self, editNth):
        self.editNth = editNth

    def updateProject(self, text):
        self.project = text

    def save(self):
        self.editNth(self.row, self.project)
        self.close()
