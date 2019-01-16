# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Lib\UI\LAYOUT\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SQLMANAGER(object):
    def setupUi(self, SQLMANAGER):
        SQLMANAGER.setObjectName("SQLMANAGER")
        SQLMANAGER.setWindowModality(QtCore.Qt.ApplicationModal)
        SQLMANAGER.resize(1085, 758)
        SQLMANAGER.setAutoFillBackground(False)
        SQLMANAGER.setWindowFilePath("")
        SQLMANAGER.setInputMethodHints(QtCore.Qt.ImhNone)
        SQLMANAGER.setIconSize(QtCore.QSize(24, 24))
        SQLMANAGER.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        SQLMANAGER.setAnimated(True)
        SQLMANAGER.setDocumentMode(False)
        SQLMANAGER.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(SQLMANAGER)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(280, 0, 760, 570))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self._desc = QtWidgets.QWidget()
        self._desc.setObjectName("_desc")
        self.desc_result = QtWidgets.QTableWidget(self._desc)
        self.desc_result.setGeometry(QtCore.QRect(0, 0, 760, 540))
        self.desc_result.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.desc_result.setFrameShadow(QtWidgets.QFrame.Plain)
        self.desc_result.setLineWidth(1)
        self.desc_result.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.desc_result.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.desc_result.setTabKeyNavigation(False)
        self.desc_result.setProperty("showDropIndicator", False)
        self.desc_result.setDragDropOverwriteMode(False)
        self.desc_result.setAlternatingRowColors(True)
        self.desc_result.setShowGrid(True)
        self.desc_result.setGridStyle(QtCore.Qt.SolidLine)
        self.desc_result.setWordWrap(True)
        self.desc_result.setCornerButtonEnabled(True)
        self.desc_result.setRowCount(0)
        self.desc_result.setColumnCount(0)
        self.desc_result.setObjectName("desc_result")
        self.tabWidget.addTab(self._desc, "")
        self._data = QtWidgets.QWidget()
        self._data.setObjectName("_data")
        self.data_result = QtWidgets.QTableWidget(self._data)
        self.data_result.setGeometry(QtCore.QRect(0, 0, 760, 540))
        self.data_result.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.data_result.setFrameShadow(QtWidgets.QFrame.Plain)
        self.data_result.setLineWidth(1)
        self.data_result.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.data_result.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.data_result.setTabKeyNavigation(False)
        self.data_result.setProperty("showDropIndicator", False)
        self.data_result.setDragDropOverwriteMode(False)
        self.data_result.setAlternatingRowColors(True)
        self.data_result.setShowGrid(True)
        self.data_result.setGridStyle(QtCore.Qt.SolidLine)
        self.data_result.setWordWrap(True)
        self.data_result.setCornerButtonEnabled(True)
        self.data_result.setRowCount(0)
        self.data_result.setColumnCount(0)
        self.data_result.setObjectName("data_result")
        self.tabWidget.addTab(self._data, "")
        self._query = QtWidgets.QWidget()
        self._query.setObjectName("_query")
        self.result_out = QtWidgets.QTableWidget(self._query)
        self.result_out.setGeometry(QtCore.QRect(0, 262, 756, 278))
        self.result_out.setFrameShape(QtWidgets.QFrame.Box)
        self.result_out.setFrameShadow(QtWidgets.QFrame.Plain)
        self.result_out.setLineWidth(1)
        self.result_out.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.result_out.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.result_out.setTabKeyNavigation(False)
        self.result_out.setProperty("showDropIndicator", False)
        self.result_out.setDragDropOverwriteMode(False)
        self.result_out.setAlternatingRowColors(True)
        self.result_out.setShowGrid(True)
        self.result_out.setGridStyle(QtCore.Qt.SolidLine)
        self.result_out.setWordWrap(True)
        self.result_out.setCornerButtonEnabled(False)
        self.result_out.setRowCount(0)
        self.result_out.setObjectName("result_out")
        self.result_out.setColumnCount(0)
        self.query_in = QtWidgets.QPlainTextEdit(self._query)
        self.query_in.setGeometry(QtCore.QRect(0, 0, 756, 260))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.query_in.setFont(font)
        self.query_in.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.query_in.setAutoFillBackground(False)
        self.query_in.setStyleSheet("border: 1 solid lightgray;")
        self.query_in.setInputMethodHints(QtCore.Qt.ImhDate|QtCore.Qt.ImhDialableCharactersOnly|QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhEmailCharactersOnly|QtCore.Qt.ImhExclusiveInputMask|QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhLatinOnly|QtCore.Qt.ImhLowercaseOnly|QtCore.Qt.ImhMultiLine|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoEditMenu|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhNoTextHandles|QtCore.Qt.ImhPreferLatin|QtCore.Qt.ImhPreferLowercase|QtCore.Qt.ImhPreferNumbers|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhSensitiveData|QtCore.Qt.ImhTime|QtCore.Qt.ImhUppercaseOnly|QtCore.Qt.ImhUrlCharactersOnly)
        self.query_in.setFrameShape(QtWidgets.QFrame.Box)
        self.query_in.setFrameShadow(QtWidgets.QFrame.Plain)
        self.query_in.setLineWidth(1)
        self.query_in.setMidLineWidth(0)
        self.query_in.setPlainText("select * from ")
        self.query_in.setObjectName("query_in")
        self.tabWidget.addTab(self._query, "")
        self.console_out = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.console_out.setGeometry(QtCore.QRect(280, 580, 760, 170))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.console_out.setFont(font)
        self.console_out.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.console_out.setFrameShadow(QtWidgets.QFrame.Plain)
        self.console_out.setLineWidth(1)
        self.console_out.setMidLineWidth(0)
        self.console_out.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.console_out.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.console_out.setUndoRedoEnabled(False)
        self.console_out.setReadOnly(True)
        self.console_out.setPlainText("")
        self.console_out.setBackgroundVisible(False)
        self.console_out.setCenterOnScroll(False)
        self.console_out.setObjectName("console_out")
        self.tables_out = QtWidgets.QTreeWidget(self.centralwidget)
        self.tables_out.setGeometry(QtCore.QRect(10, 10, 260, 700))
        self.tables_out.setAutoFillBackground(False)
        self.tables_out.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tables_out.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tables_out.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tables_out.setObjectName("tables_out")
        self.tables_out.headerItem().setTextAlignment(0, QtCore.Qt.AlignCenter)
        self.createdb_btn = QtWidgets.QPushButton(self.centralwidget)
        self.createdb_btn.setGeometry(QtCore.QRect(190, 710, 78, 40))
        self.createdb_btn.setObjectName("createdb_btn")
        self.createdb_in = QtWidgets.QLineEdit(self.centralwidget)
        self.createdb_in.setGeometry(QtCore.QRect(10, 710, 180, 40))
        self.createdb_in.setObjectName("createdb_in")
        SQLMANAGER.setCentralWidget(self.centralwidget)
        self.actionImport_Query = QtWidgets.QAction(SQLMANAGER)
        self.actionImport_Query.setShortcutContext(QtCore.Qt.WidgetWithChildrenShortcut)
        self.actionImport_Query.setObjectName("actionImport_Query")
        self.actionExport_Query = QtWidgets.QAction(SQLMANAGER)
        self.actionExport_Query.setObjectName("actionExport_Query")
        self.actionCompile = QtWidgets.QAction(SQLMANAGER)
        self.actionCompile.setObjectName("actionCompile")
        self.actionExecute_Selected = QtWidgets.QAction(SQLMANAGER)
        self.actionExecute_Selected.setObjectName("actionExecute_Selected")
        self.actionAbout = QtWidgets.QAction(SQLMANAGER)
        self.actionAbout.setObjectName("actionAbout")
        self.actionDocuments = QtWidgets.QAction(SQLMANAGER)
        self.actionDocuments.setObjectName("actionDocuments")
        self.actionCopy = QtWidgets.QAction(SQLMANAGER)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(SQLMANAGER)
        self.actionPaste.setObjectName("actionPaste")
        self.actionCrop = QtWidgets.QAction(SQLMANAGER)
        self.actionCrop.setObjectName("actionCrop")
        self.actionSelect_All = QtWidgets.QAction(SQLMANAGER)
        self.actionSelect_All.setObjectName("actionSelect_All")
        self.actionInvert_Selection = QtWidgets.QAction(SQLMANAGER)
        self.actionInvert_Selection.setObjectName("actionInvert_Selection")
        self.actionExit = QtWidgets.QAction(SQLMANAGER)
        self.actionExit.setObjectName("actionExit")
        self.actionRefresh_Database = QtWidgets.QAction(SQLMANAGER)
        self.actionRefresh_Database.setObjectName("actionRefresh_Database")

        self.retranslateUi(SQLMANAGER)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SQLMANAGER)
        SQLMANAGER.setTabOrder(self.tabWidget, self.data_result)
        SQLMANAGER.setTabOrder(self.data_result, self.console_out)
        SQLMANAGER.setTabOrder(self.console_out, self.desc_result)
        SQLMANAGER.setTabOrder(self.desc_result, self.result_out)
        SQLMANAGER.setTabOrder(self.result_out, self.query_in)

    def retranslateUi(self, SQLMANAGER):
        _translate = QtCore.QCoreApplication.translate
        SQLMANAGER.setWindowTitle(_translate("SQLMANAGER", "SQL MANAGER"))
        self.desc_result.setToolTip(_translate("SQLMANAGER", "<html><head/><body><p><span style=\" font-weight:600;\">DATA DESCRIPTIONS</span></p></body></html>"))
        self.desc_result.setSortingEnabled(False)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self._desc), _translate("SQLMANAGER", "Table"))
        self.data_result.setToolTip(_translate("SQLMANAGER", "<html><head/><body><p><span style=\" font-weight:600;\">ALL DATA IN TABLE</span></p></body></html>"))
        self.data_result.setSortingEnabled(False)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self._data), _translate("SQLMANAGER", "Data"))
        self.result_out.setToolTip(_translate("SQLMANAGER", "<html><head/><body><p><span style=\" font-weight:600;\">RESULTS</span></p></body></html>"))
        self.result_out.setSortingEnabled(False)
        self.query_in.setToolTip(_translate("SQLMANAGER", "<html><head/><body><p><span style=\" font-weight:600;\">NEW CONSULT</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self._query), _translate("SQLMANAGER", "Query"))
        self.console_out.setToolTip(_translate("SQLMANAGER", "<html><head/><body><p><span style=\" font-weight:600;\">CONSOLE</span></p></body></html>"))
        self.console_out.setPlaceholderText(_translate("SQLMANAGER", "CONSOLE"))
        self.tables_out.setToolTip(_translate("SQLMANAGER", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">DATABASES AND TABLES</span></p></body></html>"))
        self.tables_out.headerItem().setText(0, _translate("SQLMANAGER", "DATABASES"))
        self.createdb_btn.setText(_translate("SQLMANAGER", "CREATE"))
        self.createdb_in.setPlaceholderText(_translate("SQLMANAGER", "Create Database:"))
        self.actionImport_Query.setText(_translate("SQLMANAGER", "Load SQL File"))
        self.actionImport_Query.setShortcut(_translate("SQLMANAGER", "Ctrl+W"))
        self.actionExport_Query.setText(_translate("SQLMANAGER", "Execute SQL File"))
        self.actionExport_Query.setShortcut(_translate("SQLMANAGER", "Ctrl+E"))
        self.actionCompile.setText(_translate("SQLMANAGER", "Execute Query"))
        self.actionCompile.setShortcut(_translate("SQLMANAGER", "Ctrl+Return"))
        self.actionExecute_Selected.setText(_translate("SQLMANAGER", "Execute Selected"))
        self.actionExecute_Selected.setShortcut(_translate("SQLMANAGER", "Ctrl+Shift+Return"))
        self.actionAbout.setText(_translate("SQLMANAGER", "About"))
        self.actionDocuments.setText(_translate("SQLMANAGER", "Documents"))
        self.actionCopy.setText(_translate("SQLMANAGER", "Copy"))
        self.actionCopy.setShortcut(_translate("SQLMANAGER", "Ctrl+C"))
        self.actionPaste.setText(_translate("SQLMANAGER", "Paste"))
        self.actionPaste.setShortcut(_translate("SQLMANAGER", "Ctrl+V"))
        self.actionCrop.setText(_translate("SQLMANAGER", "Crop"))
        self.actionCrop.setShortcut(_translate("SQLMANAGER", "Ctrl+X"))
        self.actionSelect_All.setText(_translate("SQLMANAGER", "Select All"))
        self.actionSelect_All.setShortcut(_translate("SQLMANAGER", "Ctrl+A"))
        self.actionInvert_Selection.setText(_translate("SQLMANAGER", "Invert Selection"))
        self.actionInvert_Selection.setShortcut(_translate("SQLMANAGER", "Ctrl+Shift+A"))
        self.actionExit.setText(_translate("SQLMANAGER", "Exit"))
        self.actionRefresh_Database.setText(_translate("SQLMANAGER", "Refresh Database"))
        self.actionRefresh_Database.setShortcut(_translate("SQLMANAGER", "Ctrl+R"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SQLMANAGER = QtWidgets.QMainWindow()
    ui = Ui_SQLMANAGER()
    ui.setupUi(SQLMANAGER)
    SQLMANAGER.show()
    sys.exit(app.exec_())

