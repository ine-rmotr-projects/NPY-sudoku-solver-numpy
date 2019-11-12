import numpy as np
from sudoku import string_puzzle_to_arr, Board

EMPTY_BOARD_STR = """
801003906
009007850
250100470
500061704
760830000
032000000
020019500
005000302
000452197"""

EMPTY_BOARD_ARR = np.array([[8, 0, 1, 0, 0, 3, 9, 0, 6],
       [0, 0, 9, 0, 0, 7, 8, 5, 0],
       [2, 5, 0, 1, 0, 0, 4, 7, 0],
       [5, 0, 0, 0, 6, 1, 7, 0, 4],
       [7, 6, 0, 8, 3, 0, 0, 0, 0],
       [0, 3, 2, 0, 0, 0, 0, 0, 0],
       [0, 2, 0, 0, 1, 9, 5, 0, 0],
       [0, 0, 5, 0, 0, 0, 3, 0, 2],
       [0, 0, 0, 4, 5, 2, 1, 9, 7]])


def test_board_creation_string():
    expected = np.array([[8, 0, 1, 0, 0, 3, 9, 0, 6],
       [0, 0, 9, 0, 0, 7, 8, 5, 0],
       [2, 5, 0, 1, 0, 0, 4, 7, 0],
       [5, 0, 0, 0, 6, 1, 7, 0, 4],
       [7, 6, 0, 8, 3, 0, 0, 0, 0],
       [0, 3, 2, 0, 0, 0, 0, 0, 0],
       [0, 2, 0, 0, 1, 9, 5, 0, 0],
       [0, 0, 5, 0, 0, 0, 3, 0, 2],
       [0, 0, 0, 4, 5, 2, 1, 9, 7]])
    board = Board(EMPTY_BOARD_STR)
    assert np.array_equal(board.arr, expected)
    

def test_board_creation_array():    
    expected = np.array([[8, 0, 1, 0, 0, 3, 9, 0, 6],
       [0, 0, 9, 0, 0, 7, 8, 5, 0],
       [2, 5, 0, 1, 0, 0, 4, 7, 0],
       [5, 0, 0, 0, 6, 1, 7, 0, 4],
       [7, 6, 0, 8, 3, 0, 0, 0, 0],
       [0, 3, 2, 0, 0, 0, 0, 0, 0],
       [0, 2, 0, 0, 1, 9, 5, 0, 0],
       [0, 0, 5, 0, 0, 0, 3, 0, 2],
       [0, 0, 0, 4, 5, 2, 1, 9, 7]])

    board = Board(EMPTY_BOARD_ARR)
    
    assert np.array_equal(board.arr, expected)
    
def test_board_get_rows():
    board = Board(EMPTY_BOARD_ARR)
    assert np.array_equal(board.get_row(2), np.array([2, 5, 0, 1, 0, 0, 4, 7, 0]))
    assert np.array_equal(board.get_row(8), np.array([0, 0, 0, 4, 5, 2, 1, 9, 7]))
    
def test_board_get_cols():
    board = Board(EMPTY_BOARD_ARR)
    assert np.array_equal(board.get_column(4), np.array([0, 0, 0, 6, 3, 0, 1, 0, 5]))
    
def test_board_get_blocks():
    board = Board(EMPTY_BOARD_ARR)
    assert np.array_equal(board.get_block(1, 2), np.array([[7, 0, 4],
                                                         [0, 0, 0],
                                                         [0, 0, 0]]))

def test_board_iter_rows():
    board = Board(EMPTY_BOARD_ARR)
    expected = [
        np.array([8, 0, 1, 0, 0, 3, 9, 0, 6]),
        np.array([0, 0, 9, 0, 0, 7, 8, 5, 0]),
        np.array([2, 5, 0, 1, 0, 0, 4, 7, 0]),
        np.array([5, 0, 0, 0, 6, 1, 7, 0, 4]),
        np.array([7, 6, 0, 8, 3, 0, 0, 0, 0]),
        np.array([0, 3, 2, 0, 0, 0, 0, 0, 0]),
        np.array([0, 2, 0, 0, 1, 9, 5, 0, 0]),
        np.array([0, 0, 5, 0, 0, 0, 3, 0, 2]),
        np.array([0, 0, 0, 4, 5, 2, 1, 9, 7])
    ]
    assert np.array_equal(board.iter_rows(), expected)


def test_board_iter_cols():
    expected = [
        np.array([8, 0, 2, 5, 7, 0, 0, 0, 0]),
        np.array([0, 0, 5, 0, 6, 3, 2, 0, 0]),
        np.array([1, 9, 0, 0, 0, 2, 0, 5, 0]),
        np.array([0, 0, 1, 0, 8, 0, 0, 0, 4]),
        np.array([0, 0, 0, 6, 3, 0, 1, 0, 5]),
        np.array([3, 7, 0, 1, 0, 0, 9, 0, 2]),
        np.array([9, 8, 4, 7, 0, 0, 5, 3, 1]),
        np.array([0, 5, 7, 0, 0, 0, 0, 0, 9]),
        np.array([6, 0, 0, 4, 0, 0, 0, 2, 7])
    ]
    board = Board(EMPTY_BOARD_ARR)
    
    assert np.array_equal(board.iter_columns(), expected)

    
def test_board_iter_blocks():
    expected = [
        np.array(
         [[8, 0, 1],
         [0, 0, 9],
         [2, 5, 0]]),
        np.array(
        [[0, 0, 3],
        [0, 0, 7],
        [1, 0, 0]]),
        np.array(
         [[9, 0, 6],
         [8, 5, 0],
         [4, 7, 0]]),
        np.array(
         [[5, 0, 0],
         [7, 6, 0],
         [0, 3, 2]]),
        np.array(
         [[0, 6, 1],
         [8, 3, 0],
         [0, 0, 0]]),
        np.array(
         [[7, 0, 4],
         [0, 0, 0],
         [0, 0, 0]]),
        np.array(
         [[0, 2, 0],
         [0, 0, 5],
         [0, 0, 0]]),
        np.array(
         [[0, 1, 9],
         [0, 0, 0],
         [4, 5, 2]]),
        np.array(
         [[5, 0, 0],
         [3, 0, 2],
         [1, 9, 7]]),
    ]
    board = Board(EMPTY_BOARD_ARR)
    
    assert np.array_equal(board.iter_blocks(), expected)
