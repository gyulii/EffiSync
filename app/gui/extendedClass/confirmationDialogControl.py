from PySide6.QtCore import Qt
from app.gui.baseClass.confirmationDialog import Ui_confirmationDialog
from PySide6.QtWidgets import QDialog, QWidget

class confirmationDialogControl(QDialog):
    def __init__(self, text=None):
        super().__init__()
        self.diag = Ui_confirmationDialog()
        self.diag.setupUi(self)

        if text is not None:
            self.diag.label.setText(text)
        
        self.diag.saveBtn.clicked.connect(self.yes)
        self.diag.discardBtn.clicked.connect(self.no)

    def yes(self):
        self.close()
        self.action = True
    
    def no(self):
        self.close()
        self.action = False