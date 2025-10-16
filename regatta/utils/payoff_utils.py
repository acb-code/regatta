import numpy as np

def normalize_payoffs(payoffs):
    return (payoffs - np.min(payoffs)) / (np.max(payoffs) - np.min(payoffs))
