# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GroupBuilder.ui'
#
# Created: Wed Jan 14 17:50:33 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import Typedef
import GroupSelector as GS
from copy import deepcopy
import numpy as np

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

def callGroupBuilder(dataManager, currentGroup):
    widget = Ui_AddGroup(dataManager, currentGroup)
    result = widget.exec_()
    if result == QtGui.QDialog.Accepted:
        return widget.getDataManager(), widget.getCurrentGroup()
    else:
        return widget.getDataManager(), None

class Ui_AddGroup(QtGui.QDialog):
    
    def __init__(self, dataManager = None, currentGroup = None):
        super(Ui_AddGroup, self).__init__()
        self.setupUi(self)
        self.dataLoaded = False
        self.dataManager = dataManager
        self.currentGroup = currentGroup
        self.textSpacer = None
        self.oldCol = 0
        if self.currentGroup is None:
            self.makeEmptyGroup()
        self.checkboxes = []
        if dataManager is not None:
            self.setupData()
        else:
            print('No Data received.')
    
    # TODO Make sure the groupBuilder behaves all correctly. A lot of bugs now it seems.    
    
    def setupData(self):
    # Setup the column combo.        
        self.colCombo.clear()
        for groupName in self.dataManager.getColumnNames():
            self.colCombo.addItem(groupName)
        self.colCombo.setCurrentIndex(0)
        self.nameEdit.setText(self.currentGroup.getName())
        self.dataLoaded = True
            
    def makeEmptyGroup(self):
        ruleList = []
        defaultName = 'Custom'
        for i in range(self.dataManager.getNumColumns()):
            if self.dataManager.getColType(i) == Typedef.numeric:
                newRule = RuleNum(False, 0.0, False, False, 0.0, False, i, self.dataManager.getColumnNameOfIndex(i))
                ruleList.append(newRule)
            elif self.dataManager.getColType(i) == Typedef.text:
                newRule = RuleText(self.dataManager.getTextSet(self.dataManager.getColumnNameOfIndex(i)), i, self.dataManager.getColumnNameOfIndex(i))
                ruleList.append(newRule)
        #print([x.isEmpty() for x in ruleList])
        self.currentGroup = Group(defaultName, ruleList)
        #print('Printing empty group.')        
        #self.currentGroup.printGroup()
        #print('Empty group printed.')
    
    def setupColumnGroupData(self):
        index = self.colCombo.currentIndex()
        # If the column selected is of type text:
        # Check all the checkboxes whose criteria are included in the group's rule.
        if self.dataManager.getColType(index) == Typedef.text:
            if not self.currentGroup.ruleIsEmpty(index):
                for box in self.checkboxes:
                    #print(box.text())
                    box.setChecked(self.currentGroup.rules[index].includedInGroup(box.text()))
            else:
                for box in self.checkboxes:                    
                    box.setChecked(True)
        # Else if the column is type numeric:
        # Fill in the fields covered by the group's rule.
        elif self.dataManager.getColType(index) == Typedef.numeric:
            if not self.currentGroup.ruleIsEmpty(index):
                numGroup = self.currentGroup.rules[index]
                self.lessThanCheck.setChecked(numGroup.lessCheck)
                if self.lessThanCheck:
                    self.lessThanEdit.setText(str(numGroup.lessValue))
                else:
                    self.lessThanEdit.clear()
                self.lessThanEdit.setEnabled(numGroup.lessCheck)
                self.lessThanEquals.setChecked(numGroup.lessInclude)
                self.lessThanEquals.setEnabled(numGroup.lessCheck)
                self.moreThanCheck.setChecked(numGroup.moreCheck)
                if self.moreThanCheck:
                    self.moreThanEdit.setText(str(numGroup.moreValue))
                else:
                    self.lessThanEdit.clear()
                self.moreThanEdit.setEnabled(numGroup.moreCheck)
                self.moreThanEquals.setChecked(numGroup.moreInclude)
                self.moreThanEquals.setEnabled(numGroup.moreCheck)
            else:
                self.lessThanCheck.setChecked(False)
                self.lessThanEdit.setEnabled(False)
                self.lessThanEdit.setText('0')
                self.lessThanEquals.setEnabled(False)
                self.moreThanCheck.setChecked(False)
                self.moreThanEdit.setEnabled(False)
                self.moreThanEdit.setText('0')
                self.moreThanEquals.setEnabled(False)
            minVal, maxVal = self.getMinAndMaxOfCol()
            self.minValDisp.setText('Min. Value: ' + str(minVal))
            self.maxValDisp.setText('Max. Value: ' + str(maxVal))
    
    def saveColumnToCurrentGroup(self, colNum):
        
        # Find out which checkboxes have been checked, and add their corr. strings
        # To a textSet.
        # Use this textSet and the current colNum to rebuild a new RuleText and
        # replace currentGroup's corr. rule with this new RuleText        
        
        if self.dataManager.getColType(colNum) == Typedef.text:
            textSet = set(box.text() for box in self.checkboxes if box.isChecked())
            self.currentGroup.changeRule(colNum, RuleText(textSet, colNum, self.dataManager.getColumnNameOfIndex(colNum)))
        
        # Retrieve the rule associated with this column number,
        # Replace the fields which are to be changed, and reassign this new rule
        # within the current group.
        
        elif self.dataManager.getColType(colNum) == Typedef.numeric:
            lessCheck = self.lessThanCheck.isChecked()
            if self.isNumeric(self.lessThanEdit.text()):
                lessValue = float(self.lessThanEdit.text())
            lessInclude = self.lessThanEquals.isChecked()
            moreCheck = self.moreThanCheck.isChecked()
            if self.isNumeric(self.moreThanEdit.text()):
                moreValue = float(self.moreThanEdit.text())
            moreInclude = self.moreThanEquals.isChecked()
            
            currentRule = RuleNum(lessCheck, lessValue, lessInclude, moreCheck, moreValue, moreInclude, colNum, self.dataManager.getColumnNameOfIndex(colNum))
            
            self.currentGroup.changeRule(colNum, currentRule)
    
    def populateTextBox(self, colNum):
        # If running for the first time, self.checkboxes should be empty.
        # In any case, this is to clear the checkboxes.
        while self.checkboxes:
            #self.elementArea.removeWidget(self.checkboxes[-1])
            self.checkboxes[-1].deleteLater()
            self.checkboxes.pop()
        # Now we get the new textSet.
        textSet = self.dataManager.getTextSet(self.dataManager.getColumnNameOfIndex(colNum))
        for txt in textSet:
            self.checkboxes.append(QtGui.QCheckBox(txt))
            self.verticalLayout_7.addWidget(self.checkboxes[-1])
            self.checkboxes[-1].show()
        self.verticalLayout_7.removeItem(self.textSpacer)
        self.textSpacer = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(self.textSpacer)
        return
    
    def setupUi(self, AddGroup):
        self.AddGroup = AddGroup
        AddGroup.setObjectName(_fromUtf8("AddGroup"))
        AddGroup.resize(458, 603)
        self.verticalLayout_4 = QtGui.QVBoxLayout(AddGroup)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.saveGroupButton = QtGui.QPushButton(AddGroup)
        self.saveGroupButton.setObjectName(_fromUtf8("saveGroupButton"))
        self.horizontalLayout_6.addWidget(self.saveGroupButton)
        self.loadGroupButton = QtGui.QPushButton(AddGroup)
        self.loadGroupButton.setObjectName(_fromUtf8("loadGroupButton"))
        self.horizontalLayout_6.addWidget(self.loadGroupButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.nameLabel = QtGui.QLabel(AddGroup)
        self.nameLabel.setObjectName(_fromUtf8("nameLabel"))
        self.horizontalLayout_4.addWidget(self.nameLabel)
        self.nameEdit = QtGui.QLineEdit(AddGroup)
        self.nameEdit.setObjectName(_fromUtf8("nameEdit"))
        self.horizontalLayout_4.addWidget(self.nameEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.colLabel = QtGui.QLabel(AddGroup)
        self.colLabel.setObjectName(_fromUtf8("colLabel"))
        self.horizontalLayout.addWidget(self.colLabel)
        self.colCombo = QtGui.QComboBox(AddGroup)
        self.colCombo.setObjectName(_fromUtf8("colCombo"))
        self.horizontalLayout.addWidget(self.colCombo)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.typeLabel = QtGui.QLabel(AddGroup)
        self.typeLabel.setObjectName(_fromUtf8("typeLabel"))
        self.horizontalLayout_3.addWidget(self.typeLabel)
        self.typeDisplay = QtGui.QLabel(AddGroup)
        self.typeDisplay.setObjectName(_fromUtf8("typeDisplay"))
        self.horizontalLayout_3.addWidget(self.typeDisplay)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line_2 = QtGui.QFrame(AddGroup)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.stackedWidget = QtGui.QStackedWidget(AddGroup)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.textPage = QtGui.QWidget()
        self.textPage.setObjectName(_fromUtf8("textPage"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.textPage)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.selectorLabel = QtGui.QLabel(self.textPage)
        self.selectorLabel.setObjectName(_fromUtf8("selectorLabel"))
        self.verticalLayout_2.addWidget(self.selectorLabel)
        self.elementArea = QtGui.QScrollArea(self.textPage)
        self.elementArea.setWidgetResizable(True)
        self.elementArea.setObjectName(_fromUtf8("elementArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 408, 320))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.elementArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.elementArea)
        self.verticalLayout_6.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.selectAllTextButton = QtGui.QPushButton(self.textPage)
        self.selectAllTextButton.setObjectName(_fromUtf8("selectAllTextButton"))
        self.horizontalLayout_2.addWidget(self.selectAllTextButton)
        self.unselectAllTextButton = QtGui.QPushButton(self.textPage)
        self.unselectAllTextButton.setObjectName(_fromUtf8("unselectAllTextButton"))
        self.horizontalLayout_2.addWidget(self.unselectAllTextButton)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.stackedWidget.addWidget(self.textPage)
        self.numericPage = QtGui.QWidget()
        self.numericPage.setObjectName(_fromUtf8("numericPage"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.numericPage)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupRangeTopLabel = QtGui.QLabel(self.numericPage)
        self.groupRangeTopLabel.setObjectName(_fromUtf8("groupRangeTopLabel"))
        self.verticalLayout_3.addWidget(self.groupRangeTopLabel)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.lessThanCheck = QtGui.QCheckBox(self.numericPage)
        self.lessThanCheck.setObjectName(_fromUtf8("lessThanCheck"))
        self.horizontalLayout_7.addWidget(self.lessThanCheck)
        self.lessThanEdit = QtGui.QLineEdit(self.numericPage)
        self.lessThanEdit.setObjectName(_fromUtf8("lessThanEdit"))
        self.horizontalLayout_7.addWidget(self.lessThanEdit)
        self.lessThanEquals = QtGui.QCheckBox(self.numericPage)
        self.lessThanEquals.setObjectName(_fromUtf8("lessThanEquals"))
        self.horizontalLayout_7.addWidget(self.lessThanEquals)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.moreThanCheck = QtGui.QCheckBox(self.numericPage)
        self.moreThanCheck.setObjectName(_fromUtf8("moreThanCheck"))
        self.horizontalLayout_8.addWidget(self.moreThanCheck)
        self.moreThanEdit = QtGui.QLineEdit(self.numericPage)
        self.moreThanEdit.setObjectName(_fromUtf8("moreThanEdit"))
        self.horizontalLayout_8.addWidget(self.moreThanEdit)
        self.moreThanEquals = QtGui.QCheckBox(self.numericPage)
        self.moreThanEquals.setObjectName(_fromUtf8("moreThanEquals"))
        self.horizontalLayout_8.addWidget(self.moreThanEquals)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.line = QtGui.QFrame(self.numericPage)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_5.addWidget(self.line)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.minValDisp = QtGui.QLabel(self.numericPage)
        self.minValDisp.setObjectName(_fromUtf8("minValDisp"))
        self.horizontalLayout_5.addWidget(self.minValDisp)
        self.maxValDisp = QtGui.QLabel(self.numericPage)
        self.maxValDisp.setObjectName(_fromUtf8("maxValDisp"))
        self.horizontalLayout_5.addWidget(self.maxValDisp)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.stackedWidget.addWidget(self.numericPage)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.dialogButtons = QtGui.QDialogButtonBox(AddGroup)
        self.dialogButtons.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.dialogButtons.setObjectName(_fromUtf8("dialogButtons"))
        self.verticalLayout.addWidget(self.dialogButtons)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.actionSave_Group = QtGui.QAction(AddGroup)
        self.actionSave_Group.setObjectName(_fromUtf8("actionSave_Group"))

        self.retranslateUi(AddGroup)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.lessThanCheck, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.lessThanEdit.setEnabled)
        QtCore.QObject.connect(self.moreThanCheck, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.moreThanEdit.setEnabled)
        QtCore.QObject.connect(self.dialogButtons, QtCore.SIGNAL(_fromUtf8("accepted()")), self.saveAndExit)
        QtCore.QObject.connect(self.dialogButtons, QtCore.SIGNAL(_fromUtf8("rejected()")), AddGroup.reject)
        QtCore.QMetaObject.connectSlotsByName(AddGroup)

        self.setSignals()


    def getCurrentGroup(self):
        self.currentGroup.setName(self.nameEdit.text())
        return self.currentGroup
    
    def setSignals(self):
        self.colCombo.currentIndexChanged.connect(self.changeColumn)
        self.saveGroupButton.clicked.connect(self.saveGroup)
        self.loadGroupButton.clicked.connect(self.loadGroup)
        self.selectAllTextButton.clicked.connect(self.selectAllText)
        self.unselectAllTextButton.clicked.connect(self.unselectAllText)
    
    def printDictionary(self):
        print("The Dictionary is currently:")
        for group in self.dataManager.getGroups().values():
            group.printGroup()     
    
    def loadGroup(self):
        loadedGroup = GS.callGroupSelector(self.dataManager.getGroups())
        if loadedGroup is not None:
            self.currentGroup = loadedGroup
            self.nameEdit.setText(self.currentGroup.getName())
            self.setupColumnGroupData()
        else:
            print('No Group returned.')
        return
        
    def saveAndExit(self):
        self.saveColumnToCurrentGroup(self.colCombo.currentIndex())
        self.currentGroup.setName(self.nameEdit.text())
        #print(self.nameEdit.text() + 'vs' + self.currentGroup.getName())
        self.AddGroup.accept()        
        
    def saveGroup(self):
        if self.nameEdit.text():
            self.saveColumnToCurrentGroup(self.colCombo.currentIndex())
            self.currentGroup.setName(self.nameEdit.text())
            groupToSave = deepcopy(self.currentGroup)
            self.dataManager.addGroup(self.nameEdit.text(), groupToSave)
            
            msgString = 'Group "' + self.nameEdit.text() + '" has been saved.'        
            
            QtGui.QMessageBox.warning(self.AddGroup, 'Group Saved', msgString, buttons = QtGui.QMessageBox.Ok, defaultButton = QtGui.QMessageBox.Ok)

            
            #print('Saving group: ' + groupToSave.getName() + '...')
            #groupToSave.printGroup()
            #print("Group " + groupToSave.getName() + " Saved!")
    
    def selectAllText(self):
        for box in self.checkboxes:
            box.setChecked(True)
    
    def unselectAllText(self):
        for box in self.checkboxes:
            box.setChecked(False)
    
    def changeColumn(self):
        index = self.colCombo.currentIndex()
        if self.dataLoaded:
            # If the statement is already loaded, we must save the data currently
            # on the column onto the current group.
            self.saveColumnToCurrentGroup(self.oldCol)
        # Once the data is saved, then we can start the switching.
        if self.dataManager.getColType(index) == Typedef.text:
            self.stackedWidget.setCurrentWidget(self.textPage)
            self.typeDisplay.setText('Text')
            self.populateTextBox(index)
        else:
            self.stackedWidget.setCurrentWidget(self.numericPage)
            self.typeDisplay.setText('Numeric')
        self.setupColumnGroupData()
        self.oldCol = self.colCombo.currentIndex()

    def getMinAndMaxOfCol(self):
        if self.dataManager.getColType(self.colCombo.currentIndex()) == Typedef.text:
            return None, None
        array = np.array([float(x[self.colCombo.currentIndex()]) for x in self.dataManager.entries])
        return np.min(array), np.max(array)
    
    def getDataManager(self):
        return self.dataManager
    
    def isNumeric(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def retranslateUi(self, AddGroup):
        AddGroup.setWindowTitle(_translate("AddGroup", "Form", None))
        self.saveGroupButton.setText(_translate("AddGroup", "Save Group", None))
        self.loadGroupButton.setText(_translate("AddGroup", "Load Group", None))
        self.nameLabel.setText(_translate("AddGroup", "Group Name", None))
        self.colLabel.setText(_translate("AddGroup", "Column", None))
        self.typeLabel.setText(_translate("AddGroup", "Datatype of column is:", None))
        self.typeDisplay.setText(_translate("AddGroup", "Numeric", None))
        self.selectorLabel.setText(_translate("AddGroup", "Elements Included in Group:", None))
        self.selectAllTextButton.setText(_translate("AddGroup", "Select All", None))
        self.unselectAllTextButton.setText(_translate("AddGroup", "Unselect All", None))
        self.groupRangeTopLabel.setText(_translate("AddGroup", "Group Range:", None))
        self.lessThanCheck.setText(_translate("AddGroup", "Less Than:", None))
        self.lessThanEquals.setText(_translate("AddGroup", "Inclusive", None))
        self.moreThanCheck.setText(_translate("AddGroup", "More Than:", None))
        self.moreThanEquals.setText(_translate("AddGroup", "Inclusive", None))
        self.minValDisp.setText(_translate("AddGroup", "Min. Value: 123", None))
        self.maxValDisp.setText(_translate("AddGroup", "Max. Value: 456", None))
        self.actionSave_Group.setText(_translate("AddGroup", "Save Group", None))
        self.actionSave_Group.setToolTip(_translate("AddGroup", "<html><head/><body><p>Save your current filter for use later.</p></body></html>", None))
        self.actionSave_Group.setShortcut(_translate("AddGroup", "Ctrl+S", None))

class Group:
    
# Each group contains a list of rules, ordered according to their corresponding column index.    

# Each rule can be either Text type or Num type.
# All rules come with an 'empty' boolean var which is used to determine if they are empty.
# When a group's rule changes, the whole rule has to be reassigned within the list.  
    def __init__(self, name, rules):
        self.groupName = name
        self.rules = rules
        
    def changeRule(self,index, newRule):
        if index < len(self.rules):
            self.rules[index] = newRule
            
    def getName(self):
        return self.groupName
        
    def setName(self, name):
        self.groupName = name

# Filter receives a list of entries, and filters them all according to the criteria
# stored within its rules.
    def filter(self, data):
        for rule in self.rules:
            if not rule.isEmpty():
                data = rule.filter(data)
        return data
    
    def getSetOfRuleIndices(self):
        retSet = set([rule.getColNum() for rule in self.rules if not rule.isEmpty()])
        print(retSet)
        return retSet
    
    def getRules(self):
        return self.rules
    
    def ruleIsEmpty(self, colNum):
        return self.rules[colNum].isEmpty()
        
    def printGroup(self):
        print("Group " + self.groupName)
        if not self.rules:
            print ('No Rules inside.')
        else:
            for rule in self.rules:
                print(rule.printCriteria())
                
    def isEqualTo(self, group):
        for i in range(len(self.rules)):
            if not self.rules[i].isEqualTo(group.getRules()[i]):
                break
        else:
            return False
        return True
    
    

class Rule:    
    
    def __init__(self):
        self.colNum = 0
        self.empty = True
        self.colName = ''
    
    def __init(self, colNum):
        self.colNum = colNum
        self.empty = True
    
    def setIsEmpty(self):
        self.empty = True
    
    def isEmpty(self):
        return self.empty

    def getColNum(self):
        return self.colNum                
    
    def setColNum(self, colNum):
        self.colNum = colNum
        
    def getColName(self):
        return self.colName
        
    def printGroup(self):
        return
    
    #def printCriteria(self):
    #    return ''
    
    def includedInGroup(self, entry):
        return False
    
    def isEqualTo(self, rule):
        return False
    
    def filter(self, data):
        return [entry for entry in data if self.includedInGroup(entry[self.colNum])]
    
class RuleNum(Rule):    
    
    def __init__(self, lessCheck, lessValue, lessInclude, moreCheck, moreValue, moreInclude, colNum, colName):
        self.lessCheck = lessCheck
        self.lessValue = lessValue
        self.lessInclude = lessInclude
        self.moreCheck = moreCheck
        self.moreValue = moreValue
        self.moreInclude = moreInclude
        self.colNum = colNum
        self.colName = colName
        self.setIsEmpty()
    
    def __init(self, colNum, colName):
        self.lessCheck = False
        self.lessValue = 0.0
        self.lessInclude = False
        self.moreCheck = False
        self.moreValue = 0.0
        self.moreInclude = False
        self.colNum = colNum
        self.colName = colName
        self.empty = True
       
    
    def isEqualTo(self, rule):
        if type(rule) is not RuleNum:
            return False
        if self.colNum != rule.colNum:
            return False
        if self.empty != rule.empty:
            return False
        if self.lessCheck != rule.lessCheck:
            return False
        if self.lessCheck:
            if self.lessValue != rule.lessValue:
                return False
            if self.lessInclude != rule.lessInclude:
                return False
        if self.moreCheck != rule.moreCheck:
            return False
        if self.moreCheck:
            if self.moreValue != rule.moreValue:
                return False
            if self.moreInclude != rule.moreInclude:
                return False
        return True
    
    def setIsEmpty(self):
        self.empty = True if not self.lessCheck and not self.moreCheck else False
    

# Print the criteria for display purposes.     
    
    def printCriteria(self):
        if self.isEmpty():
            return 'No rule.'
        criteriaString = ''
        #print(str(self.lessCheck))
        #print(str(self.moreCheck))
        if(self.lessCheck and self.moreCheck):
            criteriaString += 'Between '
            criteriaString += str(self.moreValue)
            if self.lessInclude:
                criteriaString += ' inclusive'
            criteriaString += ' And '
            criteriaString += str(self.lessValue)
            if self.moreInclude:
                criteriaString += ' inclusive'
            criteriaString += '.'
        elif (self.lessCheck and not self.moreCheck):
            criteriaString += 'Less Than '
            criteriaString += str(self.lessValue)
            if(self.lessInclude):
                criteriaString += ' Inclusive'
            criteriaString += '.'
        elif(not self.lessCheck and self.moreCheck):
            criteriaString += 'More Than '
            criteriaString += str(self.moreValue)
            if(self.moreInclude):
                criteriaString += ' Inclusive'
            criteriaString += '.'
        return criteriaString
    
    def includedInGroup(self, elem):
        # If the rule is empty, by default there is no rule applied.
        # Return true.
        if self.isEmpty():
            return True
        included = True
        try:        
            elem = float(elem)
        except ValueError:
            print('Value Error. Non-numeric string parsed into RuleNum.')
        elem = float(elem)
        if self.lessCheck:
            if self.lessInclude:
                included = elem <= self.lessValue
            else:
                included = elem < self.lessValue
        if not included:
            return False
        if self.moreCheck:
            if self.moreInclude:
                included = elem >= self.moreValue
            else:
                included = elem > self.moreValue
        return included

class RuleText(Rule):
    
    def __init__(self, elems, colNum, colName):
        self.includedElems = elems
        self.colNum = colNum
        self.colName = colName
        self.empty = False
    
    def __init(self, colNum, colName):
        self.groupName = 'newGroup'
        self.includedElems = set()
        self.colNum = colNum
        self.colName = colName
        self.empty = True

    def setIsEmpty(self):
        return False
    
    def isEqualTo(self, rule):
        if type(rule) is not RuleText:
            return False
        if self.colNum != rule.colNum:
            return False
        return not (self.includedElems ^ rule.includedElems)
    
    def printCriteria(self):
        if self.empty:
            return 'No Rule.'
        printCriteria = '['
        for elem in self.includedElems:
            printCriteria += elem
            printCriteria += ' '
        printCriteria += ']'
        return printCriteria
    
    def includedInGroup(self, elem):
        # If there is no rule then by default the element is included.
        if self.isEmpty():
            return True
        if elem:
            #print(self.includedElems)
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

