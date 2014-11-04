# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StatementGroups.ui'
#
# Created: Fri Oct 24 19:23:20 2014
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.topLabel = QtGui.QLabel(Dialog)
        self.topLabel.setObjectName(_fromUtf8("topLabel"))
        self.verticalLayout.addWidget(self.topLabel)
        self.groupSelector = QtGui.QListWidget(Dialog)
        self.groupSelector.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.groupSelector.setObjectName(_fromUtf8("groupSelector"))
        self.verticalLayout.addWidget(self.groupSelector)
        self.toolButton = QtGui.QToolButton(Dialog)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.verticalLayout.addWidget(self.toolButton)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.topLabel.setText(_translate("Dialog", "Select the groups you want for the sample:", None))
        self.toolButton.setText(_translate("Dialog", "Remove all Groups", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

