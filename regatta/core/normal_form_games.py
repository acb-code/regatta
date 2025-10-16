"""
Normal-form game representations and Nash equilibrium solvers.
"""

import numpy as np
from itertools import product

class NormalFormGame:
    def __init__(self, payoffs):
        self.payoffs = payoffs
        self.num_players = len(payoffs)
        self.num_actions = [p.shape[i] for i, p in enumerate(payoffs)]

    def best_response(self, opponent_strategy, player=0):
        payoff_matrix = self.payoffs[player]
        expected = payoff_matrix @ opponent_strategy
        return np.argmax(expected)

    def enumerate_pure_equilibria(self):
        eqs = []
        for actions in product(*[range(n) for n in self.num_actions]):
            if all(
                self.payoffs[p][actions] >= 
                self.payoffs[p][tuple(actions[:p] + (a,) + actions[p+1:])]
                for p in range(self.num_players)
                for a in range(self.num_actions[p])
            ):
                eqs.append(actions)
        return eqs
