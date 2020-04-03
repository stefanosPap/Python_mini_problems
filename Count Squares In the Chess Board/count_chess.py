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
    chessBoard = np.array(chessBoard)
    p = 2
    for i in range(len(chessBoard) - p + 1):
        for j in range(len(chessBoard) - p  + 1):
            k = 2
            a = chessBoard[i:i+k,j:j+k]
            if all(a.flatten()):
               dictionary[k] += 1
               while True:
                   k += 1
                   if i+k <= len(chessBoard) and j+k <= len(chessBoard):
                       a = chessBoard[i:i+k,j:j+k]
                       if all(a.flatten()):
                           dictionary[k] += 1
                   else:
                      break
    for k in range(2,len(chessBoard) + 1):
        if dictionary[k] == 0:
            del dictionary[k]
    return dictionary
        
chessBoard1=[
  [1,2,3,4,5],
  [6,7,8,9,10],
  [11,12,13,14,15],
  [16,17,18,19,20],
  [21,22,23,24,25] 
]
'''        
    numpyChess = np.array(chessBoard)
    l = len(numpyChess)
    rows = slice(0,l)
    columns = slice(0,l)
    cur = numpyChess[rows,columns].flatten()
    if all(cur):
       dictionary[l] += 1        
    
    l = len(numpyChess)    
    upperRight = numpyChess[::,l::-1]
    downLeft = numpyChess[l::-1]
    downRight = downLeft[::,l::-1]
    
    while True:
        start = slice(l,None,-1)
        end = slice(None,l+1)
        cur = numpyChess[start,end].flatten()
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
'''

        
        
chessBoard2 = [
            [0,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1],
            [0,1,1,0,1],
            [1,1,1,1,1]
        ]
chessBoard=[
  [1,1,1,1,1],
  [1,1,1,1,1],
  [1,1,1,1,1],
  [1,1,1,1,1],
  [1,1,1,1,1] 
]
d = count(chessBoard2)
chessBoard=[
  [1,1,1,1],
  [1,1,0,0],
  [1,0,1,1],
  [1,1,1,1] 
]