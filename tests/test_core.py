"""
Basic sanity tests for regatta core modules.
Run with: pytest -q
"""

import numpy as np
import pytest
from regatta.core.normal_form_games import NormalFormGame
from regatta.core.zero_sum import solve_minimax
from regatta.core.evolutionary_games import replicator_dynamics


def test_normal_form_game_pure_equilibria():
    # Prisoner's Dilemma payoff matrices
    A = np.array([[3, 0],
                  [5, 1]])  # Player 1
    B = np.array([[3, 5],
                  [0, 1]])  # Player 2

    game = NormalFormGame([A, B])
    eqs = game.enumerate_pure_equilibria()

    # (1,1) is mutual defection, the only equilibrium
    assert (1, 1) in eqs
    assert len(eqs) == 1


def test_zero_sum_minimax_solution():
    # Rock-paper-scissors payoff matrix for player 1
    A = np.array([[0, -1, 1],
                  [1, 0, -1],
                  [-1, 1, 0]])
    p_star, value = solve_minimax(A)
    # Strategy should be approximately uniform
    assert np.allclose(p_star, np.ones(3) / 3, atol=1e-2)
    # Game value should be close to 0
    assert abs(value) < 1e-2


def test_replicator_dynamics_convergence():
    A = np.array([[2, 0],
                  [0, 1]])  # Coordination game
    x0 = np.array([0.5, 0.5])
    x_final = replicator_dynamics(A, x0, steps=5000)
    # Should converge to one of the pure strategies
    assert np.isclose(np.sum(x_final), 1.0)
    assert any(x_final[i] > 0.9 for i in range(2))


if __name__ == "__main__":
    pytest.main([__file__])
