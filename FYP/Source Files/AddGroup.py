# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddGroup.ui'
#
# Created: Thu Oct  2 14:18:04 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import Typedef, numpy as np
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

def callAddGroup(dataManager, currentIndex = 0, parent = None):
    ui = Ui_AddGroup(dataManager)
    ui.setup(dataManager, currentIndex)
    result = ui.exec_()
    newGroup = ui.getGroup()
    return newGroup, ui.getColumnIndex(), result == QtGui.QDialog.Accepted

class Ui_AddGroup(QtGui.QDialog):
    
    def __init__(self, dataManager, parent = None):
        super(Ui_AddGroup, self).__init__()
        self.dataManager = dataManager
        self.setupUi(self)
        
    def setup(self, dataManager, index):
        self.dataManager = dataManager
    # Populate the column combo box.
        for i in range(self.dataManager.getNumColumns()):
            self.colCombo.addItem(self.dataManager.getColumnNameOfIndex(i))
        self.colCombo.setCurrentIndex(index)
        self.changeWidgetType()
    
    def getGroupName(self):
        return str(self.nameEdit.text())
    
    def getGroup(self):
        # colCombo.currentIndex is a quick hack. It must be changed in future.
        if self.dataManager.getColTypeByIndex(self.getColumnIndex()) == Typedef.text:
            newGroup = GroupText()
            groupElems = set()
            for i in range(self.elementSelector.count()):
                if self.elementSelector.isItemSelected(self.elementSelector.item(i)):
                    groupElems.add(str(self.elementSelector.item(i).text()))
            newGroup.includedElems = groupElems
            newGroup.setParent(self.dataManager.getColumnByIndex(self.getColumnIndex()))
        elif self.dataManager.getColTypeByIndex(self.getColumnIndex()) == Typedef.numeric:
            newGroup = GroupNum()
            newGroup.setParent(self.dataManager.getColumnByIndex(self.getColumnIndex()))
            newGroup.lessCheck = self.lessThanCheck.checkState()
            if(self.lessThanCheck.checkState()):
                if self.lessThanEdit.text() == '':
                    self.lessThanEdit.setText('0')
                newGroup.lessValue = float(self.lessThanEdit.text())
                newGroup.lessInclude = self.lessThanEquals.checkState()
            newGroup.moreCheck = self.moreThanCheck.checkState()
            if(self.moreThanCheck.checkState()):
                if self.moreThanEdit.text() == '':
                    self.moreThanEdit.setText('0')
                newGroup.moreValue = float(self.moreThanEdit.text())
                newGroup.moreInclude = self.moreThanEquals.checkState()
        newGroup.setName(self.getGroupName())
        return newGroup
        
    def getColumnIndex(self):
        return self.colCombo.currentIndex()
        
    def setupUi(self, AddGroup):
        self.AddGroup = AddGroup
        AddGroup.setObjectName(_fromUtf8("AddGroup"))
        AddGroup.resize(400, 300)
        self.verticalLayoutWidget = QtGui.QWidget(AddGroup)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 401, 301))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.nameLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.nameLabel.setObjectName(_fromUtf8("nameLabel"))
        self.horizontalLayout_4.addWidget(self.nameLabel)
        self.nameEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.nameEdit.setObjectName(_fromUtf8("nameEdit"))
        self.horizontalLayout_4.addWidget(self.nameEdit)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.colLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.colLabel.setObjectName(_fromUtf8("colLabel"))
        self.horizontalLayout.addWidget(self.colLabel)
        self.colCombo = QtGui.QComboBox(self.verticalLayoutWidget)
        self.colCombo.setObjectName(_fromUtf8("colCombo"))
        self.horizontalLayout.addWidget(self.colCombo)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.typeLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.typeLabel.setObjectName(_fromUtf8("typeLabel"))
        self.horizontalLayout_3.addWidget(self.typeLabel)
        self.typeDisplay = QtGui.QLabel(self.verticalLayoutWidget)
        self.typeDisplay.setObjectName(_fromUtf8("typeDisplay"))
        self.horizontalLayout_3.addWidget(self.typeDisplay)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.stackedWidget = QtGui.QStackedWidget(self.verticalLayoutWidget)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.textPage = QtGui.QWidget()
        self.textPage.setObjectName(_fromUtf8("textPage"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.textPage)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(-1, 9, 391, 141))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.selectorLabel = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.selectorLabel.setObjectName(_fromUtf8("selectorLabel"))
        self.verticalLayout_2.addWidget(self.selectorLabel)
        self.elementSelector = QtGui.QListWidget(self.verticalLayoutWidget_2)
        self.elementSelector.setObjectName(_fromUtf8("elementSelector"))
        item = QtGui.QListWidgetItem()
        self.elementSelector.addItem(item)
        item = QtGui.QListWidgetItem()
        self.elementSelector.addItem(item)
        self.verticalLayout_2.addWidget(self.elementSelector)
        self.stackedWidget.addWidget(self.textPage)
        self.numericPage = QtGui.QWidget()
        self.numericPage.setObjectName(_fromUtf8("numericPage"))
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.numericPage)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(-1, 9, 391, 141))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.line = QtGui.QFrame(self.verticalLayoutWidget_3)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_3.addWidget(self.line)
        self.groupRangeTopLabel = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.groupRangeTopLabel.setObjectName(_fromUtf8("groupRangeTopLabel"))
        self.verticalLayout_3.addWidget(self.groupRangeTopLabel)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.moreThanCheck = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.moreThanCheck.setObjectName(_fromUtf8("moreThanCheck"))
        self.horizontalLayout_8.addWidget(self.moreThanCheck)
        self.moreThanEdit = QtGui.QLineEdit(self.verticalLayoutWidget_3)
        self.moreThanEdit.setObjectName(_fromUtf8("moreThanEdit"))
        self.moreThanEdit.setEnabled(False)
        self.horizontalLayout_8.addWidget(self.moreThanEdit)
        self.moreThanEquals = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.moreThanEquals.setObjectName(_fromUtf8("moreThanEquals"))
        self.horizontalLayout_8.addWidget(self.moreThanEquals)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.lessThanCheck = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.lessThanCheck.setObjectName(_fromUtf8("lessThanCheck"))
        self.horizontalLayout_7.addWidget(self.lessThanCheck)
        self.lessThanEdit = QtGui.QLineEdit(self.verticalLayoutWidget_3)
        self.lessThanEdit.setObjectName(_fromUtf8("lessThanEdit"))
        self.lessThanEdit.setEnabled(False)
        self.horizontalLayout_7.addWidget(self.lessThanEdit)
        self.lessThanEquals = QtGui.QCheckBox(self.verticalLayoutWidget_3)
        self.lessThanEquals.setObjectName(_fromUtf8("lessThanEquals"))
        self.horizontalLayout_7.addWidget(self.lessThanEquals)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.stackedWidget.addWidget(self.numericPage)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.dialogButtons = QtGui.QDialogButtonBox(self.verticalLayoutWidget)
        self.dialogButtons.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.dialogButtons.setObjectName(_fromUtf8("dialogButtons"))
        self.verticalLayout.addWidget(self.dialogButtons)
        self.stackedWidget.setCurrentWidget(self.textPage)
        self.changeWidgetType()

        self.retranslateUi(AddGroup)
        self.setSignals()
        
        self.elementSelector.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        
    def setSignals(self):
        QtCore.QObject.connect(self.lessThanCheck, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.lessThanEdit.setEnabled)
        QtCore.QObject.connect(self.moreThanCheck, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.moreThanEdit.setEnabled)
        QtCore.QObject.connect(self.dialogButtons, QtCore.SIGNAL(_fromUtf8("accepted()")), self.AddGroup.accept)
        QtCore.QObject.connect(self.dialogButtons, QtCore.SIGNAL(_fromUtf8("rejected()")), self.AddGroup.reject)
        self.colCombo.currentIndexChanged.connect(self.changeWidgetType)

