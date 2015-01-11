# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StatementGroups.ui'
#
# Created: Tue Oct 21 01:06:12 2014
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

def callStatementGroupings(groupList):
    widget = Ui_Dialog(groupList)
    result = widget.exec_()
    sampleGroupList = widget.getGroupList()
    return sampleGroupList if result == QtGui.QDialog.Accepted else []
    
class Ui_Dialog(QtGui.QDialog):
    
    def __init__(self, groupList):
        super(Ui_Dialog, self).__init__()
        self.groupList = groupList
        self.setupUi(self)
        
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
        self.clearSelectionButton = QtGui.QToolButton(Dialog)
        self.clearSelectionButton.setObjectName(_fromUtf8("clearSelectionButton"))
        self.verticalLayout.addWidget(self.clearSelectionButton)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.clearSelectionButton.clicked.connect(self.clearSelection)
        
        self.setupList()

    def clearSelection(self):
        self.groupSelector.clearSelection()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.topLabel.setText(_translate("Dialog", "Select the groups you want for the sample:", None))
        self.clearSelectionButton.setText(_translate("Dialog", "Remove all Groups", None))

    def setupList(self):
        for group in self.groupList:
            displayName = group.getName() + '(' + group.getParentName() + ')'
            self.groupSelector.addItem(displayName)
    
    def getGroupList(self):
        indexList = self.groupSelector.selectedIndexes()
        indexes = []
        for index in indexList:
            indexes.append(index.row())
        indexes.sort()
        print indexes
        print 'Indexes printed.'
        actualList = []
        for i in indexes:
            actualList.append(self.groupList[i])
        return actualList
        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

