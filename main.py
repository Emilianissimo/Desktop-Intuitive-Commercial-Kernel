'''

DON'T TOUCH OR CHANGE THIS FILE.
THERE IS NOTHING YOU NEED TO CHANGE!

'''

from core.window import Window
from auth.models import auth
from PyQt5 import QtWidgets
from auth.contollers import authentication

if __name__ == '__main__':
    App = QtWidgets.QApplication([])
    if not auth.Auth.check_session():
        window = authentication.LoginController()
    else:
        window = Window()
    window.show()
    App.exec()