# ColTypes is assumed to follow Typedef's int values of 'text' and 'numeric'
    def changeWidgetType(self):
        if(self.dataManager.getColTypeByIndex(self.colCombo.currentIndex()) == Typedef.text):
            self.stackedWidget.setCurrentWidget(self.textPage)
            self.typeDisplay.setText('Text')
            self.repopulateElementSelector()
        else:
            self.stackedWidget.setCurrentWidget(self.numericPage)
            self.typeDisplay.setText('Numeric')
        return
    
    def repopulateElementSelector(self):
        self.elementSelector.clear()
        newElements = self.dataManager.getTextSet(self.dataManager.getColumnNameOfIndex(self.getColumnIndex()))
        for elem in newElements:
            self.elementSelector.addItem(elem)
        return
    
    def retranslateUi(self, AddGroup):
        AddGroup.setWindowTitle(_translate("AddGroup", "Add Group", None))
        self.nameLabel.setText(_translate("AddGroup", "Group Name", None))
        self.colLabel.setText(_translate("AddGroup", "Column", None))
        self.typeLabel.setText(_translate("AddGroup", "Datatype of column is:", None))
        self.typeDisplay.setText(_translate("AddGroup", "Numeric", None))
        self.selectorLabel.setText(_translate("AddGroup", "Elements Included in Group:", None))
        self.elementSelector.setSortingEnabled(True)
        self.groupRangeTopLabel.setText(_translate("AddGroup", "Group Range:", None))
        self.lessThanCheck.setText(_translate("AddGroup", "Less Than:", None))
        self.lessThanEquals.setText(_translate("AddGroup", "Inclusive", None))
        self.moreThanCheck.setText(_translate("AddGroup", "More Than:", None))
        self.moreThanEquals.setText(_translate("AddGroup", "Inclusive", None))

