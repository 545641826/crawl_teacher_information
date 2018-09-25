#! /usr/bin/env python
'''
Created on 2018年7月23日

@author: 54564
'''

def cut(str):
    imf={}    
    f=open(str, 'r', encoding='UTF-8')
    for line in f.read().splitlines(False):
        a,b=line.split(':',1)
        imf[a]=b
    f.close()    
    return(imf)


