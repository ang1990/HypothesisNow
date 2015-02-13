# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainV3.ui'
#
# Created: Mon Sep 29 15:49:58 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import StatementBuilder as SB
import Typedef
import logicMain
import os
from operator import attrgetter

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

class mainUI(object):
    
    low = 0.6
    average = 0.8
    high = 0.95
    
    def __init__(self): 
        self.dataManager = None
        self.logic = logicMain.logicMain()
        self.fileLoaded = False
        self.statement = None
        
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(787, 504)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.topLabel = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topLabel.sizePolicy().hasHeightForWidth())
        self.topLabel.setSizePolicy(sizePolicy)
        self.topLabel.setTextFormat(QtCore.Qt.RichText)
        self.topLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.topLabel.setWordWrap(False)
        self.topLabel.setObjectName(_fromUtf8("topLabel"))
        self.verticalLayout.addWidget(self.topLabel)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.filenameLabel = QtGui.QLabel(self.centralwidget)
        self.filenameLabel.setObjectName(_fromUtf8("filenameLabel"))
        self.horizontalLayout.addWidget(self.filenameLabel)
        self.filenameDisplay = QtGui.QLabel(self.centralwidget)
        self.filenameDisplay.setObjectName(_fromUtf8("filenameDisplay"))
        self.horizontalLayout.addWidget(self.filenameDisplay)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.selectFileButton = QtGui.QToolButton(self.centralwidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Resources/Open-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.selectFileButton.setIcon(icon)
        self.selectFileButton.setObjectName(_fromUtf8("selectFileButton"))
        self.horizontalLayout.addWidget(self.selectFileButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.inquiryTopLabel = QtGui.QLabel(self.centralwidget)
        self.inquiryTopLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.inquiryTopLabel.setObjectName(_fromUtf8("inquiryTopLabel"))
        self.verticalLayout.addWidget(self.inquiryTopLabel)
        self.statementBuilderButton = QtGui.QPushButton(self.centralwidget)
        self.statementBuilderButton.setObjectName(_fromUtf8("statementBuilderButton"))
        self.verticalLayout.addWidget(self.statementBuilderButton)
        self.expressionLabel = QtGui.QLabel(self.centralwidget)
        self.expressionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.expressionLabel.setObjectName(_fromUtf8("expressionLabel"))
        self.verticalLayout.addWidget(self.expressionLabel)
        self.expressionDisplay = QtGui.QTextBrowser(self.centralwidget)
        self.expressionDisplay.setObjectName(_fromUtf8("expressionDisplay"))
        self.verticalLayout.addWidget(self.expressionDisplay)
        self.additionalOptionsTitle = QtGui.QLabel(self.centralwidget)
        self.additionalOptionsTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.additionalOptionsTitle.setObjectName(_fromUtf8("additionalOptionsTitle"))
        self.verticalLayout.addWidget(self.additionalOptionsTitle)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.outlierCheck = QtGui.QCheckBox(self.centralwidget)
        self.outlierCheck.setObjectName(_fromUtf8("outlierCheck"))
        self.verticalLayout.addWidget(self.outlierCheck)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.minSampleSliderLabel = QtGui.QLabel(self.centralwidget)
        self.minSampleSliderLabel.setObjectName(_fromUtf8("minSampleSliderLabel"))
        self.horizontalLayout_9.addWidget(self.minSampleSliderLabel)
        self.minSampleSizeDisp = QtGui.QLabel(self.centralwidget)
        self.minSampleSizeDisp.setObjectName(_fromUtf8("minSampleSizeDisp"))
        self.horizontalLayout_9.addWidget(self.minSampleSizeDisp)
        self.minSampleSizeSlider = QtGui.QSlider(self.centralwidget)
        self.minSampleSizeSlider.setMinimum(1)
        self.minSampleSizeSlider.setMaximum(25)
        self.minSampleSizeSlider.setProperty("value", 5)
        self.minSampleSizeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.minSampleSizeSlider.setObjectName(_fromUtf8("minSampleSizeSlider"))
        self.horizontalLayout_9.addWidget(self.minSampleSizeSlider)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.validityLabel = QtGui.QLabel(self.centralwidget)
        self.validityLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.validityLabel.setObjectName(_fromUtf8("validityLabel"))
        self.verticalLayout.addWidget(self.validityLabel)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.validityDisplay = QtGui.QTextBrowser(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.validityDisplay.sizePolicy().hasHeightForWidth())
        self.validityDisplay.setSizePolicy(sizePolicy)
        self.validityDisplay.setMaximumSize(QtCore.QSize(16777215, 64))
        self.validityDisplay.setObjectName(_fromUtf8("validityDisplay"))
        self.horizontalLayout_4.addWidget(self.validityDisplay)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.resultsTopLabel = QtGui.QLabel(self.centralwidget)
        self.resultsTopLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.resultsTopLabel.setObjectName(_fromUtf8("resultsTopLabel"))
        self.verticalLayout_2.addWidget(self.resultsTopLabel)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.first = QtGui.QWidget()
        self.first.setObjectName(_fromUtf8("first"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.first)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.resultsDisplay1 = QtGui.QTextBrowser(self.first)
        font = QtGui.QFont()
        font.setPointSize(7.5)
        self.resultsDisplay1.setFont(font)
        self.resultsDisplay1.setObjectName(_fromUtf8("resultsDisplay1"))
        self.horizontalLayout_3.addWidget(self.resultsDisplay1)
        self.tabWidget.addTab(self.first, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.tab_2)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.resultsDisplay2 = QtGui.QTextBrowser(self.tab_2)
        self.resultsDisplay2.setObjectName(_fromUtf8("resultsDisplay2"))
        self.horizontalLayout_6.addWidget(self.resultsDisplay2)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.tab_3)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.resultsDisplay3 = QtGui.QTextBrowser(self.tab_3)
        self.resultsDisplay3.setObjectName(_fromUtf8("resultsDisplay3"))
        self.horizontalLayout_7.addWidget(self.resultsDisplay3)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.tab_4)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.resultsDisplayOutlying = QtGui.QTextBrowser(self.tab_4)
        self.resultsDisplayOutlying.setObjectName(_fromUtf8("resultsDisplayOutlying"))
        self.horizontalLayout_8.addWidget(self.resultsDisplayOutlying)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.confidenceLabel = QtGui.QLabel(self.centralwidget)
        self.confidenceLabel.setObjectName(_fromUtf8("confidenceLabel"))
        self.horizontalLayout_5.addWidget(self.confidenceLabel)
        self.confidenceDisplay = QtGui.QLabel(self.centralwidget)
        self.confidenceDisplay.setObjectName(_fromUtf8("confidenceDisplay"))
        self.horizontalLayout_5.addWidget(self.confidenceDisplay)
        self.testNowButton = QtGui.QPushButton(self.centralwidget)
        self.testNowButton.setObjectName(_fromUtf8("testNowButton"))
        self.horizontalLayout_5.addWidget(self.testNowButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 787, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuCredits = QtGui.QMenu(self.menubar)
        self.menuCredits.setObjectName(_fromUtf8("menuCredits"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_open = QtGui.QAction(MainWindow)
        self.action_open.setObjectName(_fromUtf8("action_open"))
        self.actionClose_Program = QtGui.QAction(MainWindow)
        self.actionClose_Program.setObjectName(_fromUtf8("actionClose_Program"))
        self.actionData_Explorer = QtGui.QAction(MainWindow)
        self.actionData_Explorer.setObjectName(_fromUtf8("actionData_Explorer"))
        self.menuFile.addAction(self.action_open)
        self.menuFile.addAction(self.actionData_Explorer)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose_Program)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuCredits.menuAction())
        self.toolBar.addAction(self.action_open)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionData_Explorer)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)

        QtCore.QObject.connect(self.minSampleSizeSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.minSampleSizeDisp.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.setSignals()
        self.setShortcuts()

    def setSignals(self):
        self.statementBuilderButton.clicked.connect(self.callSB)
        self.actionClose_Program.triggered.connect(QtGui.qApp.quit)
        self.action_open.triggered.connect(self.openFileOperation)
        self.testNowButton.clicked.connect(self.commenceTest)
        self.selectFileButton.clicked.connect(self.openFileOperation)
        self.outlierCheck.clicked.connect(self.toggleOutlierCheck)
        self.minSampleSizeSlider.valueChanged.connect(self.changeMinSizeVal)
        
    def changeMinSizeVal(self):
        self.logic.setMinSampleLength(self.minSampleSizeSlider.value())

    def toggleOutlierCheck(self):
        self.logic.setRemoveOutliers(self.outlierCheck.isChecked())
        print(self.logic.getRemoveOutliers())

# Call Statement Builder.
# A Statement class representing the test is generated.
# When SB closes successfully, it creates said class which is passed over to logic, which then unpacks it
# according to the test contained within. main will take the English-language statement from stmt
# and display it.

    def callSB(self):
        if self.fileLoaded:
            groups, stmt = SB.callBuilder(self.dataManager, self.statement)
            if groups:
                self.dataManager.groups = groups
            if stmt is not None:
                self.statement = stmt
            if self.statement is not None:
                self.logic.setStmt(self.statement)
                self.setExpDisplays()
            else:
                self.resetExpDisplays()
        else:
            QtGui.QMessageBox.warning(self.MainWindow, 'Warning', 'Please load a file before opening hypothesis menu.', buttons = QtGui.QMessageBox.Ok, defaultButton = QtGui.QMessageBox.Ok)

    def setExpDisplays(self):
        self.expressionDisplay.setText(self.statement.getStmtPrint())
        self.validityDisplay.setText(self.logic.getValidationPrint())

    def resetExpDisplays(self):
        self.expressionDisplay.clear()
        self.expressionDisplay.setPlainText(Typedef.noHypDisplay)
        self.validityDisplay.clear()
        self.validityDisplay.setPlainText('-')
    
    def setShortcuts(self):
        self.action_open.setShortcut('O')
        

# At this point, we cannot assume that the groupings are updated. Logic may be out of sync with main.
# We have to force an update of all the groups.
    def commenceTest(self):
        self.logic.updateDataManager(self.dataManager)
        if self.statement:
            resultPrints = self.logic.performTest()
        # The first box is for the overall test results.
            firstPrint = resultPrints[0]
            self.resultsDisplay1.setText(firstPrint.getResultPrint())
            self.confidenceDisplay.setText(self.getConfidencePrint(firstPrint.getPValue()))
            sortDescending = firstPrint.getPValue() > 0.5
            resultPrints = sorted(resultPrints, key = lambda result: result.getPValue(), reverse = sortDescending)
            print('Number of tests: ' + str(len(resultPrints)))
            if len(resultPrints) > 1:
                self.resultsDisplay2.setText(resultPrints[0].getResultPrint())
                self.resultsDisplay3.setText(resultPrints[1].getResultPrint())
                self.resultsDisplayOutlying.setText(resultPrints[-1].getResultPrint())
            else:
                self.resultsDisplay2.setText('Not enough tests performed.')
                self.resultsDisplay3.setText('Not enough tests performed.')
                self.resultsDisplayOutlying.setText('Not enough tests performed.')
        else:
            QtGui.QMessageBox.warning(self.MainWindow, 'Warning', 'No expression entered.', buttons = QtGui.QMessageBox.Ok, defaultButton = QtGui.QMessageBox.Ok)

    def getConfidencePrint(self, confidence):
        if confidence <= Typedef.emptySampleErrorValue:
            return 'N/A'
        elif confidence < 0.01:
            return ' Very low (<1%)'
        elif confidence < self.low:
            return 'Low (' + str(confidence*100) + '%)'
        elif confidence < self.average:
            return 'Medium (' + str(confidence*100) + '%)'
        elif confidence < self.high:
            return 'High (' + str(confidence*100) + '%)'
        elif confidence > 0.99:
            return 'Very high (> 99%)'
        else:
            return str(confidence*100) + '%'

    def openFileOperation(self):
        # Open the file first.
        fName = self.openFileDialog()
        if '.csv' in str(fName):
            # logicMain will sort out the sample data, and find the types of data in each column.
            # More on this function in logicMain.setSampleData.
            self.logic.setSampleData(fName)
            self.dataManager = self.logic.getDataManager()
            print(self.dataManager.columnNames)
            # Display the new filename.
            self.filenameDisplay.setText(str(fName).split("/").pop())         
            # We set fileLoaded to be true now.
            self.fileLoaded = True
        # If filename is empty, do nothing.
        elif fName == '':
            return
        # If the file is not of .csv form, display a warning.
        else:
            QtGui.QMessageBox.warning(self.MainWindow, 'Warning', 'File not of CSV form.', buttons = QtGui.QMessageBox.Ok, defaultButton = QtGui.QMessageBox.Ok)

    def openFileDialog(self):
        fName = QtGui.QFileDialog.getOpenFileName(self.MainWindow, 'Open file', os.getcwd())
        return fName

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Hypothesis Now! A Stats Test Application", None))
        self.topLabel.setText(_translate("MainWindow", "Hypothesis Now!", None))
        self.filenameLabel.setText(_translate("MainWindow", "Data File:", None))
        self.filenameDisplay.setText(_translate("MainWindow", "No Data yet.", None))
        self.selectFileButton.setText(_translate("MainWindow", "...", None))
        self.inquiryTopLabel.setText(_translate("MainWindow", "What would you like to compare?", None))
        self.statementBuilderButton.setText(_translate("MainWindow", "Click to change test expression", None))
        self.expressionLabel.setText(_translate("MainWindow", "Expression", None))
        self.additionalOptionsTitle.setText(_translate("MainWindow", "Additional Options", None))
        self.outlierCheck.setText(_translate("MainWindow", "Remove Outlying Data Points", None))
        self.minSampleSliderLabel.setText(_translate("MainWindow", "Minimum sample size", None))
        self.minSampleSizeDisp.setText(_translate("MainWindow", "5", None))
        self.validityLabel.setText(_translate("MainWindow", "Expression Validity", None))
        self.resultsTopLabel.setText(_translate("MainWindow", "Test Results", None))
        self.resultsDisplay1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.5pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">No Test Performed.</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.first), _translate("MainWindow", "Overall", None))
        self.resultsDisplay2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.5pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">No Test Performed.</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Best", None))
        self.resultsDisplay3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.5pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">No Test Performed.</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "2nd", None))
        self.resultsDisplayOutlying.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.5pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">No Test Performed.</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Unexpected / Outlying", None))
        self.confidenceLabel.setText(_translate("MainWindow", "Statement Accuracy:", None))
        self.confidenceDisplay.setText(_translate("MainWindow", "N/A", None))
        self.testNowButton.setText(_translate("MainWindow", "Test Now!", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuCredits.setTitle(_translate("MainWindow", "Credits", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.action_open.setText(_translate("MainWindow", "Open Sample File...", None))
        self.actionClose_Program.setText(_translate("MainWindow", "Close Program", None))
        self.actionData_Explorer.setText(_translate("MainWindow", "Data Explorer", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = mainUI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

