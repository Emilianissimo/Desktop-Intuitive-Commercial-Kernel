from __future__ import annotations

import importlib

from core.providers.core_provider import CoreProvider
from core.routes import routes
from PyQt5 import QtWidgets, QtCore
from settings.settings import APP_CONTROLLERS_PATH


class PageWindow(QtWidgets.QMainWindow):
    gotoSignal = QtCore.pyqtSignal(str)
    __translate__ = QtCore.QCoreApplication.translate

    def goto(self, name: str) -> None:
        self.gotoSignal.emit(name)

    def set_lang(self, lang: str, auth_module) -> None:
        auth_module.set_language(lang)
        self.render_translation()

    def render_data(self):
        self.render_translation()

    def render_translation(self):
        pass


class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.showMaximized()
        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.m_pages = {}
        for route in routes:
            module_name = APP_CONTROLLERS_PATH + route['module']
            module = importlib.import_module(module_name)
            class_ = getattr(module, route['class'])
            self.register(class_(self), route['name'])

        self.goto(routes[0]['name'])

    def register(self, widget: QtWidgets.QMainWindow, name: str) -> None:
        self.m_pages[name] = widget
        self.stacked_widget.addWidget(widget)
        if isinstance(widget, PageWindow):
            widget.gotoSignal.connect(self.goto)

    @QtCore.pyqtSlot(str)
    def goto(self, name: str) -> None:
        if name in self.m_pages:
            widget = self.m_pages[name]
            self.stacked_widget.setCurrentWidget(widget)
            self.setWindowTitle(widget.windowTitle())
            # Interfare before page opening
            CoreProvider.boot(widget)
