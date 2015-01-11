# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StatementBuilder.ui'
#
# Created: Wed Oct  1 15:45:12 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import Typedef
import StatementGroupings

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

def callBuilder(dataManager, testType, stmt = None):
    widget = Ui_Form(dataManager)
    widget.setup(testType, stmt)
    if widget.exec_():
        stmt = widget.getTestStatement()
        return stmt
    else:
        return None

class Ui_Form(QtGui.QDialog):
    
    dataManager = None
    g1 = []
    g2 = []
    testType = 0
    oldZComp = 0
    oldTComp = 0
    tCol = 0
    
    def __init__(self, dataManager, parent = None):
        super(Ui_Form, self).__init__()
        self.dataManager = dataManager
        self.setupUi(self)
        self.setupCombos()
        self.loaded = False
    
    def setWidget(self, testType):
        self.testType = testType
        self.stackedWidget.setCurrentIndex(testType)
    
    def setup(self, testType, stmt = None):
        self.setWidget(testType)
        if stmt is not None:
            self.setupStmt(stmt)
        self.loaded = True
    
    def setupCombos(self):
        self.setupColumnCombo(self.ZCompareCombo)
        self.setupColumnCombo(self.TCompareCombo)
        self.setupColumnCombo(self.DepBeforeCombo)
        self.setupColumnCombo(self.DepAfterCombo)
        self.setupColumnCombo(self.sqColCombo)
        
    def setupColumnCombo(self, combo):
        for i in range(self.dataManager.getNumColumns()):
            combo.addItem(self.dataManager.getColumnNameOfIndex(i))
    
    
    #TODO:
    # Gotta rebuild the statements.
    
    def setupStmt(self, stmt):
        if self.testType == Typedef.TTest:
            self.g1, self.g2, tCol, eRange = stmt.getTTest()
            self.TCompareCombo.setCurrentIndex(tCol)
            self.TERangeCombo.setCurrentIndex(eRange)
            self.updateListPrint(self.TCol1Display, self.g1)
            self.updateListPrint(self.TCol2Display, self.g2)
        elif self.testType == Typedef.ZTest:
            self.g1, zComp, zMean, zVar, eRange = stmt.getZTest()
            self.ZMeanEdit.setText(str(zMean))
            self.ZVarianceEdit.setText(str(zVar))
            self.ZCompareCombo.setCurrentIndex(zComp)
            self.ZERangeCombo.setCurrentIndex(eRange)
            self.updateListPrint(self.ZSampleDisplay, self.g1)
        elif self.testType == Typedef.DepTest:
            before, after, self.g1, eRange = stmt.getDepTest()
            self.DepBeforeCombo.setCurrentIndex(before)
            self.DepAfterCombo.setCurrentIndex(after)
            self.updateListPrint(self.DepGroupDisplay, self.g1)
        elif self.testType == Typedef.ChiSqTest:
            sqCol, self.g1 = stmt.getChiSqTest()
            self.sqColCombo.setCurrentIndex(sqCol)
            self.updateListPrint(self.sqGroupDisplay, self.g1)
        return
    
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(368, 465)
        self.stackedWidget = QtGui.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 361, 411))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.TTestPage = QtGui.QWidget()
        self.TTestPage.setObjectName(_fromUtf8("TTestPage"))
        self.verticalLayoutWidget = QtGui.QWidget(self.TTestPage)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 361, 411))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.TTopLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.TTopLabel.setObjectName(_fromUtf8("TTopLabel"))
        self.verticalLayout.addWidget(self.TTopLabel)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.TCol1Label = QtGui.QLabel(self.verticalLayoutWidget)
        self.TCol1Label.setObjectName(_fromUtf8("TCol1Label"))
        self.horizontalLayout_13.addWidget(self.TCol1Label)
        self.TCol1Display = QtGui.QLabel(self.verticalLayoutWidget)
        self.TCol1Display.setObjectName(_fromUtf8("TCol1Display"))
        self.horizontalLayout_13.addWidget(self.TCol1Display)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        self.TCol1Button = QtGui.QPushButton(self.verticalLayoutWidget)
        self.TCol1Button.setObjectName(_fromUtf8("TCol1Button"))
        self.verticalLayout.addWidget(self.TCol1Button)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.TCol2Label = QtGui.QLabel(self.verticalLayoutWidget)
        self.TCol2Label.setObjectName(_fromUtf8("TCol2Label"))
        self.horizontalLayout_14.addWidget(self.TCol2Label)
        self.TCol2Display = QtGui.QLabel(self.verticalLayoutWidget)
        self.TCol2Display.setObjectName(_fromUtf8("TCol2Display"))
        self.horizontalLayout_14.addWidget(self.TCol2Display)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        self.TCol2Button = QtGui.QPushButton(self.verticalLayoutWidget)
        self.TCol2Button.setObjectName(_fromUtf8("TCol2Button"))
        self.verticalLayout.addWidget(self.TCol2Button)
        self.horizontalLayout_19 = QtGui.QHBoxLayout()
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        self.TCompareLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.TCompareLabel.setObjectName(_fromUtf8("TCompareLabel"))
        self.horizontalLayout_19.addWidget(self.TCompareLabel)
        self.TCompareCombo = QtGui.QComboBox(self.verticalLayoutWidget)
        self.TCompareCombo.setObjectName(_fromUtf8("TCompareCombo"))
        self.horizontalLayout_19.addWidget(self.TCompareCombo)
        self.verticalLayout.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.TERangeLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.TERangeLabel.setObjectName(_fromUtf8("TERangeLabel"))
        self.horizontalLayout_4.addWidget(self.TERangeLabel)
        self.TERangeCombo = QtGui.QComboBox(self.verticalLayoutWidget)
        self.TERangeCombo.setObjectName(_fromUtf8("TERangeCombo"))
        self.TERangeCombo.addItem(_fromUtf8(""))
        self.TERangeCombo.addItem(_fromUtf8(""))
        self.TERangeCombo.addItem(_fromUtf8(""))
        self.horizontalLayout_4.addWidget(self.TERangeCombo)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.TStatementLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.TStatementLabel.setObjectName(_fromUtf8("TStatementLabel"))
        self.verticalLayout.addWidget(self.TStatementLabel)
        self.TStatementDisplay = QtGui.QTextBrowser(self.verticalLayoutWidget)
        self.TStatementDisplay.setObjectName(_fromUtf8("TStatementDisplay"))
        self.verticalLayout.addWidget(self.TStatementDisplay)
        self.stackedWidget.addWidget(self.TTestPage)
        self.ZTestPage = QtGui.QWidget()
        self.ZTestPage.setObjectName(_fromUtf8("ZTestPage"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.ZTestPage)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 361, 411))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.ZTopLabel = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.ZTopLabel.setObjectName(_fromUtf8("ZTopLabel"))
        self.verticalLayout_2.addWidget(self.ZTopLabel)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.ZSampleLabel = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.ZSampleLabel.setObjectName(_fromUtf8("ZSampleLabel"))
        self.horizontalLayout_16.addWidget(self.ZSampleLabel)
        self.ZSampleDisplay = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.ZSampleDisplay.setObjectName(_fromUtf8("ZSampleDisplay"))
        self.horizontalLayout_16.addWidget(self.ZSampleDisplay)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_16)
        self.ZSampleButton = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.ZSampleButton.setObjectName(_fromUtf8("ZSampleButton"))
        self.verticalLayout_2.addWidget(self.ZSampleButton)
        self.horizontalLayout_20 = QtGui.QHBoxLayout()
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        self.ZCompareLabel = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.ZCompareLabel.setObjectName(_fromUtf8("ZCompareLabel"))
        self.horizontalLayout_20.addWidget(self.ZCompareLabel)
        self.ZCompareCombo = QtGui.QComboBox(self.verticalLayoutWidget_2)
        self.ZCompareCombo.setObjectName(_fromUtf8("ZCompareCombo"))
        self.horizontalLayout_20.addWidget(self.ZCompareCombo)
        self.verticalLayout_2.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.ZMeanLabel = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.ZMeanLabel.setObjectName(_fromUtf8("ZMeanLabel"))
        self.horizontalLayout_6.addWidget(self.ZMeanLabel)
        self.ZMeanEdit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.ZMeanEdit.setObjectName(_fromUtf8("ZMeanEdit"))
        self.horizontalLayout_6.addWidget(self.ZMeanEdit)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.ZVarianceLabel = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.ZVarianceLabel.setObjectName(_fromUtf8("ZVarianceLabel"))
        self.horizontalLayout_7.addWidget(self.ZVarianceLabel)
        self.ZVarianceEdit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.ZVarianceEdit.setObjectName(_fromUtf8("ZVarianceEdit"))
        self.horizontalLayout_7.addWidget(self.ZVarianceEdit)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.ZERangeLabel = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.ZERangeLabel.setObjectName(_fromUtf8("ZERangeLabel"))
        self.verticalLayout_2.addWidget(self.ZERangeLabel)
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.ZERangeCombo = QtGui.QComboBox(self.verticalLayoutWidget_2)
        self.ZERangeCombo.setMinimumSize(QtCore.QSize(111, 0))
        self.ZERangeCombo.setObjectName(_fromUtf8("ZERangeCombo"))
        self.ZERangeCombo.addItem(_fromUtf8(""))
        self.ZERangeCombo.addItem(_fromUtf8(""))
        self.ZERangeCombo.addItem(_fromUtf8(""))
        self.horizontalLayout_17.addWidget(self.ZERangeCombo)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_17)
        self.ZERangeLabel2 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.ZERangeLabel2.setObjectName(_fromUtf8("ZERangeLabel2"))
        self.verticalLayout_2.addWidget(self.ZERangeLabel2)
        self.line_2 = QtGui.QFrame(self.verticalLayoutWidget_2)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_2.addWidget(self.line_2)
        self.ZStatementLabel = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.ZStatementLabel.setObjectName(_fromUtf8("ZStatementLabel"))
        self.verticalLayout_2.addWidget(self.ZStatementLabel)
        self.ZStatementDisplay = QtGui.QTextBrowser(self.verticalLayoutWidget_2)
        self.ZStatementDisplay.setObjectName(_fromUtf8("ZStatementDisplay"))
        self.verticalLayout_2.addWidget(self.ZStatementDisplay)
        self.stackedWidget.addWidget(self.ZTestPage)
        self.DependentPage = QtGui.QWidget()
        self.DependentPage.setObjectName(_fromUtf8("DependentPage"))
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.DependentPage)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 361, 411))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.DepTopLabel = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.DepTopLabel.setObjectName(_fromUtf8("DepTopLabel"))
        self.verticalLayout_3.addWidget(self.DepTopLabel)
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.DepGroupLabel = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.DepGroupLabel.setObjectName(_fromUtf8("DepGroupLabel"))
        self.horizontalLayout_18.addWidget(self.DepGroupLabel)
        self.DepGroupDisplay = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.DepGroupDisplay.setObjectName(_fromUtf8("DepGroupDisplay"))
        self.horizontalLayout_18.addWidget(self.DepGroupDisplay)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem7)
        self.verticalLayout_3.addLayout(self.horizontalLayout_18)
        self.DepGroupButton = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.DepGroupButton.setObjectName(_fromUtf8("DepGroupButton"))
        self.verticalLayout_3.addWidget(self.DepGroupButton)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.DepBeforeLabel = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.DepBeforeLabel.setObjectName(_fromUtf8("DepBeforeLabel"))
        self.horizontalLayout_8.addWidget(self.DepBeforeLabel)
        self.DepBeforeCombo = QtGui.QComboBox(self.verticalLayoutWidget_3)
        self.DepBeforeCombo.setObjectName(_fromUtf8("DepBeforeCombo"))
        self.horizontalLayout_8.addWidget(self.DepBeforeCombo)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.DepAfterLabel = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.DepAfterLabel.setObjectName(_fromUtf8("DepAfterLabel"))
        self.horizontalLayout_9.addWidget(self.DepAfterLabel)
        self.DepAfterCombo = QtGui.QComboBox(self.verticalLayoutWidget_3)
        self.DepAfterCombo.setObjectName(_fromUtf8("DepAfterCombo"))
        self.horizontalLayout_9.addWidget(self.DepAfterCombo)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem9)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.DepERangeLabel = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.DepERangeLabel.setObjectName(_fromUtf8("DepERangeLabel"))
        self.horizontalLayout_10.addWidget(self.DepERangeLabel)
        self.DepERangeCombo = QtGui.QComboBox(self.verticalLayoutWidget_3)
        self.DepERangeCombo.setObjectName(_fromUtf8("DepERangeCombo"))
        self.DepERangeCombo.addItem(_fromUtf8(""))
        self.DepERangeCombo.addItem(_fromUtf8(""))
        self.DepERangeCombo.addItem(_fromUtf8(""))
        self.horizontalLayout_10.addWidget(self.DepERangeCombo)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.DepERangeLabel2 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.DepERangeLabel2.setObjectName(_fromUtf8("DepERangeLabel2"))
        self.verticalLayout_3.addWidget(self.DepERangeLabel2)
        self.line = QtGui.QFrame(self.verticalLayoutWidget_3)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_3.addWidget(self.line)
        self.DepStatementLabel = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.DepStatementLabel.setObjectName(_fromUtf8("DepStatementLabel"))
        self.verticalLayout_3.addWidget(self.DepStatementLabel)
        self.DepStatementDisplay = QtGui.QTextBrowser(self.verticalLayoutWidget_3)
        self.DepStatementDisplay.setObjectName(_fromUtf8("DepStatementDisplay"))
        self.verticalLayout_3.addWidget(self.DepStatementDisplay)
        self.stackedWidget.addWidget(self.DependentPage)
        self.ChiSqPage = QtGui.QWidget()
        self.ChiSqPage.setObjectName(_fromUtf8("ChiSqPage"))
        self.verticalLayoutWidget_4 = QtGui.QWidget(self.ChiSqPage)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 361, 411))
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.sqTopLabel = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.sqTopLabel.setObjectName(_fromUtf8("sqTopLabel"))
        self.verticalLayout_4.addWidget(self.sqTopLabel)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.sqColLabel = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.sqColLabel.setObjectName(_fromUtf8("sqColLabel"))
        self.horizontalLayout_11.addWidget(self.sqColLabel)
        self.sqColCombo = QtGui.QComboBox(self.verticalLayoutWidget_4)
        self.sqColCombo.setObjectName(_fromUtf8("sqColCombo"))
        self.horizontalLayout_11.addWidget(self.sqColCombo)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem11)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.sqGroupLabel = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.sqGroupLabel.setObjectName(_fromUtf8("sqGroupLabel"))
        self.horizontalLayout_15.addWidget(self.sqGroupLabel)
        self.sqGroupDisplay = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.sqGroupDisplay.setObjectName(_fromUtf8("sqGroupDisplay"))
        self.horizontalLayout_15.addWidget(self.sqGroupDisplay)
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem12)
        self.verticalLayout_4.addLayout(self.horizontalLayout_15)
        self.sqGroupButton = QtGui.QPushButton(self.verticalLayoutWidget_4)
        self.sqGroupButton.setObjectName(_fromUtf8("sqGroupButton"))
        self.verticalLayout_4.addWidget(self.sqGroupButton)
        self.sqStatementLabel = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.sqStatementLabel.setObjectName(_fromUtf8("sqStatementLabel"))
        self.verticalLayout_4.addWidget(self.sqStatementLabel)
        self.sqStatementDisplay = QtGui.QTextBrowser(self.verticalLayoutWidget_4)
        self.sqStatementDisplay.setObjectName(_fromUtf8("sqStatementDisplay"))
        self.verticalLayout_4.addWidget(self.sqStatementDisplay)
        self.stackedWidget.addWidget(self.ChiSqPage)
        self.dialogButtons = QtGui.QDialogButtonBox(Form)
        self.dialogButtons.setGeometry(QtCore.QRect(180, 420, 164, 32))
        self.dialogButtons.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.dialogButtons.setObjectName(_fromUtf8("dialogButtons"))

        QtCore.QObject.connect(self.dialogButtons, QtCore.SIGNAL(_fromUtf8("accepted()")), Form.accept)
        QtCore.QObject.connect(self.dialogButtons, QtCore.SIGNAL(_fromUtf8("rejected()")), Form.reject)

        #Signals for group combo boxes.
        self.TCol1Button.clicked.connect(self.callStatementGroupings)
        self.TCol2Button.clicked.connect(self.callStatementGroupings)
        self.ZSampleButton.clicked.connect(self.callStatementGroupings)
        self.DepGroupButton.clicked.connect(self.callStatementGroupings)
        self.sqGroupButton.clicked.connect(self.callStatementGroupings)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        # Currently this does not behave as expected.
        
