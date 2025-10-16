"""
Basic sanity tests for regatta core modules.
Run with: pytest -q
"""

import numpy as np
import pytest
from regatta.core.normal_form_games import NormalFormGame
from regatta.core.zero_sum import solve_minimax
from regatta.core.evolutionary_games import replicator_dynamics
from regatta.learning.regret_matching import regret_matching
from regatta.utils.payoff_utils import normalize_payoffs


def test_normal_form_game_pure_equilibria():
    # Prisoner's Dilemma payoff matrices
    A = np.array([[3, 0], [5, 1]])  # Player 1
    B = np.array([[3, 5], [0, 1]])  # Player 2

    game = NormalFormGame([A, B])
    eqs = game.enumerate_pure_equilibria()

    # (1,1) is mutual defection, the only equilibrium
    assert (1, 1) in eqs
    assert len(eqs) == 1


def test_zero_sum_minimax_solution():
    # Rock-paper-scissors payoff matrix for player 1
    A = np.array([[0, -1, 1], [1, 0, -1], [-1, 1, 0]])
    p_star, value = solve_minimax(A)
    # Strategy should be approximately uniform
    assert np.allclose(p_star, np.ones(3) / 3, atol=1e-2)
    # Game value should be close to 0
    assert abs(value) < 1e-2


def test_replicator_dynamics_convergence():
    A = np.array([[2, 0], [0, 1]])  # Coordination game
    x0 = np.array([0.5, 0.5])
    x_final = replicator_dynamics(A, x0, steps=5000)
    # Should converge to one of the pure strategies
    assert np.isclose(np.sum(x_final), 1.0)
    assert any(x_final[i] > 0.9 for i in range(2))


def test_best_response_handles_column_player():
    A = np.array([[3, 0], [5, 1]])
    B = np.array([[3, 5], [0, 1]])
    game = NormalFormGame([A, B])
    # Player 1 (column player) should best respond with action 1 (defect) to a uniform opponent
    assert game.best_response(np.array([0.5, 0.5]), player=1) == 1


def test_replicator_dynamics_zero_matrix_stable():
    zero_game = np.zeros((3, 3))
    x0 = np.array([0.2, 0.3, 0.5])
    x_final = replicator_dynamics(zero_game, x0, steps=100)
    assert np.allclose(x_final, x0)


def test_normalize_payoffs_constant_input():
    payoffs = np.full((2, 2), 7.0)
    normalized = normalize_payoffs(payoffs)
    assert np.all(normalized == 0.0)


def test_regret_matching_uniform_convergence():
    rps_payoff = np.array([[0, -1, 1], [1, 0, -1], [-1, 1, 0]])
    strategy = regret_matching(rps_payoff, iterations=5000)
    assert np.allclose(strategy, np.ones(3) / 3, atol=0.05)


if __name__ == "__main__":
    pytest.main([__file__])
