'''
Created on 26/12/2011

@author: rosjose
'''
' -*- coding: cp1252 -*-'
UNDESIRABLE = ["\\","|","\"", "'",":","!","?","&",".",",",";","(",")","[","]","{","}"]

def cleanNonAlfabeticalChars(w):
    print w,len(w)
    if len(w)>0:
        if UNDESIRABLE.count(w[0])>0:  
            w = w[1:]
    if len(w)>0:
        if UNDESIRABLE.count(w[-1])>0:
            w = w[:(len(w)-1)]
    return w