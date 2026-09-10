import sys
import json
from client import CounterfactualRegretMinimization

cfr = CounterfactualRegretMinimization(["check", "bet"])

def handle_call(name, arguments):
    if name == "get_strategy":
        return {"strategy": cfr.get_strategy()}
    elif name == "update":
        utils = arguments["action_utilities"]
        eu = arguments["expected_utility"]
        cfr.update_regrets(utils, eu)
        return {"regrets": cfr.cumulative_regrets}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_call(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
