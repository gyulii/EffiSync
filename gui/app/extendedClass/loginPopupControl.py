from loginPopup import Ui_Dialog
from PySide6.QtWidgets import QDialog 
from PySide6.QtCore import Signal

class loginPopupControl(QDialog):
    signInType = None

    def __init__(self, type=None):
        super().__init__()
        self.diagUI = Ui_Dialog()
        self.diagUI.setupUi(self)

        if type is not None:
            self.diagUI.loginWidget.hide()
            self.diagUI.title.setText("How would you like to log in?")
            self.adjustSize()
        else:
            self.diagUI.user_adminWidget.hide()
            self.diagUI.title.setText("Log in to access to developer mode!")
            self.adjustSize()

        self.diagUI.loginBtn.clicked.connect(self.login)
        self.diagUI.asAdminBtn.clicked.connect(self.setAsManager)
        self.diagUI.asUserBtn.clicked.connect(self.setAsUser)
        self.diagUI.cancelBtn.clicked.connect(self.close)
        
    def getUserName(self):
        return self.diagUI.userNameInput.text()
    
    def getPassword(self):
        return self.diagUI.passwordInput.text()
    
    def setAsManager(self):
        self.signInType = "asManager"
        self.diagUI.loginWidget.show()
        self.diagUI.user_adminWidget.hide()
        self.adjustSize()
    
    def setAsUser(self):
        self.signInType = "asUser"
        self.close()

    def login(self):
        userName = self.getUserName()
        password = self.getPassword()

        print(f"Username: {userName}. Password: {password}")

        if userName == "admin" and password == "admin":
            print("The authentication was sucessfully")
            self.close()
            self.auth = True
        else:
            print("The authetication was unsucessfully")
            self.diagUI.userNameInput.clear()
            self.diagUI.passwordInput.clear()
            self.diagUI.infoMsg.setText("The username or the passwor is incorrect. Try again!")
            self.auth = False
        