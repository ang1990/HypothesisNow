# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StatementBuilder.ui'
#
# Created: Wed Oct  1 15:45:12 2014
#      by: PyQt4 UI code generator 4.11.1
#

from PyQt4 import QtCore, QtGui
import Typedef
import GroupBuilder as GB
import Parser
import VarianceInput

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

def callBuilder(dataManager, stmt = None):
    widget = Ui_Form(dataManager)
    widget.setup(stmt)
    result = widget.exec_()
    if result == QtGui.QDialog.Accepted:
        return widget.getGroups(), widget.getStatement()
    return None, None

class Ui_Form(QtGui.QDialog):
    
    def __init__(self, dataManager = None):
        super(Ui_Form, self).__init__()
        self.dataManager = dataManager
        self.setupUi(self)
        self.loaded = False
        self.expNumVal = 0
        self.parser = Parser.Parser(dataManager)
        self.setupCompleter()
        self.AGroup = None
        self.BGroup = None
        self.variance1 = None
        self.variance2 = None
   
    def setWidget(self, testType):
        self.testType = testType
        self.stackedWidget.setCurrentIndex(testType)
    
    def setup(self, stmt = None):
        if stmt is not None:
            self.setupStmt(stmt)
        else:
            self.setBlankStmt()
        self.loaded = True

    def setBlankStmt(self):
        self.expNumVal = 0
        self.AGroup = None
        self.BGroup = None
    
    def setupCompleter(self):
        completer = QtGui.QCompleter()
        self.AExpEdit.setCompleter(completer)
        self.BExpEdit.setCompleter(completer)
        model = QtGui.QStringListModel()
        completer.setModel(model)
        model.setStringList(self.dataManager.getColumnNames())
        
    
    def setupStmt(self, stmt):
        self.AExpEdit.setText(stmt.getLHSInfix())
        self.BExpEdit.setText(stmt.getRHSInfix())
        self.expNumVal = Typedef.compExps.index(stmt.getExpression())
        self.compDisp.setText(_translate("Form", Typedef.compStrings[self.expNumVal], None))
        LGroup = stmt.getLHSGroup()
        if LGroup:
            self.AGroupDisp.setText(LGroup.getName())
        else:
            self.AGroupDisp.setText('All data.')
        RGroup = stmt.getRHSGroup()
        if RGroup:
            self.BGroupDisp.setText(RGroup.getName())
        else:
            self.BGroupDisp.setText('All data.')
    
    def setupUi(self, Form):
        self.Form = Form
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(834, 193)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.ATopDisp = QtGui.QLabel(Form)
        self.ATopDisp.setObjectName(_fromUtf8("ATopDisp"))
        self.horizontalLayout.addWidget(self.ATopDisp, QtCore.Qt.AlignHCenter)
        self.compTopDisp = QtGui.QLabel(Form)
        self.compTopDisp.setObjectName(_fromUtf8("compTopDisp"))
        self.horizontalLayout.addWidget(self.compTopDisp, QtCore.Qt.AlignHCenter)
        self.BTopDisp = QtGui.QLabel(Form)
        self.BTopDisp.setObjectName(_fromUtf8("BTopDisp"))
        self.horizontalLayout.addWidget(self.BTopDisp, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.AExpLabel = QtGui.QLabel(Form)
        self.AExpLabel.setObjectName(_fromUtf8("AExpLabel"))
        self.horizontalLayout_2.addWidget(self.AExpLabel)
        self.AExpEdit = QtGui.QLineEdit(Form)
        self.AExpEdit.setObjectName(_fromUtf8("AExpEdit"))
        self.horizontalLayout_2.addWidget(self.AExpEdit)
        self.compDisp = QtGui.QLabel(Form)
        self.compDisp.setObjectName(_fromUtf8("compDisp"))
        self.horizontalLayout_2.addWidget(self.compDisp)
        self.BExpLabel = QtGui.QLabel(Form)
        self.BExpLabel.setObjectName(_fromUtf8("BExpLabel"))
        self.horizontalLayout_2.addWidget(self.BExpLabel)
        self.BExpEdit = QtGui.QLineEdit(Form)
        self.BExpEdit.setObjectName(_fromUtf8("BExpEdit"))
        self.horizontalLayout_2.addWidget(self.BExpEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.AGroupLabel = QtGui.QLabel(Form)
        self.AGroupLabel.setObjectName(_fromUtf8("AGroupLabel"))
        self.horizontalLayout_3.addWidget(self.AGroupLabel)
        self.AGroupDisp = QtGui.QLabel(Form)
        self.AGroupDisp.setObjectName(_fromUtf8("AGroupDisp"))
        self.horizontalLayout_3.addWidget(self.AGroupDisp)
        self.AGroupButton = QtGui.QPushButton(Form)
        self.AGroupButton.setObjectName(_fromUtf8("AGroupButton"))
        self.horizontalLayout_3.addWidget(self.AGroupButton)
        self.compButton = QtGui.QPushButton(Form)
        self.compButton.setObjectName(_fromUtf8("compButton"))
        self.horizontalLayout_3.addWidget(self.compButton)
        self.BGroupLabel = QtGui.QLabel(Form)
        self.BGroupLabel.setObjectName(_fromUtf8("BGroupLabel"))
        self.horizontalLayout_3.addWidget(self.BGroupLabel)
        self.BGroupDisp = QtGui.QLabel(Form)
        self.BGroupDisp.setObjectName(_fromUtf8("BGroupDisp"))
        self.horizontalLayout_3.addWidget(self.BGroupDisp)
        self.BGroupButton = QtGui.QPushButton(Form)
        self.BGroupButton.setObjectName(_fromUtf8("BGroupButton"))
        self.horizontalLayout_3.addWidget(self.BGroupButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.varDispButton = QtGui.QPushButton(Form)
        self.varDispButton.setObjectName(_fromUtf8("varDispButton"))
        self.horizontalLayout_4.addWidget(self.varDispButton)
        self.buttonBox = QtGui.QDialogButtonBox(Form)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_4.addWidget(self.buttonBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.acceptDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Form.reject)  
        
        self.setSignals()
    
    def setSignals(self):
        self.compButton.clicked.connect(self.changeCompExp)
        self.AGroupButton.clicked.connect(self.changeClass)
        self.BGroupButton.clicked.connect(self.changeClass)
        self.varDispButton.clicked.connect(self.showVarNameWindow)
        return
    
    def showVarNameWindow(self):
        varNames = self.dataManager.getColumnNames()
        msgString = 'The following variables can be used as part of the expression:\n\n'
        for var in varNames:
            if self.dataManager.getColType(var) == Typedef.numeric:
                msgString += var + '\n'
        QtGui.QMessageBox.warning(self.Form, 'Note', msgString, buttons = QtGui.QMessageBox.Ok, defaultButton = QtGui.QMessageBox.Ok)

    
    def changeCompExp(self):
        self.expNumVal = (self.expNumVal + 1) % 4
        self.compDisp.setText(_translate("Form", Typedef.compStrings[self.expNumVal], None))
        #print(self.expNumVal)
        
    # Call StatementGroupings to change the classes here.        
    
    def acceptDialog(self):
        error = self.verifyExpressions()
        if error is not None:
            QtGui.QMessageBox.warning(self.Form, 'Warning', error, buttons = QtGui.QMessageBox.Ok, defaultButton = QtGui.QMessageBox.Ok)
            return
        sample1HasVars = any(token in self.dataManager.getColumnNames() for token in self.parser.parse(self.AExpEdit.text()))
        sample2HasVars = any(token in self.dataManager.getColumnNames() for token in self.parser.parse(self.BExpEdit.text()))
        if not sample1HasVars and not sample2HasVars:
            self.form.accept()
            return
        if not sample1HasVars:
            self.variance1 = 0
            self.variance1 = VarianceInput.callVarianceInput(self.variance1, 'Sample 1')
        if not sample2HasVars:
            self.variance2 = 0
            self.variance2 = VarianceInput.callVarianceInput(self.variance2, 'Sample 2')
        self.Form.accept()
        


    # TODO: Verify that expressions are parseable and contain valid variable names.

    def verifyExpressions(self):
        error = self.parser.verifyExpression(self.AExpEdit.text())
        if error is not None:
            error = 'Error detected in Sample A expression.\n' + error
            return error
        error = self.parser.verifyExpression(self.BExpEdit.text())
        if error is not None:
            error = 'Error detected in Sample B expression.\n' + error
            return error
        return None            

    def changeClass(self):
        #print(self.dataManager.columnNames)
        if self.sender() == self.AGroupButton:
            self.dataManager, group = GB.callGroupBuilder(self.dataManager, self.AGroup)
            if group:
                self.AGroup = group
                self.AGroupDisp.setText(self.AGroup.getName())
                #print(self.AGroup.getName())
            return
        elif self.sender() == self.BGroupButton:
            self.dataManager, group = GB.callGroupBuilder(self.dataManager, self.BGroup)
            if group:
                self.BGroup = group
                self.BGroupDisp.setText(self.BGroup.getName())
            return
        
    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Statement Builder", None))
        self.ATopDisp.setText(_translate("Form", "SAMPLE A", None))
        self.compTopDisp.setText(_translate("Form", "COMPARED TO", None))
        self.BTopDisp.setText(_translate("Form", "SAMPLE B", None))
        self.AExpLabel.setText(_translate("Form", "Expression", None))
        self.AExpEdit.setPlaceholderText(_translate("Form", "Eg. (ABC + 123) * 456", None))
        self.compDisp.setText(_translate("Form", "IS GREATER THAN", None))
        self.BExpLabel.setText(_translate("Form", "Expression", None))
        self.BExpEdit.setPlaceholderText(_translate("Form", "Eg. (ABC + 123) * 456", None))
        self.AGroupLabel.setText(_translate("Form", "Group:", None))
        self.AGroupDisp.setText(_translate("Form", "All Data", None))
        self.AGroupButton.setText(_translate("Form", "Change Group", None))
        self.compButton.setText(_translate("Form", "Click to Change", None))
        self.BGroupLabel.setText(_translate("Form", "Group:", None))
        self.BGroupDisp.setText(_translate("Form", "All Data", None))
        self.BGroupButton.setText(_translate("Form", "Change Group", None))
        self.varDispButton.setText(_translate("Form", "Click here to see available column variables", None))
  
    def getGroups(self):
        return self.dataManager.getGroups()
    
    def getStatement(self):
        AInfix = self.AExpEdit.text()
        BInfix = self.BExpEdit.text()
        ATokens = self.parser.parse(self.AExpEdit.text())
        BTokens = self.parser.parse(self.BExpEdit.text())
        AGroup = self.AGroup
        BGroup = self.BGroup
        expression = Typedef.compExps[self.expNumVal]
        varA = self.variance1
        varB = self.variance2
        return Statement(AInfix, BInfix, ATokens, expression, BTokens, AGroup, BGroup, varA, varB)
    
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QDialog()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

class Statement(object):
    
    def __init__(self, AInfix, BInfix, ATokens, exp, BTokens, AGroup, BGroup, varA = 0, varB = 0):
        self.AInfix = AInfix
        self.BInfix = BInfix
        self.ATokens = ATokens
        self.expression = exp
        self.BTokens = BTokens
        self.AGroup = AGroup
        self.BGroup = BGroup
        self.varianceA = varA
        self.varianceB = varB
    

    def containsVars(self, tokens):
        return any(token[0].isalpha() for token in tokens)

    def getLHSInfix(self):
        return self.AInfix
        
    def getRHSInfix(self):
        return self.BInfix

    def getLHSTokens(self):
        return self.ATokens
    
    def getExpression(self):
        return self.expression
    
    def getRHSTokens(self):
        return self.BTokens
        
    def getLHSGroup(self):
        return self.AGroup
        
    def getRHSGroup(self):
        return self.BGroup
        
    def getVarA(self):
        return self.varianceA

    def getVarB(self):
        return self.varianceB        
        
        
    def getStmtPrint(self):
        expDispString = ''
        if self.AGroup is not None:
            expDispString = '#' + self.AGroup.getName()
        expDispString += '('
        expDispString += self.AInfix + ') '     
        
        expDispString += self.getExpression() + ' '

        if self.BGroup is not None:
            expDispString += '#' + self.BGroup.getName()
        expDispString += '('
        expDispString += self.BInfix + ')'

        return expDispString