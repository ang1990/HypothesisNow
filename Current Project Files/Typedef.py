'''
Created on 1 Sep, 2014

@author: Mark Ang
'''


import numpy as np

numeric = 0
text = 1
greaterThan = 0
lessThan = 1
equalTo = 2
notEqualTo = 3

minSampleLength = 5

emptySampleErrorValue = -1.0

sampleDiffThreshold = 0.95

textset = 'Textset'
include = 'Include'
exclude = 'Exclude'

noGrouping = "No Grouping"
noHypDisplay = 'No hypothesis yet. Click on button above to build hypothesis.'

numTypeDisplay = 'Numeric'
textTypeDisplay = 'Text'

sample1EmptyText = 'Sample 1 has no entries. Please check your filter criteria and try again.'
sample2EmptyText = 'Sample 2 has no entries. Please check your filter criteria and try again.'
bothSamplesEmptyText = 'Both samples have no entries. Please check your filter criteria and try again.'

sampleEmptyText = 'Sample has no entries. Please check your filter criteria and try again.'

compStrings = ['IS GREATER THAN', 'IS SMALLER THAN', 'IS EQUAL TO', 'IS NOT EQUAL TO']
compExps = ['>', '<', '==', '!=']

# normalSafe and normalUnsafe denotes sample size thresholds that determine how safe a sample
# can be assumed to follow normal distribution.

# If the sample size exceeds 40 after removing outliers, we can assume normality.

# If the sample size is between 16 and 40 after removing outliers, we can assume normality if:
#
# 1. The data has only 1 peak (Is unimodal)
# 2. The data is symmetric (Zero skew or mode is close to median.)
# 
 
normalSafe = 40
normalUnsafe = 15

# skewThreshold is the default confidence level of the skewness test used in logicMain.
# Anything below this value will lead logicMain to assume that the sample is skewed.

skewThreshold = 0.2
unimodalityThreshold = 186.0/125

# Grubbs threshold is the default confidence level of the Grubb's test for outliers.
# A test returning a value above this threshold has detected an outlier.

grubbsThreshold = 0.975

typeZ = 'Z'
typeT = 'T'
typeCalc = 'Calc'


def emptySampleError(sample1, sample2 = None):
    if sample2 is None:
        return sampleEmptyText
    if len(sample1) <= 0 and len(sample2) <= 0:
        return bothSamplesEmptyText
    elif len(sample1) <= 0 and len(sample2) > 0:
        return sample1EmptyText
    elif len(sample1) > 0 and len(sample2) <= 0:
        return sample2EmptyText




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
    
    # Preset groups as a dictionary, whose keys are their names.
    
    
    def __init__(self, columnNames, colTypes, entries, textSets):
        self.colTypes = colTypes
        self.columnNames = columnNames
        self.entries = entries
        self.textSets = textSets
        self.groups = {}
        
    def __init(self):
        self.colTypes = np.zeros(1)
        self.columnNames = []
        self.textSets = {}
        self.groups = {}

    def getGroups(self):
        return self.groups

    def getGroupNames(self):
        return [name for name in self.groups.keys()]

    def addGroup(self, groupName, groupData):
        self.groups[groupName] = groupData

    def getNumColumns(self):
        return len(self.columnNames)

    # This function can receive either the column index or the column name.
    # It will return the column type of the corr. column.

    # This function assumes that the token, if a string, exists in columnNames,
    # or if it is an integer, is within range of colTypes.

    def getColType(self, token):
        if type(token) is not str:
            return self.colTypes[token]
        else:
            return self.colTypes[self.columnNames.index(token)]
        
    def getColumnNames(self):
        return self.columnNames
        
    def getColumnIndexOfName(self, name):
        return self.columnNames.index(name)
    
    def getColumnNameOfIndex(self, index):
        return self.columnNames[index]

    def getColTypeByIndex(self, index):
        return self.colTypes[index]

    def getTextSet(self, setName):
        if setName in self.textSets:
            return self.textSets[setName]
        else:
            return None
    
    def getAllTextSets(self):
        return self.textSets
        
class TestResult(object):
    import numpy as np
    def getResultPrint(self):
        return None
        
    def getPValue(self):
        return self.pValue
        
class TestResultZ(TestResult):
    def __init__(self, sMean, sVar, sSize, zMean, zVar, zScore, pVal, appliedRules = []):
        self.sMean = sMean
        self.sVar = sVar
        self.sSize = sSize
        self.zMean = zMean
        self.zVar = zVar
        self.zScore = zScore
        self.pValue = pVal
        self.appliedRules = appliedRules

    def getSampleVariance(self):
        return self.sVar / (self.sSize - 1)

    def getResultPrint(self):
        resultPrint = 'Z-test on:\n'
        if self.appliedRules:
            for rule in self.appliedRules:
                resultPrint += 'Column ' + rule.getColName() + ':'
                resultPrint += rule.printCriteria() + '\n'
        else:
            resultPrint += 'All data.\n'
            
        resultPrint += '\nPopulation Mean: ' + str(np.around(self.zMean,6))
        resultPrint += '\nPopulation Variance: ' + str(np.around(self.zVar,6))
        resultPrint += '\n'
        resultPrint += '\nSample Size: ' + str(self.sSize)
        resultPrint += '\nSample Mean: ' + str(np.around(self.sMean,6))
        
        resultPrint += '\nZ-Score: ' + str(self.zScore)
        resultPrint += '\nConfidence level: ' + str(self.pValue*100) + '%\n'    
        return resultPrint

class TestResultT(TestResult):
    def __init__(self, s1Mean, s1Var, s1Size, s2Mean, s2Var, s2Size, tScore, pVal, appliedRules = [], dep = False):
        self.s1Mean = s1Mean
        self.s1Var = s1Var
        self.s1Size = s1Size
        self.s2Mean = s2Mean
        self.s2Var = s2Var
        self.s2Size = s2Size
        self.tScore = tScore
        self.pValue = pVal
        self.appliedRules = appliedRules  
        self.dep = dep

    # This function will return the larger of the sample variances. This is to compare which test result
    # is more unreliable due to the sample's larger variance.    
    
    def getSampleVariance(self):    
        return max(self.s1Var, self.s2Var)
    
    def getResultPrint(self):
        if self.dep:
            resultPrint = 'Dependent T-test on:\n'
        else:
            resultPrint = 'Independent T-test on:\n'
        if self.appliedRules:
            for rule in self.appliedRules:
                resultPrint += 'Column ' + rule.getColName() + ':'
                resultPrint += rule.printCriteria() + '\n'
        else:
            resultPrint += 'All data.\n'
            
        resultPrint += '\nLeft-Hand Side:'
        resultPrint += '\nSample Size: ' + str(self.s1Size)
        resultPrint += '\nMean: ' + str(np.around(self.s1Mean,6))
        resultPrint += '\nVariance: ' + str(np.around(self.s1Var,6))
        resultPrint += '\n\nRight-Hand Side:\n'
        resultPrint += '\nSample Size: ' + str(self.s2Size)
        resultPrint += '\nMean: ' + str(np.around(self.s2Mean,6))
        resultPrint += '\nVariance: ' + str(np.around(self.s2Var,6))
        resultPrint += '\n'        
        
        resultPrint += '\nConfidence level ' + str(self.pValue*100) + '%\n'  
        return resultPrint