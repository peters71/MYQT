# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\assets\UI\Layout\DB_Creator.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Creator(object):
    def setupUi(self, Creator):
        Creator.setObjectName("Creator")
        Creator.setWindowModality(QtCore.Qt.ApplicationModal)
        Creator.resize(508, 271)
        Creator.setMinimumSize(QtCore.QSize(508, 271))
        Creator.setMaximumSize(QtCore.QSize(508, 271))
        self.centralwidget = QtWidgets.QWidget(Creator)
        self.centralwidget.setObjectName("centralwidget")
        self.CreateDB_BOX = QtWidgets.QGroupBox(self.centralwidget)
        self.CreateDB_BOX.setGeometry(QtCore.QRect(10, 10, 240, 150))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.CreateDB_BOX.setFont(font)
        self.CreateDB_BOX.setObjectName("CreateDB_BOX")
        self.db_name = QtWidgets.QLineEdit(self.CreateDB_BOX)
        self.db_name.setGeometry(QtCore.QRect(10, 55, 220, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.db_name.setFont(font)
        self.db_name.setObjectName("db_name")
        self.createBtn = QtWidgets.QPushButton(self.CreateDB_BOX)
        self.createBtn.setGeometry(QtCore.QRect(10, 100, 220, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.createBtn.setFont(font)
        self.createBtn.setObjectName("createBtn")
        self.label = QtWidgets.QLabel(self.CreateDB_BOX)
        self.label.setGeometry(QtCore.QRect(10, 23, 220, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.DeleteDatabase = QtWidgets.QGroupBox(self.centralwidget)
        self.DeleteDatabase.setGeometry(QtCore.QRect(260, 10, 240, 250))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.DeleteDatabase.setFont(font)
        self.DeleteDatabase.setObjectName("DeleteDatabase")
        self.label_2 = QtWidgets.QLabel(self.DeleteDatabase)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 220, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.databases = QtWidgets.QListWidget(self.DeleteDatabase)
        self.databases.setGeometry(QtCore.QRect(10, 40, 220, 160))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.databases.setFont(font)
        self.databases.setObjectName("databases")
        self.deleteBtn = QtWidgets.QPushButton(self.DeleteDatabase)
        self.deleteBtn.setGeometry(QtCore.QRect(10, 210, 220, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.deleteBtn.setFont(font)
        self.deleteBtn.setObjectName("deleteBtn")
        self.ClearSelection_BOX = QtWidgets.QGroupBox(self.centralwidget)
        self.ClearSelection_BOX.setGeometry(QtCore.QRect(10, 180, 240, 80))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ClearSelection_BOX.setFont(font)
        self.ClearSelection_BOX.setObjectName("ClearSelection_BOX")
        self.clearBtn = QtWidgets.QPushButton(self.ClearSelection_BOX)
        self.clearBtn.setGeometry(QtCore.QRect(10, 30, 220, 34))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.clearBtn.setFont(font)
        self.clearBtn.setAutoDefault(False)
        self.clearBtn.setDefault(True)
        self.clearBtn.setObjectName("clearBtn")
        Creator.setCentralWidget(self.centralwidget)

        self.retranslateUi(Creator)
        self.clearBtn.clicked.connect(self.db_name.clear)
        QtCore.QMetaObject.connectSlotsByName(Creator)

    def retranslateUi(self, Creator):
        _translate = QtCore.QCoreApplication.translate
        Creator.setWindowTitle(_translate("Creator", "Create a Database"))
        self.CreateDB_BOX.setTitle(_translate("Creator", "Create a Database"))
        self.db_name.setPlaceholderText(_translate("Creator", "Enter DB Name:"))
        self.createBtn.setText(_translate("Creator", "Create Database"))
        self.label.setText(_translate("Creator", "Enter database name to create"))
        self.DeleteDatabase.setTitle(_translate("Creator", "Delete a Database"))
        self.label_2.setText(_translate("Creator", "Selected database to delete"))
        self.deleteBtn.setText(_translate("Creator", "DELETE"))
        self.ClearSelection_BOX.setTitle(_translate("Creator", "Clear entry section"))
        self.clearBtn.setText(_translate("Creator", "Clear entry selection"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Creator = QtWidgets.QMainWindow()
    ui = Ui_Creator()
    ui.setupUi(Creator)
    Creator.show()
    sys.exit(app.exec_())

