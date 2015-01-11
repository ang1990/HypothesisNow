'''
Created on 1 Sep, 2014

@author: Mark Ang
'''
numeric = 0
text = 1
notEqual = 2
lessThan = 0
greaterThan = 1

TTest = 0
ZTest = 1
DepTest = 2
ChiSqTest = 3

emptySampleErrorValue = -1.0

noGrouping = "No Grouping"
noHypDisplay = 'No hypothesis yet. Click on button below to build hypothesis.'

numTypeDisplay = 'Numeric'
textTypeDisplay = 'Text'

sample1EmptyText = 'Sample 1 has no entries. Please check your filter criteria and try again.'
sample2EmptyText = 'Sample 1 has no entries. Please check your filter criteria and try again.'
bothSamplesEmptyText = 'Both samples have no entries. Please check your filter criteria and try again.'

sampleEmptyText = 'Sample has no entries. Please check your filter criteria and try again.'

def emptySampleError(sample1, sample2 = None):
    if sample2 is None:
        return sampleEmptyText
    if len(sample1) <= 0 and len(sample2) <= 0:
        return bothSamplesEmptyText
    elif len(sample1) <= 0 and len(sample2) > 0:
        return sample1EmptyText
    elif len(sample1) > 0 and len(sample2) <= 0:
        return sample2EmptyText

