'''
Created on 19/12/2011

@author: josegustavozagatorosa
'''
# -*- coding: cp1252 -*-

import os

RAW_DATA_PATH = "C:/development/python/python_rep/LearnAndClassify2/rawData/"
CONTEXT_PATH = "C:/development/python/python_rep/LearnAndClassify2/contextData/"

KEY_ID = "@@@k:"
LIST_VALUES_ID = "@@@Values:"
LIST_SIZE = "@@@size:"
KV_SEPARATOR = "@:@"

def loadRaw(tag,container,fileName,chunkSize=1000, startingAt=0):

    rawFile = open(RAW_DATA_PATH+fileName,'r')
        
    data = []
    i,index = 0,0
    
    for line in rawFile:
        if i>=startingAt:
            if index<chunkSize:
                data.append(line)
                index += 1
            else:
                break
        i+=1
        
    container[tag]=data
    rawFile.close()

    return container

def assertContextPath():
    if not os.path.exists(CONTEXT_PATH):
        os.makedirs(CONTEXT_PATH)
        
def assertContextFile(fileName):
    return os.path.exists(CONTEXT_PATH+fileName)


def saveContext(context,filename):
    assertContextPath()
    toSave = open(CONTEXT_PATH+filename,'w')
    for k,v in context.iteritems():
        toSave.write(KEY_ID + k )
        toSave.write(LIST_SIZE + str(len(v)) + "\n")
        [(l, toSave.write(l)) for l in v]
    toSave.close()
    
def saveProbabilisticContext(context,filename):
    assertContextPath()
    toSave = open(CONTEXT_PATH+filename,'w')
    for k in context.iterkeys():
        toSave.write(KEY_ID+k)
        toSave.write(LIST_SIZE + str(len(context[k])) + "\n")
        content = context[k]
        for l,m in content.iteritems():
            toSave.write(l+KV_SEPARATOR+str(m)+"\n")
    toSave.close()    

def loadStopWords(filename):
    toLoad = open(CONTEXT_PATH+filename)
    ret = []
    [(l, ret.append(l.lower())) for l in toLoad]
    toLoad.close()
    return ret

def isKeyId(line):
    return line.startswith(KEY_ID)

def extractKey(line):
    r = line.rsplit("k:")[1]
    return r.rsplit("@")[0]


def getValuesSize(line):
    return line.rsplit(LIST_SIZE)[1]

def loadContext(filename):
    
    newContext = {}
    toLoad = open(CONTEXT_PATH+filename,'r')
    k = ''
    l = 'x'
    while l<>'':
        data=[]
        l = toLoad.readline()
        lsize = 0
        if isKeyId(l):
            k = extractKey(l)
            lsize = int(getValuesSize(l))
        i=0
        while i<lsize:
            l = toLoad.readline()
            data.append(l)
            i+=1
        if k <>'' and len(data)>0:
            newContext.update({k:data})
    toLoad.close()
    return newContext
    
def loadProbabilisticContext(filename):
    
    newContext = {}
    toLoad = open(CONTEXT_PATH+filename,'r')
    l='x'
    while l<>'':
        freqs = {}
        l = toLoad.readline()
        if isKeyId(l):
            k= extractKey(l)
            lsize = int(getValuesSize(l))
        i=0
        while i<lsize:
            l = toLoad.readline()
            if l<>"":
                freqs[l.split(KV_SEPARATOR)[0]]=float(l.split(KV_SEPARATOR)[1])
            i+=1
        if k <>'' and len(freqs)>0:
            newContext.update({k:freqs})
    toLoad.close()
    return newContext
    
        
def basicTest():
    cont = {}
    cont = loadRaw("bacon",cont,"pg46.txt",100,20)
    saveContext(cont,"batman.raw")
    cont2 = loadContext("batman.raw")
    cont2.update(loadRaw("cheese",cont2,"pg46.txt",10,200))
    saveContext(cont2,"robin.raw")
    
    finalTest = loadContext("robin.raw")
    for k,v in finalTest.iteritems():
        print k,
        print v
    return finalTest
