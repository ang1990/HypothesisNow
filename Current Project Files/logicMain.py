'''
Created on 1 Sep, 2014

@author: Mark Ang Yan Sheng
'''

import csv
import Typedef
import numpy as np
from Typedef import DataManager, TestResultZ, TestResultT
from GroupBuilder import Group, Rule, RuleNum, RuleText
from copy import deepcopy
import scipy.stats as st

# LogicMain performs the following jobs:

# 1. Process the incoming CSV file.
#    The Column names, column types, and entry data is collected from the CSV file. They are placed in a DataManager
#    class, through which all calls to data have to go through.

# 2. Perform the tests.
#    The logic must take statements from StatementBuilder (via main class) and use those statements to perform the
#    relevant tests.

class logicMain(object):

    stmt = ''
    textSets = {}
    columns = []
    colTypes = np.zeros(1)
    columnNames = []
    dataManager = None
    #parser = Parser()
    expression = ''
    operators = ['+', '-', '*', '/']
    removeOutliersCheck = False
    testType = None
    ZMean = 0
    ZVar = 0
    ZSampleIsLHS = False
    minSampleLength = 5
    

    def setMinSampleLength(self, val):
        self.minSampleLength = val    
    
    def setRemoveOutliers(self, state):
        self.removeOutliersCheck = state
        
    def getRemoveOutliers(self):
        return self.removeOutliersCheck
    
    def setSampleData(self, fName):
        self.processSample(fName)
    '''
    Function: processSample
    processSample takes the raw text from the sample file (Expected to be in CSV form).
    Expected Input:
    1st Row:            Names of columns
    2nd Row onwards:    Entries with values for each column. If actual values do not exist in the data,
                        pre-processing to set the value as zero or some special value is required.
    Expected Output:
    columns:            List of columnData classes containing all the necessary column data.
    entries:            Entries given in the data.
    textSets:           Sets representing all available strings in the corr. column.
                        It is represented as a dictionary. Key - ColumnName, Val - Corr. set.
    
    NOTE: NOTHING IS RETURNED TO CALLER. CALLER MUST GET DATA MANAGER THROUGH GET CALLS.
    '''
    def processSample(self, fName):
        reader = csv.reader(open(fName, 'rU'))
        self.entries = [line for line in reader if line]
        columnNames = self.entries.pop(0)
    # Now we figure out the types of data present in each column.
        self.entries = [x for x in self.entries if len(x) == len(columnNames)]
        colTypes = []
        for i in range(len(columnNames)):
            colTypes.append(Typedef.numeric if all([self.isNumeric(x[i]) for x in self.entries]) else Typedef.text)
        # Handle element sets here.
        for i in range(len(columnNames)):
            if colTypes[i] == Typedef.text:
                self.textSets[columnNames[i]] = set(entry[i] for entry in self.entries)
        #print columnNames
        #print colTypes
        #print len(self.entries)
        #print self.textSets
        self.columnNames = columnNames
        self.colTypes = colTypes
        #print(self.colTypes)
    
    # Getter functions for main use.
    
    def getDataManager(self):
        return DataManager(self.columnNames, self.colTypes, self.entries, self.textSets)
    
    # The validation print function assumes that the statement is fully loaded in logicMain
    # before it is called.
    
    def getValidationPrint(self):
        validationPrint = ''
        sample1 = self.filterEntries(self.entries, self.g1)
        if not self.sampleIsNormal(sample1):
            validationPrint += "Take care, the Left-Hand Side's sample size is too small to assume normal distribution.\n"
        sample2 = self.filterEntries(self.entries, self.g2)
        if not self.sampleIsNormal(sample2):
            validationPrint += "Take care, the Right-Hand Side's sample size is too small to assume normal distribution.\n"
        if validationPrint:
            return validationPrint
        else:
            return 'Your test is OK.'
    
    
    def getEntries(self):
        return self.entries
    
    def getTextSets(self):
        return self.textSets
    
    def updateDataManager(self, dataManager):
        self.dataManager = dataManager

    # main will call this to set the new test expression.
        
    def setStmt(self, stmt):
        self.stmt = stmt
        self.g1 = stmt.getLHSGroup()
        self.g2 = stmt.getRHSGroup()
        self.LHSTokens = stmt.getLHSTokens()
        self.RHSTokens = stmt.getRHSTokens()
        self.expression = stmt.getExpression()
        self.var1 = stmt.getVarA()
        print(str(self.var1))
        self.var2 = stmt.getVarB()
        print(str(self.var2))
        self.determineTestType()
        #print(self.LHSTokens)
        #print(self.expression)
        #print(self.RHSTokens)

    # This function determines the type of test to perform.
    # If both LHS and RHS contain column variables, we use the T-Test.
    # If either LHS or RHS does not contain column variables, we use the Z-Test.
    # If neither LHS nor RHS contains column variables, we can just calculate the answer.
    
    def determineTestType(self):
        lHasVars = any(token in self.columnNames for token in self.LHSTokens)
        rHasVars = any(token in self.columnNames for token in self.RHSTokens)
    # If both sides have vars, we use the T-test.
        if lHasVars and rHasVars:
            self.testType = Typedef.typeT
    # If LHS has vars but not RHS, we use the Z-Test with population as RHS.
    # There's an XOR implementation to combine the following 2 elif statements, but we will keep it this
    # way for clarity.
        elif lHasVars and not rHasVars:
            self.testType = Typedef.typeZ
            self.ZSampleIsLHS = True
            self.ZMean = self.evalExpression(None, self.RHSTokens)
            self.ZVar = self.var2
        elif not lHasVars and rHasVars:
            self.testType = Typedef.typeZ
            self.ZSampleIsLHS = False
            self.ZMean = self.evalExpression(None, self.LHSTokens)
            self.ZVar = self.var1
        elif not lHasVars and not rHasVars:
            self.testType = Typedef.typeCalc
    
    
    # A sample is assumed to be normal if, after removing outliers (Quantities are default):
    # 
    # 1. The sample size is greater than 40.
    #
    # 2. The sample size is greater than 15, is unimodal (Only 1 peak)
    #    and can be considered symmetric (Has low skew).
    
    def sampleIsNormal(self, sample):
        samplesOK = True
        if not sample:
            return False
        for i in range(len(self.columnNames)):
            if self.colTypes[i] == Typedef.numeric:
                array = np.array([float(entry[i]) for entry in sample])
                if self.removeOutliersCheck:
                    array = self.removeOutliers(array)
                if len(array) < Typedef.normalUnsafe:
                    samplesOK = False
                    break
            # If the sample size is greater than 40, by Central Limit Theorem we can
            # assume the sample to follow normal distribution.
                if len(array) > Typedef.normalSafe:
                    continue
                elif len(array) > Typedef.normalUnsafe:
                # Test for skewness.
                    if st.skewtest(array)[1] < Typedef.skewThreshold:
                        samplesOK = False
                        break
                # Test for unimodality:
                    skew = st.skew(array)
                    kurtosis = st.kurtosis(array)
                    if (np.square(skew) - kurtosis) > Typedef.unimodalityThreshold:
                        samplesOK = False
                        break
        return samplesOK
            
       
    # To remove outliers we use Grubb's test for outliers iteratively until
    # The test cannot detect any more outliers.
       
    # This version is for 1D numpy arrays, for full entry sets, we use
    # removeOutliersInCol.
   
    def removeOutliers(self, array):
        if not self.removeOutliersCheck:
            print('Error! removeOutliers called incorrectly.')
            return array
        array = np.sort(array)
        originalLen = len(array)
        while len(array) > 0:
            mean = np.mean(array)
            stdev = np.std(array)
            if st.norm.cdf((mean - array[0]) / stdev) > Typedef.grubbsThreshold:
                array = array[1:]
                print('Min Value removed.')
                continue
            if st.norm.cdf((array[-1] - mean) / stdev) > Typedef.grubbsThreshold:
                array = array[:-1]
                print('Max Value removed.')
                continue
            break
        
        print(str(originalLen - len(array)) + ' outliers removed.')
        if len(array) > 0:
            #print(str(originalLen - len(array)) + ' outliers removed.')
            return array
        else:
            return None
    
    def removeOutliersInCol(self, entries, colNum):
        if not self.removeOutliersCheck:
            print('Error! removeOutliers called incorrectly.')
            return entries
        entries = sorted(entries, key = lambda x: float(x[colNum]), reverse = False)
        originalLen = len(entries)
        
        # This implementation may become inefficient for larger datasets.
        # Consider an in-place function.        
        
        array = np.array([float(entry[colNum]) for entry in entries])
        while len(array) > 0:
            mean = np.mean(array)
            stdev = np.std(array)
            if st.norm.cdf((mean - array[0]) / stdev) > Typedef.grubbsThreshold:
                array = array[1:]
                entries = entries[1:]
                continue
            if st.norm.cdf((array[-1] - mean) / stdev) > Typedef.grubbsThreshold:
                array = array[:-1]
                entries = entries[:-1]
                continue
            break
        
        print(str(originalLen - len(array)) + ' outliers removed.')
        if len(array) > 0:
            print(str(originalLen - len(array)) + ' outliers removed.')
            return entries
        else:
            return None
    
   
    # Perform the test here.

    def performTest(self):
        
        # TODO: Complete Z Test implementation. Make use of the variance in stmts.
        if self.testType == Typedef.typeZ:
            sample = self.filterEntries(self.entries, self.g1 if self.ZSampleIsLHS else self.g2)
            splitRuleListList = self.checkSplitsZ(sample)
            return self.recZTest(sample, self.ZMean, self.ZVar, splitRuleListList, [])
        elif self.testType == Typedef.typeT:    
            sample1 = self.filterEntries(self.entries, self.g1)
            sample2 = self.filterEntries(self.entries, self.g2)
        # This is where we figure out which groups require splitting.          
            splitRuleListList = self.checkSplitsT(sample1, sample2)
        
    # In order to stratify effectively, we must implement a "dynamic" function.
        
        printResultList = self.recTTest(sample1, sample2, splitRuleListList, [])
        return printResultList

    def filterEntries(self, entries, group):
        sample = entries
        if type(group) is Group:
            sample = group.filter(sample)            
            if self.removeOutliersCheck:
                for i in range(len(self.columnNames)):
                    if self.colTypes[i] == Typedef.numeric:
                        sample = self.removeOutliersInCol(sample, i)
            if not sample:
                return []
        elif type(group) is Rule or type(group) is RuleNum or type(group) is RuleText:
            sample = group.filter(sample)
            if self.removeOutliersCheck:
                sample = self.removeOutliersInCol(sample, group.getColNum())
            if not sample:
                return []
        return sample

    def checkSplitsZ(self, sample):
        ruleListList = []
        # For each column, we must determine what rules to split by.
        ruleList = []                
        
        # We have to remove all the variables that exist within the expression.
        # So we find all these variables and place their indices in an exclude list.

        tokens = self.LHSTokens if self.ZSampleIsLHS else self.RHSTokens
        group = self.g1 if self.ZSampleIsLHS else self.g2

        excludeIndices = self.getExpVarIndices(tokens)
        
        colStatus = [Typedef.include] * len(self.columnNames)
        for i in excludeIndices:
            colStatus[i] = Typedef.exclude
        
        # Now we decide how to split based on the rules already present on the sample.

        textGroupList = []
        
        # If the rule is of type text:
        # We keep the elements included by the rule for later use.

        # If the rule is of type numeric:
        # We exclude this column entirely. # TODO: THIS MAY CHANGE.        
        if group:
            rules = [rule for rule in group.getRules() if not rule.isEmpty()]
            for rule in rules:
                if type(rule) is RuleText:
                    colStatus[rule.getColNum()] = Typedef.textset
                    textGroupList.append([rule.getColNum(), rule.includedElems])
                    # If the rule is of type numeric, we automatically exclude it.
                elif type(rule) is RuleNum:
                    colStatus[rule.getColNum()] = Typedef.exclude

        # After deciding which columns are excluded and all, we can proceed based on
        # that information.

        print(colStatus)
        if textGroupList:
            print(textGroupList)

        for i in range(len(colStatus)):
            if colStatus[i] == Typedef.include:
                ruleList.clear()
                if self.dataManager.getColType(i) == Typedef.numeric:
                    numList = np.array([float(entry[i]) for entry in sample])
                    # First handle the lower quartile:
                    lowerQuartRule = RuleNum(True, np.percentile(numList,25), True, False, 0.0, False, i, self.dataManager.getColumnNameOfIndex(i))
                    ruleList.append(lowerQuartRule)
                    # Then we handle the inter-quartile range:
                    IQRange = RuleNum(True, np.percentile(numList, 75), False, True, np.percentile(numList, 25), False, i, self.dataManager.getColumnNameOfIndex(i))
                    ruleList.append(IQRange)
                    # Finally, we handle the upper quartile.
                    upperQuartRule = RuleNum(False, 0.0, False, True, np.percentile(numList,75), True, i, self.dataManager.getColumnNameOfIndex(i))
                    ruleList.append(upperQuartRule)
                elif self.dataManager.getColType(i) == Typedef.text:
                    for elem in self.textSets[self.columnNames[i]]:
                    # Just add a rule corr. to each element in the list.
                    # Remember to check for a sig. mean diff and verify that there will
                    # be differences!
                        ruleToAdd = RuleText(set(elem), i, self.dataManager.getColumnNameOfIndex(i))
                        if self.verifyMeanDiff(sample, ruleToAdd):
                            ruleList.append(ruleToAdd)
            #for rule in ruleList:
            #    print(rule.getColNum())
                ruleListList.append(deepcopy(ruleList))
            #print('length of ruleListList: ' + str(len(ruleListList)))
            elif colStatus[i] == Typedef.textset:
                for textGroup in textGroupList:
                    if textGroup[0] == i:
                        for elem in textGroup[1]:
                    # Just add a rule corr. to each element in the list.
                    # Remember to check for a sig. mean diff and verify that there will
                    # be differences!
                            ruleToAdd = RuleText(set(elem), i, self.dataManager.getColumnNameOfIndex(i))
                            if self.verifyMeanDiff(sample, ruleToAdd):
                                ruleList.append(ruleToAdd)
        return ruleListList


