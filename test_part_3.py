import numpy as np
from sudoku import Board, find_empty, is_full, find_possibilities

EMPTY_BOARD_ARR = np.array([
    [8, 0, 1, 0, 0, 3, 9, 0, 6],
    [0, 0, 9, 0, 0, 7, 8, 5, 0],
    [2, 5, 0, 1, 0, 0, 4, 7, 0],
    [5, 0, 0, 0, 6, 1, 7, 0, 4],
    [7, 6, 0, 8, 3, 0, 0, 0, 0],
    [0, 3, 2, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 1, 9, 5, 0, 0],
    [0, 0, 5, 0, 0, 0, 3, 0, 2],
    [0, 0, 0, 4, 5, 2, 1, 9, 7]])

SOLVED_BOARD_ARR = np.array([
    [8, 7, 1, 5, 4, 3, 9, 2, 6],
    [3, 4, 9, 6, 2, 7, 8, 5, 1],
    [2, 5, 6, 1, 9, 8, 4, 7, 3],
    [5, 9, 8, 2, 6, 1, 7, 3, 4],
    [7, 6, 4, 8, 3, 5, 2, 1, 9],
    [1, 3, 2, 9, 7, 4, 6, 8, 5],
    [4, 2, 7, 3, 1, 9, 5, 6, 8],
    [9, 1, 5, 7, 8, 6, 3, 4, 2],
    [6, 8, 3, 4, 5, 2, 1, 9, 7]])


def test_find_empty():
    expected = np.array([
        [0, 1], [0, 3], [0, 4], [0, 7], [1, 0],
        [1, 1], [1, 3], [1, 4], [1, 8], [2, 2],
        [2, 4], [2, 5], [2, 8], [3, 1], [3, 2],
        [3, 3], [3, 7], [4, 2], [4, 5], [4, 6],
        [4, 7], [4, 8], [5, 0], [5, 3], [5, 4],
        [5, 5], [5, 6], [5, 7], [5, 8], [6, 0],
        [6, 2], [6, 3], [6, 7], [6, 8], [7, 0],
        [7, 1], [7, 3], [7, 4], [7, 5], [7, 7],
        [8, 0], [8, 1], [8, 2]])
    board = Board(EMPTY_BOARD_ARR)
    assert np.array_equal(find_empty(board), expected)

    
def test_is_full():
    assert is_full(Board(EMPTY_BOARD_ARR)) is False, is_full(Board(EMPTY_BOARD_ARR))
    assert is_full(Board(SOLVED_BOARD_ARR)) is True
    

def test_find_possibilities():
    board = Board(EMPTY_BOARD_ARR)

    assert set(find_possibilities(board, 0, 1)) == set([4, 7])
    assert set(find_possibilities(board, 1, 0)) == set([3, 4, 6])
    assert set(find_possibilities(board, 1, 1)) == set([4])