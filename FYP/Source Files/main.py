# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainV3.ui'
#
# Created: Mon Sep 29 15:49:58 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
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

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.topLabel.setText(_translate("MainWindow", "Hypothesis Now!", None))
        self.filenameLabel.setText(_translate("MainWindow", "Filename", None))
        self.filenameDisplay.setText(_translate("MainWindow", "____________________________", None))
        self.filenameSelectButton.setText(_translate("MainWindow", "...", None))
        self.inquiryTopLabel.setText(_translate("MainWindow", "What is your inquiry?", None))
        self.inquiryCombo.setItemText(0, _translate("MainWindow", "Is one sample different from another sample?", None))
        self.inquiryCombo.setItemText(1, _translate("MainWindow", "Is the data significantly different from some given standard?", None))
        self.inquiryCombo.setItemText(2, _translate("MainWindow", "Is data different after some event?", None))
        self.inquiryCombo.setItemText(3, _translate("MainWindow", "Does the occurrence of some data affect another\'s behaviour?", None))
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
        self.confidenceLabel.setText(_translate("MainWindow", "Statement Accuracy", None))
        self.confidenceDisplay.setText(_translate("MainWindow", "99%", None))
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
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

