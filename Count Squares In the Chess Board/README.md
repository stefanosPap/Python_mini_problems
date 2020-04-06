## Count Squares In the Chess Board

You are given a chessBoard, a 2d integer array that contains only 0 or 1. 0 represents a chess piece and 1 represents a empty grid. It's always square shape.

Your task is to count the number of squares made of empty grids.

The smallest size of the square is 2 x 2. The biggest size of the square is n x n, where n is the size of chess board.

A square can overlap the part of other squares. For example:

If
<pre>
chessBoard=[ 
  [1,1,1],
  [1,1,1],
  [1,1,1]
]

</pre>
...there are four 2 x 2 squares in the chess board:

<pre>
[1,1, ]  [ ,1,1]  [ , , ]  [ , , ]
[1,1, ]  [ ,1,1]  [1,1, ]  [ ,1,1]
[ , , ]  [ , , ]  [1,1, ]  [ ,1,1]
</pre>
And one 3 x 3 square:
<pre>
[1,1,1]
[1,1,1]
[1,1,1]
</pre>
Your output should be an object/dict. Each item in it should be: size:number, where size is the square's size, and number is the number of squares.

For example, if there are four 2 x 2 squares and one 3 x 3 square in the chess board, the output should be: {2:4,3:1} (or any equivalent hash structure in your language). The order of items is not important, {3:1,2:4} is also a valid output.

If there is no square in the chess board, just return {}.

The problem is from https://www.codewars.com/kata/5bc6f9110ca59325c1000254
