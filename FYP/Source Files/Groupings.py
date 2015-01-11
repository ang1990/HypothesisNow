# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Groupings.ui'
#
# Created: Mon Sep 29 15:54:53 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import numpy as np
import copy
import Typedef, AddGroup

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

# This function is called whenever the Groupings Widget is activated.

def callGroupings(dataManager, parent = None):
    widget = Ui_Dialog()
    widget.setup(dataManager)
    result = widget.exec_()
    if result == QtGui.QDialog.Accepted:
        dataManager = widget.updateData()
    return dataManager

class Ui_Dialog(QtGui.QDialog):    
 
    def __init__(self, parent = None):
        super(Ui_Dialog, self).__init__()
        self.dataManager = None
        self.setupUi(self)
    
    def updateData(self):
        return self.dataManager
    
    def setup(self, dataManager):
        self.dataManager = copy.deepcopy(dataManager)
        self.changeDatatypeDisplay()
        self.setupCombos()
    
    def setupCombos(self):
        self.columnCombo.clear()
        for i in range(self.dataManager.getNumColumns()):
            self.columnCombo.addItem(self.dataManager.getColumnNameOfIndex(i))
    
    def changeDatatypeDisplay(self):
        if self.dataManager.getColTypeByIndex(self.columnCombo.currentIndex()) == Typedef.numeric:
            self.DatatypeDisplay.setText(Typedef.numTypeDisplay)
        elif self.dataManager.getColTypeByIndex(self.columnCombo.currentIndex()) == Typedef.text:
            self.DatatypeDisplay.setText(Typedef.textTypeDisplay)
    
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
        self.setSignals()

    def setSignals(self):
        self.addGroupButton.clicked.connect(self.addGroup)
        self.columnCombo.currentIndexChanged.connect(self.updateTable)
        self.columnCombo.currentIndexChanged.connect(self.changeDatatypeDisplay)
        self.removeGroupButton.clicked.connect(self.removeGroups)

    def removeGroups(self):
        itemsToRemove = self.GroupingsTable.selectedIndexes()
        rowsToRemove = []
        for item in itemsToRemove:
            rowsToRemove.append(item.row())
            print item.row()
        self.dataManager.getColumnByIndex(self.columnCombo.currentIndex()).removeGroupsByIndex(rowsToRemove)
        self.updateTable()

    def addGroup(self):
        newGroup, colIndex, accepted = AddGroup.callAddGroup(self.dataManager, self.columnCombo.currentIndex())
        if accepted:
            self.dataManager.getColumnByIndex(colIndex).addGroup(newGroup)
        #self.printColGroups()
        self.updateTable()
        
    def printColGroups(self):
        for i in range(len(self.colGroups)):
            print self.dataManager.getColumnByIndex(i).getName()
            self.dataManager.getColumnByIndex(i).printData()

    def updateTable(self):
        groupNames, groupCriteria = self.dataManager.getColumnByIndex(self.columnCombo.currentIndex()).getGroupNamesAndCriteria()
        print groupNames
        print groupCriteria
        print 'Printed~!'
        if groupNames is not None:
            self.GroupingsTable.clearContents()
            self.GroupingsTable.setColumnCount(2)
            self.GroupingsTable.setRowCount(len(groupNames))
            for i in range(len(groupNames)):
                self.GroupingsTable.setItem(i,0,QtGui.QTableWidgetItem(groupNames[i]))
                self.GroupingsTable.setItem(i,1,QtGui.QTableWidgetItem(groupCriteria[i]))

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Groupings Menu", None))
        self.columnLabel.setText(_translate("Dialog", "Column", None))
        self.DatatypeLabel.setText(_translate("Dialog", "Datatype", None))
        self.DatatypeDisplay.setText(_translate("Dialog", "Numeric", None))
        item = self.GroupingsTable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Set Name", None))
        item = self.GroupingsTable.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Set Cover", None))
        __sortingEnabled = self.GroupingsTable.isSortingEnabled()
        self.GroupingsTable.setSortingEnabled(False)
        self.addGroupButton.setText(_translate("Dialog", "Add Group", None))
        self.removeGroupButton.setText(_translate("Dialog", "Remove Selected Groups", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

# Data Manager class.

class DataManager:
    
    # DataManager stores:
    # columnNames as a list, each name is ordered according to the order it appears in the CSV.
    # This makes for easy calling of indexes, hence the list form.
    
    # colTypes as a numpy array. A list could be used as well, but this implementation works fine.
    
    # Entries as a list of lists. All items within are strings.
    
    # columnData as a dictionary, keys being column names and values being ColumnData objects.
    
    # textSets as a dictionary, similar to columnData, only values being the set of elements that can be found in
    # the respective column.
    
    def __init__(self, columnNames, colTypes, columnData, entries, textSets):
        self.columnData = columnData
        self.colTypes = colTypes
        self.columnNames = columnNames
        self.entries = entries
        self.textSets = textSets
        
    def __init(self):
        self.columnData = {}
        self.colTypes = np.zeros(1)
        self.columnNames = []
        self.textSets = {}

    def getAllGroups(self):
        groupList = []
        for col in self.columnData:
            groupList.extend(self.columnData[col].getGroups())
        return groupList

    def getNumColumns(self):
        return len(self.columnNames)

    def getColumn(self, name = ''):
        return self.columnData[name]
    
    def getColumnByIndex(self, index = 0):
        return self.columnData[self.columnNames[index]]

    def removeGroupsInColumn(self, columnIndex, groupIndexList):
        self.getColumnByIndex(columnIndex).removeGroupsByIndex(groupIndexList)
        
    def getColumnNameOfIndex(self, index):
        return self.columnNames[index]

    def getColTypeByIndex(self, index):
        return self.colTypes[index]

    def getTextSet(self, setName):
        if self.textSets.has_key(setName):
            return self.textSets[setName]
        else:
            return None

    def getAllTextSets(self):
        return self.textSets

# ColumnData class.

class ColumnData:
    
    def printData(self):
        for i in range(len(self.groups)):
            print 'Group: ' + self.groups[i].getName()
            print self.groups[i].printCriteria()    
    
    def __init__(self, index = 0, colType = Typedef.numeric, name = ''):
        self.index = index
        self.type = type
        self.groups = []
        self.name = name

    def getGroups(self):
        return self.groups
    
    def getName(self):
        return self.name
    
    def getColType(self):
        return self.colType
    
    def getIndex(self):
        return self.index

    def addGroup(self, newGroup):
        index = self.findGroup(newGroup)
        if(index == -1):
            self.groups.append(newGroup)
        else:
            self.groups[index] = newGroup

    def findGroup(self, candidate):
        for i in range(len(self.groups)):
            if candidate.getName() == self.groups[i].getName():
                return i
        return -1
    
    def findGroupByName(self, name):
        for i in range(len(self.groups)):
            if name == self.groups[i].getName():
                return i
        return -1

    def removeGroupsByIndex(self, indices = []):
        if len(indices) > 0:
            indices = list(set(indices))
            indices.sort()
            print indices
            while len(indices) > 0:
                element = indices.pop()
                self.groups.pop(element)

    def removeGroupByName(self, groupName = ''):
        index = self.findGroupByName(groupName)
        if(index != -1):
            del self.groups[index]
        
    # This is for the table's display.
    # We will need the groups' names and criteria. They will be returned as 2 lists of strings, bundled together
    # in the return statement.    

    def getGroupNames(self):
        groupNames = []
        for group in self.groups:
            groupNames.append(group.getName())
        return groupNames

    def getGroupNamesAndCriteria(self):
        groupNames = []
        groupCriteria = []
        for i in range(len(self.groups)):
            groupNames.append(self.groups[i].getName())
            groupCriteria.append(self.groups[i].printCriteria())
        return groupNames, groupCriteria
    
    # filterByGroup will take input entries, and return only the set of entries that fit the group criteria.
    # The filtering will be performed by the group class.
    
    def filter(self, data, groupName):
        filteredGroup = []
        group = self.findGroupByName(groupName)
        for entry in data:
            if(self.groups[group].includedInGroup(entry[self.index])):
                filteredGroup.append(entry)
        return filteredGroup
    