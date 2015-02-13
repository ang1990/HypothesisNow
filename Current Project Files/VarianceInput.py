# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'varianceInput.ui'
#
# Created: Wed Jan 28 19:31:48 2015
#      by: PyQt4 UI code generator 4.11.3
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

def callVarianceInput(meanVal, sampleString):
    widget = Ui_Dialog(meanVal, sampleString)
    result = widget.exec_()
    if result == QtGui.QDialog.Accepted:
        return widget.getVariance()
    else:
        return meanVal

class Ui_Dialog(QtGui.QDialog):
    
    def __init__(self, meanVal, sampleString):
        super(Ui_Dialog, self).__init__()
        self.mean = meanVal
        self.sampleString = sampleString
        self.setupUi(self)
        self.varEdit.setText(str(meanVal))
    
    def getVariance(self):
        return float(self.varEdit.text())
    
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(298, 102)
        self.Dialog = Dialog
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.varLabel = QtGui.QLabel(Dialog)
        self.varLabel.setObjectName(_fromUtf8("varLabel"))
        self.verticalLayout.addWidget(self.varLabel)
        self.varEdit = QtGui.QLineEdit(Dialog)
        self.varEdit.setObjectName(_fromUtf8("varEdit"))
        self.verticalLayout.addWidget(self.varEdit)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.acceptDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Set the Variance", None))
        self.varLabel.setText(_translate("Dialog", "Please set a variance for " + self.sampleString + " (Default is " + str(self.mean) + ")", None))
        self.varEdit.setText(str(self.mean))

    def acceptDialog(self):
        if self.isNumeric(self.varEdit.text()):
            self.Dialog.accept()
        else:
            QtGui.QMessageBox.warning(self.Dialog, 'Warning', 'Invalid variance input.', buttons = QtGui.QMessageBox.Ok, defaultButton = QtGui.QMessageBox.Ok)


    def isNumeric(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog(0, 'ABC')
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

