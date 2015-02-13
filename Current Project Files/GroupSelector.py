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

# Currently getSelectedGroup is taking only the group at the top of the list.
# I'm not sure why.

# TODO: Need to figure this out.

def callGroupSelector(groupDict):
    widget = Ui_Dialog(groupDict)
    #print (type(groupDict))
    #for group in groupDict.values():
        #print(group.getName() + ':')
        #group.printGroup()
    result = widget.exec_()
    if result == QtGui.QDialog.Accepted:
        #group = widget.getSelectedGroup()
        #print(group.getName() + ' was taken.')
        return widget.getSelectedGroup()
    else:
        return None

class Ui_Dialog(QtGui.QDialog):
    
    def __init__(self, groups):
        super(Ui_Dialog, self).__init__()
        self.groups = groups
        self.setupUi(self)
        self.setupList()
    
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.topLabel = QtGui.QLabel(Dialog)
        self.topLabel.setObjectName(_fromUtf8("topLabel"))
        self.verticalLayout.addWidget(self.topLabel)
        self.groupSelector = QtGui.QListWidget(Dialog)
        self.groupSelector.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.groupSelector.setObjectName(_fromUtf8("groupSelector"))
        self.verticalLayout.addWidget(self.groupSelector)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def clearSelection(self):
        self.groupSelector.clearSelection()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Group Select", None))
        self.topLabel.setText(_translate("Dialog", "Select the group you want to load:", None))

    def setupList(self):
        for groupName in self.groups.keys():
            self.groupSelector.addItem(groupName)
    
    def getSelectedGroup(self):
        #print ('Group ' + self.groupSelector.currentItem().text() + ' selected.')
        return self.groups[self.groupSelector.currentItem().text()]
    
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

