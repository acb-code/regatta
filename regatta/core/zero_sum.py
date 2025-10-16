import numpy as np

def solve_minimax(A):
    from scipy.optimize import linprog
    m, n = A.shape
    c = np.zeros(m + 1)
    c[-1] = -1
    A_ub = np.hstack([-A.T, np.ones((n, 1))])
    b_ub = np.zeros(n)
    A_eq = np.hstack([np.ones((1, m)), np.zeros((1, 1))])
    b_eq = np.array([1])
    bounds = [(0, None)] * m + [(None, None)]
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds)
    return res.x[:-1], res.x[-1]
