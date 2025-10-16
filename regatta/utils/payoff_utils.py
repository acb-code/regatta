import numpy as np


def normalize_payoffs(payoffs):
    payoffs = np.asarray(payoffs, dtype=float)
    min_payoff = np.min(payoffs)
    max_payoff = np.max(payoffs)
    span = max_payoff - min_payoff
    if np.isclose(span, 0.0):
        return np.zeros_like(payoffs, dtype=float)
    return (payoffs - min_payoff) / span
