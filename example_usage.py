from client import CounterfactualRegretMinimization

def main():
    print("=== Testing Counterfactual Regret Minimization (CFR) ===")
    cfr = CounterfactualRegretMinimization(actions=["fold", "call"])

    s0 = cfr.get_strategy()
    print("Initial balanced strategy:", s0)
    assert s0["fold"] == 0.5 and s0["call"] == 0.5

    # Simulate round where 'call' gives high counterfactual utility
    cfr.update_regrets({"fold": -1.0, "call": 3.0}, expected_utility=1.0)
    s1 = cfr.get_strategy()
    print("Updated regret-matched strategy:", s1)
    assert s1["call"] > s1["fold"]
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
