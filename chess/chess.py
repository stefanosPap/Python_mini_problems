# -*- coding: utf-8 -*-
#function for checking if king is in check from ♛, ♜ or ♝
def check(chessman, board, queen = '♛'):
    posKing = -1 # keep king's and  
    pos = -1 # chessman's positions
            # chessman is ♜ or ♝
    for i in range(len(board)):    
        if board[i] == queen or board[i] == chessman:
            pos = i
        if board[i] == ' ':
            board[i] = ''
        if board[i] == '♔':
            posKing = i
        if posKing is not -1 and pos is not -1: #stop when both found 
            break
    if posKing < pos:
        state = not any(board[posKing+1:pos]) #check if between king and the current chessman exists another chessman 
    elif posKing > pos and pos != -1:
        state = not any(board[pos+1:posKing])
    
    if pos == -1: #if there is no chessman then state will be False 
        state = False 
    return state

def king_is_in_check(chessboard):
    
    for i in range(len(chessboard)): #find king's position in at chessboard 
        for j in range(len(chessboard[i])):
            if chessboard[i][j] == '♔':
                posi = i 
                posj = j
    
    BoardVertically = [' '] * len(chessboard)
    BoardHorizontically = [' '] * len(chessboard)
    mainBoardDiagonally = [' '] * len(chessboard)
    secondaryBoardDiagonally = [' '] * len(chessboard)
    horseBoard = [''] * len(chessboard)
    
    k = 0
    initialized = False #flag for checking if pawn exists
    
    for i in range(len(chessboard)):
        
        BoardVertically[i] = chessboard[i][posj]
        
        for j in range(len(chessboard[0])):
        
            BoardHorizontically[j] = chessboard[posi][j]
            if abs(i - posi) == abs(j - posj) or (i == posi and j == posj):
                if (i < posi and j < posj) or (i > posi and j > posj) or (i == posi and j == posj):
                    mainBoardDiagonally[i] = chessboard[i][j] #keep the elements for the main diagonal 
                    # only in two positions pawns can beat the king
                    #1st 
                    if posi - i == 1 and chessboard[i][j] == '♟': #check for pawn in main diag 
                        pawni = i
                        pawnj = j
                        initialized = True  
                if (i > posi and j < posj) or (i < posi and j > posj) or (i == posi and j == posj):
                    secondaryBoardDiagonally[i] = chessboard[i][j] #keep the elements for the secondary diagonal
                    #2nd
                    if j - posj == 1 and chessboard[i][j] == '♟': #check for pawn in secondary diag
                        pawni = i
                        pawnj = j
                        initialized = True
            #check for horses 
            if (abs(i - posi) == 1 and abs(j - posj) == 2) or (abs(i - posi) == 2 and abs(j - posj) == 1): 
                if chessboard[i][j] != '♞':
                    horseBoard[k] = ''
                else:
                    horseBoard[k] = chessboard[i][j]
                k += 1 
    #state contains the status of each check          
    state = [False] * 6
    state[0] = check('♜',BoardVertically)
    state[1] = check('♜',BoardHorizontically)
    state[2] = check('♝',mainBoardDiagonally)
    state[3] = check('♝',secondaryBoardDiagonally) 
         
    if any(horseBoard):
        state[4] = True
    if initialized == True:
        if chessboard[pawni][pawnj] == '♟':
            state[5] = True 
        
    return any(state)   
    
#test
chessboard =   [
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ','♛',' ',' ',' ',' '],
            [' ','♟',' ',' ',' ',' ',' ',' '],
            [' ',' ','♔',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ','♜',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ']
        ]
king_is_in_check(chessboard)