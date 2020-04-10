#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 17:55:09 2020

@author: Stefanos Papadam
"""
def line(grid):
    col = -1 
    for row in range(len(grid)):
        col = grid[row].find('X')
        if col is not -1:
            break
    
    previousRow = row
    previousCol = col

    while True:
        pos = []
        cor = []
        currentRow = previousRow
        currentCol = previousCol + 1
        if currentCol < len(grid[0]) and currentCol >= 0:
            pos.append(grid[currentRow][currentCol])
            if grid[currentRow][currentCol] != ' ':
                cor.append([currentRow,currentCol])
                
        currentRow = previousRow
        currentCol = previousCol - 1
        if currentCol < len(grid[0]) and currentCol >= 0:
            pos.append(grid[currentRow][currentCol])
            if grid[currentRow][currentCol] != ' ':
                cor.append([currentRow,currentCol])
                 
        currentRow = previousRow + 1
        currentCol = previousCol  
        if currentRow < len(grid[0]) and currentRow >= 0:
            pos.append(grid[currentRow][currentCol])    
            if grid[currentRow][currentCol] != ' ':
                cor.append([currentRow,currentCol])
                
                
        currentRow = previousRow - 1
        currentCol = previousCol 
        if currentRow < len(grid[0]) and currentRow >= 0:
            pos.append(grid[currentRow][currentCol])            
            if grid[currentRow][currentCol] != ' ':
                cor.append([currentRow,currentCol])
            
        pos.remove(grid[currentRow][currentCol])
        
        if currentRow == previousRow:
            if grid[currentRow][currentCol] == "|":
                return False 
            
        if currentCol == previousCol:
            if grid[currentRow][currentCol] == "-":
                return False
        for i in range(len(cor)):
            if cor[i][0] == previousRow and cor[i][1] == previousCol:
                cor.remove(cor[i])
        previousRow = cor[0][0]
        previousCol = cor[0][1]
    
    
grid = ["                    ",
        "     +--------+     ",
        "  X--+        +--+  ",
        "                 |  ",
        "                 X  ",
        "                    "]

b = line(grid)