# TODO: Need to work out all the APIs.

    # This function takes sample1 and sample2, and returns a list of lists of rules.
    # Each list of rules represents the set of rules for the columns which the
    # hypothesis can use to make it more 'specific'.

    # Each rule must first be verified to produce significantly different means
    # BEFORE adding into the list. #[Optimization. We can work on this later.]

    def checkSplitsT(self, sample1, sample2):
        ruleListList = []
        # For each column, we must determine what rules to split by.
        ruleList = []                
        
        # We have to remove all the variable that exist within the expression.
        # So we find all these variables and place their indices in an exclude list.

        excludeIndices = self.getExpVarIndices(self.LHSTokens)        
        excludeIndices |= self.getExpVarIndices(self.RHSTokens)
        
        colStatus = [Typedef.include] * len(self.columnNames)
        for i in excludeIndices:
            colStatus[i] = Typedef.exclude
        
        # Now we decide how to split based on the rules already present on both samples.

        textGroupList = []
        
        # If the rule is of type text:
        # We keep the elements included by the rule for later use.

        # If the rule is of type numeric:
        # We exclude this column entirely. # TODO: THIS MAY CHANGE.        
        if self.g1:
            rules1 = [rule for rule in self.g1.getRules() if not rule.isEmpty()]
            for rule in rules1:
                if type(rule) is RuleText:
                    colStatus[rule.getColNum()] = Typedef.textset
                    textGroupList.append([rule.getColNum(), rule.includedElems])
                    # If the rule is of type numeric, we automatically exclude it.
                elif type(rule) is RuleNum:
                    colStatus[rule.getColNum()] = Typedef.exclude
        
        # Same thing for rules2, but this time, we have to consider the textsets
        # obtained from rules1.        
        if self.g2:
            rules2 = [rule for rule in self.g2.getRules() if not rule.isEmpty()]
            for rule in rules2:
                if type(rule) is RuleText:
                    if colStatus[rule.getColNum()] == Typedef.textset:
                        for textGroup in textGroupList:
                            if textGroup[0] == rule.getColNum():
                                textGroup[1] -= (textGroup[1] ^ rule.includedElems)
                                if not textGroup[1]:
                                    colStatus[rule.getColNum()] = Typedef.exclude
                elif type(rule) is RuleNum:
                    colStatus[rule.getColNum()] = Typedef.exclude


        # After deciding which column is excluded and all, we can proceed based on
        # that information.

        print(colStatus)
        if textGroupList:
            print(textGroupList)
        

        for i in range(len(colStatus)):
            if colStatus[i] == Typedef.include:
                ruleList.clear()
                if self.dataManager.getColType(i) == Typedef.numeric:
                    numList = np.array([float(entry[i]) for entry in sample1])
                    # First handle the lower quartile:
                    lowerQuartRule = RuleNum(True, np.percentile(numList,25), True, False, 0.0, False, i, self.dataManager.getColumnNameOfIndex(i))
                    ruleList.append(lowerQuartRule)
                    # Then we handle the inter-quartile range:
                    IQRange = RuleNum(True, np.percentile(numList, 75), False, True, np.percentile(numList, 25), False, i, self.dataManager.getColumnNameOfIndex(i))
                    ruleList.append(IQRange)
                    # Finally, we handle the upper quartile.
                    upperQuartRule = RuleNum(False, 0.0, False, True, np.percentile(numList,75), True, i, self.dataManager.getColumnNameOfIndex(i))
                    ruleList.append(upperQuartRule)
                elif self.dataManager.getColType(i) == Typedef.text:
                    for elem in self.textSets[self.columnNames[i]]:
                    # Just add a rule corr. to each element in the list.
                    # Remember to check for a sig. mean diff and verify that there will
                    # be differences!
                        ruleToAdd = RuleText(set(elem), i, self.dataManager.getColumnNameOfIndex(i))
                        print(ruleToAdd.printCriteria())
                        #if self.verifyMeanDiff(sample1, ruleToAdd) or self.verifyMeanDiff(sample2, ruleToAdd):
                        ruleList.append(ruleToAdd)
            #for rule in ruleList:
            #    print(rule.getColNum())
                ruleListList.append(deepcopy(ruleList))
            #print('length of ruleListList: ' + str(len(ruleListList)))
            elif colStatus[i] == Typedef.textset:
                for textGroup in textGroupList:
                    if textGroup[0] == i:
                        for elem in textGroup[1]:
                    # Just add a rule corr. to each element in the list.
                    # Remember to check for a sig. mean diff and verify that there will
                    # be differences!
                            ruleToAdd = RuleText(set(elem), i, self.dataManager.getColumnNameOfIndex(i))
                            #if self.verifyMeanDiff(sample1, ruleToAdd) or self.verifyMeanDiff(sample2, ruleToAdd):
                            ruleList.append(ruleToAdd)
                            
        return ruleListList

    def getExpVarIndices(self, tokens):
        columnSet = set()
        for token in tokens:
            if token in self.columnNames:
                columnSet.add(self.dataManager.getColumnIndexOfName(token))
        return columnSet
        
    # This section verifies that the samples will churn out significant mean
    # differences when the rule is applied. A simple independent T-test is used to verify this.
        
    # If only verifying for one sample (As in for Z-Tests), set sample2 param as None.

    def verifyMeanDiff(self, sample, rule):
        filteredSample = self.filter(sample, rule)
        pValue = self.performSingleTest(sample, filteredSample)
        return pValue > Typedef.sampleDiffThreshold
        
    def performSingleTest(self, sample1, sample2):
        sample1Array = np.array(self.evalExpression(sample1, self.LHSTokens))
        #print('Sample 1 done')
        sample2Array = np.array(self.evalExpression(sample2, self.RHSTokens))
        tStat, pValue = st.ttest_ind(sample1Array, sample2Array, equal_var = False)
        return pValue

    def recZTest(self, sample, mean, var, ruleListList, appliedRules):
        # Perform the Z-test first.
        if appliedRules:
            sample = self.filterEntries(sample, appliedRules[-1])
            
        # TODO: We have to verify that the Z-test can still be applied here (Sample sizes > 5 (Default))
        # If the Z-test cannot be applied here, we do not recurse further, and exit instead.

        if not self.isTestable(sample):
            #print('not testable')
            return None

        #print('Testing...')
        # First, we evaluate the expressions given.
        sampleArray = np.array(self.evalExpression(sample, self.LHSTokens if self.ZSampleIsLHS else self.RHSTokens))
        sampleMean = np.mean(sampleArray)
        
        standardError = np.sqrt(var / float(len(sampleArray)))
        zScore = ((sampleMean - mean) / standardError)
        #print(str(standardError))
        #print(zScore)
        pValue = 0
        
        if self.expression == Typedef.compExps[Typedef.lessThan]:
            pValue = st.norm.cdf(-zScore)
        elif self.expression == Typedef.compExps[Typedef.greaterThan]:
            pValue = st.norm.cdf(zScore)
        elif self.expression == Typedef.compExps[Typedef.notEqualTo]:
            pValue = st.norm.cdf(np.abs(zScore)) - st.norm.cdf(-np.abs(zScore))
        elif self.expression == Typedef.compExps[Typedef.equalTo]:
            pValue = st.norm.cdf(-np.abs(zScore)) * 2
        
        
        #print('Z-test completed.')
        
        pValue = np.around(pValue, 6)
        
        sMean = np.around(sampleMean,6)
        sVar = np.around(np.var(sampleArray),6)
        sSize = len(sampleArray)
        
        resultPrintList = [TestResultZ(sMean, sVar, sSize, mean, var, zScore, pValue, appliedRules)]
        
        # Now the Z-test is done.        
        
        # After that, if there are any rules by which we can refine our hypothesis,
        # We recurse one more level using that rule.
        
        if ruleListList:
            # If no rules have been applied yet, we give every rule in the ruleListList a go.
            if not appliedRules:
                for ruleList in ruleListList:
                    for rule in ruleList:  
                        recResultPrints = self.recZTest(sample, mean, var, ruleListList, [rule])
                        if recResultPrints:
                            resultPrintList.extend(recResultPrints)
            # If rules have been applied however, we give every rule whose colNum is BIGGER than
            # the latest rule's colNum a go.
            else:
                latestRuleIndex = appliedRules[-1].getColNum()
                #print('ColNum: ' + str(latestRuleIndex))
                #print('Rule: ' + appliedRules[-1].printCriteria())
                #print(len(ruleListList))
                if latestRuleIndex < (len(ruleListList) - 1) and len(appliedRules) < len(ruleListList):
                    for i in range(latestRuleIndex+1, len(ruleListList)):
                        for rule in ruleListList[i]:
                            if rule.getColNum() > latestRuleIndex:
                                recResultPrints = self.recZTest(sample, mean, var, ruleListList, appliedRules + [rule])
                                if recResultPrints:
                                    resultPrintList.extend(recResultPrints)
        return resultPrintList
        
    def recTTest(self, sample1, sample2, ruleListList, appliedRules):    
        # Perform the test first.
        if appliedRules:
            sample1 = self.filterEntries(sample1, appliedRules[-1])
            sample2 = self.filterEntries(sample2, appliedRules[-1])
        # TODO: We have to verify that the T-test can still be applied here (Sample sizes > 5, for example)
        # If the T-test cannot be applied here, we do not recurse further, and exit instead.

        if not self.isTestable(sample1, sample2):
            return None

        #print('Testing...')
        # First, we evaluate the expressions given.
        sample1Array = np.array(self.evalExpression(sample1, self.LHSTokens))
        #print('Sample 1 done')
        sample2Array = np.array(self.evalExpression(sample2, self.RHSTokens))
        
        #print('Sample 2 done')
        if self.samplesAreSame(sample1, sample2):
            print("Dep test")
            dep = True
            tStat, pValue = st.ttest_rel(sample1Array, sample2Array)
        else:
            dep = False
            tStat, pValue = st.ttest_ind(sample1Array, sample2Array, equal_var = False)
        #print('T-test completed.')
        if self.expression == Typedef.compExps[Typedef.lessThan]:
            if tStat > 0:
                pValue = 1 - (pValue/2)
            elif tStat < 0:
                pValue = pValue / 2
        elif self.expression == Typedef.compExps[Typedef.greaterThan]:
            if tStat < 0:
                pValue = 1 - (pValue / 2)
            elif tStat > 0:
                pValue = pValue / 2
        elif self.expression == Typedef.compExps[Typedef.notEqualTo]:
            pValue = 1 - pValue
        
        s1Mean = np.mean(sample1Array)        
        s1Var = np.var(sample1Array)
        s1Size = len(sample1Array)
        s2Mean = np.mean(sample2Array)   
        s2Var = np.var(sample2Array)
        s2Size = len(sample2Array)
        pValue = np.around(1 - pValue, 6)     
        
        resultPrintList = [TestResultT(s1Mean, s1Var, s1Size, s2Mean, s2Var, s2Size, tStat, pValue, appliedRules, dep)]  
        
        # Now the T-test is done.        
        
        # After that, if there are any rules by which we can refine our hypothesis,
        # We recurse one more level using that rule.
        
        if ruleListList:
            # If no rules have been applied yet, we give every rule in the ruleListList a go.
            if not appliedRules:
                for ruleList in ruleListList:
                    for rule in ruleList:  
                        recResultPrints = self.recTTest(sample1, sample2, ruleListList, [rule])
                        if recResultPrints:
                            resultPrintList.extend(recResultPrints)
            # If rules have been applied however, we give every rule whose colNum is BIGGER than
            # the latest rule's colNum a go.
            else:
                latestRuleIndex = appliedRules[-1].getColNum()
                if latestRuleIndex < (len(ruleListList) - 1) and len(appliedRules) < len(ruleListList):
                    for i in range(latestRuleIndex+1, len(ruleListList)):
                        for rule in ruleListList[i]:
                            if rule.getColNum() > latestRuleIndex:
                                recResultPrints = self.recTTest(sample1, sample2, ruleListList, appliedRules + [rule])
                                if recResultPrints:
                                    resultPrintList.extend(recResultPrints)
        return resultPrintList
    
    def samplesAreSame(self, s1, s2):
        if not s1 or not s2:
            return False
        elif len(s1) != len(s2):
            return False
        for entry1, entry2 in zip(s1, s2):
            if any(a != b for a, b in zip(entry1, entry2)):
                return False
        return True
    
    def isTestable(self, sample1, sample2 = None):
        if sample1 is not None and sample2 is not None:
            return (len(sample1) > self.minSampleLength) and (len(sample2) > self.minSampleLength)
        elif sample1 is not None and sample2 is None:
            return len(sample1) > self.minSampleLength
        else:
            return False

    # Receiving a list of entries and tokens representing an RPN expression to evaluate,
    # Evaluate the expression and return a list of values after the RPN expression.

    # This is where the actual expression processing takes place.

    def evalExpression(self, sample, tokens):
        if sample is None:
            valueStack = []
            for token in tokens:
                if self.isNumeric(token):
                    valueStack.append(float(token))
                elif token[0] in self.operators:
                    v1 = valueStack.pop()
                    v2 = valueStack.pop()
                    ans = self.evaluate(v1, v2, token[0])
                    valueStack.append(float(ans))
                elif token[0].isalpha():
                    print('Error! Variable-absent expression handling called incorrectly!')
            if valueStack:
                answer = valueStack.pop()
            else:
                print ("Error, expression has too few variables.")
            if valueStack:
                print ("Error, expression has too many variables.")
            return answer

        ansList = []
        for entry in sample:
            valueStack = []
            for token in tokens:
                if self.isNumeric(token):
                    valueStack.append(float(token))
                elif token[0] in self.operators:
                    v1 = valueStack.pop()
                    v2 = valueStack.pop()
                    ans = self.evaluate(v1, v2, token[0])
                    valueStack.append(float(ans))
                elif token[0].isalpha():
                    valueStack.append(float(entry[self.dataManager.getColumnIndexOfName(token)]))
            if valueStack:
                ansList.append(valueStack.pop())
            else:
                print ("Error, expression has too few variables.")
            if valueStack:
                print ("Error, expression has too many variables.")
        return ansList

    # This function receives two number values (in string form), and an expresion.
    # It returns the answer to that expression.
    def evaluate(self, v1, v2, expression):
        v1 = float(v1)
        v2 = float(v2)
        if expression == '+':
            return v2 + v1
        elif expression == '-':
            return v2 - v1
        elif expression == '*':
            return v2 * v1
        elif expression == '/':
            return v2 / v1

    def filter(self, inputEntries, group):
        filteredEntries = group.filter(inputEntries)
        return filteredEntries

    def isNumeric(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False