#        self.ZCompareCombo.currentIndexChanged.connect(self.verifyCompareZ)
#        self.TCompareCombo.currentIndexChanged.connect(self.verifyCompareT)
    
        # StatementGroupings takes in the full list of groups, and returns the list of groups which were selected.
    
    def callStatementGroupings(self):
        groupList = self.dataManager.getAllGroups()
        if self.sender() == self.TCol1Button:
            self.g1 = StatementGroupings.callStatementGroupings(groupList)
            self.updateListPrint(self.TCol1Display, self.g1)
        elif self.sender() == self.TCol2Button:
            self.g2 = StatementGroupings.callStatementGroupings(groupList)
            self.updateListPrint(self.TCol2Display, self.g2)
        elif self.sender() == self.ZSampleButton:
            self.g1 = StatementGroupings.callStatementGroupings(groupList)
            self.updateListPrint(self.ZSampleDisplay, self.g1)
        elif self.sender() == self.DepGroupButton:
            self.g1 = StatementGroupings.callStatementGroupings(groupList)
            self.updateListPrint(self.depGroupDisplay, self.g1)
        elif self.sender() == self.sqGroupButton:
            self.g1 = StatementGroupings.callStatementGroupings(groupList)
            self.updateListPrint(self.sqGroupDisplay, self.g1)
    
    def updateListPrint(self, combo, group):
        groupPrint = self.getGroupListPrint(group)
        combo.setText(groupPrint)
        
    
    def getGroupListPrint(self, groupList):
        print groupList
        printString = ''
        for group in groupList:
            printString += group.getName() + ' (' + group.getParentName() + '), '
        return printString
    
    def statementValid(self):
        if self.testType == Typedef.TTest:
            return self.colTypes[self.TCompareCombo.currentIndex()] == Typedef.numeric
        elif self.testType == Typedef.ZTest:
            return self.colTypes[self.ZCompareCombo.currentIndex()] == Typedef.numeric
        elif self.testType == Typedef.DepTest:
            return self.colTypes[self.ZCompareCombo.currentIndex()] == Typedef.numeric
        else:
            return True

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.TTopLabel.setText(_translate("Form", "Two samples differ from one another", None))
        self.TCol1Label.setText(_translate("Form", "Sample 1 Group:", None))
        self.TCol1Display.setText(_translate("Form", "No Group", None))
        self.TCol1Button.setText(_translate("Form", "Change", None))
        self.TCol2Label.setText(_translate("Form", "Sample 2 Group:", None))
        self.TCol2Display.setText(_translate("Form", "No Group", None))
        self.TCol2Button.setText(_translate("Form", "Change", None))
        self.TCompareLabel.setText(_translate("Form", "What data are we comparing?", None))
        self.TERangeLabel.setText(_translate("Form", "Is Sample 1\'s data smaller? ", None))
        self.TERangeCombo.setItemText(0, _translate("Form", "Yes", None))
        self.TERangeCombo.setItemText(1, _translate("Form", "No", None))
        self.TERangeCombo.setItemText(2, _translate("Form", "Just Different", None))
        self.TStatementLabel.setText(_translate("Form", "Test Statement", None))
        self.ZTopLabel.setText(_translate("Form", "Data is different from some given standard population", None))
        self.ZSampleLabel.setText(_translate("Form", "Sample Group:", None))
        self.ZSampleDisplay.setText(_translate("Form", "No Groups", None))
        self.ZSampleButton.setText(_translate("Form", "Change", None))
        self.ZCompareLabel.setText(_translate("Form", "What data are we comparing?", None))
        self.ZMeanLabel.setText(_translate("Form", "Population Mean", None))
        self.ZVarianceLabel.setText(_translate("Form", "Population Variance", None))
        self.ZERangeLabel.setText(_translate("Form", "I predict the sample will be", None))
        self.ZERangeCombo.setItemText(0, _translate("Form", "Smaller", None))
        self.ZERangeCombo.setItemText(1, _translate("Form", "Bigger", None))
        self.ZERangeCombo.setItemText(2, _translate("Form", "Either Bigger or Smaller", None))
        self.ZERangeLabel2.setText(_translate("Form", "Than the Population.", None))
        self.ZStatementLabel.setText(_translate("Form", "Test Statement", None))
        self.DepTopLabel.setText(_translate("Form", "Data Change After Some Event", None))
        self.DepGroupLabel.setText(_translate("Form", "Group to Test:", None))
        self.DepGroupDisplay.setText(_translate("Form", "No Group", None))
        self.DepGroupButton.setText(_translate("Form", "Change", None))
        self.DepBeforeLabel.setText(_translate("Form", "Data Column Before Event", None))
        self.DepAfterLabel.setText(_translate("Form", "Data Column After Event", None))
        self.DepERangeLabel.setText(_translate("Form", "I think Data Before is", None))
        self.DepERangeCombo.setItemText(0, _translate("Form", "Smaller Than", None))
        self.DepERangeCombo.setItemText(1, _translate("Form", "Larger Than", None))
        self.DepERangeCombo.setItemText(2, _translate("Form", "Just Different From", None))
        self.DepERangeLabel2.setText(_translate("Form", "Data After.", None))
        self.DepStatementLabel.setText(_translate("Form", "Test Statement", None))
        self.sqTopLabel.setText(_translate("Form", "The entries have equal chance of occurring", None))
        self.sqColLabel.setText(_translate("Form", "Column", None))
        self.sqGroupLabel.setText(_translate("Form", "Grouping:", None))
        self.sqGroupDisplay.setText(_translate("Form", "No Group", None))
        self.sqGroupButton.setText(_translate("Form", "Change", None))
        self.sqStatementLabel.setText(_translate("Form", "Test Statement", None))

    def getTestStatement(self):
        newStmt = Statement()
        newStmt.setTestType(self.testType)
        if self.testType == Typedef.TTest:
            newStmt.setTTest(self.g1, self.g2, self.TCompareCombo.currentIndex(), self.TERangeCombo.currentIndex())
        elif self.testType == Typedef.ZTest:
            if self.ZMeanEdit.text() == '':
                self.ZMeanEdit.setText('0')
            if self.ZVarianceEdit.text() == '':
                self.ZVarianceEdit.setText('0')
            newStmt.setZTest(self.g1, self.ZCompareCombo.currentIndex(), float(self.ZMeanEdit.text()), float(self.ZVarianceEdit.text()), self.ZERangeCombo.currentIndex())
        elif self.testType == Typedef.DepTest:
