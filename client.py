class CounterfactualRegretMinimization:
    """
    Counterfactual Regret Minimization (CFR) for 2-Action Normal/Extensive Form.
    Regret Matching strategy derivation.
    """
    def __init__(self, actions=("fold", "call")):
        self.actions = actions
        self.cumulative_regrets = {a: 0.0 for a in actions}
        self.strategy_sum = {a: 0.0 for a in actions}

    def get_strategy(self):
        pos_regrets = {a: max(0.0, r) for a, r in self.cumulative_regrets.items()}
        total = sum(pos_regrets.values())
        if total > 0:
            strat = {a: r / total for a, r in pos_regrets.items()}
        else:
            uniform = 1.0 / len(self.actions)
            strat = {a: uniform for a in self.actions}
        for a in self.actions:
            self.strategy_sum[a] += strat[a]
        return strat

    def update_regrets(self, action_utilities, expected_utility):
        for a in self.actions:
            self.cumulative_regrets[a] += (action_utilities[a] - expected_utility)
