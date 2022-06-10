import random
import string
from PyQt5 import QtWidgets
from auth.models import auth
from importlib import import_module


def get_random_string(length: int) -> str:
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    digits = string.digits
    return ''.join(random.choice(letters + digits) for i in range(length))


def centralize_window(instance: QtWidgets.QMainWindow) -> None:
    qtRectangle = instance.frameGeometry()
    centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
    qtRectangle.moveCenter(centerPoint)
    instance.move(qtRectangle.topLeft())


def set_default_controller_properties(instance: QtWidgets.QMainWindow, title: str) -> None:
    # Setting up UI and page as itself
    instance.setupUi(instance)
    instance.setWindowTitle(title)
    centralize_window(instance)

    # Menu buttons
    instance.logout_button.pressed.connect(lambda: auth.Auth.forget_session(instance))
    instance.main_page_button.pressed.connect(lambda: instance.goto('main'))
    instance.user_page_button.pressed.connect(lambda: instance.goto('users'))

    # Language buttons
    instance.lang_1.setText('RU')
    instance.lang_1.pressed.connect(lambda: instance.set_lang('ru', auth.Auth))
    instance.lang_2.setText('EN')
    instance.lang_2.pressed.connect(lambda: instance.set_lang('en', auth.Auth))


def get_translate(key: str) -> str:
    try:
        module = import_module('core.languages.' + auth.Auth.get_session().language)
        return module.messages.get(key, 'No_Text')
    except ModuleNotFoundError:
        print('Please use "messages" variable with dict inside in your language package')
