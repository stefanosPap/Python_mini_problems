Starting with an empty grid of dots, two players take turns adding a single horizontal or vertical line between two unjoined adjacent dots. The player who completes the fourth side of a 1×1 box earns one point and takes another turn only if another box can be made. (A point is typically recorded by placing a mark that identifies the player in the box, such as an initial). The game ends when no more lines can be placed. The winner is the player with the most points. The board may be of any size. When short on time, a 2×2 board (a square of 9 dots) is good for beginners. A 5×5 is good for experts. 

**Task**

  	Your task is to complete the class called Game. You will be given the board size as an integer board that will be between 1 and 26, therefore the game size will be board x board. You will be given an array of lines that have already been taken, so you must complete all possible squares.

**Rules**


    1.  The integer board will be passed when the class is initialised.

    2.  board will be between 1 and 26.

    3.  The lines array maybe empty or contain a list of line integers.

    4.  You can only complete a square if 3 out of the 4 sides are already complete.

    5.  The lines array that is passed into the play() function may not be sorted numerically!

**Returns**

  	Return an array of all the lines filled in including the original lines.

    Return array must be sorted numerically.

    Return array must not contain duplicate integers. 


Example 1

board = 2
lines = [1, 3, 4]
game = Game(board)
game.play(lines) => [1, 3, 4, 6]

Example 2

board = 2
lines = [1, 2, 3, 4, 5, 8, 10, 11, 12]
game = Game.new(board)
game.play(lines) => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

The problem is from https://www.codewars.com/kata/58fdcc51b4f81a0b1e00003e/train/python
