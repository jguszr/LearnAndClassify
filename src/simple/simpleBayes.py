'''
Created on 08/12/2011

@author: josegustavozagatorosa
'''


testContext = {"A": [1.0,2.0,3.0,1.0,2.0,3.0,1.0,2.0,3.0,1.0,2.0,3.0],
                "B":[0.0,4.0,4.0,4.0,5.0,5.0,5.0,5.0,6.0,6.0,2.0,3.0]}


def frequencies(sample):
    return [(a, float(sample.count(a))) for a in sample]

def overall_probability(sample):
    return  [((a, sample.count(a)/float(len(sample))) for a in sample)]

def tuplesToDictionaires(tuples):
    ret = {}
    [ret.update({k,v}) for k,v in tuples]
    return ret
        
def test():
    print "frequencies",
    for k in testContext.iterkeys():
        print k, frequencies(testContext[k])
        
    print "Probability Sample",
    for p in testContext.iterkeys():
        ninjaDict = tuplesToDictionaires(overall_probability(testContext[p])) 
        print ninjaDict


