# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'T-Test Options.ui'
#
# Created: Sat Sep  6 14:26:45 2014
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

class Ui_TTestDialog(object):
    def setupUi(self, TTestDialog):
        TTestDialog.setObjectName(_fromUtf8("TTestDialog"))
        TTestDialog.resize(456, 152)
        self.gridLayout = QtGui.QGridLayout(TTestDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.testCombo = QtGui.QComboBox(TTestDialog)
        self.testCombo.setObjectName(_fromUtf8("testCombo"))
        self.testCombo.addItem(_fromUtf8(""))
        self.testCombo.addItem(_fromUtf8(""))
        self.testCombo.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.testCombo, 0, 1, 1, 1)
        self.testLabel = QtGui.QLabel(TTestDialog)
        self.testLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.testLabel.setObjectName(_fromUtf8("testLabel"))
        self.gridLayout_2.addWidget(self.testLabel, 0, 0, 1, 1)
        self.eRangeLabel2 = QtGui.QLabel(TTestDialog)
        self.eRangeLabel2.setObjectName(_fromUtf8("eRangeLabel2"))
        self.gridLayout_2.addWidget(self.eRangeLabel2, 1, 2, 1, 1)
        self.eRangeLabel1 = QtGui.QLabel(TTestDialog)
        self.eRangeLabel1.setAlignment(QtCore.Qt.AlignCenter)
        self.eRangeLabel1.setObjectName(_fromUtf8("eRangeLabel1"))
        self.gridLayout_2.addWidget(self.eRangeLabel1, 1, 0, 1, 1)
        self.eRangeBox = QtGui.QComboBox(TTestDialog)
        self.eRangeBox.setObjectName(_fromUtf8("eRangeBox"))
        self.eRangeBox.addItem(_fromUtf8(""))
        self.eRangeBox.addItem(_fromUtf8(""))
        self.eRangeBox.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.eRangeBox, 1, 1, 1, 1)
        self.OKButton = QtGui.QPushButton(TTestDialog)
        self.OKButton.setObjectName(_fromUtf8("OKButton"))
        self.gridLayout_2.addWidget(self.OKButton, 2, 1, 1, 1)
        self.cancelButton = QtGui.QPushButton(TTestDialog)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.gridLayout_2.addWidget(self.cancelButton, 2, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 1, 1, 1)

        self.retranslateUi(TTestDialog)
        QtCore.QMetaObject.connectSlotsByName(TTestDialog)

    def retranslateUi(self, TTestDialog):
        TTestDialog.setWindowTitle(_translate("TTestDialog", "Dialog", None))
        self.testCombo.setItemText(0, _translate("TTestDialog", "One Sample (Independent)", None))
        self.testCombo.setItemText(1, _translate("TTestDialog", "Paired", None))
        self.testCombo.setItemText(2, _translate("TTestDialog", "Paired Dependent", None))
        self.testLabel.setText(_translate("TTestDialog", "Test Type", None))
        self.eRangeLabel2.setText(_translate("TTestDialog", "Population", None))
        self.eRangeLabel1.setText(_translate("TTestDialog", "Sample is", None))
        self.eRangeBox.setItemText(0, _translate("TTestDialog", "Not the same as", None))
        self.eRangeBox.setItemText(1, _translate("TTestDialog", "Smaller than", None))
        self.eRangeBox.setItemText(2, _translate("TTestDialog", "Larger than", None))
        self.OKButton.setText(_translate("TTestDialog", "OK", None))
        self.cancelButton.setText(_translate("TTestDialog", "Cancel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    TTestDialog = QtGui.QDialog()
    ui = Ui_TTestDialog()
    ui.setupUi(TTestDialog)
    TTestDialog.show()
    sys.exit(app.exec_())

