# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddGroupText.ui'
#
# Created: Mon Sep 29 15:54:21 2014
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
        Form.resize(400, 300)
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 401, 301))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.columnLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.columnLabel.setObjectName(_fromUtf8("columnLabel"))
        self.horizontalLayout.addWidget(self.columnLabel)
        self.columnCombo = QtGui.QComboBox(self.verticalLayoutWidget)
        self.columnCombo.setObjectName(_fromUtf8("columnCombo"))
        self.horizontalLayout.addWidget(self.columnCombo)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.nameLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.nameLabel.setObjectName(_fromUtf8("nameLabel"))
        self.horizontalLayout_2.addWidget(self.nameLabel)
        self.nameEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.nameEdit.setObjectName(_fromUtf8("nameEdit"))
        self.horizontalLayout_2.addWidget(self.nameEdit)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.elementsTopLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.elementsTopLabel.setObjectName(_fromUtf8("elementsTopLabel"))
        self.verticalLayout.addWidget(self.elementsTopLabel)
        self.elementList = QtGui.QListWidget(self.verticalLayoutWidget)
        self.elementList.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.elementList.setObjectName(_fromUtf8("elementList"))
        item = QtGui.QListWidgetItem()
        self.elementList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.elementList.addItem(item)
        self.verticalLayout.addWidget(self.elementList)
        self.buttonBox = QtGui.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.columnLabel.setText(_translate("Form", "Column Name: ", None))
        self.nameLabel.setText(_translate("Form", "Group Name: ", None))
        self.elementsTopLabel.setText(_translate("Form", "Elements that the group contains:", None))
        __sortingEnabled = self.elementList.isSortingEnabled()
        self.elementList.setSortingEnabled(False)
        item = self.elementList.item(0)
        item.setText(_translate("Form", "M", None))
        item = self.elementList.item(1)
        item.setText(_translate("Form", "F", None))
        self.elementList.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

