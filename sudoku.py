import numpy as np
import collections
import itertools

# Part 1:
def string_puzzle_to_arr(puzzle):
    return np.array([list(line.strip()) for line in puzzle.split('\n') if line.strip()], dtype=np.int)


class Board:
    def __init__(self, puzzle):
        self.arr = string_puzzle_to_arr(puzzle) if isinstance(puzzle, str) else puzzle

    def get_row(self, row_index):
        return self.arr[row_index]

    def get_column(self, col_index):
        return self.arr.T[col_index]

    def get_block(self, pos_1, pos_2):
        row = pos_1 * 3
        col = pos_2 * 3
        return self.arr[row: row + 3, col: col + 3]

    def iter_rows(self):
        return self.arr

    def iter_columns(self):
        return self.arr.T

    def iter_blocks(self):
        blocks = []
        for row in range(3):
            for col in range(3):
                blocks.append(self.get_block(row, col))
        return blocks


# Part 2:
def is_subset_valid(arr):
    valids = set()
    for v in arr.flatten():
        if v == 0:
            continue
        if v in valids:
            return False
        valids.add(v)
    return True

def is_valid(board):
    for block in board.iter_blocks():
        if not is_subset_valid(block):
            return False
    return True

# Part 3:
def find_empty(board):
    empties = []
    rows, cols = board.arr.shape
    for row in range(rows):
        for col in range(cols):
            val = board.arr[row][col]
            if val == 0:
                empties.append([row, col])
    return np.array(empties) if empties else None

def is_full(board):
    return bool(np.all(board.arr))

from math import ceil

def find_possibilities(board, x, y):
    res = []
    block_row = 0 if x < 3 else 1 if x < 6 else 2
    block_col = 0 if y < 3 else 1 if y < 6 else 2
    block = board.get_block(block_row, block_col)
    print(block)
    row = board.get_row(x)
    col = board.get_column(y)
    for num in range(1, 10):
        if num in block or num in row or num in col:
            continue
        res.append(num)
    return res

# Part 4:
def adapt_long_sudoku_line_to_array(line):
    line = np.array(list(line.strip()), dtype=np.int)
    return np.split(line, 9)

def read_sudokus_from_csv(filename, read_solutions=False):
    with open(filename) as fp:
        next(fp)
        data = list(fp)
    sudos = []
    col = 1 if read_solutions else 0
    for line in data:
        line = line.split(',')
        line = line[col]
        sudos.append(adapt_long_sudoku_line_to_array(line))
    return np.array(sudos)

def detect_invalid_solutions(filename):
    solutions = read_sudokus_from_csv(filename, read_solutions=True)
    invalid = []
    for solution in solutions:
        board = Board(solution)
        if not is_valid(board):
            invalid.append(solution)
    return np.array(invalid)