class Game():
    
    def __init__(self, board):
        self.board = board
    
    def loop(self,lines,packages):
        lines_temp = lines 
        for i in range(len(packages)):
            count = 0
            lines_temp = sorted(lines_temp) 
            for j in range(len(lines_temp)):
                if lines_temp[j] == packages[i][0] or lines_temp[j] == packages[i][1] or lines_temp[j] == packages[i][2] or lines_temp[j] == packages[i][3]:
                    count += 1
            if count == 3:
                for k in range(4):
                    lines_temp.append(packages[i][k])
            lines_temp = sorted(list(set(lines_temp)))
        if lines != lines_temp:
            lines_temp = self.loop(lines_temp,packages)
        return lines_temp   
    
    def play(self, lines):
        
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
        lines = self.loop(lines,packages)
        return lines
    
    def boardConstruct(self):
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
        return Board 
        
     
game = Game(3)
a = [5, 6, 12, 13, 16, 19, 20, 23] 
b = [2, 5, 6, 9, 12, 13, 16, 19, 20, 23]
print(game.play(a))
print(b)