# Dependent test works.
            newStmt.setDepTest(self.DepBeforeCombo.currentIndex(), self.DepAfterCombo.currentIndex(), self.g1, self.DepERangeCombo.currentIndex())
        elif self.testType == Typedef.ChiSqTest:
# Chi-Square testing in this iteration is limited to testing if the distribution in a single column is equal element-wise.
# Testing if all elements have an equal chance of occurring.
            newStmt.setChiSqTest(self.sqColCombo.currentIndex(),self.g1)
# Write the statement that will be shown in the main window.
        newStmt.setStmt(self.writeStatement())
        return newStmt
    
    def writeStatement(self):
        starter = 'I think that '
        if self.testType == Typedef.TTest:
            return starter + self.writeTStatement()
        elif self.testType == Typedef.ZTest:
            return starter + self.writeZStatement()
        elif self.testType == Typedef.DepTest:
            return 'Dependent T-Test'
        elif self.testType == Typedef.ChiSqTest:
            return 'Chi-Square Test'
        else:
            return starter + 'Something\'s wrong.'

    def writeTStatement(self):
        statement = ''
        if len(self.g1) > 0:
            statement += 'Group ' + self.getGroupListPrint(self.g1) + ' '
        else:
            statement += 'the data '
        if self.TERangeCombo.currentIndex() == Typedef.lessThan:
            statement += 'has a smaller '
        elif self.TERangeCombo.currentIndex() == Typedef.greaterThan:
            statement += 'has a greater '
        elif self.TERangeCombo.currentIndex() == Typedef.notEqual:
            statement += 'has a distinctly different '
        statement += '[' + self.TCompareCombo.currentText() + '] compared to '
        if len(self.g2) > 0:
            statement += 'Group ' + self.getGroupListPrint(self.g2) + ' '
        else:
            statement += 'the data.'
        return statement

    def writeZStatement(self):
        statement = ''
        if len(self.g1) > 0:
            statement += 'Group ' + self.getGroupListPrint(self.g1) + '\'s '
        else:
            statement += 'the data\'s average '
        statement += '[' + self.ZCompareCombo.currentText() + '] '
        if self.ZERangeCombo.currentIndex() == Typedef.lessThan:
            statement += 'is smaller than '
        elif self.ZERangeCombo.currentIndex() == Typedef.greaterThan:
            statement += 'is greater than '
        elif self.ZERangeCombo.currentIndex() == Typedef.notEqual:
            statement += 'is not '
        statement += self.ZMeanEdit.text() + '.'
        return statement

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QDialog()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

