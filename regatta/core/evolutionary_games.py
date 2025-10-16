import numpy as np

def replicator_dynamics(payoff_matrix, x, dt=0.01, steps=1000):
    """
    Simulate discrete-time replicator dynamics for a symmetric game.

    payoff_matrix : np.ndarray
        Payoff matrix (n x n)
    x : np.ndarray
        Initial strategy distribution (sum = 1)
    dt : float
        Step size
    steps : int
        Number of iterations
    """
    x = np.asarray(x, dtype=float)
    x /= np.sum(x)
    for _ in range(steps):
        fitness = payoff_matrix @ x
        avg_fitness = x @ fitness
        x = x * (fitness / avg_fitness)
        x /= np.sum(x)
    return x
