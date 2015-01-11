'''
Created on 1 Sep, 2014

@author: Mark Ang Yan Sheng
'''

import csv
import Typedef
import numpy as np, scipy.stats
from Groupings import ColumnData, DataManager

# LogicMain performs the following jobs:

# 1. Process the incoming CSV file.
#    The Column names, column types, and entry data is collected from the CSV file. They are placed in a DataManager
#    class, through which all calls to data have to go through.

# 2. Perform the tests.
#    The logic must take statements from StatementBuilder (via main class) and use those statements to perform the
#    relevant tests.

class logicMain(object):
    
    expRange = {Typedef.ZTest: Typedef.notEqual, Typedef.TTest: Typedef.notEqual, Typedef.DepTest: Typedef.notEqual}
    testType = 0
    stmt = ''
    ZMean = 0
    ZVar = 0
    textSets = {}
    columns = []
    colTypes = np.zeros(1)
    currentText = Typedef.TTest
    g1 = []
    g2 = []
    c1 = 0
    c2 = 0
    columnNames = []
    dataManager = None
    
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
    entryData:          Entries given in the data.
    
    NOTE: NOTHING IS RETURNED TO CALLER. CALLER MUST GET REQUIRED DATA THROUGH GET CALLS.
    '''
    def processSample(self, fName):
        reader = csv.reader(open(fName, 'rU'))
        self.entries = [line for line in reader]
        columnNames = self.entries.pop(0)
    # Now we figure out the types of data present in each column.
        colTypes = np.zeros(len(self.entries[0]))
        for entry in self.entries:
    # For each entry:
            for i in range(len(entry)):
    # If the column is still considered to contain numeric data only:
                if colTypes[i] == Typedef.numeric:
    # If the entry contains text data, then the column will be considered to be of text type.
                    if self.isNumeric(entry[i]) is False:
                        colTypes[i] = Typedef.text
    # Handle element sets here.
        for i in range(len(colTypes)):
            if colTypes[i] == Typedef.text:
                elemSet = set()
                for j in range(len(self.entries)):
                    elemSet.add(self.entries[j][i])
                self.textSets[columnNames[i]] = elemSet
        print columnNames
        print colTypes
        print len(self.entries)
        print self.textSets
        self.columns = {}
        self.columnNames = columnNames
        self.colTypes = colTypes
        for i in range(len(colTypes)):
            self.columns[self.columnNames[i]] = (ColumnData(i,colTypes[i],columnNames[i]))
    
    # Getter functions for main use.
    
    def getDataManager(self):
        return DataManager(self.columnNames, self.colTypes, self.columns, self.entries, self.textSets)
    
    def getColumns(self):
        return self.columns
    
    def getEntries(self):
        return self.entries
    
    def getTextSets(self):
        return self.textSets
    
    def updateDataManager(self, dataManager):
        self.dataManager = dataManager

    def setStmt(self, stmt):
        self.stmt = stmt
    # The statement's data is put into logicMain here. Only the relevant fields are sent in via the
    # Statement class's APIs.
        self.testType = stmt.testType
        if self.testType == Typedef.TTest:
            self.g1, self.g2, self.tCol, self.expRange[Typedef.TTest] = stmt.getTTest()
        elif self.testType == Typedef.ZTest:
            self.g1, self.tCol, self.ZMean, self.ZVar, self.expRange[Typedef.ZTest] = stmt.getZTest() 
        elif self.testType == Typedef.DepTest:
            self.c1, self.c2, self.g1, self.expRange[Typedef.DepTest] = stmt.getDepTest()
        elif self.testType == Typedef.ChiSqTest:
            self.c1, self.g1 = stmt.getChiSqTest()
    # Perform the test here.

    def performTest(self):
        pValue = Typedef.emptySampleErrorValue
        printResult = 'Stub.'
        if self.testType == Typedef.TTest:
            pValue, printResult = self.performTTest()
        elif self.testType == Typedef.ZTest:
            pValue, printResult = self.performZTest()
        elif self.testType == Typedef.DepTest:
            pValue, printResult = self.performDepTest()
        elif self.testType == Typedef.ChiSqTest:
            pValue, printResult = self.performChiSqTest()
        return pValue, printResult
    
# TODO: Need to work out all the APIs.

    def filter(self, inputEntries, group):
        filteredEntries = group.filter(inputEntries)
        return filteredEntries

# T-Test. All the required values are assumed to be parsed in already.
    def performTTest(self):
        sample1 = self.entries
        if len(self.g1) > 0:
            for group in self.g1:
                sample1 = self.filter(sample1, group)
        sample2 = self.entries
        if len(self.g2) > 0:
            for group in self.g2:
                sample2 = self.filter(sample2, group)
        if len(sample1) > 0 and len(sample2) > 0:
            column1 = [float(entry[self.tCol]) for entry in sample1]
            column2 = [float(entry[self.tCol]) for entry in sample2]
            column1 = np.array(column1)
            column2 = np.array(column2)
            tStat, pValue = scipy.stats.ttest_ind(column1, column2, equal_var = True)
            testPrint = 'Welch\'s T-test used.\n'
            testPrint += 'Sample 1 Mean: ' + str(np.mean(column1)) + '\n'
            testPrint += 'Sample 1 Std. Dev.: ' + str(np.std(column1)) + '\n'
            testPrint += 'Sample 1 Size: ' + str(np.size(column1)) + '\n\n'            
            testPrint += 'Sample 2 Mean: ' + str(np.mean(column2)) + '\n'
            testPrint += 'Sample 2 Std. Dev.: ' + str(np.std(column2)) + '\n'
            testPrint += 'Sample 2 Size: ' + str(np.size(column2)) + '\n\n'    
            testPrint += 'Assumptions are unverified at this time. This will be implemented in future iterations.'
    
            if self.expRange[Typedef.TTest] == Typedef.lessThan:
                if tStat > 0:
                    pValue = 1 - (pValue/2)
                elif tStat < 0:
                    pValue = pValue / 2
            elif self.expRange[Typedef.TTest] == Typedef.greaterThan:
                if tStat < 0:
                    pValue = 1 - (pValue / 2)
                elif tStat > 0:
                    pValue = pValue / 2
            return np.around(1 - pValue, 4), testPrint
        else:
            testPrint = Typedef.emptySampleError(sample1, sample2)
            return Typedef.emptySampleErrorValue, testPrint

    def performZTest(self):
        sample = self.entries
        if len(self.g1) > 0:
            for group in self.g1:
                sample = self.filter(sample, group)
        if len(sample) > 0:
            data = [float(entry[self.tCol]) for entry in sample]
            data = np.array(data)
            meanDifference = np.mean(data) - self.ZMean
            if self.ZVar == 0:
                return 1 if meanDifference == 0 and np.var(data) == 0 else 0
            stdError = np.sqrt(self.ZVar / len(data))
            zScore = meanDifference / stdError
        
            # Producing the test print data.
            testPrint = 'Z-Test performed.\n'
            testPrint += 'Expected Range: '
            if self.expRange[Typedef.ZTest] == Typedef.notEqual:
                testPrint += 'Not Equal\n'
            elif self.expRange[Typedef.ZTest] == Typedef.lessThan:
                testPrint += 'Less Than\n'
            elif self.expRange[Typedef.ZTest] == Typedef.greaterThan:
                testPrint += 'Greater Than\n'
            testPrint += 'Population Mean: ' + str(self.ZMean) + '\n'
            testPrint += 'Population Variance: ' + str(self.ZVar) + '\n\n'
            testPrint += 'Sample Mean: ' + str(meanDifference + self.ZMean) + '\n'
            testPrint += 'Mean deviation from Popn: ' + str(meanDifference) + '\n\n'
            testPrint += 'Sample Size: ' + str(len(data)) + '\n\n'
            testPrint += 'Z-Score: ' + str(zScore) + '\n\n'
            testPrint += 'Assumptions are unverified at this time. This will be implemented in future iterations.'
            pValue = 0 
            if self.expRange[Typedef.ZTest] == Typedef.notEqual:
                pValue = scipy.stats.norm.cdf(zScore/2)
            elif self.expRange[Typedef.ZTest] == Typedef.lessThan:
                pValue = scipy.stats.norm.cdf(-zScore)
            elif self.expRange[Typedef.ZTest] == Typedef.greaterThan:
                pValue = scipy.stats.norm.cdf(zScore)
            return np.around(pValue, 4), testPrint
        else:
            testPrint = Typedef.emptySampleError(sample)
            return Typedef.emptySampleErrorValue, testPrint
    
    def performDepTest(self):
        sample = self.entries
        if len(self.g1) > 0:
            for group in self.g1:
                sample = self.filter(sample, group)
        column1 = [float(entry[self.c1]) for entry in sample]
        column2 = [float(entry[self.c2]) for entry in sample]
        column1 = np.array(column1)
        column2 = np.array(column2)
        tStat, pValue = scipy.stats.ttest_rel(column1, column2)
        testPrint = 'Dependent T-test used.\n'
        testPrint += 'Sample 1 Mean: ' + str(np.mean(column1)) + '\n'
        testPrint += 'Sample 1 Std. Dev.: ' + str(np.std(column1)) + '\n'
        testPrint += 'Sample 1 Size: ' + str(np.size(column1)) + '\n\n'            
        testPrint += 'Sample 2 Mean: ' + str(np.mean(column2)) + '\n'
        testPrint += 'Sample 2 Std. Dev.: ' + str(np.std(column2)) + '\n'
        testPrint += 'Sample 2 Size: ' + str(np.size(column2)) + '\n\n'    
        testPrint += 'Assumptions are unverified at this time. This will be implemented in future iterations.'
    
        if self.expRange[Typedef.DepTest] == Typedef.lessThan:
            if tStat > 0:
                pValue = 1 - (pValue/2)
            elif tStat < 0:
                pValue = pValue / 2
        elif self.expRange[Typedef.DepTest] == Typedef.greaterThan:
            if tStat < 0:
                pValue = 1 - (pValue / 2)
            elif tStat > 0:
                pValue = pValue / 2
        print 'pValue = ' + str(pValue)
        return np.around(1 - pValue, 4), testPrint
    
    def performChiSqTest(self):
        sample = self.entries
        if len(self.g1) > 0:
            for group in self.g1:
                sample = self.filter(sample, group)
        column1 = [entry[self.c1] for entry in sample]
        textSet1 = self.dataManager.getTextSet(self.dataManager.getColumnNameOfIndex(self.c1))
        column1Counts = []
        expectedCounts = []
        for elem in textSet1:
            elemCount = column1.count(elem)
            column1Counts.append(column1.count(elem))
            expectedCounts.append(len(column1) / len(textSet1))
        correction = False
        for elem in column1Counts:
            if elem < 5:
                correction = True
                break
        chi2, pValue, dof, exp = scipy.stats.chi2_contingency([column1Counts, expectedCounts], correction)
        
        print 'pValue = ' + str(pValue)
        print 'Expected: '
        print exp
        
        testPrint = 'Pearson\'s Chi-Squared test used.\n\n'
        testPrint += 'Contingency table:\n'
        for elem in textSet1:
            testPrint += elem + ' : ' + str(column1.count(elem)) + '\n'
        testPrint += '\n'
        testPrint += 'Assumptions are unverified at this time. This will be implemented in future iterations.'
        
        return pValue, testPrint
    
    def isNumeric(self, s):
        try:
            float(s.strip())
            return True
        except ValueError:
            return False
