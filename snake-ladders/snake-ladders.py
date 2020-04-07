#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:57:06 2020

@author: Stefanos Papadam
"""

class SnakesLadders():

    def __init__(self):
        self.player1 = 0
        self.player2 = 0 
        self.ladders = {2: 38, 7: 14, 8: 31, 15: 26,21: 42, 28: 84, 36: 44, 51: 67, 71: 91,78: 98,87: 94}
        self.snakes = {16: 6, 46: 25, 49: 11, 62: 19, 64: 60, 74: 53, 89: 68, 92: 88, 95: 75, 99: 80}
        self.turn = 0
        
    def play(self, die1, die2):
         
        self.turn += 1                                          # increase turn 
        if self.player1 != 101 and self.player2 != 101:         # 101 is the value that is assigned when a player has won 
            
            if self.turn % 2 == 1:
                summary = die1 + die2 + self.player1            # find whole summary 
                if summary in self.ladders:                     # check for ladders
                    self.player1 = self.ladders[summary]
                elif summary in self.snakes:                    # check for snakes 
                    self.player1 = self.snakes[summary]
                else:
                    self.player1 = summary
                square = self.player1
                player = 1
                                                                # if summary surpassed 100 then subtract from 100 
                if square > 100:
                    dif = square - 100
                    self.player1 = square = 100 - dif
                    if self.player1 in self.snakes:
                        self.player1 = square = self.snakes[self.player1]
            else:
                summary = die1 + die2 + self.player2            # find whole summary
                if summary in self.ladders:                     # check for ladders
                    self.player2 = self.ladders[summary]
                elif summary in self.snakes:                    # check for snakes
                    self.player2 = self.snakes[summary]
                else:
                    self.player2 = summary
                square = self.player2
                player = 2
                                                                # if summary surpassed 100 then subtract from 100 
                if square > 100:
                    dif = square - 100
                    self.player2 = square = 100 - dif
                    if self.player2 in self.snakes:
                        self.player2 = square = self.snakes[self.player2]
                        
                                                                # if dice have same value then this player is playing again     
        if die1 == die2:
            self.turn += 1
            
                                                                # return     
        if self.player1 < 100 and self.player2 < 100:
            return f"Player {player} is on square {square}"
        elif self.player1 == 100:
            self.player1 = 101
            return f"Player {player} Wins!"
        elif self.player2 == 100:
            self.player2 = 101
            return f"Player {player} Wins!"
        elif self.player1 == 101:
            return "Game over!"
        elif self.player2 == 101:
            return "Game over!"
        
# test
game = SnakesLadders()
print(game.play(1,1))
print(game.play(1,5))
print(game.play(6,2))
print(game.play(1,1))
print(game.play(2,3))
print(game.play(2,3))
print(game.play(2,1))
print(game.play(2,1))
print(game.play(2,1))
print(game.play(2,2))
print(game.play(2,2))
print(game.play(5,2))
print(game.play(5,4))
print(game.play(1,5))
print(game.play(1,6))
print(game.play(2,3))
print(game.play(1,6))