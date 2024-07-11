import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from app.index import myApp
from app.gui import loginPopupControl


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
