from auth.models import auth
from ui import registration_ui
from app.models.user import User
from PyQt5 import QtWidgets, QtCore
from settings.database import db_session
from settings.settings import SALT_LENGTH
from core.helpers.helper import get_random_string, centralize_window


class RegistrationController(QtWidgets.QMainWindow, registration_ui.Ui_MainWindow):
    def __init__(self):
        super(RegistrationController, self).__init__()
        self.setupUi(self)
        self.label_2.setText('Registration')
        self.lineEdit.setPlaceholderText('Enter login')
        self.lineEdit_2.setPlaceholderText('Enter password')
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setPlaceholderText('Enter name')
        self.pushButton.setText('Sign up')
        self.pushButton_2.setText('Sign in')
        self.setWindowTitle('Authentication')
        self.pushButton.pressed.connect(self.register)
        self.pushButton_2.pressed.connect(self.login)
        centralize_window(self)
        self.setWindowFlag(QtCore.Qt.WindowMinMaxButtonsHint, False)
        self.setFixedSize(597, 406)

    def register(self) -> None:
        login = self.lineEdit.text().strip()
        password = self.lineEdit_2.text()
        name = self.lineEdit_3.text()

        if len(login) == 0 or len(password) == 0:
            return

        # Encoding password
        salt = get_random_string(SALT_LENGTH)
        password = User.hash_password(password, salt)

        try:
            user = db_session.query(User).filter(User.login == login).first()
            if not user:
                db_session.add(
                    User(
                        login=login,
                        password=password,
                        name=name,
                        salt=salt
                    )
                )
                self.login()
            else:
                self.label_2.setText(f'Account {login} already exists!')
        except Exception as err:
            print(err)
            self.label_2.setText('Registration error')

    def login(self) -> None:
        self.login = LoginController()
        self.login.show()
        self.hide()


class LoginController(QtWidgets.QMainWindow, registration_ui.Ui_MainWindow):
    def __init__(self):
        super(LoginController, self).__init__()
        self.setupUi(self)
        self.setupUi(self)
        self.setWindowTitle('Authentication')
        self.label_2.setText('Sign in')
        centralize_window(self)
        self.setWindowFlag(QtCore.Qt.WindowMinMaxButtonsHint, False)
        self.setFixedSize(597, 406)
        self.lineEdit_3.hide()

        # Will use in something else, like blocking remote app user in future
        # DEPRECATED was needed until new ORM uploaded
        if User.__table__ is not None:
            self.activated_view()
        else:
            self.deactivated_view()

    def activate(self) -> None:
        # Future code to activate blocked program by remote
        self.activated_view()

    def activated_view(self) -> None:
        self.lineEdit.setPlaceholderText('Enter login')
        self.lineEdit_2.setPlaceholderText('Enter password')
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton.setText('Sign in')
        self.pushButton_2.setText('Sign up')
        self.pushButton.pressed.connect(self.login)
        self.pushButton_2.pressed.connect(self.register)
        self.lineEdit.setEnabled(True)
        self.lineEdit_2.setEnabled(True)
        self.pushButton.setEnabled(True)

    def deactivated_view(self) -> None:
        self.lineEdit.setPlaceholderText('No data')
        self.lineEdit.setEnabled(False)
        self.lineEdit_2.setPlaceholderText('No data')
        self.lineEdit_2.setEnabled(False)
        self.pushButton.setText('You blocked')
        self.pushButton.setEnabled(False)
        self.pushButton_2.setText('Activate')
        self.pushButton_2.pressed.connect(self.activate)

    def register(self) -> None:
        self.register = RegistrationController()
        self.register.show()
        self.hide()

    def login(self) -> None:
        login = self.lineEdit.text().strip()
        password = self.lineEdit_2.text()

        if len(login) == 0 or len(password) == 0:
            self.label_2.setText('Pass data!')
            return

        user = db_session.query(User).filter(User.login == login).first()
        if user:
            password = User.hash_password(password, user.salt)
            if user.password == password:
                auth.Auth.write_session(user.id, self)
            else:
                self.label_2.setText('Incorrect credentials')
        else:
            self.label_2.setText('Account is not found')
