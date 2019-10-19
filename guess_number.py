#!/usr/bin/env python 

__author__ = 'bernied'

import sys

import numpy

def print_results(guess_num, num_guesses, tot_guesses, tot_games):
    """
    This function prints results from each run of the game.
    """
    print("Your number is %d" % guess_num)
    print("It took me %d guesses." % num_guesses)
    print("I averaged %.1f guesses per game for %d game(s)." % (float(
        tot_guesses)/tot_games , tot_games))

def guess_number(min_num, max_num, num_guesses):
    """
    This is a recursive function that guesses between min_num and max_num using
    binary search.
    """

    # keep track of guesses in this run of the game
    num_guesses = num_guesses + 1

    # make sure our algorithm doesn't have a bug and runs away!
    if (num_guesses > (1 + numpy.log2(orig_max))):
        raise(ArithmeticError("exceeded 1 + log2(n) guesses!"))

    # using binary search based on supplied min_num and max_num get next median

    guess_num = min_num + (max_num - min_num) / 2

    # if exactly 2 between max_num and min_num, the guess must be in between
    if (max_num - min_num) == 2:
        # cache final recursion's copy of guestNum, num_guesses so that we only
        # return these up the stack
        end_guess, end_num_guess = guess_num, num_guesses
        return (end_guess, end_num_guess)

    resultStr = "?"
    while((resultStr != "c") or (resultStr != "h") or (resultStr != "l")):
        resultStr = raw_input(str(guess_num) + "? ")
        if (resultStr == "c"):
        # cache final recursion's copy of guestNum, num_guesses so that we only
        # return these up the stack
            end_guess, end_num_guess = guess_num, num_guesses
            return (end_guess, end_num_guess)
        elif resultStr == "h":
        # Since this guess was too high, we can bisect the search range below
        # the guess_num
            return(guess_number(min_num, guess_num, num_guesses))
        elif resultStr == "l":
            # Since this guess was too low, we can bisect the search range above
            # the guess_num
            return(guess_number(guess_num, max_num, num_guesses))

def main():

    # used for checking convergence of algorithm to 1 + log2(max_num)
    global orig_max

    # check that no arg was supplied
    if len(sys.argv) != 1:
        raise TypeError("Can not have any arguments!")

    print "In this game, you think of a number from 1 through n and I will\n" \
          "try to guess what it is.  After each guess, enter h if my guess\n" \
          "is too high, if too low, or c if correct."

    # set up variables
    min_num = 1
    orig_max = max_num =  int(raw_input("Please enter a maximum number n: "))

    tot_games = 0
    tot_guesses = 0
    play_again = "y"

    # loop while user wants to play the game
    while((play_again == "y") or (play_again == "Y")):
        num_guesses = 0
        tot_games = tot_games + 1

        # starts one run of the game by calling guess_number
        end_guess, endnum_guesses = guess_number(min_num, max_num, num_guesses)
        tot_guesses = tot_guesses + endnum_guesses

        # display current run and total stats
        print_results(end_guess, endnum_guesses, tot_guesses, tot_games)
        play_again = raw_input("Play again (y/n)")

if __name__ == "__main__":
    main()
