from ui import main_ui
from PyQt5 import QtWidgets
from auth.models.auth import Auth
from core.window import PageWindow
from core.helpers.helper import set_default_controller_properties, get_translate


class MainController(PageWindow, QtWidgets.QMainWindow, main_ui.Ui_MainWindow):
    def __init__(self, main_window):
        super(MainController, self).__init__()
        self.main_window = main_window
        set_default_controller_properties(self, title=get_translate('main'))
        self._set_data()

    def _set_data(self):
        if Auth.get_session():
            self.username.setText(
                f"{get_translate('user')}: {Auth.get_session().user.name.capitalize()}"
            )

    # Rendering data
    def render_data(self):
        self.render_translation()
        self._set_data()

    def render_translation(self):
        self.groupBox_3.setTitle(get_translate('main'))
        # Menu
        self.groupBox.setTitle(get_translate('menu'))
        self.user_page_button.setText(get_translate('users'))
        self.main_page_button.setText(get_translate('main'))
        self.logout_button.setText(get_translate('logout'))
