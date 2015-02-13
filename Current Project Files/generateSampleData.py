'''
Created on 8 Oct, 2014

@author: iang
'''

import csv
import random
import numpy as np

class randUtil:

    def randValue(self, numBase, randFactor):
        return np.round(numBase + (random.random() - 0.5) * randFactor, 2)
    
    def randInt(self, numBase, randFactor):
        return np.trunc(numBase + (random.random() - 0.5) * randFactor)
    
numRows = 100
numMen = 60

# Age
age = 40
ageRand = 20

#Weight
wtM = 70
wtMRand = 20
wtF = 70
wtFRand = 20

#Height
htM = 170
htMRand = 20
htF = 170
htFRand = 20

#Score Before
sM = 5000
sMRand = 100
sF = 5000
sFRand = 100

#Score After
SAfterM = 5200
SAfterMRand = 100
SAfterF = 4850
SAfterFRand = 100

with open('sample.csv', 'w') as fp:
    a = csv.writer(fp, delimiter=',')
    util = randUtil()
    data = []
    colNames = ['Gender', 'Age', 'Height', 'Weight', 'Score Before', 'Score After']
    data.append(colNames)
    for i in range(numRows):
        if i < numMen:
            row = ['M', util.randInt(age,ageRand),util.randValue(htM,htMRand), util.randValue(wtM, wtMRand), util.randInt(sM,sMRand), util.randInt(SAfterM, SAfterMRand)]
        else:
            row = ['F', util.randInt(age,ageRand), util.randValue(htF, htFRand), util.randValue(wtF, wtFRand), util.randInt(sF, sFRand), util.randInt(SAfterF, SAfterFRand)]
        data.append(row)
    a.writerows(data)