import numpy as np


def regret_matching(payoff_matrix, iterations=1000):
    n = payoff_matrix.shape[0]
    regrets = np.zeros(n)
    strategy_sum = np.zeros(n)
    for _ in range(iterations):
        pos_regrets = np.maximum(regrets, 0)
        if np.sum(pos_regrets) > 0:
            strategy = pos_regrets / np.sum(pos_regrets)
        else:
            strategy = np.ones(n) / n
        strategy_sum += strategy
        payoff_per_action = payoff_matrix @ strategy
        avg_payoff = strategy @ payoff_per_action
        regrets += payoff_per_action - avg_payoff

    total = np.sum(strategy_sum)
    if np.isclose(total, 0.0):
        return np.ones(n) / n
    return strategy_sum / total