class Statement():
    
    def __init__(self):    
        self.testType = 0
        self.g1 = []
        self.g2 = []
        self.tCol = 0
        self.ERange = Typedef.notEqual
        self.stmt = ''
        self.ZMean = 0
        self.ZVar = 0
        self.c1 = 0
        self.c2 = 0

    def setTestType(self, testType):
        self.testType = testType

# T-Test.

    def setTTest(self, g1, g2, tCol, ERange):
        self.g1 = g1
        self.g2 = g2
        self.tCol = tCol
        self.ERange = ERange

    def getTTest(self):
        return self.g1, self.g2, self.tCol, self.ERange

# Z-Test.

    def setZTest(self, g1, tCol, mean, var, ERange):
        self.g1 = g1
        self.tCol = tCol
        self.ZMean = mean
        self.ZVar = var
        self.ERange = ERange

    def getZTest(self):
        return self.g1, self.tCol, self.ZMean, self.ZVar, self.ERange

# Dependent T-Test. Still have to figure out how to get the column which the group was taken from.

    def setDepTest(self, c1, c2, g1, ERange):
        self.c1 = c1
        self.c2 = c2
        self.g1 = g1
        self.ERange = ERange
        
    def getDepTest(self):
        return self.c1, self.c2, self.g1, self.ERange
        
# Chi-Square Test of independence. The current iteration will take null hypothesis as equal distribution of outcomes.
# So there is no transfer of distribution-specific data currently.
        
    def setChiSqTest(self, c1, g1):
        self.c1 = c1
        self.g1 = g1

    def getChiSqTest(self):
        return self.c1, self.g1
    
    def setStmt(self, stmt):
        self.stmt = stmt
        
    def getStmt(self):
        return self.stmt
        
