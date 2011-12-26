'''
Created on 19/12/2011

@author: josegustavozagatorosa
'''
# -*- coding: cp1252 -*-

import probabilities
import operator
from collections import OrderedDict
from simple.loader import textLoader

raw_context = {"batman" : ["my other computer is installed on the batcave",
                           "robin is my bitch", "cat womoan isn't a milf",
                           "Alfred, bring me milk ! Please !", "bat mobile is bacon powered",
                           "Robin take your hands off my pistol"],
              "Vader" : ["Dark side is the only side", "I'm not emperor's little bitch",
                         "My other sword is a ninja sword", "You don't know the power of the dark side"
                         "I find you lack of faith disturbin", "my soon is out there"],
               "Morpheus" : ["welcome to the desert of real", "you are the choosen one",
                             "take the blue pill and see how deep is the rabbit hole",
                             "let it all go, fear, disbeliff",
                             "tree capitains, tree ships there is no coincidence on this"
                   ]}


frequencies = {}
context = {}

def numOfWords():

    return sum(frequencies.itervalues())

def genBagOfWords():
    
    megaList = []
    for v in raw_context.itervalues():
        megaList +=  [x.split() for x in v]
    vocabulary = sum(map(list, megaList), [])
    tempFreq = ((a, vocabulary.count(a)) for a in set(vocabulary))
    [frequencies.update({k:v}) for k,v in tempFreq]
    
    return frequencies

def flatContext(ret):

    for k in ret.iterkeys():
        item = sum(map(list, ret[k]), [])
        ret.update({k:item})
        
    return ret


def mostInformativeFeature(top=10):
    freqs = genBagOfWords();
    f = OrderedDict(sorted(freqs.iteritems(), key=operator.itemgetter(1),reverse=False))
    return f

def contextInfo():
    
    print "---------------------------------------------------"
    print " General Context Information"
    print "---------------------------------------------------"
    print " SIZE (words)                                      "
    print "---------------------------------------------------"
    for k in raw_context.iterkeys():
        print k, "\t\t\t=  ", len(raw_context[k])
    print "---------------------------------------------------"
    print "Total \t\t\t\t=  ", countAllContext()         
    print "---------------------------------------------------"
    print " Context Probabilities                             "
    print "---------------------------------------------------"
    total = 0
    for k in raw_context.iterkeys():
        prob = contextProbability(k)
        print k, "\t\t\t=  ", prob
        total += prob
    print "---------------------------------------------------"
    print "Total \t\t\t\t= ",total
    print "---------------------------------------------------"
    print "---------------------------------------------------"
    
    
    
def splitContext():
    
    ret = {}
    for k in raw_context.iterkeys():
        item = []
        for v in raw_context[k]:
            item.append( v.split())
        ret.update({k:item})

    return flatContext(ret)

def generateProbabilisticContext(stopWords=[]):
    
    ret = {}
    for k in raw_context.iterkeys():
        sub = {}
        size = len(raw_context[k])
        for v in raw_context[k]:
            if stopWords.count(v.lower())==0:
                sub[v] = raw_context[k].count(v) /float(size)  
        ret[k]=sub
    
    return ret

def getSingleItemProbability(item,ctxKey):
    ctx = context[ctxKey]
    try:
        return float(ctx[item])
    except KeyError:
        return 0.0
#    try:
#        return context[ctxKey][item]
#    except KeyError:
#        return 0.001
    
def getSingleFeatureProbabilityToAllContexts(item):
    
    total = 0.000001
    
    for k in context.iterkeys():
        p = getSingleItemProbability(item,k)
        if p<>0.0:
            total *= p 
        
    return total

def naiveBayes(toTest,ctxKey):
    
    itemProbs = 0.0001
    wordList = toTest.split()
    for l in wordList:
        p = getSingleItemProbability(l,ctxKey)
        if p<>0.0:
            itemProbs *=p

    totalProbs = 0.0001
    for x in wordList:
        totalProbs += getSingleFeatureProbabilityToAllContexts(x)
    return (itemProbs * contextProbability(ctxKey)) / float(totalProbs)

def classify(toTest):
    resp = {}
    for k in context.iterkeys():
        resp[k] = naiveBayes(toTest,k)
    return resp

def maxLikelyHood(toTest):
    
    k = max(toTest, key=toTest.get)
    return [(k,toTest[k])]


def contextProbability(key):

    return len(raw_context[key])/float(countAllContext())
    
def countAllContext():
    total = 0
    for k in raw_context.iterkeys():
        total += len(raw_context[k])
    return total

def basicTest():
    probabilities.context = splitContext()
    print probabilities.classify("desert of real".split())
    
def test():
    probabilities.context = splitContext()
    x = OrderedDict(sorted(probabilities.classify("dark side".split()).iteritems(),key=operator.itemgetter(1),reverse=False))
    print x
    print "probabilities.maxLikelyHood(x) = ",probabilities.maxLikelyHood(x)
    
    
