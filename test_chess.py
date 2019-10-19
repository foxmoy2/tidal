#!/usr/bin/env python

import unittest

from chessercise import calculate_bishop, calculate_knight, calculate_queen, \
  calculate_rook

class TestApp(unittest.TestCase):
  def setUp(self):
    pass

  def tearDown(self):
    pass


  # test functions for the individual pieces
  def test_bishop(self):
    possible_moves = calculate_bishop("c", "4")
    self.assertEqual(possible_moves, ["a2","a6","b3","b5","d3","d5","e2","e6",
                                      "f1","f7","g8"])

  def test_knight(self):
    possible_moves = calculate_knight("e", "5")
    self.assertEqual(possible_moves, ["c4","c6","d3","d7","f3","f7","g4","g6"])

  def test_queen(self):
    possible_moves = calculate_queen("d", "3")
    self.assertEqual(possible_moves, ["a3","b3","c3","e3","f3","g3","h3",
                                      "d1","d2","d4","d5","d6","d7","d8",
                                      "a6","b1","b5","c2","c4","e2","e4","f1",
                                      "f5","g6","h7"])
  def test_rook(self):
    possible_moves = calculate_rook("e", "4")
    self.assertEqual(possible_moves, ["a4","b4","c4","d4","f4","g4","h4","e1",
                                      "e2","e3","e5","e6","e7","e8"])

  # test functions for the indvidual pieces in all 4 corners
  def test_upper_left_rook(self):
    possible_moves = calculate_rook("a", "8")
    self.assertEqual(possible_moves, ["b8","c8","d8","e8","f8","g8","h8",
                                      "a1","a2","a3","a4","a5","a6","a7"])

  def test_upper_left_bishop(self):
    possible_moves = calculate_bishop("a", "8")
    self.assertEqual(possible_moves, ["b7","c6","d5","e4","f3","g2","h1"])

  def test_upper_left_knight(self):
    possible_moves = calculate_knight("a","8")
    self.assertEqual(possible_moves, ["b6","c7"])


  def test_upper_right_rook(self):
    possible_moves = calculate_rook("h", "8")
    self.assertEqual(possible_moves, ["a8", "b8","c8","d8","e8","f8","g8",
                                      "h1","h2","h3","h4","h5","h6","h7"])

  def test_upper_right_bishop(self):
    possible_moves = calculate_bishop("h", "8")
    self.assertEqual(possible_moves, ["a1","b2","c3","d4","e5","f6","g7"])

  def test_upper_right_knight(self):
    possible_moves = calculate_knight("h","8")
    self.assertEqual(possible_moves, ['f7', 'g6'])


  def test_lower_left_rook(self):
    possible_moves = calculate_rook("a", "1")
    self.assertEqual(possible_moves, ["b1","c1","d1","e1","f1","g1","h1",
                                      "a2","a3","a4","a5","a6","a7","a8"])

  def test_lower_left_bishop(self):
    possible_moves = calculate_bishop("a", "1")
    self.assertEqual(possible_moves, ["b2","c3","d4","e5","f6","g7","h8"])

  def test_lower_left_knight(self):
    possible_moves = calculate_knight("a","1")
    self.assertEqual(possible_moves, ['b3', 'c2'])


  def test_lower_right_rook(self):
    possible_moves = calculate_rook("h", "1")
    self.assertEqual(possible_moves, ["a1","b1","c1","d1","e1","f1","g1",
                                      "h2","h3","h4","h5","h6","h7","h8"])

  def test_lower_right_bishop(self):
    possible_moves = calculate_bishop("h", "1")
    self.assertEqual(possible_moves, ["a8","b7","c6","d5","e4","f3","g2"])

  def test_lower_right_knight(self):
    possible_moves = calculate_knight("h","1")
    self.assertEqual(possible_moves, ['f2', 'g3'])


if __name__ == '__main__':
  unittest.main()
