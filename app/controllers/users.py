from PyQt5 import QtWidgets
from PyQt5.QtCore import QEvent
from app.models.user import User
from auth.models.auth import Auth
from PyQt5.QtWidgets import QMessageBox
from settings.database import db_session
from settings.settings import SALT_LENGTH
from core.window import PageWindow, Window
from ui.users import users_ui, users_modal_ui
from core.helpers.helper import set_default_controller_properties, get_random_string, get_translate


class UsersController(PageWindow, QtWidgets.QMainWindow, users_ui.Ui_MainWindow):
    def __init__(self, main_window: Window):
        super(UsersController, self).__init__()

        # CRUD actions
        self.add_action = None
        self.edit_action = None
        self.context_menu = None
        self.delete_action = None

        # Init page
        self.main_window = main_window

        ''' 
            Populating mass properties for the page 
            Should be rewrote in case of using your own interface
            By default properties are required: lang_1, lang_2 buttons for language switching, user_page_button and
            logout_button for menu.
        '''
        set_default_controller_properties(self, title=get_translate('users'))

        # Register context menu
        self.create_context_menu()

        # Load data
        self._load_users()

        # Double click action to edit data
        self.tableWidget.itemDoubleClicked.connect(self._edit_modal)

        self.createModal.pressed.connect(self._create_modal)
        self.editModal.pressed.connect(self._edit_modal)
        self.deleteModal.pressed.connect(self._remove_user)

    ''' Init functions '''

    def create_context_menu(self):
        self.context_menu = QtWidgets.QMenu(self.tableWidget)
        self.add_action = self.context_menu.addAction(get_translate('add'))
        self.edit_action = self.context_menu.addAction(get_translate('edit'))
        self.delete_action = self.context_menu.addAction(get_translate('delete'))

        self.tableWidget.installEventFilter(self)

    # Registering context menu
    def eventFilter(self, source, event):
        if event.type() == QEvent.ContextMenu:
            if source == self.tableWidget:
                action = self.context_menu.exec_(event.globalPos())
                if action == self.edit_action:
                    self._edit_modal()
                elif action == self.delete_action:
                    self._remove_user()
                elif action == self.add_action:
                    self._create_modal()
                return True

        return super().eventFilter(source, event)

    # Rendering data
    def render_data(self):
        self.render_translation()
        self._load_users()

    # Adding translations to text inside
    def render_translation(self):
        self.groupBox_3.setTitle(get_translate('users'))

        # Table
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(get_translate('name'))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(get_translate('login'))

        # Action menu
        self.createModal.setText(get_translate('add'))
        self.editModal.setText(get_translate('edit'))
        self.deleteModal.setText(get_translate('delete'))

        # Context menu
        self.add_action.setText(get_translate('add'))
        self.edit_action.setText(get_translate('edit'))
        self.delete_action.setText(get_translate('delete'))

        # Menu
        self.groupBox.setTitle(get_translate('menu'))
        self.user_page_button.setText(get_translate('users'))
        self.main_page_button.setText(get_translate('main'))
        self.logout_button.setText(get_translate('logout'))

    ''' Working with data '''

    def _load_users(self) -> None:
        # Cleaning table if it has rows to re-render data
        if self.tableWidget.rowCount() > 0:
            self.tableWidget.setRowCount(0)

        row = 0
        users = db_session.query(User).order_by(User.id.desc()).all()
        for user in users:
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(user.id)))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(user.name))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(user.login))

    def _create_modal(self) -> None:
        modal = CreateUserModal(self)
        modal.exec_()

    def _edit_modal(self) -> None:
        # Finding current row by mouse position (selected by item index)
        row = self.tableWidget.currentIndex().row()
        # Checking that row is checked
        if row > -1:
            # Getting ID from first column of this row
            user_id = self.tableWidget.item(row, 0).text()
            modal = EditUserModal(user_id, self, row)
            modal.exec_()
        else:
            QMessageBox.warning(self, 'Message', get_translate('choose_row_to_edit'), QMessageBox.Ok)
            self.show()

    def _remove_user(self) -> None:
        # Finding current row by mouse position (selected by item index)
        row = self.tableWidget.currentIndex().row()
        # Checking that row is checked
        if row > -1:
            # Getting ID from first column of this row
            user_id = self.tableWidget.item(row, 0).text()
            session = Auth.get_session()
            if int(user_id) == session.user.id:
                QMessageBox.critical(self, 'Message', get_translate('cant_delete_yourself'), QMessageBox.Ok)
                self.show()
                return
            db_session.delete(
                db_session.get(User, user_id)
            )
            db_session.commit()
            self.tableWidget.removeRow(self.tableWidget.currentIndex().row())
        else:
            QMessageBox.warning(self, 'Message', get_translate('choose_row_to_delete'), QMessageBox.Ok)
            self.show()


class CreateUserModal(QtWidgets.QDialog, users_modal_ui.Ui_Dialog):
    def __init__(self, page):
        super(CreateUserModal, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('')
        self.page = page
        self.buttonBox.accepted.connect(self._save_new)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

    def _save_new(self) -> None:
        login = self.login.text().strip()
        password = self.password.text()
        name = self.name.text()

        if len(login) == 0 or len(password) == 0:
            return

        # Encoding password
        salt = get_random_string(SALT_LENGTH)
        password = User.hash_password(password, salt)

        try:
            user = db_session.query(User).filter(User.login == login).first()
            if not user:
                user = User(
                    login=login,
                    password=password,
                    name=name,
                    salt=salt
                )
                db_session.add(
                    user
                )
                db_session.commit()
                new_row = self.page.tableWidget.rowCount()
                self.page.tableWidget.insertRow(new_row)
                self.page.tableWidget.setItem(new_row, 0, QtWidgets.QTableWidgetItem(str(user.id)))
                self.page.tableWidget.setItem(new_row, 1, QtWidgets.QTableWidgetItem(user.name))
                self.page.tableWidget.setItem(new_row, 2, QtWidgets.QTableWidgetItem(user.login))
        except Exception as err:
            print(err)


class EditUserModal(QtWidgets.QDialog, users_modal_ui.Ui_Dialog):
    def __init__(self, user_id, page, row):
        super(EditUserModal, self).__init__()
        self.setupUi(self)
        self.page = page
        self.row = row
        self.user = db_session.get(User, user_id)
        self.login.setText(self.user.login)
        self.name.setText(self.user.name)
        self.buttonBox.accepted.connect(self._save_changes)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

    def _save_changes(self) -> None:
        login = self.login.text().strip()
        password = self.password.text()
        name = self.name.text()

        if len(login) == 0:
            return

        if len(password) > 0:
            salt = get_random_string(SALT_LENGTH)
            password = User.hash_password(password, salt)
            self.user.password = password

        self.user.name = name
        self.user.login = login
        db_session.commit()
        self.page.tableWidget.item(self.row, 1).setText(self.user.name)
        self.page.tableWidget.item(self.row, 2).setText(self.user.login)
