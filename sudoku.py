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


#### Solution ####
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
        #         block = puzzle[(pos_1 * 3): ((pos_1+1) * 3), (pos_2 * 3): ((pos_2+1) * 3)]
        #         result.append(block)


# Part 2:
def is_subset_valid(arr):
    pass

def is_valid(board):
    pass

#### Solution ####
def is_subset_valid(arr):
    count = dict(collections.Counter(arr.flatten()))
    if 0 in count:
        del count[0]
    return len([key for key, val in count.items() if val > 1]) == 0

def is_valid(board):
    rows = board.iter_rows()
    cols = board.iter_columns()
    blocks = board.iter_blocks()
    for subset in itertools.chain(rows, cols, blocks):
        if not is_subset_valid(subset):
            return False
    return True

# Part 3:
def find_empty(board):
    pass

def is_full(board):
    pass

def find_possibilities(board, x, y):
    pass

#### Solution ####
def find_empty(board):
    empty_cells = np.argwhere(board.arr == 0)
    if len(empty_cells) == 0:
        return None
    return empty_cells

def is_full(board):
    return bool(np.sum(board.arr == 0) == 0)

def find_possibilities(board, x, y):
    block_pos_1, block_pos_2 = x // 3, y // 3
    all_elements = (board.get_row(x), board.get_column(y), board.get_block(block_pos_1, block_pos_2).flatten())
    values = np.concatenate(all_elements)
    non_zero = values[values != 0]
    uniques = np.unique(non_zero)
    return np.setdiff1d(np.arange(1, 10), uniques)

# Part 4:
def adapt_long_sudoku_line_to_array(line):
    pass

def read_sudokus_from_csv(filename, read_solutions=False):
    pass

def detect_invalid_solutions(filename):
    pass


#### Solution ####

import csv

def adapt_long_sudoku_line_to_array(line):
    return np.array([int(c) for c in line]).reshape(9, 9)


def read_sudokus_from_csv(filename, read_solutions=False):
    index = 0 if not read_solutions else 1
    with open(filename) as fp:
        reader = csv.reader(fp)
        next(reader)  # Drop the header
        puzzles = [
            adapt_long_sudoku_line_to_array(line[index])
            for line in reader
        ]
        return np.array(puzzles)


def detect_invalid_solutions(filename):
    solutions = read_sudokus_from_csv(filename, read_solutions=True)
    return np.array([solution for solution in solutions if not is_valid(Board(solution))])