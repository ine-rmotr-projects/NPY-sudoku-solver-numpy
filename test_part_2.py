import numpy as np
from sudoku import Board, is_subset_valid, is_valid

VALID_BOARD_ARR = np.array([
    [8, 0, 1, 0, 0, 3, 9, 0, 6],
    [0, 0, 9, 0, 0, 7, 8, 5, 0],
    [2, 5, 0, 1, 0, 0, 4, 7, 0],
    [5, 0, 0, 0, 6, 1, 7, 0, 4],
    [7, 6, 0, 8, 3, 0, 0, 0, 0],
    [0, 3, 2, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 1, 9, 5, 0, 0],
    [0, 0, 5, 0, 0, 0, 3, 0, 2],
    [0, 0, 0, 4, 5, 2, 1, 9, 7]])


INVALID_BOARD_ARR = np.array([
    [8, 0, 1, 0, 3, 3, 9, 0, 6],   # There's a 3 in (0, 4)
    [0, 0, 9, 0, 0, 7, 8, 5, 0],
    [2, 5, 0, 1, 0, 0, 4, 7, 0],
    [5, 0, 0, 0, 6, 1, 7, 0, 4],
    [7, 6, 0, 8, 3, 0, 0, 0, 0],
    [0, 3, 2, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 1, 9, 5, 0, 0],
    [0, 0, 5, 0, 0, 0, 3, 0, 2],
    [0, 0, 0, 4, 5, 2, 1, 9, 7]])


# Invalid subsets:
def test_subset_invalid_row():
    board = Board(INVALID_BOARD_ARR)
    assert is_subset_valid(board.get_row(0)) is False

    
def test_subset_invalid_column():
    board = Board(INVALID_BOARD_ARR)
    assert is_subset_valid(board.get_column(4)) is False

    
def test_subset_invalid_block():
    board = Board(INVALID_BOARD_ARR)
    assert is_subset_valid(board.get_block(0, 1)) is False

# Valid subsets:
def test_subset_valid_row():
    board = Board(VALID_BOARD_ARR)
    assert is_subset_valid(board.get_row(0)) is True

    
def test_subset_valid_column():
    board = Board(VALID_BOARD_ARR)
    assert is_subset_valid(board.get_column(4)) is True

    
def test_subset_valid_block():
    board = Board(VALID_BOARD_ARR)
    assert is_subset_valid(board.get_block(0, 1)) is True


# Valid Board:
def test_is_valid():
    board = Board(VALID_BOARD_ARR)
    assert is_valid(board) is True

    
# Invalid Board:
def test_is_invalid():
    board = Board(INVALID_BOARD_ARR)
    assert is_valid(board) is False