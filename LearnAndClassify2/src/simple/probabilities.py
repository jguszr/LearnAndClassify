'''
Created on 19/12/2011

@author: josegustavozagatorosa
'''
# -*- coding: cp1252 -*-

from collections import OrderedDict
import operator


#from collections import OrderedDict



context = {"A" : [0.0,0.0,0.0,1.0,1.0,1.0,1.0,2.0,2.0,2.0,2.0,2.0],
           "B" : [3.0,3.0,3.0,4.0,4.0,4.0,4.0,1.0,6.0,7.0,6.0,5.0],
           "C" : [3.0,0.0,0.0,4.0,4.0,1.0,1.0,1.0,7.0,7.0,8.0,5.0]}


def setNewContext(theNew):
    context = theNew 

def frequencies(s):
    return [((a, s.count(a)) for a in set(s))]


def individualProbabilites(key):
    m = {}
    [m.update({k:v}) for k,v in frequencies(context[key])]

    return m

def countAllContext():
    total = 0
    for k in context.iterkeys():
        total += len(context[k])
    return total

def itemProbability(toTest,givenContext):
    return context[givenContext].count(toTest) / float(len(context[givenContext]))

def contextProbability(key):
    return len(context[key]) / float(countAllContext())
    

def naiveBayes(toTest,givenContext):
    return (contextProbability(givenContext) * combinedItemsProbability(toTest,givenContext))/ float(countAllContext())

def combinedItemsProbability(toTest,givenContext):
    
    tp = 0
    for i in toTest:
        tp += itemProbability(i,givenContext)
    return tp



def classify(toTest):
    resp = {}
    for k in context.iterkeys():
        resp[k] = naiveBayes(toTest,k)
    return resp

def maxLikelyHood(toTest):
    
    k = max(toTest, key=toTest.get)
    return [(k,toTest[k])]
    
def basicTest():
    print len(context["A"])
    print individualProbabilites("B")
    print "contextSize = ", countAllContext()
    print "context relevance = ", contextProbability("A")
    print naiveBayes([0.0,0.0],"C")
    for k in context.iterkeys():
        print k, " = ", itemProbability(1.0,k)
    
def test():
    print "classify \n"
    cls = OrderedDict(sorted(classify([0.0,0.0]).iteritems(),key=operator.itemgetter(1),reverse=False))
    for x,y in cls.iteritems():
        print x," = ", y

    print "maximum likelihood = ",maxLikelyHood(cls)