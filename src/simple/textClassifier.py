'''
Created on 19/12/2011

@author: josegustavozagatorosa
'''
# -*- coding: cp1252 -*-

import probabilities
import operator
#from collections import OrderedDict

context = {"batman" : ["my other computer is installed on the batcave",
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

def numOfWords():

    return sum(frequencies.itervalues())

def genBagOfWords():
    
    megaList = []
    for v in context.itervalues():
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

def splitContext():
    
    ret = {}
    for k in context.iterkeys():
        item = []
        for v in context[k]:
            item.append( v.split())
        ret.update({k:item})

    return flatContext(ret)


def basicTest():
    probabilities.context = splitContext()
    print probabilities.classify("desert of real".split())
    
def test():
    probabilities.context = splitContext()
    x = sorted(probabilities.classify("dark side".split()).iteritems(),key=operator.itemgetter(1),reverse=False)
    print x
    #print "probabilities.maxLikelyHood(x) = ",probabilities.maxLikelyHood(x)
    
    
