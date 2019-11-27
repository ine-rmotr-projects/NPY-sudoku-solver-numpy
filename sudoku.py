import numpy as np
import collections
import itertools

# Part 1:
def string_puzzle_to_arr(puzzle):
    return np.array([list(line.strip()) for line in puzzle.split('\n') if line.strip()], dtype=np.int)

class Board:
    def __init__(self, puzzle):
        pass

    def get_row(self, row_index):
        pass

    def get_column(self, col_index):
        pass

    def get_block(self, pos_1, pos_2):
        pass

    def iter_rows(self):
        pass

    def iter_columns(self):
        pass

    def iter_blocks(self):
        pass


# Part 2:
def is_subset_valid(arr):
    pass

def is_valid(board):
    pass


# Part 3:
def find_empty(board):
    pass

def is_full(board):
    pass

def find_possibilities(board, x, y):
    pass


# Part 4:
def adapt_long_sudoku_line_to_array(line):
    pass

def read_sudokus_from_csv(filename, read_solutions=False):
    pass

def detect_invalid_solutions(filename):
    pass