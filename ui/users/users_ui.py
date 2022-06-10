# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resource/UI/users.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(905, 716)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QWidget{\n"
"    background: #222;\n"
"    color: white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setStyleSheet("background-color: white !important;\n"
"    color: black;")
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 679, 508))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_3)
        self.tableWidget.setStyleSheet("QMenu::item {\n"
"    background-color: transparent;\n"
"}\n"
"            \n"
"QMenu::item:selected {\n"
"    background-color: #0074cc;\n"
"    color: white;\n"
" }")
        self.tableWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.gridLayout_6.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_3)
        self.verticalLayout.setStretch(0, 2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_3, 0, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.deleteModal = QtWidgets.QPushButton(self.groupBox_2)
        self.deleteModal.setStyleSheet("padding: 20px; background: #d9534f; color: #222")
        self.deleteModal.setObjectName("deleteModal")
        self.gridLayout_5.addWidget(self.deleteModal, 0, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 0, 0, 1, 1)
        self.editModal = QtWidgets.QPushButton(self.groupBox_2)
        self.editModal.setStyleSheet("padding: 20px; background:#f0ad4e;color:#222")
        self.editModal.setObjectName("editModal")
        self.gridLayout_5.addWidget(self.editModal, 0, 3, 1, 1)
        self.createModal = QtWidgets.QPushButton(self.groupBox_2)
        self.createModal.setStyleSheet("padding: 20px; background: green")
        self.createModal.setObjectName("createModal")
        self.gridLayout_5.addWidget(self.createModal, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setStyleSheet("groupBox{\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton{\n"
"    padding: 10px 10px 10px 0;\n"
"    border: 2px #222;\n"
"    border-style: none none solid none;\n"
"    transition: all 500ms;\n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  border-color: white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"   background: white;\n"
"    color: #222;\n"
"    border-color: #222;\n"
"}\n"
"\n"
"")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.logout_button = QtWidgets.QPushButton(self.groupBox)
        self.logout_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logout_button.setObjectName("logout_button")
        self.gridLayout_3.addWidget(self.logout_button, 4, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setStyleSheet("QPushButton{text-align:center;}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lang_1 = QtWidgets.QPushButton(self.frame)
        self.lang_1.setObjectName("lang_1")
        self.gridLayout_4.addWidget(self.lang_1, 0, 0, 1, 1)
        self.lang_2 = QtWidgets.QPushButton(self.frame)
        self.lang_2.setStyleSheet("")
        self.lang_2.setObjectName("lang_2")
        self.gridLayout_4.addWidget(self.lang_2, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.frame, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 5, 0, 1, 1)
        self.user_page_button = QtWidgets.QPushButton(self.groupBox)
        self.user_page_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.user_page_button.setObjectName("user_page_button")
        self.gridLayout_3.addWidget(self.user_page_button, 3, 0, 1, 1)
        self.main_page_button = QtWidgets.QPushButton(self.groupBox)
        self.main_page_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.main_page_button.setObjectName("main_page_button")
        self.gridLayout_3.addWidget(self.main_page_button, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 4)
        self.gridLayout_2.setRowStretch(0, 4)
        self.gridLayout_2.setRowStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Учет расхода и дохода"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Пользователи"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Логин"))
        self.deleteModal.setText(_translate("MainWindow", "Удалить"))
        self.editModal.setText(_translate("MainWindow", "Изменить"))
        self.createModal.setText(_translate("MainWindow", "Добавить"))
        self.groupBox.setTitle(_translate("MainWindow", "Меню"))
        self.logout_button.setText(_translate("MainWindow", "Выход"))
        self.lang_1.setText(_translate("MainWindow", "lang_1"))
        self.lang_2.setText(_translate("MainWindow", "lang_2"))
        self.user_page_button.setText(_translate("MainWindow", "Пользователи"))
        self.main_page_button.setText(_translate("MainWindow", "Главная"))
