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
    cont = {}
    cont = textLoader.loadRaw("Christmas Carol",cont,"pg46.txt",200,60)
    cont.update(textLoader.loadRaw("moby dick",cont,"pg2701.txt",200,500))
    print "Raw Data"
    for k,v in cont.iteritems():
        print k,v
    textClassifier.context = cont
    
    

if __name__ == '__main__':
    for i in TO_RUN:
        if i and basic:
            runBasics()
        if i and train:
            train()
            
