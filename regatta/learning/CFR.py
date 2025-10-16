# Simple Counterfactual Regret Minimization (CFR) placeholder

class CFR:
    def __init__(self):
        self.regret_sum = {}
        self.strategy_sum = {}

    def get_strategy(self, info_set):
        regrets = self.regret_sum.get(info_set, [0, 0])
        pos_regrets = [max(r, 0) for r in regrets]
        normalizing_sum = sum(pos_regrets)
        if normalizing_sum > 0:
            strategy = [r / normalizing_sum for r in pos_regrets]
        else:
            strategy = [0.5, 0.5]
        return strategy

    def update_regret(self, info_set, action, regret):
        if info_set not in self.regret_sum:
            self.regret_sum[info_set] = [0, 0]
        self.regret_sum[info_set][action] += regret
