'''
Created on 19/12/2011

@author: josegustavozagatorosa
'''
from simple import probabilities, textClassifier
from simple import loader
if __name__ == '__main__':
    print "Running probabilities TEST() --------------------------"
    probabilities.test()
    print "Running text Classifier TEST() --------------------------"
    textClassifier.test()
    print "Running loader BasicTest() --------------------------"
    loader.textLoader.basicTest()
    