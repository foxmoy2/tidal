File Descriptions:

guess_number.py: Code Exercise 1

chessercise.py: Code Exercise 2

test_check.py: Unittests for Exercise 2


External Dependencies (install via pip)
numby, unittest

Samples output:

>ls
chessercise.py	chessercise.pyc	guess_number.py	test_chess.py
>./guess_number.py 
In this game, you think of a number from 1 through n and I will
try to guess what it is.  After each guess, enter h if my guess
is too high, if too low, or c if correct.
Please enter a maximum number n: 100
50? h
25? l
37? l
43? h
40? h
38? l
Your number is 39
It took me 7 guesses.
I averaged 7.0 guesses per game for 1 game(s).
Play again (y/n)y
50? l
75? l
87? l
93? l
96? h
94? c
Your number is 94
It took me 6 guesses.
I averaged 6.5 guesses per game for 2 game(s).
Play again (y/n)n
>./chessercise.py -piece KNIGHT -position e5
c4,c6,d3,d7,f3,f7,g4,g6
>./test_chess.py 
................
----------------------------------------------------------------------
Ran 16 tests in 0.001s

OK
>