class Group:
    
    def __init__(self):
        self.groupName = ''
        self.parent = None
    
    def getName(self):
        return self.groupName
    
    def setName(self, name = ''):
        self.groupName = name
    
    def setParent(self, parent = None):
        self.parent = parent
    
    def printGroup(self):
        return
    
    def compareName(self, string):
        return False
    
    def printCriteria(self):
        return ''
    
    def includedInGroup(self, entry):
        return False
    
class GroupNum(Group):    
    
    def __init__(self, name = '', lessCheck = False, lessValue = 0.0, lessInclude = False, moreCheck = False, moreValue = 0.0, moreInclude = False, parent = None):
        self.groupName = name
        self.lessCheck = lessCheck
        self.lessValue = lessValue
        self.lessInclude = lessInclude
        self.moreCheck = moreCheck
        self.moreValue = moreValue
        self.moreInclude = moreInclude
        self.parent = parent
    
    def __init(self):
        self.groupName = 'newGroup'
        self.lessCheck = False
        self.lessValue = 0.0
        self.lessInclude = False
        self.moreCheck = False
        self.moreValue = 0.0
        self.moreInclude = False
    
    def getName(self):
        return self.groupName
    
    def setParent(self, parent = None):
        self.parent = parent
    
    def compareName(self, string):
        return self.groupName == string
    
    def getParentName(self):
        return self.parent.getName()
    
    def filter(self, data):
        filteredGroup = []
        for entry in data:
            if(self.includedInGroup(entry[self.parent.index])):
                filteredGroup.append(entry)
        return filteredGroup
    
# Print the criteria for display purposes.    
    
    def printCriteria(self):
        criteriaString = ''
        if(self.lessCheck and self.moreCheck):
            criteriaString += 'Between '
            criteriaString += str(self.moreValue)
            criteriaString += ' And '
            criteriaString += str(self.lessValue)
            criteriaString += '.'
        elif (self.lessCheck and not self.moreCheck):
            criteriaString += 'Less Than '
            criteriaString += str(self.lessValue)
            if(self.lessInclude):
                criteriaString += ' Inclusive'
            criteriaString += '.'
        elif (not self.lessCheck and self.moreCheck):
            criteriaString += 'More Than '
            criteriaString += str(self.moreValue)
            if(self.moreInclude):
                criteriaString += ' Inclusive'
            criteriaString += '.'
        return criteriaString
    
    def includedInGroup(self, elem):
        included = True
        elem = float(elem)
        if(self.lessCheck):
            if (self.lessInclude):
                included = elem > self.lessValue
            else:
                included = elem >= self.lessValue
        if(not included):
            return False
        if(self.moreCheck):
            if(self.moreInclude):
                included = elem < self.moreValue
            else:
                included = elem <= self.moreValue
        return included

class GroupText(Group):
    
    def __init__(self, name = 'newGroup', elems = set(), parent = None):
        self.groupName = name
        self.includedElems = elems
        self.parent = parent
    
    def setParent(self, parent = None):
        self.parent = parent
        
    def getName(self):
        return self.groupName
    
    def compareName(self, string):
        return self.groupName == string
    
    def getParentName(self):
        return self.parent.getName()
    
    def printCriteria(self):
        printCriteria = ''
        for elem in self.includedElems:
                printCriteria += elem
                printCriteria += ' '
        return str(printCriteria)
    
    def setElems(self, elemSet):
        self.includedElems = set(elemSet)
    
    def filter(self, data):
        filteredGroup = []
        for entry in data:
            if(self.includedInGroup(entry[self.parent.index])):
                filteredGroup.append(entry)
        return filteredGroup
    
    def includedInGroup(self, elem = ''):
        if elem is not '':
            return elem in self.includedElems
        else:
            return False

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    AddGroup = QtGui.QDialog()
    ui = Ui_AddGroup()
    ui.setupUi(AddGroup)
    AddGroup.show()
    sys.exit(app.exec_())

