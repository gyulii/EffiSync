import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from index import myApp
from loginPopupControl import loginPopupControl
from MainWindow import Ui_MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    startup = loginPopupControl("start")
    startup.exec()

    if startup.signInType == "asUser":
        window = myApp("User")
        window.show()
        app.exec()
    elif startup.signInType == "asManager" and startup.auth:
        window = myApp("Manager")
        window.show()
        app.exec()
