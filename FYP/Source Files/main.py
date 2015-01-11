# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainV3.ui'
#
# Created: Mon Sep 29 15:49:58 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import StatementBuilder as SB
import logicMain, Groupings
from Groupings import ColumnData
import os
import Typedef

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
    
    low = 0.4
    average = 0.8
    high = 0.9
    
    
    def __init__(self): 
        self.dataManager = None
        self.logic = logicMain.logicMain()
        self.fileLoaded = False
        self.statements = {}
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        self.MainWindow = MainWindow
        MainWindow.resize(754, 450)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 456, 401))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.topLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.topLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.topLabel.setObjectName(_fromUtf8("topLabel"))
        self.verticalLayout.addWidget(self.topLabel)
        self.line = QtGui.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.filenameLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.filenameLabel.setObjectName(_fromUtf8("filenameLabel"))
        self.horizontalLayout.addWidget(self.filenameLabel)
        self.filenameDisplay = QtGui.QLabel(self.verticalLayoutWidget)
        self.filenameDisplay.setObjectName(_fromUtf8("filenameDisplay"))
        self.horizontalLayout.addWidget(self.filenameDisplay)
        self.filenameSelectButton = QtGui.QToolButton(self.verticalLayoutWidget)
        self.filenameSelectButton.setObjectName(_fromUtf8("filenameSelectButton"))
        self.horizontalLayout.addWidget(self.filenameSelectButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.groupingsOpenButton = QtGui.QToolButton(self.verticalLayoutWidget)
        self.groupingsOpenButton.setObjectName(_fromUtf8("gropuingsOpenButton"))
        self.verticalLayout.addWidget(self.groupingsOpenButton)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.inquiryTopLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.inquiryTopLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.inquiryTopLabel.setObjectName(_fromUtf8("inquiryTopLabel"))
        self.verticalLayout.addWidget(self.inquiryTopLabel)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.inquiryCombo = QtGui.QComboBox(self.verticalLayoutWidget)
        self.inquiryCombo.setObjectName(_fromUtf8("inquiryCombo"))
        self.inquiryCombo.addItem(_fromUtf8(""))
        self.inquiryCombo.addItem(_fromUtf8(""))
        self.inquiryCombo.addItem(_fromUtf8(""))
        self.inquiryCombo.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.inquiryCombo)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.hypothesisTopLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.hypothesisTopLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.hypothesisTopLabel.setObjectName(_fromUtf8("hypothesisTopLabel"))
        self.verticalLayout.addWidget(self.hypothesisTopLabel)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.hypothesisDisplay = QtGui.QPlainTextEdit(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hypothesisDisplay.sizePolicy().hasHeightForWidth())
        self.hypothesisDisplay.setSizePolicy(sizePolicy)
        self.hypothesisDisplay.setMaximumSize(QtCore.QSize(16777215, 64))
        self.hypothesisDisplay.setObjectName(_fromUtf8("hypothesisDisplay"))
        self.horizontalLayout_4.addWidget(self.hypothesisDisplay)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.statementBuilderButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.statementBuilderButton.setObjectName(_fromUtf8("statementBuilderButton"))
        self.verticalLayout.addWidget(self.statementBuilderButton)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(460, 0, 296, 401))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.resultsTopLabel = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.resultsTopLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.resultsTopLabel.setObjectName(_fromUtf8("resultsTopLabel"))
        self.verticalLayout_2.addWidget(self.resultsTopLabel)
        self.resultsDisplay = QtGui.QTextBrowser(self.verticalLayoutWidget_2)
        self.resultsDisplay.setObjectName(_fromUtf8("resultsDisplay"))
        self.verticalLayout_2.addWidget(self.resultsDisplay)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.confidenceLabel = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.confidenceLabel.setObjectName(_fromUtf8("confidenceLabel"))
        self.horizontalLayout_5.addWidget(self.confidenceLabel)
        self.confidenceDisplay = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.confidenceDisplay.setObjectName(_fromUtf8("confidenceDisplay"))
        self.horizontalLayout_5.addWidget(self.confidenceDisplay)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.testNowButton = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.testNowButton.setObjectName(_fromUtf8("testNowButton"))
        self.verticalLayout_2.addWidget(self.testNowButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 754, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuCredits = QtGui.QMenu(self.menubar)
        self.menuCredits.setObjectName(_fromUtf8("menuCredits"))
        self.menuGroupings = QtGui.QMenu(self.menubar)
        self.menuGroupings.setObjectName(_fromUtf8("menuGroupings"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionClose_Program = QtGui.QAction(MainWindow)
        self.actionClose_Program.setObjectName(_fromUtf8("actionClose_Program"))
        self.actionAdd_Group = QtGui.QAction(MainWindow)
        self.actionAdd_Group.setObjectName(_fromUtf8("actionAdd_Group"))
        self.actionModify_Groups = QtGui.QAction(MainWindow)
        self.actionModify_Groups.setObjectName(_fromUtf8("actionModify_Groups"))
        self.actionDelete_Groups = QtGui.QAction(MainWindow)
        self.actionDelete_Groups.setObjectName(_fromUtf8("actionDelete_Groups"))
        self.actionGroupings_Menu = QtGui.QAction(MainWindow)
        self.actionGroupings_Menu.setObjectName(_fromUtf8("actionGroupings_Menu"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose_Program)
        self.menuGroupings.addAction(self.actionGroupings_Menu)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuGroupings.menuAction())
        self.menubar.addAction(self.menuCredits.menuAction())
        self.hypothesisDisplay.setReadOnly(True)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.setSignals()
        self.setShortcuts()

    def setSignals(self):
        self.statementBuilderButton.clicked.connect(self.callSB)
        self.actionGroupings_Menu.triggered.connect(self.openGroupingsMenu)
        self.actionClose_Program.triggered.connect(QtGui.qApp.quit)
        self.actionOpen.triggered.connect(self.openFileOperation)
        self.testNowButton.clicked.connect(self.commenceTest)
        self.inquiryCombo.currentIndexChanged.connect(self.testChanged)
        self.filenameSelectButton.clicked.connect(self.openFileOperation)
        self.groupingsOpenButton.clicked.connect(self.openGroupingsMenu)

# Call Statement Builder.
# A Statement class is generated, which can handle data from all 4 tests.
# When SB closes successfully, it creates said class which is passed over to logic, which then unpacks it
# according to the test contained within. main will take the English-language statement from stmt, and cache
# the stmt should the user change the hypothesis type via changing inquiryCombo.

    def callSB(self):
        if self.fileLoaded:
            if not self.statements.has_key(self.inquiryCombo.currentIndex()):
                stmt = SB.callBuilder(self.dataManager, self.inquiryCombo.currentIndex())
            else:
                stmt = SB.callBuilder(self.dataManager, self.inquiryCombo.currentIndex(), self.statements[self.inquiryCombo.currentIndex()])
            if stmt is not None:
                self.hypothesisDisplay.clear()
                self.hypothesisDisplay.setPlainText(stmt.getStmt())
                self.statements[self.inquiryCombo.currentIndex()] = stmt
                self.logic.setStmt(stmt)
            else:
                if not self.statements.has_key(self.inquiryCombo.currentIndex()):
                    self.resetHypDisplay()
                else:
                    self.hypothesisDisplay.clear()
                    self.hypothesisDisplay.setPlainText(self.statements[self.inquiryCombo.currentIndex()].getStmt())
        else:
            QtGui.QMessageBox.warning(self.MainWindow, 'Warning', 'Please load a file before opening hypothesis menu.', buttons = QtGui.QMessageBox.Ok, defaultButton = QtGui.QMessageBox.Ok)
 
    def openGroupingsMenu(self):
        # If there is no file loaded, call a dialog informing user that there is no data to build groups from.
        if self.fileLoaded:
            self.dataManager = Groupings.callGroupings(self.dataManager)
        else:
            QtGui.QMessageBox.warning(self.MainWindow, 'Warning', 'Please load a file before opening groupings menu.', buttons = QtGui.QMessageBox.Ok, defaultButton = QtGui.QMessageBox.Ok)
    
    def resetHypDisplay(self):
        self.hypothesisDisplay.clear()
        self.hypothesisDisplay.setPlainText(Typedef.noHypDisplay)
    
    def setShortcuts(self):
        self.actionOpen.setShortcut('O')

    def testChanged(self):
        if self.statements.has_key(self.inquiryCombo.currentIndex()):
            self.hypothesisDisplay.setPlainText(self.statements[self.inquiryCombo.currentIndex()].getStmt())
            self.logic.setStmt(self.statements[self.inquiryCombo.currentIndex()])
        else:
            self.resetHypDisplay()
            

# At this point, we cannot assume that the groupings or hypothesis are updated. Logic may be out of sync with main.
# We have to force an update of all the groups.
    def commenceTest(self):
        self.logic.updateDataManager(self.dataManager)
        if self.statements.has_key(self.inquiryCombo.currentIndex()):
            self.logic.setStmt(self.statements[self.inquiryCombo.currentIndex()])
    # Now we can commence the test.
            confidence, testPrint = self.logic.performTest()
            self.confidenceDisplay.setText(self.getConfidencePrint(confidence))
            self.resultsDisplay.setText(testPrint)
        else:
            QtGui.QMessageBox.warning(self.MainWindow, 'Warning', 'No hypothesis entered.', buttons = QtGui.QMessageBox.Ok, defaultButton = QtGui.QMessageBox.Ok)

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
            # Display the new filename.
            self.filenameDisplay.setText(str(fName).split("/\\").pop())
            # After loading a new sample file, the last hypothesis is voided. Reset the hypothesis.
            self.resetHypDisplay()
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.topLabel.setText(_translate("MainWindow", "Hypothesis Now!", None))
        self.filenameLabel.setText(_translate("MainWindow", "Filename", None))
        self.filenameDisplay.setText(_translate("MainWindow", "____________________________", None))
        self.filenameSelectButton.setText(_translate("MainWindow", "...", None))
        self.groupingsOpenButton.setText(_translate("MainWindow", "Open Groupings Menu", None))
        self.inquiryTopLabel.setText(_translate("MainWindow", "What is your inquiry?", None))
        self.inquiryCombo.setItemText(Typedef.TTest, _translate("MainWindow", "Are two samples significantly different from each other?", None))
        self.inquiryCombo.setItemText(Typedef.ZTest, _translate("MainWindow", "Is the data significantly different from some given standard?", None))
        self.inquiryCombo.setItemText(Typedef.DepTest, _translate("MainWindow", "Is data different after some event?", None))
        self.inquiryCombo.setItemText(Typedef.ChiSqTest, _translate("MainWindow", "Do the entries have equal chance of occurring?", None))
        self.hypothesisTopLabel.setText(_translate("MainWindow", "Hypothesis Statement", None))
        self.hypothesisDisplay.setPlainText(_translate("MainWindow", "I think that Group M (Gender) has greater [Salary] than Group F (Gender)", None))
        self.statementBuilderButton.setText(_translate("MainWindow", "Click here to change statement", None))
        self.resultsTopLabel.setText(_translate("MainWindow", "Test Results", None))
        self.resultsDisplay.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.Lucida Grande UI\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Performing 2 Sample Independent Student\'s T-Test.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Group M Salary Mean: $5,000</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Group M Salary Std. Dev.:$4,000</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Group M Sample Size: 50</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Group F Salary Mean: $4,750</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Group F Salary Std. Dev.: $3,000</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Group F Sample Size: 50</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Assumptions:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Both samples have normal distribution: Good</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The test is sound.</p></body></html>", None))
        self.confidenceLabel.setText(_translate("MainWindow", "Confidence Level", None))
        self.confidenceDisplay.setText(_translate("MainWindow", "Very high (> 99%)", None))
        self.testNowButton.setText(_translate("MainWindow", "Test Now!", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuCredits.setTitle(_translate("MainWindow", "Credits", None))
        self.menuGroupings.setTitle(_translate("MainWindow", "Groupings", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionClose_Program.setText(_translate("MainWindow", "Close Program", None))
        self.actionAdd_Group.setText(_translate("MainWindow", "Add Group", None))
        self.actionModify_Groups.setText(_translate("MainWindow", "Modify Groups", None))
        self.actionDelete_Groups.setText(_translate("MainWindow", "Delete Groups", None))
        self.actionGroupings_Menu.setText(_translate("MainWindow", "Groupings Menu", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = mainUI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

