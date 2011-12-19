'''
Created on 19/12/2011

@author: josegustavozagatorosa
'''
from simple import probabilities, textClassifier
from simple.loader import textLoader

basic = False
train = True
TO_RUN = [basic,train]


def runBasics():
    print "Running probabilities TEST() --------------------------"
    probabilities.test()
    print "Running text Classifier TEST() --------------------------"
    textClassifier.test()
    print "Running loader BasicTest() --------------------------"
    textLoader.basicTest()
    
def train():
    print "def train():"

if __name__ == '__main__':
    for i in TO_RUN:
        if i and basic:
            runBasics()
        if i and train:
            train()
            
