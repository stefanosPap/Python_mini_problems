class Game():
    
    def __init__(self, board):
        self.board = board
        
    def play(self, lines):
        Board = [[' '] * (2*self.board + 1)]
        for i in range(2 * self.board):
            Board.append([' '] * (2 * self.board + 1))
            
        k = 1
        for i in range(len(Board)):
            for j in range(len(Board)):
                if i%2 == 0:
                    if j%2 == 0:
                        Board[i][j] = '*'
                    else:
                        Board[i][j] = k
                        k += 1
                else:
                    if j%2 == 0:
                        Board[i][j] = k
                        k += 1
                        
        packages = [[0] * 4]
        for i in range(self.board**2):
            packages.append([0] *4)
            
        k = 1
        count = 0     
        for i in range(self.board**2):
            packages[i][0] = k
            packages[i][1] = packages[i][0] + self.board
            packages[i][2] = packages[i][1] + 1
            packages[i][3] = packages[i][2] + self.board
            count += 1 
            if count == self.board:
                count = 0
                k += self.board + 2
            else:
                k += 1   
        
        
        for i in range(len(packages)):
            count = 0
            lines = sorted(lines) 
            for j in range(len(lines)):
                if lines[j] == packages[i][0] or lines[j] == packages[i][1] or lines[j] == packages[i][2] or lines[j] == packages[i][3]:
                    count += 1
            if count == 3:
                for k in range(4):
                    lines.append(packages[i][k])
            lines = sorted(list(set(lines)))    
        return lines    
game = Game(4)
game.play([1, 2, 3, 4, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 20, 21, 22, 23, 24])
