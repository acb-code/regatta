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
        """
        Compute a pure best response for the specified player given the
        (possibly factorised) strategies of the other players.

        Parameters
        ----------
        opponent_strategy : array-like, sequence, or dict
            Strategy profile for the other players. For two-player games this
            can be a 1-D array. For games with >2 players, provide either a
            list/tuple aligned with the other players' indices, or a dict
            keyed by player index.
        player : int
            Index of the player whose best response is requested.
        """
        if self.num_players == 1:
            return int(np.argmax(self.payoffs[player]))

        other_players = [i for i in range(self.num_players) if i != player]
        if isinstance(opponent_strategy, dict):
            strategies = [
                np.asarray(opponent_strategy[i], dtype=float) for i in other_players
            ]
        elif isinstance(opponent_strategy, (list, tuple)):
            strategies = [np.asarray(s, dtype=float) for s in opponent_strategy]
        else:  # single opponent (two-player game)
            strategies = [np.asarray(opponent_strategy, dtype=float)]

        if len(strategies) != len(other_players):
            raise ValueError(
                "Mismatch between opponent strategies and number of opposing players."
            )

        expected_payoffs = np.zeros(self.num_actions[player], dtype=float)
        other_action_ranges = [range(self.num_actions[i]) for i in other_players]

        for own_action in range(self.num_actions[player]):
            total_payoff = 0.0
            for other_actions in product(*other_action_ranges):
                profile = [0] * self.num_players
                profile[player] = own_action
                prob = 1.0
                for idx, other_player in enumerate(other_players):
                    action = other_actions[idx]
                    profile[other_player] = action
                    prob *= strategies[idx][action]
                total_payoff += self.payoffs[player][tuple(profile)] * prob
            expected_payoffs[own_action] = total_payoff

        return int(np.argmax(expected_payoffs))

    def enumerate_pure_equilibria(self):
        eqs = []
        for actions in product(*[range(n) for n in self.num_actions]):
            if all(
                self.payoffs[p][actions]
                >= self.payoffs[p][tuple(actions[:p] + (a,) + actions[p + 1 :])]
                for p in range(self.num_players)
                for a in range(self.num_actions[p])
            ):
                eqs.append(actions)
        return eqs
