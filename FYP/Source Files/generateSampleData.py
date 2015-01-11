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

age = 40
ageRand = 20

wtM = 70
wtMRand = 20
wtF = 63
wtFRand = 16

htM = 170
htMRand = 20
htF = 160
htFRand = 18

sM = 5000
sMRand = 2000
sF = 4000
sFRand = 1500

SAfterM = 4990
SAfterMRand = 1500
SAfterF = 4025
SAfterFRand = 1400

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
