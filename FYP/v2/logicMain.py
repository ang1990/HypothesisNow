'''
Created on 1 Sep, 2014

@author: Mark Ang Yan Sheng
'''

import os, csv
import Typedef
import numpy, scipy.stats

ofType = Typedef.Type()

class logicMain(object):
    
    columnNames = ''
    colTypes = numpy.zeros(1)
    nMeanZ = 0
    nVarZ = 0
    expRangeZ = ofType.notEqual
    
    
    
    def setSampleData(self, fName):
        columns, entryData, datatypes = self.processSample(fName)
        return columns, entryData, datatypes
    '''
    Function: processSample
    processSample takes the raw text from the sample file (Expected to be in CSV form).
    Expected Input:
    1st Row:            Names of columns
    2nd Row onwards:    Entries with values for each column. If actual values do not exist in the data,
                        pre-processing to set the value as zero or some special value is required.
    Expected Output:
    columns:            Names of columns
    entryData:          Entries given in the data.
    datatypes:          The types of data in each column (Numeric or text).
    '''
    def processSample(self, fName):
        reader = csv.reader(open(fName, 'rb'))
        entries = [line for line in reader]
        columnNames = [entries.pop(0)]
        print 'Names: ', columnNames
    # Now we figure out the types of data present in each column.
        colTypes = numpy.zeros(len(entries[0]))
        for entry in entries:
    # For each entry:
            for i in range (len(entry)):
    # If the column is still considered to contain numeric data only:
                if colTypes[i] == ofType.numeric:
    # If the entry contains text data, which the str(int)) function should detect, then the column will be considered
    # to be of text type.
                    if self.isNumeric(entry[i]) is False:
                        colTypes[i] = ofType.text
        print colTypes
        return columnNames[0], entries, colTypes
    
    def getZTestParams(self):
        return self.nMeanZ, self.nVarZ, self.expRangeZ

    def setZTestParams(self, nMean, nVar, expRange):
        self.nMeanZ = nMean
        self.nVarZ = nVar
        self.expRangeZ = expRange

        # Perform the Z Test here.

    def performZTest(self, sampleData, columnNumber):
        colValues = numpy.array([numpy.float(entry[columnNumber]) for entry in sampleData])
        print colValues
        meanDifference = numpy.average(colValues) - self.nMeanZ
        if self.nVarZ == 0:
            return 0 if meanDifference == 0 and numpy.var(colValues) == 0 else 1
        stdError = numpy.sqrt(self.nVarZ / len(colValues))
        zScore = meanDifference / stdError
        
        # Producing the test print data
        fullText = 'Z-Test information:\n'
        fullText += 'Expected Range: '
        if self.expRangeZ == ofType.notEqual:
            fullText += 'Not Equal\n'
        elif self.expRangeZ == ofType.lessThan:
            fullText += 'Less Than\n'
        elif self.expRangeZ == ofType.greaterThan:
            fullText += 'Greater Than\n'
        fullText += 'Population Mean: ' + str(self.nMeanZ) + '\n'
        fullText += 'Population Variance: ' + str(self.nVarZ) + '\n\n'
        fullText += 'Sample Mean: ' + str(meanDifference + self.nMeanZ) + '\n'
        fullText += 'Mean deviation from Popn: ' + str(meanDifference) + '\n\n'
        fullText += 'Sample Size: ' + str(len(colValues)) + '\n\n'
        fullText += 'Z-Score: ' + str(zScore)
        
        if self.expRangeZ == ofType.notEqual:
            return fullText, 1 - scipy.stats.norm.sf(zScore)*2
        elif self.expRangeZ == ofType.lessThan:
            return fullText, 1 - scipy.stats.norm.sf(-zScore)
        else:
            return fullText, 1 - scipy.stats.norm.sf(zScore)
    
    def isNumeric(self, s):
        try:
            float(s.strip())
            return True
        except ValueError:
            return False