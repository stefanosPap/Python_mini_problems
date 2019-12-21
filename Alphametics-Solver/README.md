Alphametics is a type of cryptarithm in which a set of words is written down in the form of a long addition sum or some other mathematical problem. The objective is to replace the letters of the alphabet with decimal digits to make a valid arithmetic sum.

For this kata, your objective is to write a function that accepts an alphametic equation in the form of a single-line string and returns a valid arithmetic equation in the form of a single-line string.


example_tests = (
	('SEND + MORE = MONEY','9567 + 1085 = 10652'),
	('ZEROES + ONES = BINARY','698392 + 3192 = 701584'),
	('COUPLE + COUPLE = QUARTET','653924 + 653924 = 1307848'),
	('DO + YOU + FEEL = LUCKY','57 + 870 + 9441 = 10368'),
	('ELEVEN + NINE + FIVE + FIVE = THIRTY','797275 + 5057 + 4027 + 4027 = 810386')
)


https://www.codewars.com/kata/alphametics-solver/train/python