# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StatementBuilder.ui'
#
# Created: Wed Oct  1 15:45:12 2014
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

class Ui_Form(object):
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
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.TCol1Label = QtGui.QLabel(self.verticalLayoutWidget)
        self.TCol1Label.setObjectName(_fromUtf8("TCol1Label"))
        self.horizontalLayout.addWidget(self.TCol1Label)
        self.TCol1Combo = QtGui.QComboBox(self.verticalLayoutWidget)
        self.TCol1Combo.setObjectName(_fromUtf8("TCol1Combo"))
        self.horizontalLayout.addWidget(self.TCol1Combo)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.TCol1GroupLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.TCol1GroupLabel.setObjectName(_fromUtf8("TCol1GroupLabel"))
        self.horizontalLayout_13.addWidget(self.TCol1GroupLabel)
        self.TCol1GroupCombo = QtGui.QComboBox(self.verticalLayoutWidget)
        self.TCol1GroupCombo.setObjectName(_fromUtf8("TCol1GroupCombo"))
        self.TCol1GroupCombo.addItem(_fromUtf8(""))
        self.horizontalLayout_13.addWidget(self.TCol1GroupCombo)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.TCol2Label = QtGui.QLabel(self.verticalLayoutWidget)
        self.TCol2Label.setObjectName(_fromUtf8("TCol2Label"))
        self.horizontalLayout_2.addWidget(self.TCol2Label)
        self.TCol2Combo = QtGui.QComboBox(self.verticalLayoutWidget)
        self.TCol2Combo.setObjectName(_fromUtf8("TCol2Combo"))
        self.horizontalLayout_2.addWidget(self.TCol2Combo)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.TCol2GroupLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.TCol2GroupLabel.setObjectName(_fromUtf8("TCol2GroupLabel"))
        self.horizontalLayout_14.addWidget(self.TCol2GroupLabel)
        self.TCol2GroupCombo = QtGui.QComboBox(self.verticalLayoutWidget)
        self.TCol2GroupCombo.setObjectName(_fromUtf8("TCol2GroupCombo"))
        self.TCol2GroupCombo.addItem(_fromUtf8(""))
        self.horizontalLayout_14.addWidget(self.TCol2GroupCombo)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
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
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
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
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.ZSampleColLabel = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.ZSampleColLabel.setObjectName(_fromUtf8("ZSampleColLabel"))
        self.horizontalLayout_15.addWidget(self.ZSampleColLabel)
        self.ZSampleColCombo = QtGui.QComboBox(self.verticalLayoutWidget_2)
        self.ZSampleColCombo.setObjectName(_fromUtf8("ZSampleColCombo"))
        self.horizontalLayout_15.addWidget(self.ZSampleColCombo)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.ZSampleGroupLabel = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.ZSampleGroupLabel.setObjectName(_fromUtf8("ZSampleGroupLabel"))
        self.horizontalLayout_16.addWidget(self.ZSampleGroupLabel)
        self.ZSampleGroupCombo = QtGui.QComboBox(self.verticalLayoutWidget_2)
        self.ZSampleGroupCombo.setObjectName(_fromUtf8("ZSampleGroupCombo"))
        self.ZSampleGroupCombo.addItem(_fromUtf8(""))
        self.horizontalLayout_16.addWidget(self.ZSampleGroupCombo)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_16)
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
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.ZVarianceLabel = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.ZVarianceLabel.setObjectName(_fromUtf8("ZVarianceLabel"))
        self.horizontalLayout_7.addWidget(self.ZVarianceLabel)
        self.ZVarianceEdit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.ZVarianceEdit.setObjectName(_fromUtf8("ZVarianceEdit"))
        self.horizontalLayout_7.addWidget(self.ZVarianceEdit)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
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
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem9)
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
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.DepBeforeLabel = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.DepBeforeLabel.setObjectName(_fromUtf8("DepBeforeLabel"))
        self.horizontalLayout_8.addWidget(self.DepBeforeLabel)
        self.DepBeforeCombo = QtGui.QComboBox(self.verticalLayoutWidget_3)
        self.DepBeforeCombo.setObjectName(_fromUtf8("DepBeforeCombo"))
        self.horizontalLayout_8.addWidget(self.DepBeforeCombo)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.DepAfterLabel = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.DepAfterLabel.setObjectName(_fromUtf8("DepAfterLabel"))
        self.horizontalLayout_9.addWidget(self.DepAfterLabel)
        self.DepAfterCombo = QtGui.QComboBox(self.verticalLayoutWidget_3)
        self.DepAfterCombo.setObjectName(_fromUtf8("DepAfterCombo"))
        self.horizontalLayout_9.addWidget(self.DepAfterCombo)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem11)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.DepGroupLabel = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.DepGroupLabel.setObjectName(_fromUtf8("DepGroupLabel"))
        self.horizontalLayout_18.addWidget(self.DepGroupLabel)
        self.DepGroupCombo = QtGui.QComboBox(self.verticalLayoutWidget_3)
        self.DepGroupCombo.setObjectName(_fromUtf8("DepGroupCombo"))
        self.DepGroupCombo.addItem(_fromUtf8(""))
        self.horizontalLayout_18.addWidget(self.DepGroupCombo)
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem12)
        self.verticalLayout_3.addLayout(self.horizontalLayout_18)
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
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem13)
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
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.sqCol1Label = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.sqCol1Label.setObjectName(_fromUtf8("sqCol1Label"))
        self.horizontalLayout_3.addWidget(self.sqCol1Label)
        self.sqCol1Combo = QtGui.QComboBox(self.verticalLayoutWidget_4)
        self.sqCol1Combo.setObjectName(_fromUtf8("sqCol1Combo"))
        self.horizontalLayout_3.addWidget(self.sqCol1Combo)
        spacerItem14 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem14)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.sqCol1GroupLabel = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.sqCol1GroupLabel.setObjectName(_fromUtf8("sqCol1GroupLabel"))
        self.horizontalLayout_11.addWidget(self.sqCol1GroupLabel)
        self.sqCol1GroupCombo = QtGui.QComboBox(self.verticalLayoutWidget_4)
        self.sqCol1GroupCombo.setObjectName(_fromUtf8("sqCol1GroupCombo"))
        self.sqCol1GroupCombo.addItem(_fromUtf8(""))
        self.horizontalLayout_11.addWidget(self.sqCol1GroupCombo)
        spacerItem15 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem15)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.sqCol2Label = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.sqCol2Label.setObjectName(_fromUtf8("sqCol2Label"))
        self.horizontalLayout_5.addWidget(self.sqCol2Label)
        self.sqCol2Combo = QtGui.QComboBox(self.verticalLayoutWidget_4)
        self.sqCol2Combo.setObjectName(_fromUtf8("sqCol2Combo"))
        self.horizontalLayout_5.addWidget(self.sqCol2Combo)
        spacerItem16 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem16)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.sqCol2GroupLabel = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.sqCol2GroupLabel.setObjectName(_fromUtf8("sqCol2GroupLabel"))
        self.horizontalLayout_12.addWidget(self.sqCol2GroupLabel)
        self.sqCol2GroupCombo = QtGui.QComboBox(self.verticalLayoutWidget_4)
        self.sqCol2GroupCombo.setObjectName(_fromUtf8("sqCol2GroupCombo"))
        self.sqCol2GroupCombo.addItem(_fromUtf8(""))
        self.horizontalLayout_12.addWidget(self.sqCol2GroupCombo)
        spacerItem17 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem17)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
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

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.TTopLabel.setText(_translate("Form", "Two samples differ from one another", None))
        self.TCol1Label.setText(_translate("Form", "Sample 1 Column", None))
        self.TCol1GroupLabel.setText(_translate("Form", "Sample 1 Group", None))
        self.TCol1GroupCombo.setItemText(0, _translate("Form", "No Grouping", None))
        self.TCol2Label.setText(_translate("Form", "Sample 2 Column", None))
        self.TCol2GroupLabel.setText(_translate("Form", "Sample 2 Group", None))
        self.TCol2GroupCombo.setItemText(0, _translate("Form", "No Grouping", None))
        self.TCompareLabel.setText(_translate("Form", "What data are we comparing?", None))
        self.TERangeLabel.setText(_translate("Form", "Is Sample 1\'s data smaller? ", None))
        self.TERangeCombo.setItemText(0, _translate("Form", "Yes", None))
        self.TERangeCombo.setItemText(1, _translate("Form", "No", None))
        self.TERangeCombo.setItemText(2, _translate("Form", "Just Different", None))
        self.TStatementLabel.setText(_translate("Form", "Test Statement", None))
        self.ZTopLabel.setText(_translate("Form", "Data is different from some given standard population", None))
        self.ZSampleColLabel.setText(_translate("Form", "Sample Column", None))
        self.ZSampleGroupLabel.setText(_translate("Form", "Sample Group", None))
        self.ZSampleGroupCombo.setItemText(0, _translate("Form", "No Grouping", None))
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
        self.DepBeforeLabel.setText(_translate("Form", "Data Column Before Event", None))
        self.DepAfterLabel.setText(_translate("Form", "Data Column After Event", None))
        self.DepGroupLabel.setText(_translate("Form", "Group to Test", None))
        self.DepGroupCombo.setItemText(0, _translate("Form", "No Grouping", None))
        self.DepERangeLabel.setText(_translate("Form", "I think Data Before is", None))
        self.DepERangeCombo.setItemText(0, _translate("Form", "Smaller Than", None))
        self.DepERangeCombo.setItemText(1, _translate("Form", "Larger Than", None))
        self.DepERangeCombo.setItemText(2, _translate("Form", "Just Different From", None))
        self.DepERangeLabel2.setText(_translate("Form", "Data After.", None))
        self.DepStatementLabel.setText(_translate("Form", "Test Statement", None))
        self.sqTopLabel.setText(_translate("Form", "One column\'s data is influenced by another column", None))
        self.sqCol1Label.setText(_translate("Form", "Column 1", None))
        self.sqCol1GroupLabel.setText(_translate("Form", "Column 1 Group", None))
        self.sqCol1GroupCombo.setItemText(0, _translate("Form", "No Grouping", None))
        self.sqCol2Label.setText(_translate("Form", "Column 2", None))
        self.sqCol2GroupLabel.setText(_translate("Form", "Column 2 Group", None))
        self.sqCol2GroupCombo.setItemText(0, _translate("Form", "No Grouping", None))
        self.sqStatementLabel.setText(_translate("Form", "Test Statement", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

