#!/usr/bin/env python

__author__ = 'bernied'

import argparse

# Constants
PERMITTED_COLS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
PERMITTED_ROWS = ['1', '2', '3', '4', '5', '6', '7', '8']

def calculate_rook(col, row):
    """
    This is a function calculates the possible moves for a rook starting from
    position (col, row)
    """
    permitted_moves_vertical = []
    permitted_moves_horizontal = []
    for scan_col in PERMITTED_COLS:
        for scan_row in PERMITTED_ROWS:
            if col == scan_col:
                if row != scan_row:
                    # as long as I am in my column, unless the row also matches
                    # (then I am on the actual location of the piece)
                    permitted_moves_vertical.append(scan_col + scan_row)
            if row == scan_row:
                if col != scan_col:
                    # as long as I am in my row, unless the column also matches
                    # (then I am on the actual location of the piece)
                    permitted_moves_horizontal.append(scan_col + scan_row)

    return (permitted_moves_horizontal + permitted_moves_vertical)

def calculate_knight(col, row):
    """
    This is a function calculates the possible moves for a knight starting from
    position (col, row)
    """
    permitted_moves=[]
    for scan_col in PERMITTED_COLS:
        for scan_row in PERMITTED_ROWS:
            if ((col == scan_col) and
                (row == scan_row)):
                # skip my actual position
                continue
            # left or right 2
            if abs(PERMITTED_COLS.index(scan_col) -
                   PERMITTED_COLS.index(col)) == 2:
                # up or down 1
                if abs(PERMITTED_ROWS.index(scan_row) - PERMITTED_ROWS.index(
                        row)) == 1:
                    permitted_moves.append(scan_col + scan_row)

            # left or  right 1
            if abs(PERMITTED_COLS.index(scan_col) - PERMITTED_COLS.index(col)) == 1:
                # up or down 2
                if abs(PERMITTED_ROWS.index(scan_row) - PERMITTED_ROWS.index(
                        row)) == 2:
                    permitted_moves.append(scan_col + scan_row)

    return (permitted_moves)

def calculate_bishop(col, row):
    """
    This is a function calculates the possible moves for a bishop starting from
    position (col, row)
    """
    permitted_moves = []
    for scan_col in PERMITTED_COLS:
        for scan_row in PERMITTED_ROWS:
            if ((col == scan_col) and
                (row == scan_row)):
                # skip my actual position
                continue
            if abs(PERMITTED_COLS.index(scan_col) - PERMITTED_COLS.index(
                    col)) == abs(PERMITTED_ROWS.index(scan_row) - PERMITTED_ROWS.index(
                        row)):
                    permitted_moves.append(scan_col + scan_row)

    return (permitted_moves)

def calculate_queen(col, row):
    """
    This is a function calculates the possible moves for a queen starting from
    position (col, row) which is the combination of a rook and a bishop's
    possible moves
    """
    return(calculate_rook(col,row) + calculate_bishop(col,row))


def main():
    parser = argparse.ArgumentParser(description='Forecast chess moves.')

    parser.add_argument("-piece", required=True)
    parser.add_argument("-position", required=True)

    args = parser.parse_args()

    col = args.position[0]
    row = args.position[1]

    if len(args.position) != 2:
        exit("-position must be a letter followed by a number ([a-h][1-8])")

    if ((not col in PERMITTED_COLS) or
        (not row in PERMITTED_ROWS)):
        exit( "-position has to be in range of [a-h][1-8]")


    if args.piece == "BISHOP":
        print ",".join(calculate_bishop(col, row))
    elif args.piece == "KNIGHT":
        print ",".join(calculate_knight(col, row))
    elif args.piece == "QUEEN":
        print ",".join(calculate_queen(col, row))
    elif args.piece == "ROOK":
        print ",".join(calculate_rook(col, row))
    else:
        exit("-piece needs to be one of (BISHOP, KNIGHT, QUEEN, ROOK)")



if __name__ == "__main__":
    main()
