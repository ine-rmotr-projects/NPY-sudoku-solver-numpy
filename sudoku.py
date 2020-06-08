import numpy as np
import collections
import itertools

# Part 1:
def string_puzzle_to_arr(puzzle):
    return np.array([list(line.strip()) for line in puzzle.split('\n') if line.strip()], dtype=np.int)

class Board:
    def __init__(self, puzzle): 
        if type(puzzle) == str:
            puzzle = np.array([list(line.strip()) for line in puzzle.split('\n') if line.strip()], dtype=np.int)
        self.arr = puzzle

    def get_row(self, row_index):
        return self.arr[row_index, :]

    def get_column(self, col_index):
        return self.arr[:, col_index]
    
    def get_block(self, pos_1, pos_2):
        pos_1 = pos_1*3
        pos_2 = pos_2*3
        return self.arr[pos_1:pos_1+3, pos_2:pos_2+3]
    
    def iter_rows(self):
        lst = []
        for row in self.arr:
            lst.append(np.array(row))
        return np.array(lst)
    
    def iter_columns(self):
        lst = []
        for col in self.arr.T:
            lst.append(np.array(col))
        return np.array(lst)
    
    def iter_blocks(self):
        lst = []
        for i in np.arange(0,9,3):
            for j in np.arange(0,9,3):
                lst.append(np.array(self.arr[i:i+3,j:j+3]))
        return np.array(lst)
    
    

# Part 2:
def is_subset_valid(arr):
    arr_new = arr[arr > 0]
    if arr_new.size == 0:
        return True
    for i in range(0,arr_new.size):
        for j in range(i+1,arr_new.size):
            if arr_new[i] == arr_new[j]:
                return False
    return True


def is_valid(board):
    for i in range(0,9):
        row = board.get_row(i)
        col = board.get_column(i)
        if ((is_subset_valid(row) == False) | (is_subset_valid(col) == False)):
            return False
    for i in range(0,3):
        for j in range(0,3):
            block = board.get_block(i,j)
            if is_subset_valid(block) == False:
                return False
    return True


# Part 3:
def find_empty(board):
    arr = board.arr
    if((arr == 0).all()):
        return None
    lst = []
    for i in range(0,9):
        for j in range(0,9):
            if arr[i, j] == 0:
                lst.append(np.array([i,j]))
    return np.array(lst)

def is_full(board):
    arr = board.arr
    if (arr == 0).any():
        return False
    else:
        return True

def block_pos(cellno):
    if cellno <3:
        return 0
    elif 3<=cellno<6:
        return 1
    else:
        return 2
    
def find_possibilities(board, x, y):
    row = board.get_row(x)
    row_vals = row[row>0]
   
    col = board.get_column(y)
    col_vals = col[col>0]
    
    pos_1 = block_pos(x)
    pos_2 = block_pos(y)
    block = board.get_block(pos_1,pos_2)
    clean_block = block[block>0]
    
    possible_nos = [i for i in range(1,10) if (i not in row_vals) & (i not in col_vals) & (i not in clean_block)] 
    return np.array(possible_nos)



# Part 4:
def adapt_long_sudoku_line_to_array(line):
    lst = [x for x in line]
    return np.array(lst, dtype=int).reshape(9,9)

def read_sudokus_from_csv(filename, read_solutions=False):
    data = np.genfromtxt(filename, delimiter=',', skip_header=1, dtype=str)
    if read_solutions == True:
        new_data = data[:,1]
    else:
        new_data = data[:,0]
    lst = [adapt_long_sudoku_line_to_array(line) for line in new_data]
    return lst

def detect_invalid_solutions(filename):
    solution = read_sudokus_from_csv(filename, read_solutions=True)
    lst=[]
    lst = [sol for sol in solution if is_valid(Board(sol)) == False]
    return lst