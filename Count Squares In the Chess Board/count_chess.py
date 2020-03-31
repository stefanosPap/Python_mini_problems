#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 18:22:40 2020

@author: Stefanos Papadam
"""
import numpy as np

def count(chessBoard):
    # initialize dictionary 
    dictionary = {}    
    for i in range(2,len(chessBoard) + 1):
        dictionary.update({i: 0})
    numpyChess = np.array(chessBoard)
    k = 2
    l = len(numpyChess)
    while True: 
        cur = numpyChess[0:k,0:k].flatten()
        if all(cur):
            dictionary[k + 1] += 1        
        k += 1 
        if k == len(chessBoard):
            break
    l = len(numpyChess)
    while True:
        cur = numpyChess[l::-1,0:l].flatten()
        if all(cur):
            dictionary[l] += 1
        l -=1
        if l == 0:
            break
    l = len(numpyChess)
    while True:
        cur = numpyChess[0:l,l::-1].flatten()
        if all(cur):
            dictionary[l - 1] += 1
        l -=1
        if l == 0:
            break
    l = len(numpyChess)
    while True:
        cur = numpyChess[l::-1,l::-1].flatten()
        if all(cur):
            dictionary[l - 1] += 1
        l -=1
        if l == 0:
            break
    return dictionary


chessBoard1=[
  [1,2,3,4,5],
  [6,7,8,9,10],
  [11,12,13,14,15],
  [16,17,18,19,20],
  [21,22,23,24,25] 
]
chessBoard=[
  [1,1,1,1,1],
  [1,1,1,1,1],
  [1,1,1,1,1],
  [1,1,1,1,1],
  [1,1,1,1,1] 
]
d = count(chessBoard)