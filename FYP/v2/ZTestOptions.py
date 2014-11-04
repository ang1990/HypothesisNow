# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z-Test Options.ui'
#
# Created: Mon Sep  1 11:11:54 2014
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

class ZTestOptionsWindow(QtGui.QDialog):
    
    mean = 0
    var = 0
    expRange = 0
    validator = QtGui.QDoubleValidator()
    
    def __init__(self,parent = None):
        super(ZTestOptionsWindow, self).__init__()
        self.setupUi(self)
        
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("ZTestOptions"))
        Dialog.resize(377, 194)
        self.formLayout = QtGui.QFormLayout(Dialog)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.meanLabel = QtGui.QLabel(Dialog)
        self.meanLabel.setObjectName(_fromUtf8("meanLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.meanLabel)
        self.meanEdit = QtGui.QLineEdit(Dialog)
        self.meanEdit.setObjectName(_fromUtf8("meanEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.meanEdit)
        self.varianceLabel = QtGui.QLabel(Dialog)
        self.varianceLabel.setObjectName(_fromUtf8("varianceLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.varianceLabel)
        self.varianceEdit = QtGui.QLineEdit(Dialog)
        self.varianceEdit.setObjectName(_fromUtf8("varianceEdit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.varianceEdit)
        self.eRangeLabel = QtGui.QLabel(Dialog)
        self.eRangeLabel.setObjectName(_fromUtf8("eRangeLabel"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.eRangeLabel)
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setMinimumSize(QtCore.QSize(111, 0))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.comboBox)
        self.OKButton = QtGui.QPushButton(Dialog)
        self.OKButton.setObjectName(_fromUtf8("OKButton"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.OKButton)
        self.cancelButton = QtGui.QPushButton(Dialog)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.cancelButton)

        self.setSignals()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def setSignals(self):
        self.OKButton.clicked.connect(self.OK_Signal)
        self.cancelButton.clicked.connect(self.cancel_Signal)

    def OK_Signal(self):
        if self.validateInputs():
            self.saveParams()
            self.accept()
        else:
            alert = QtGui.QMessageBox.warning(self, 'Warning', 'Invalid input value(s).', buttons = QtGui.QMessageBox.Ok, defaultButton = QtGui.QMessageBox.Ok)
            return
    
    def cancel_Signal(self):
        self.meanEdit.setText(str(self.mean))
        self.varianceEdit.setText(str(self.var))
        self.comboBox.setCurrentIndex(self.expRange)
        self.reject()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Z-Test Options", None))
        self.meanEdit.setText(str(self.mean))
        self.varianceEdit.setText(str(self.var))
        self.meanLabel.setText(_translate("Dialog", "Null Variance", None))
        self.varianceLabel.setText(_translate("Dialog", "Sample Variance", None))
        self.comboBox.setItemText(0, _translate("Dialog", "!= (Not Equal)", None))
        self.comboBox.setItemText(1, _translate("Dialog", "< (Less)", None))
        self.comboBox.setItemText(2, _translate("Dialog", "> (Greater)", None))
        self.eRangeLabel.setText(_translate("Dialog", "Expected Range", None))
        self.OKButton.setText(_translate("Dialog", "OK", None))
        self.cancelButton.setText(_translate("Dialog", "Cancel", None))

    def setParams(self, mean, var, expRange):
        self.mean = mean
        self.var = var
        self.expRange = expRange

    def saveParams(self):
        self.mean = float(self.meanEdit.text())
        self.var = float(self.varianceEdit.text())
        self.expRange = self.comboBox.currentIndex()

    def validateInputs(self):
        if self.validator.validate(self.meanEdit.text(), 0)[0] == QtGui.QDoubleValidator.Acceptable:
            if self.validator.validate(self.varianceEdit.text(), 0)[0] == QtGui.QDoubleValidator.Acceptable:
                return True
        return False

# Returns the mean, variance, and the expected range.

    def getParams(self):
        return self.mean, self.var, self.expRange
    
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = ZTestOptionsWindow()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

