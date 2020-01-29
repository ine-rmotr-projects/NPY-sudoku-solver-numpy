import numpy as np
import collections
import itertools

# Part 1:
def string_puzzle_to_arr(puzzle):
    return np.array([list(line.strip()) for line in puzzle.split('\n') if line.strip()], dtype=np.int)

class Board:
    def __init__(self, puzzle):
        if type(puzzle) == str:
            self.arr = string_puzzle_to_arr(puzzle)
        else:
            self.arr = puzzle
        
        self.blocks = self.turn_to_blocks()
        
    def get_row(self, row_index):
        return self.arr[row_index]

    def turn_to_blocks(self):
        rows = self.arr.strides[0]
        cols = self.arr.strides[1]
        blocks = np.lib.stride_tricks.as_strided(self.arr, shape=(3, 3, 3, 3), strides=(rows*3, cols*3, rows, cols))
        return blocks
    
    def get_column(self, col_index):
        return self.arr[:,col_index]
    
    def get_block(self, pos_1, pos_2):
        return self.blocks[pos_1][pos_2]
    
    def iter_rows(self):
        rows = np.empty([9, 9],dtype=int)
        for idx,row in enumerate(self.arr):
            rows[idx] = row
        return rows
    
    def iter_columns(self):
        cols = np.empty([9, 9],dtype=int)
        for idx,col in enumerate(self.arr.T):
            cols[idx] = col
        return cols
    
    def iter_blocks(self):
        arr_list = []
        for idx,sub_block in enumerate(self.blocks):
            for idx2,block in enumerate(sub_block):
                arr_list.append(block)
                
        return np.array(arr_list)
                


# Part 2:
def is_subset_valid(arr):
    unique,counts = np.unique(arr, return_counts=True)
    if 0 in unique:
        values = np.asarray((unique, counts)).T[1:,:]
        for num in values[:,1]:
            if num != 1:  # If number is repeated
                return False
        return True
    else:
        values = np.asarray((unique, counts)).T
        for num in values[:,1]:
            if num != 1:
                return False
        return True

def is_valid(board):
    check_rows = [True if is_subset_valid(row) == True else False for row in board.iter_rows()]
    check_cols = [True if is_subset_valid(col) == True else False for col in board.iter_columns()]
    check_blocks = [True if is_subset_valid(block) == True else False for block in board.iter_blocks()]
    if False in check_rows or False in check_cols or False in check_blocks:
        return False
    else:
        return True


# Part 3:
def find_empty(board):
    return np.argwhere(board.iter_rows() == 0)

def is_full(board):
    rows = board.iter_rows()
    all_zeros = np.count_nonzero(rows == 0)
    if all_zeros == 0:
        return True
    else:
        return False

def find_possibilities(board, x, y):
    numbers = np.array([0,1,2,3,4,5,6,7,8,9])
    row_vals = np.unique(board.iter_rows()[x])
    col_vals = np.unique(board.iter_columns()[y])
    block_vals = np.unique(board.get_block(int(x/3),int(y/3)))
    used_numbers = np.concatenate((row_vals, col_vals[~np.isin(col_vals,row_vals)],block_vals[~np.isin(block_vals,col_vals,row_vals)],), axis=0)
    return np.setdiff1d(numbers, used_numbers)


# Part 4:
def adapt_long_sudoku_line_to_array(line):
    return np.array(list(line),dtype=int).reshape((9,9))

def read_sudokus_from_csv(filename, read_solutions=False):
    list_numbers = []
    with open(filename,"r") as file:
        next(file)
        for line in file.readlines():
            empty,solution = line.replace("\n","").split(",")
            if read_solutions:
                list_numbers.append(adapt_long_sudoku_line_to_array(solution))
            else:
                list_numbers.append(adapt_long_sudoku_line_to_array(empty))
            
    return np.array(list_numbers)

def detect_invalid_solutions(filename):
    from sudoku import Board,is_valid
    puzzles = read_sudokus_from_csv(filename,read_solutions = True)
    list_invalids = []
    for puzzle in puzzles:
        puzzle_obj = Board(puzzle)
        if not is_valid(puzzle_obj):
            list_invalids.append(puzzle)
    return np.array(list_invalids)