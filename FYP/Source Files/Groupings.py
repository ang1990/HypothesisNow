# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Groupings.ui'
#
# Created: Sat Oct  4 12:41:30 2014
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
        Dialog.resize(465, 481)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.columnLabel = QtGui.QLabel(Dialog)
        self.columnLabel.setObjectName(_fromUtf8("columnLabel"))
        self.horizontalLayout.addWidget(self.columnLabel)
        self.columnCombo = QtGui.QComboBox(Dialog)
        self.columnCombo.setObjectName(_fromUtf8("columnCombo"))
        self.horizontalLayout.addWidget(self.columnCombo)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.DatatypeLabel = QtGui.QLabel(Dialog)
        self.DatatypeLabel.setObjectName(_fromUtf8("DatatypeLabel"))
        self.horizontalLayout_3.addWidget(self.DatatypeLabel)
        self.DatatypeDisplay = QtGui.QLabel(Dialog)
        self.DatatypeDisplay.setObjectName(_fromUtf8("DatatypeDisplay"))
        self.horizontalLayout_3.addWidget(self.DatatypeDisplay)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.GroupingsTable = QtGui.QTableWidget(Dialog)
        self.GroupingsTable.setObjectName(_fromUtf8("GroupingsTable"))
        self.GroupingsTable.setColumnCount(2)
        self.GroupingsTable.setRowCount(3)
        item = QtGui.QTableWidgetItem()
        self.GroupingsTable.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.GroupingsTable.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.GroupingsTable.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.GroupingsTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.GroupingsTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.GroupingsTable.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.GroupingsTable.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.GroupingsTable.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.GroupingsTable.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        self.GroupingsTable.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        self.GroupingsTable.setItem(2, 1, item)
        self.verticalLayout.addWidget(self.GroupingsTable)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.addGroupButton = QtGui.QPushButton(Dialog)
        self.addGroupButton.setObjectName(_fromUtf8("addGroupButton"))
        self.horizontalLayout_4.addWidget(self.addGroupButton)
        self.removeGroupButton = QtGui.QPushButton(Dialog)
        self.removeGroupButton.setObjectName(_fromUtf8("removeGroupButton"))
        self.horizontalLayout_4.addWidget(self.removeGroupButton)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
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
        self.columnLabel.setText(_translate("Dialog", "Column", None))
        self.DatatypeLabel.setText(_translate("Dialog", "Datatype", None))
        self.DatatypeDisplay.setText(_translate("Dialog", "Numeric", None))
        item = self.GroupingsTable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Set Name", None))
        item = self.GroupingsTable.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Set Cover", None))
        __sortingEnabled = self.GroupingsTable.isSortingEnabled()
        self.GroupingsTable.setSortingEnabled(False)
        item = self.GroupingsTable.item(0, 0)
        item.setText(_translate("Dialog", "Young", None))
        item = self.GroupingsTable.item(0, 1)
        item.setText(_translate("Dialog", "Less than 12", None))
        item = self.GroupingsTable.item(1, 0)
        item.setText(_translate("Dialog", "Adult", None))
        item = self.GroupingsTable.item(1, 1)
        item.setText(_translate("Dialog", "12 to 55", None))
        item = self.GroupingsTable.item(2, 0)
        item.setText(_translate("Dialog", "Senior", None))
        item = self.GroupingsTable.item(2, 1)
        item.setText(_translate("Dialog", "Above 55", None))
        self.GroupingsTable.setSortingEnabled(__sortingEnabled)
        self.addGroupButton.setText(_translate("Dialog", "Add Group", None))
        self.removeGroupButton.setText(_translate("Dialog", "Remove Selected Group", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

