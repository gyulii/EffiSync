from PySide6.QtWidgets import QDialog

from app.gui.baseClass.topicModifyDialog import Ui_Dialog


class topicModifyDialogControl(QDialog):
    country = None
    wbs = None
    row = None

    def __init__(self, country=None, wbs=None):
        super().__init__()
        self.diag = Ui_Dialog()
        self.diag.setupUi(self)

        if country is not None and wbs is not None:
            self.country = country
            self.wbs = wbs
            self.diag.topicLocation.setText(country)
            self.diag.topicWbs.setText(wbs)

        self.diag.topicLocation.textChanged.connect(self.updateCountry)
        self.diag.topicWbs.textChanged.connect(self.updateWbs)
        self.diag.buttonBox.accepted.connect(self.save)
        self.diag.buttonBox.rejected.connect(self.close)

    def setRow(self, row):
        self.row = row

    def setEditNth(self, editNth):
        self.editNth = editNth

    def updateCountry(self, text):
        self.country = text

    def updateWbs(self, text):
        self.wbs = text

    def save(self):
        self.editNth(self.row, self.country, self.wbs)
        self.close()