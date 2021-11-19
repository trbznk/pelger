import numpy as np
from numpy.lib.arraysetops import unique
import graphviz
import argparse

from typing import List, Tuple


def empty_state(m) -> np.ndarray:
    state = np.empty((m, 1), dtype=np.int8)
    state[:] = -1
    return state


def empty_amount(m) -> np.ndarray:
    amount = np.zeros((m, 1), dtype=np.uint8)
    return amount


def compile(ts: List[int], w: int = 1, compress: bool = True) -> Tuple[np.ndarray, np.ndarray]:
    assert 0 < w <= len(ts), "'k' must be 0 < k <= len(ts)"
    assert isinstance(w, int), "'k' must be an integer"

    if not isinstance(ts, np.ndarray):
        ts = np.array(ts)
    
    m = ts.max()+1

    fsm = empty_state(m)
    amount = empty_amount(m)    
    
    state = 0
    next_state = 1
    for i in range(len(ts)-w+1):
        window = ts[i:i+w]
        for j in range(len(window)):
            x = window[j]
            x1 = window[j+1] if j != len(window)-1 else None
            if fsm[x][state] < 0:
                compression_found = False
                if x1 is not None and compress:
                    for k in range(len(fsm[x1])):
                        if fsm[x1][k] > -1 and k != state:
                            fsm[x][state] = k
                            state = fsm[x][state]
                            compression_found = True
                            break
                if not compression_found:
                    fsm = np.hstack((fsm, empty_state(m)))
                    amount = np.hstack((amount, empty_amount(m)))
                    fsm[x][state] = next_state
                    state = next_state
                    next_state += 1
            else:
                amount[x][state] += 1
                state = fsm[x][state]
        state = 0

    assert amount.min() >= 0, "min() amount should not be lower than '0'"

    return fsm, amount


def run():
    assert False, "run() not implemented yet"


if __name__ == "__main__":
    ts = [1, 2, 3, 2]
    ts = np.random.randint(0, 5, 100000)

    fsm, amount = compile(ts, w=5, compress=True)
    dot = graphviz.Digraph()

    for state in range(fsm.shape[1]):
        col = fsm[:, state]
        for x in range(len(col)):
            if col[x] > -1:
                label = f"{x}({amount[x][state]})"
                dot.edge(str(state), str(col[x]), label=label)

    dot.view()
