import numpy as np
import collections
import itertools

# Part 1:
def string_puzzle_to_arr(puzzle):
    return np.array([list(line.strip()) for line in puzzle.split('\n') if line.strip()], dtype=np.int)

class Board:
    def __init__(self, puzzle_string):
        if type(puzzle_string) == str:
            self.arr = string_puzzle_to_arr(puzzle_string)
        else:
            self.arr = puzzle_string

    def get_row(self, row_index):
        return self.arr[row_index]

    def get_column(self, col_index):
        return self.arr[:, col_index]

    def get_block(self, pos_1, pos_2):
        return self.arr[(pos_1 * 3): ((pos_1+1) * 3), (pos_2 * 3): ((pos_2+1) * 3)]

    def iter_rows(self):
        return [row for row in self.arr]

    def iter_columns(self):
        return [col for col in self.arr.T]

    def iter_blocks(self):
        return [self.arr[(pos_1 * 3): ((pos_1+1) * 3), (pos_2 * 3): ((pos_2+1) * 3)] for pos_1 in range(3) for pos_2 in range(3)]
        # Simplified version for reading purposes:
        # result = []
        # for pos_1 in range(3):
        #     for pos_2 in range(3):
        #         block = puzzle[(pos_1 * 3): ((pos_1+1) * 3), (pos_2 * 3): ((pos_2+1) * 3)]
        #         result.append(block)


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
