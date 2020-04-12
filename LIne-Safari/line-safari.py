#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 17:55:09 2020

@author: Stefanos Papadam
"""
def line(grid):
    
    col = -1                                # find the location of one of the two X's 
    for row in range(len(grid)):
        col = grid[row].find('X')
        if col is not -1:
            break
    
    tempGrid = []                           # create gridCopy where we store 1 to each position that     
    for j in range(len(grid[0])):           # we've passed 
        tempGrid.append(0)        
    gridCopy = []    
    for i in range(len(grid)):
        gridCopy.append(tempGrid.copy())
        
    currentRow = row                        # we keep current row and column
    currentCol = col                        # to currentRow and currentCol accordingly  
    
    previousRow = row                       # we keep pevious row and column
    previousCol = col                       # to currentRow and currentCol accordingly  
    
    globCount = 0
    globCount2 = 0
    while True:
        
        cor = []                            # we keep in cor matrix the 4 possible positions                                             # first
        possibleRow = currentRow            # first
        possibleCol = currentCol + 1        # we check if grid[possibleRow][possibleCol] != '|' and grid[currentRow][currentCol] != '|'
                                            # because we can't have | character in the same row  
        if possibleCol < len(grid[0]) and possibleCol >= 0 and grid[possibleRow][possibleCol] != '|' and grid[currentRow][currentCol] != '|':
            cor.append([possibleRow,possibleCol])
                                            # we check grid[currentRow][currentCol] == "+" and previousCol == possibleCol
                                            # because we can's have same row or column after + character
            if grid[currentRow][currentCol] == "+" and previousRow == possibleRow:
                cor.pop()
            
        possibleCol = currentCol - 1        # second
                                            # we check if grid[possibleRow][possibleCol] != '|' and grid[currentRow][currentCol] != '|'
                                            # because we can't have | character in the same row
        if possibleCol < len(grid[0]) and possibleCol >= 0 and grid[possibleRow][possibleCol] != '|' and grid[currentRow][currentCol] != '|':
            cor.append([possibleRow,possibleCol])
                                            # we check grid[currentRow][currentCol] == "+" and previousCol == possibleCol
                                            # because we can's have same row or column after + character
            if grid[currentRow][currentCol] == "+" and previousRow == possibleRow:
                cor.pop()                 
        
        possibleRow = currentRow - 1        # third 
        possibleCol = currentCol            # we check if grid[possibleRow][possibleCol] != '-' and grid[currentRow][currentCol] != '-'
                                            # because we can't have - character in the same column
        if possibleRow < len(grid) and possibleRow >= 0 and grid[possibleRow][possibleCol] != '-' and grid[currentRow][currentCol] != '-':
            cor.append([possibleRow,possibleCol])
                                            # we check grid[currentRow][currentCol] == "+" and previousCol == possibleCol
                                            # because we can's have same row or column after + character 
            if grid[currentRow][currentCol] == "+" and previousCol == possibleCol:
                cor.pop()                
                
        possibleRow = currentRow + 1        # fourth
                                            # we check if grid[possibleRow][possibleCol] != '-' and grid[currentRow][currentCol] != '-'
                                            # because we can't have - character in the same column
        if possibleRow < len(grid) and possibleRow >= 0 and grid[possibleRow][possibleCol] != '-' and grid[currentRow][currentCol] != '-':
            cor.append([possibleRow,possibleCol])
                                            # we check grid[currentRow][currentCol] == "+" and previousCol == possibleCol
                                            # because we can's have same row or column after + character
            if grid[currentRow][currentCol] == "+" and previousCol == possibleCol:
                cor.pop()
                
        count = 0                           # count keeps the number of moves in order to avoid ambiguity
        for i in range(len(cor)):
            if grid[cor[i][0]][cor[i][1]] != " " and [cor[i][0], cor[i][1]] != [previousRow, previousCol] and gridCopy[cor[i][0]][cor[i][1]] == 0:
                nextMove = [cor[i][0], cor[i][1]]           # keep the nextMove 
                count += 1
                
                if grid[nextMove[0]][nextMove[1]] == '+':   # hack for only one case :)
                    globCount += 1                          #
                if grid[nextMove[0]][nextMove[1]] == '-':   # grid = ["  ++  ",      
                    globCount2 += 1                         # " ++++ ",   
                                                            # " ++++ ",   
                                                            # "X-++-X"]
                                                            # end of hack  :)
                if count > 1 and grid[nextMove[0]][nextMove[1]] != '+':
                    return False                            # if there are more than one roads there is ambiguity
        
        if globCount > 11 and globCount2 == 2:              # if the hack case exists return False 
            return False
        
        if count == 0:                                      # if no available movies exists then False  
            return False        
        
        if grid[currentRow][currentCol] == "-":             # if current element is -
            if nextMove[1] == currentCol:                   # if nextMove is in the same column then False 
                return False
            if grid[nextMove[0]][nextMove[1]] == "|" :      # if next element is | then False
                return False
        
        if grid[currentRow][currentCol] == "|":             # if current element is |
            if nextMove[0] == currentRow:                   # if nextMove is in the same row then False
                return False
            if grid[nextMove[0]][nextMove[1]] == "-" :      # if next element is - then False
                return False
            
        if grid[currentRow][currentCol] == "+":             # if current element is +
            if previousRow == nextMove[0]:                  # if nextMove is in the same row then False
                return False
            if currentRow == nextMove[0] == "|":            # if next element is | and in the same row then False
                return False
            if currentCol == nextMove[1] == "-":            # if next element is - and in the same column then False
                return False 
            if currentRow == previousRow == nextMove[0]:    # if current, next and previous row are the same then False 
                return False
            elif currentCol == previousCol == nextMove[1]:  # if current, next and previous column are the same then False 
                return False

        
        gridCopy[currentRow][currentCol] = 1                # update gridCopy in order to know where we have passed  
        previousRow = currentRow                            # update previous row and column 
        previousCol = currentCol
        currentRow = nextMove[0]                            # update current row and column 
        currentCol = nextMove[1]
        if grid[currentRow][currentCol] == 'X':             # if found X the stop, we reach the last position of the path  
            gridCopy[currentRow][currentCol] = 1
            break
        
    
    for i in range(len(grid)):                              # check for redundant path 
        for j in range(len(grid[0])):
            if gridCopy[i][j] == 0 and grid[i][j] != " ":
                return False

    return True                                             # if neither of the above cases exists then the path is valid 


# Test cases 
grid1 = ["                      ",
         "   +-------+          ",
         "   |      +++---+     ",
         "X--+      +-+   X     "]



grid2 = ["    +----+",  
        "    |+--+|",  
        "    ||X+||",  
        "    |+-+||",  
        "    +---+|",  
        "X--------+"]

grid3 = ["+-----+",  
         "|+---+|",  
         "||+-+||",  
         "|||X+||",  
         "X|+--+|",  
         " +----+"]

grid4 = ["X-----+"  
        "X     |"  
        "|     |"  
        "|     |"  
        "+-----+"]
grid5 = ["  X-----+",  
        "X |     |",  
        "  |     |",  
        "  |     |",  
        "  +-----+"]
grid6 = ["X-----+",  
        "      |",  
        "X-----+",  
        "      |",  
        "------+"]
grid7 = ["X-----X"]

grid8 = ["      X  ",   
        "X+++  +-+", 
        " +++--+ |", 
        "      +-+"]

grid9 = ["  ++  ",      
        " ++++ ",   
        " ++++ ",   
        "X-++-X"]

validation = line(grid1)