# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddGroupNumeric.ui'
#
# Created: Mon Sep 29 15:54:09 2014
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
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.columnLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.columnLabel.setObjectName(_fromUtf8("columnLabel"))
        self.horizontalLayout_2.addWidget(self.columnLabel)
        self.columnCombo = QtGui.QComboBox(self.verticalLayoutWidget)
        self.columnCombo.setObjectName(_fromUtf8("columnCombo"))
        self.horizontalLayout_2.addWidget(self.columnCombo)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.groupNameLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.groupNameLabel.setObjectName(_fromUtf8("groupNameLabel"))
        self.horizontalLayout_3.addWidget(self.groupNameLabel)
        self.groupNameCombo = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.groupNameCombo.setObjectName(_fromUtf8("groupNameCombo"))
        self.horizontalLayout_3.addWidget(self.groupNameCombo)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.groupRangeTopLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.groupRangeTopLabel.setObjectName(_fromUtf8("groupRangeTopLabel"))
        self.verticalLayout.addWidget(self.groupRangeTopLabel)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lessThanLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.lessThanLabel.setObjectName(_fromUtf8("lessThanLabel"))
        self.horizontalLayout_4.addWidget(self.lessThanLabel)
        self.lessThanEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lessThanEdit.setObjectName(_fromUtf8("lessThanEdit"))
        self.horizontalLayout_4.addWidget(self.lessThanEdit)
        self.lessThanCheck = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.lessThanCheck.setObjectName(_fromUtf8("lessThanCheck"))
        self.horizontalLayout_4.addWidget(self.lessThanCheck)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.moreThanLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.moreThanLabel.setObjectName(_fromUtf8("moreThanLabel"))
        self.horizontalLayout_5.addWidget(self.moreThanLabel)
        self.moreThanEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.moreThanEdit.setObjectName(_fromUtf8("moreThanEdit"))
        self.horizontalLayout_5.addWidget(self.moreThanEdit)
        self.moreThanCheck = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.moreThanCheck.setObjectName(_fromUtf8("moreThanCheck"))
        self.horizontalLayout_5.addWidget(self.moreThanCheck)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.buttonBox = QtGui.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.columnLabel.setText(_translate("Form", "Column: ", None))
        self.groupNameLabel.setText(_translate("Form", "Group Name: ", None))
        self.groupRangeTopLabel.setText(_translate("Form", "Group Range:", None))
        self.lessThanLabel.setText(_translate("Form", "Less Than: ", None))
        self.lessThanCheck.setText(_translate("Form", "Inclusive", None))
        self.moreThanLabel.setText(_translate("Form", "More Than:", None))
        self.moreThanCheck.setText(_translate("Form", "Inclusive", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

