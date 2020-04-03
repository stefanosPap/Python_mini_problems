#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 18:22:40 2020

@author: Stefanos Papadam
"""
import numpy as np
import datetime
def count(chessBoard):
    tic = datetime.datetime.now()
    # initialize dictionary 
    dictionary = {}    
    for i in range(2,len(chessBoard) + 1):
        dictionary.update({i: 0})
    chessBoard = np.array(chessBoard)
    
    # implementation
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
                   else:
                       break
                   
    # remove zeros from dictionary 
    for k in range(2,len(chessBoard) + 1):
        if dictionary[k] == 0:
            del dictionary[k]
    tim = datetime.datetime.now() - tic
    return dictionary

#test        
chessBoard1=[
  [1,2,3,4,5],
  [6,7,8,9,10],
  [11,12,13,14,15],
  [16,17,18,19,20],
  [21,22,23,24,25] 
]

chessBoard2 = [
            [0,1,1,1,1],
            [1,1,1,1,1],
            [1,1,0,1,1],
            [0,1,1,0,1],
            [1,1,1,1,1]
        ]
chessBoard = np.random.randint(2, size = (1000,1000))

d = count(chessBoard)
chessBoard=[
  [1,1,1,1],
  [1,1,0,0],
  [1,0,1,1],
  [1,1,1,1] 
]