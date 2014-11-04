# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Hypothesis Now!.ui'
#
# Created: Fri Aug 29 17:45:11 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import numpy
import logicMain
import TTestOptions, ZTestOptions

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

logic = logicMain.logicMain()

class Ui_MainWindow(object):
    
    entries = []
    columns = []
    colTypes = numpy.zeros(1)
    
    ''' Qt Designer generated stuff.
        Do not modify except with Qt Designer-generated code.
    '''
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        self.MainWindow = MainWindow
        MainWindow.resize(487, 358)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.formGroupBox = QtGui.QGroupBox(self.centralwidget)
        self.formGroupBox.setGeometry(QtCore.QRect(0, 0, 221, 191))
        self.formGroupBox.setObjectName(_fromUtf8("formGroupBox"))
        self.formLayout = QtGui.QFormLayout(self.formGroupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.sampleTitle = QtGui.QLabel(self.formGroupBox)
        self.sampleTitle.setObjectName(_fromUtf8("sampleTitle"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.sampleTitle)
        self.filenameLabel = QtGui.QLabel(self.formGroupBox)
        self.filenameLabel.setObjectName(_fromUtf8("filenameLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.filenameLabel)
        self.column1Label = QtGui.QLabel(self.formGroupBox)
        self.column1Label.setObjectName(_fromUtf8("column1Label"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.column1Label)
        self.column1Combo = QtGui.QComboBox(self.formGroupBox)
        self.column1Combo.setObjectName(_fromUtf8("column1Combo"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.column1Combo)
        self.column2Label = QtGui.QLabel(self.formGroupBox)
        self.column2Label.setObjectName(_fromUtf8("column2Label"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.column2Label)
        self.column2Combo = QtGui.QComboBox(self.formGroupBox)
        self.column2Combo.setObjectName(_fromUtf8("column2Combo"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.column2Combo)
        self.filenameDisplay = QtGui.QLabel(self.formGroupBox)
        self.filenameDisplay.setObjectName(_fromUtf8("filenameDisplay"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.filenameDisplay)
        self.Datatype1 = QtGui.QLabel(self.formGroupBox)
        self.Datatype1.setObjectName(_fromUtf8("Datatype1"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.Datatype1)
        self.Datatype1Label = QtGui.QLabel(self.formGroupBox)
        self.Datatype1Label.setObjectName(_fromUtf8("Datatype1Label"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.Datatype1Label)
        self.Datatype2 = QtGui.QLabel(self.formGroupBox)
        self.Datatype2.setObjectName(_fromUtf8("Datatype2"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.Datatype2)
        self.Datatype2Label = QtGui.QLabel(self.formGroupBox)
        self.Datatype2Label.setObjectName(_fromUtf8("Datatype2Label"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.Datatype2Label)
        self.groupingsButton = QtGui.QPushButton(self.formGroupBox)
        self.groupingsButton.setObjectName(_fromUtf8("groupingsButton"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.SpanningRole, self.groupingsButton)
        self.verticalGroupBox = QtGui.QGroupBox(self.centralwidget)
        self.verticalGroupBox.setGeometry(QtCore.QRect(-1, 189, 221, 121))
        self.verticalGroupBox.setObjectName(_fromUtf8("verticalGroupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.TestTitle = QtGui.QLabel(self.verticalGroupBox)
        self.TestTitle.setMaximumSize(QtCore.QSize(16777215, 16))
        self.TestTitle.setObjectName(_fromUtf8("TestTitle"))
        self.verticalLayout_2.addWidget(self.TestTitle)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.testNameLabel = QtGui.QLabel(self.verticalGroupBox)
        self.testNameLabel.setObjectName(_fromUtf8("testNameLabel"))
        self.horizontalLayout.addWidget(self.testNameLabel)
        self.testCombo = QtGui.QComboBox(self.verticalGroupBox)
        self.testCombo.setObjectName(_fromUtf8("testCombo"))
        self.testCombo.addItem(_fromUtf8(""))
        self.testCombo.addItem(_fromUtf8(""))
        self.testCombo.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.testCombo)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.testDetailsButton = QtGui.QPushButton(self.verticalGroupBox)
        self.testDetailsButton.setObjectName(_fromUtf8("testDetailsButton"))
        self.verticalLayout.addWidget(self.testDetailsButton)
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(229, -1, 251, 311))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.resultsTitle = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.resultsTitle.setObjectName(_fromUtf8("resultsTitle"))
        self.verticalLayout_4.addWidget(self.resultsTitle)
        self.textBrowser = QtGui.QTextBrowser(self.verticalLayoutWidget_3)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout_4.addWidget(self.textBrowser)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.confidenceLabel = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.confidenceLabel.setObjectName(_fromUtf8("confidenceLabel"))
        self.horizontalLayout_2.addWidget(self.confidenceLabel)
        self.confidenceLevel = QtGui.QLineEdit(self.verticalLayoutWidget_3)
        self.confidenceLevel.setText(_fromUtf8(""))
        self.confidenceLevel.setReadOnly(True)
        self.confidenceLevel.setObjectName(_fromUtf8("confidenceLevel"))
        self.horizontalLayout_2.addWidget(self.confidenceLevel)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.testNowButton = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.testNowButton.setObjectName(_fromUtf8("testNowButton"))
        self.verticalLayout_4.addWidget(self.testNowButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 487, 22))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuCredits = QtGui.QMenu(self.menuBar)
        self.menuCredits.setObjectName(_fromUtf8("menuCredits"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionFile = QtGui.QAction(MainWindow)
        self.actionFile.setObjectName(_fromUtf8("actionFile"))
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionClose_Program = QtGui.QAction(MainWindow)
        self.actionClose_Program.setObjectName(_fromUtf8("actionClose_Program"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose_Program)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuCredits.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.setSignals(MainWindow)
        self.setShortcuts()
        self.setupChildWindows(MainWindow)
        self.setupLogic()
        
    def setupChildWindows(self,MainWindow):
        self.TTestOptionsWindow = TTestOptions.TTestOptionsWindow(self)
        self.ZTestOptionsWindow = ZTestOptions.ZTestOptionsWindow(self)

    def setShortcuts(self):
        self.actionOpen.setShortcut('O')

    def setSignals(self, MainWindow):
        self.testDetailsButton.clicked.connect(self.openTestDetails)
        self.actionClose_Program.triggered.connect(QtGui.qApp.quit)
        self.actionOpen.triggered.connect(self.openFileOperation)
        self.testNowButton.clicked.connect(self.commenceTest)
        self.testCombo.currentIndexChanged.connect(self.testChanged)
    
    def setupLogic(self):
        logic.setZTestParams(0,0,0)
    
    def testChanged(self):
        if self.testCombo.currentIndex() == 0:
            self.column2Combo.setDisabled(True)
        elif self.testCombo.currentIndex() == 1:
            self.column2Combo.setEnabled(True)
        elif self.testCombo.currentIndex() == 2:
            self.column2Combo.setEnabled(True)

    def openTestDetails(self):
        if self.testCombo.currentIndex() == 0:
            mean, var, eRange = logic.getZTestParams()
            self.ZTestOptionsWindow.setParams(mean, var, eRange)
            if self.ZTestOptionsWindow.exec_():
                mean, var, eRange = self.ZTestOptionsWindow.getParams()
                logic.setZTestParams(mean, var, eRange)
        elif self.testCombo.currentIndex() == 1:
            self.TTestOptionsWindow.exec_()

    def openFileOperation(self):
        # Open the file first.
        fName = self.openFileDialog()
        if '.csv' in str(fName):
            # logicMain will sort out the sample data, and find the types of data in each column.
            # More on this function in logicMain.setSampleData.
            self.columns, self.entries, self.colTypes = logic.setSampleData(fName)
            # Display the new filename.
            self.filenameDisplay.setText(fName.__str__().split("/\\").pop())
            # Clear the old file's combo selection.
            self.column1Combo.clear()
            self.column2Combo.clear()
            # And input the new file's combo selection.
            for i in range (len(self.columns)):
                self.column1Combo.insertItem(i, self.columns[i], None)
                self.column2Combo.insertItem(i, self.columns[i], None)
            # We consider the test to have changed after loading a new sample file.
            self.testChanged()
        # If the file is not of .csv form, display a warning.
        else:
            QtGui.QMessageBox.warning(self.MainWindow, 'Warning', 'File not of CSV form.', buttons = QtGui.QMessageBox.Ok, defaultButton = QtGui.QMessageBox.Ok)


    def openFileDialog(self):
        fName = QtGui.QFileDialog.getOpenFileName(self.MainWindow, 'Open file', '/home')
        return fName

#Test commencement. Triggers upon clicking "Test Now!" Button.
    def commenceTest(self):
# If the entries have not been initialized yet (No Sample File given), this will trigger, and no testing will be done.
        if not self.entries:
            QtGui.QMessageBox.warning(self.MainWindow, 'Warning', 'No sample data.', buttons = QtGui.QMessageBox.Ok, defaultButton = QtGui.QMessageBox.Ok)
# Else if we have data, we can start the test.
        else:
            if self.testCombo.currentIndex() == 0:
# Note:  The test print is generated alongside the testing process. Think of the test print as debug data.
#        When programming the tests, try to account for this.
                testPrint, confidencePercent = logic.performZTest(self.entries, self.column1Combo.currentIndex())
            self.confidenceLevel.setText(str(confidencePercent*100.) + '%')
            self.textBrowser.setText(testPrint)
    
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Hypothesis Now!", None))
        self.sampleTitle.setText(_translate("MainWindow", "Sample Data", None))
        self.filenameLabel.setText(_translate("MainWindow", "Filename", None))
        self.column1Label.setText(_translate("MainWindow", "Column 1", None))
        self.column2Label.setText(_translate("MainWindow", "Column 2", None))
        self.filenameDisplay.setText(_translate("MainWindow", "____________", None))
        self.Datatype1.setText(_translate("MainWindow", "Datatype", None))
        self.Datatype1Label.setText(_translate("MainWindow", "Numeric", None))
        self.Datatype2.setText(_translate("MainWindow", "Datatype", None))
        self.Datatype2Label.setText(_translate("MainWindow", "Numeric", None))
        self.groupingsButton.setText(_translate("MainWindow", "Groupings", None))
        self.TestTitle.setText(_translate("MainWindow", "Test Information", None))
        self.testNameLabel.setText(_translate("MainWindow", "Test Name", None))
        self.testCombo.setItemText(0, _translate("MainWindow", "Z-Test", None))
        self.testCombo.setItemText(1, _translate("MainWindow", "Student\'s T-Test", None))
        self.testCombo.setItemText(2, _translate("MainWindow", "Chi-Squared Test", None))
        self.testDetailsButton.setText(_translate("MainWindow", "Test Details", None))
        self.resultsTitle.setText(_translate("MainWindow", "Test Results", None))
        self.confidenceLabel.setText(_translate("MainWindow", "Confidence Level", None))
        self.testNowButton.setText(_translate("MainWindow", "Test Now!", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuCredits.setTitle(_translate("MainWindow", "Credits", None))
        self.actionFile.setText(_translate("MainWindow", "File", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionClose_Program.setText(_translate("MainWindow", "Close Program", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = QtGui.QMainWindow()
    main = Ui_MainWindow()
    main.setupUi(ui)
    ui.show()
    sys.exit(app.exec_())

