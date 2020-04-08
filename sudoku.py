import numpy as np
import collections
import itertools

# Part 1:
def string_puzzle_to_arr(puzzle):
    return np.array([list(line.strip()) for line in puzzle.split('\n') if line.strip()], dtype=np.int)

class Board:
    def __init__(self, puzzle):
        
        if isinstance(puzzle, str):
            self.arr = np.array([list(line.strip()) for line in puzzle.split('\n') if line.strip()], dtype=np.int)
        elif isinstance(puzzle, np.ndarray):
            self.arr = puzzle

    def get_row(self, row_index):
        return self.arr[row_index]

    def get_column(self, col_index):
        return self.arr[:, col_index]
    
    def get_block(self, pos_1, pos_2):
        row = pos_1 * 3
        col = pos_2 * 3
        return self.arr[row:row + 3, col:col + 3]
    
    def iter_rows(self):
        return [self.get_row(i) for i in range(9)]
    
    def iter_columns(self):
        return [self.get_column(i) for i in range(9)]
    
    def iter_blocks(self):
        return [self.get_block(i, j) for i in range(3) for j in range(3)]

# Part 2:
def is_subset_valid(arr):
    return arr[arr > 0].size == np.unique(arr[arr > 0]).size

def is_valid(board):
    
    for row in board.iter_rows():
        if is_subset_valid(row) is False:
            return False
    
    for col in board.iter_columns():
        if is_subset_valid(col) is False:
            return False
    
    for block in board.iter_blocks():
        if is_subset_valid(block) is False:
            return False
    
    return True


# Part 3:
def find_empty(board):
    return np.argwhere(board.arr == 0)

def is_full(board):
    return find_empty(board).size == 0

def find_possibilities(board, x, y):
    
    row = board.get_row(x)
    col = board.get_column(y)
    block = board.get_block(x // 3, y // 3)
    
    return set(np.arange(1, 10)) - set(row) - set(col) - set(block.flatten())


# Part 4:
def adapt_long_sudoku_line_to_array(line):
    return np.array(list(line), dtype=np.int).reshape(9, 9)

def read_sudokus_from_csv(filename, read_solutions=False):
    
    with open(filename) as f:
        
        next(f)
        
        return np.array([adapt_long_sudoku_line_to_array(row.strip().split(',')[int(read_solutions)]) for row in f])

def detect_invalid_solutions(filename):
    
    boards = read_sudokus_from_csv(filename, read_solutions=True)
        
    return [b for b in boards if is_valid(Board(b)) is False]