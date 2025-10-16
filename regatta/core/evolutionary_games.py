import numpy as np

def replicator_dynamics(payoff_matrix, x, dt=0.01, steps=1000):
    for _ in range(steps):
        fitness = payoff_matrix @ x
        avg_fitness = x @ fitness
        x = x * (1 + dt * (fitness - avg_fitness))
        x /= np.sum(x)
    return x
