import pelger
import numpy as np

INPUTS = [
    (
        [1],
        [[-1, -1],
         [ 1, -1]],
        [[0, 0],
         [0, 0]],
        1,
        False
    ),
    (
        [1, 2, 3, 2],
        [[-1, -1, -1, -1, -1],
         [ 1, -1, -1, -1, -1],
         [ 2,  2, -1,  4, -1],
         [-1, -1,  3, -1, -1]],
        [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0]],
        3,
        True
    ),
    (
        [1, 2, 3, 2],
        [[-1, -1, -1, -1, -1, -1, -1],
         [ 1, -1, -1, -1, -1, -1, -1],
         [ 4,  2, -1, -1, -1,  6, -1],
         [-1, -1,  3, -1,  5, -1, -1]],
        [[0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0]],
        3,
        False
    ),
    (
        [1, 2, 3, 2, 1, 2, 3],
        [[-1, -1, -1, -1, -1, -1, -1],
         [ 1, -1,  5, -1, -1, -1, -1],
         [ 2,  2, -1,  4, -1,  6, -1],
         [ 1, -1,  3, -1, -1, -1, -1]],
        [[0, 0, 0, 0, 0, 0, 0],
         [1, 0, 1, 0, 0, 0, 0],
         [1, 2, 0, 0, 0, 0, 0],
         [0, 0, 2, 0, 0, 0, 0]],
        3,
        True
    )
]


def test_compile():
    for ts, fsm_test, amount_test, w, compress in INPUTS:
        fsm_test = np.array(fsm_test)
        amount_test = np.array(amount_test)
        fsm, amount = pelger.compile(ts, w=w, compress=compress)
        
        assert np.array_equal(fsm, fsm_test)
        assert np.array_equal(amount, amount_test)
