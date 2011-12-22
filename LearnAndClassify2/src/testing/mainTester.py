'''
Created on 19/12/2011

@author: josegustavozagatorosa


'''
from simple import probabilities, textClassifier
from simple.loader import textLoader
from simple.textClassifier import splitContext
from collections import OrderedDict
import operator

basic = False
train = False
info = True
TO_RUN = [basic,train,info]


def runBasics():
    print "Running probabilities TEST() --------------------------"
    probabilities.test()
    print "Running text Classifier TEST() --------------------------"
    textClassifier.test()
    print "Running loader BasicTest() --------------------------"
    textLoader.basicTest()
    
def prepareProbabilisticContext():
    if not textLoader.assertContextFile("trainSet.freq"):
        print "no file found... Generating the probabilistic model"
        textClassifier.context = textClassifier.generateProbabilisticContext()
        textLoader.saveProbabilisticContext(textClassifier.context, "trainSet.freq")
    else:
        print "found freq. file... "
        textLoader.loadProbabilisticContext("trainSet.freq")

def prepareContext():
    cont = {}
    if not textLoader.assertContextFile("trainSet.ctx"):
        print "from raw files"
        cont = textLoader.loadRaw("Christmas Carol", cont, "pg46.txt", 2000, 60)
        cont.update(textLoader.loadRaw("moby dick", cont, "pg2701.txt", 2000, 500))
        cont.update(textLoader.loadRaw("The Prince", cont, "pg1232.txt", 2000, 100))
        cont.update(textLoader.loadRaw("Beowulf", cont, "pg16328.txt", 2000, 100))
        textLoader.saveContext(cont, "trainSet.ctx")
    else:
        print "from previous contexts"
        cont = textLoader.loadContext("trainSet.ctx")
    
    return cont

def train():
    print "def train():"
    textClassifier.context = prepareContext()
    probabilities.context = textClassifier.splitContext() 
    x = OrderedDict(sorted(probabilities.classify("A pile on the earth strong for the burning".split()).iteritems(),key=operator.itemgetter(1),reverse=True))
    print "probabilities.maxLikelyHood(x) = ",probabilities.maxLikelyHood(x)
    print x
    


if __name__ == '__main__':
    for i in TO_RUN:
        if i and basic:
            runBasics()
        if i and train:
            train()
        if i and info:
            print "prepare "
            textClassifier.raw_context = prepareContext()
            print "splitting "            
            textClassifier.raw_context = textClassifier.splitContext()
            probabilities.context = textClassifier.raw_context
            print "generating probabilities "               
            prepareProbabilisticContext()
            print "dumping "   
            textClassifier.contextInfo()
#            print textClassifier.context
            print "Text Classify test "
            print "The register of his burial was signed by the clergyman, the clerk, the undertaker"
#            print "",textClassifier.classify("goose")
            
            
