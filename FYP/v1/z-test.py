# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z-Test Options.ui'
#
# Created: Wed Sep  3 13:38:08 2014
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

class Ui_ZTestOptions(object):
    def setupUi(self, ZTestOptions):
        ZTestOptions.setObjectName(_fromUtf8("ZTestOptions"))
        ZTestOptions.resize(377, 194)
        self.formLayout = QtGui.QFormLayout(ZTestOptions)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.meanLabel = QtGui.QLabel(ZTestOptions)
        self.meanLabel.setObjectName(_fromUtf8("meanLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.meanLabel)
        self.meanEdit = QtGui.QLineEdit(ZTestOptions)
        self.meanEdit.setObjectName(_fromUtf8("meanEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.meanEdit)
        self.varianceLabel = QtGui.QLabel(ZTestOptions)
        self.varianceLabel.setObjectName(_fromUtf8("varianceLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.varianceLabel)
        self.varianceEdit = QtGui.QLineEdit(ZTestOptions)
        self.varianceEdit.setObjectName(_fromUtf8("varianceEdit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.varianceEdit)
        self.eRangeLabel = QtGui.QLabel(ZTestOptions)
        self.eRangeLabel.setObjectName(_fromUtf8("eRangeLabel"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.eRangeLabel)
        self.comboBox = QtGui.QComboBox(ZTestOptions)
        self.comboBox.setMinimumSize(QtCore.QSize(111, 0))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.comboBox)
        self.OKButton = QtGui.QPushButton(ZTestOptions)
        self.OKButton.setObjectName(_fromUtf8("OKButton"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.OKButton)
        self.cancelButton = QtGui.QPushButton(ZTestOptions)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.cancelButton)

        self.retranslateUi(ZTestOptions)
        QtCore.QObject.connect(self.OKButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ZTestOptions.accept)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ZTestOptions.reject)
        QtCore.QMetaObject.connectSlotsByName(ZTestOptions)

    def retranslateUi(self, ZTestOptions):
        ZTestOptions.setWindowTitle(_translate("ZTestOptions", "Dialog", None))
        self.meanLabel.setText(_translate("ZTestOptions", "Null Mean", None))
        self.varianceLabel.setText(_translate("ZTestOptions", "Null Variance", None))
        self.eRangeLabel.setText(_translate("ZTestOptions", "Expected Range", None))
        self.comboBox.setItemText(0, _translate("ZTestOptions", "!= (Not Equal)", None))
        self.comboBox.setItemText(1, _translate("ZTestOptions", "< (Less)", None))
        self.comboBox.setItemText(2, _translate("ZTestOptions", "> (Greater)", None))
        self.OKButton.setText(_translate("ZTestOptions", "OK", None))
        self.cancelButton.setText(_translate("ZTestOptions", "Cancel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ZTestOptions = QtGui.QDialog()
    ui = Ui_ZTestOptions()
    ui.setupUi(ZTestOptions)
    ZTestOptions.show()
    sys.exit(app.exec_())

