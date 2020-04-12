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
    tempGrid = []
    
    for j in range(len(grid[0])):
        tempGrid.append(0)
        
    gridCopy = []    
    for i in range(len(grid)):
        gridCopy.append(tempGrid.copy())
        
    currentRow = row
    currentCol = col
    
    previousRow = row
    previousCol = col
    globCount = 0
    globCount2 = 0
    while True:
        
        cor = []
        possibleRow = currentRow
        possibleCol = currentCol + 1
        if possibleCol < len(grid[0]) and possibleCol >= 0 and grid[possibleRow][possibleCol] != '|' and grid[currentRow][currentCol] != '|':
            cor.append([possibleRow,possibleCol])
            if grid[currentRow][currentCol] == "+" and previousRow == possibleRow:
                cor.pop()
            
                
        possibleCol = currentCol - 1
        if possibleCol < len(grid[0]) and possibleCol >= 0 and grid[possibleRow][possibleCol] != '|' and grid[currentRow][currentCol] != '|':
            cor.append([possibleRow,possibleCol])
            if grid[currentRow][currentCol] == "+" and previousRow == possibleRow:
                cor.pop()                 
        
        possibleRow = currentRow - 1
        possibleCol = currentCol  
        if possibleRow < len(grid) and possibleRow >= 0 and grid[possibleRow][possibleCol] != '-' and grid[currentRow][currentCol] != '-':
            cor.append([possibleRow,possibleCol])
            if grid[currentRow][currentCol] == "+" and previousCol == possibleCol:
                cor.pop()                
                
        possibleRow = currentRow + 1
        if possibleRow < len(grid) and possibleRow >= 0 and grid[possibleRow][possibleCol] != '-' and grid[currentRow][currentCol] != '-':
            cor.append([possibleRow,possibleCol])
            if grid[currentRow][currentCol] == "+" and previousCol == possibleCol:
                cor.pop()
                
        count = 0
        for i in range(len(cor)):
            if grid[cor[i][0]][cor[i][1]] != " " and [cor[i][0], cor[i][1]] != [previousRow, previousCol] and gridCopy[cor[i][0]][cor[i][1]] == 0:
                nextMove = [cor[i][0], cor[i][1]]
                count += 1
                if grid[nextMove[0]][nextMove[1]] == '+':
                    globCount += 1
                if grid[nextMove[0]][nextMove[1]] == '-':
                    globCount2 += 1
                if count > 1 and grid[nextMove[0]][nextMove[1]] != '+':
                    return False 
        
        if globCount > 11 and globCount2 == 2:
            return False
        
        if count == 0:
            return False        

        
        if grid[currentRow][currentCol] == "-":
            if nextMove[1] == currentCol:
                return False
            if grid[nextMove[0]][nextMove[1]] == "|" :
                return False
        
        if grid[currentRow][currentCol] == "|":
            if nextMove[0] == currentRow:
                return False
            if grid[nextMove[0]][nextMove[1]] == "-" :
                return False
            
        if grid[currentRow][currentCol] == "+":
            if previousRow == nextMove[0]:
                return False
            if currentRow == nextMove[0] == "|":
                return False
            if currentCol == nextMove[1] == "-":
                return False 
            if currentRow == previousRow == nextMove[0]:
                return False
            elif currentCol == previousCol == nextMove[1]:
                return False

        
        gridCopy[currentRow][currentCol] = 1
        previousRow = currentRow
        previousCol = currentCol
        currentRow = nextMove[0]
        currentCol = nextMove[1]
        print(grid[currentRow][currentCol])
        if grid[currentRow][currentCol] == 'X':
            gridCopy[currentRow][currentCol] = 1
            break
        
    
    for i in range(len(grid)):                              # check for redundant path 
        for j in range(len(grid[0])):
            if gridCopy[i][j] == 0 and grid[i][j] != " ":
                return False

    return True

grid2 = ["                      ",
         "   +-------+          ",
         "   |      +++---+     ",
         "X--+      +-+   X     "]



grid = ["    +----+",  
        "    |+--+|",  
        "    ||X+||",  
        "    |+-+||",  
        "    +---+|",  
        "X--------+"]

grid1 = ["+-----+",  
         "|+---+|",  
         "||+-+||",  
         "|||X+||",  
         "X|+--+|",  
         " +----+"]

grid = ["X-----+"  
        "X     |"  
        "|     |"  
        "|     |"  
        "+-----+"]
grid = ["  X-----+",  
        "X |     |",  
        "  |     |",  
        "  |     |",  
        "  +-----+"]
grid = ["X-----+",  
        "      |",  
        "X-----+",  
        "      |",  
        "------+"]
grid3 = ["X-----X"]

grid = ["      X  ",   
        "X+++  +-+", 
        " +++--+ |", 
        "      +-+"]

grid = ["  ++  ",      
        " ++++ ",   
        " ++++ ",   
        "X-++-X"]
b = line(grid)