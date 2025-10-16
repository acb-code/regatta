import numpy as np

def fictitious_play(payoff_matrix, iterations=1000):
    n = payoff_matrix.shape[0]
    beliefs = np.ones(n) / n
    counts = np.zeros(n)
    for t in range(1, iterations + 1):
        best_response = np.argmax(payoff_matrix @ beliefs)
        counts[best_response] += 1
        beliefs = counts / t
    return beliefs
