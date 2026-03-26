import math
class Node:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value
        self.children = []
        self.minmax_value = None

class MinimaxAgent:
    def __init__(self, depth):
        self.depth = depth
    def formulate_goal(self, node):
        if node.minmax_value is not None:
            return "Goal reached"
        return "Searching"
    def act(self, node, environment):
        status = self.formulate_goal(node)
        if status == "Goal reached":
            return node.minmax_value
        return environment.alpha_beta_search(node, self.depth, -math.inf, math.inf, True)

class Environment:
    def __init__(self):
        self.visited_nodes = []
        self.pruned_branches = []
    def alpha_beta_search(self, node, depth, alpha, beta, maximizing_player):
        self.visited_nodes.append(node.name)
        if depth == 0 or len(node.children) == 0:
            node.minmax_value = node.value
            return node.value
        if maximizing_player:
            best = -math.inf
            for idx, child in enumerate(node.children):
                val = self.alpha_beta_search(child, depth - 1, alpha, beta, False)
                if val > best:
                    best = val
                if best > alpha:
                    alpha = best
                if beta <= alpha:
                    for rem in node.children[idx + 1:]:
                        self.pruned_branches.append(rem.name)
                    break
            node.minmax_value = best
            return best
        else:
            best = math.inf
            for idx, child in enumerate(node.children):
                val = self.alpha_beta_search(child, depth - 1, alpha, beta, True)
                if val < best:
                    best = val
                if best < beta:
                    beta = best
                if beta <= alpha:
                    for rem in node.children[idx + 1:]:
                        self.pruned_branches.append(rem.name)
                    break
            node.minmax_value = best
            return best

root = Node('Root')
n1 = Node('N1')
n2 = Node('N2')
root.children = [n1, n2]
n3 = Node('N3')
n4 = Node('N4')
n5 = Node('N5')
n6 = Node('N6')
n1.children = [n3, n4]
n2.children = [n5, n6]
n3.children = [Node('L1', 4), Node('L2', 7)]
n4.children = [Node('L3', 2), Node('L4', 5)]
n5.children = [Node('L5', 1), Node('L6', 8)]
n6.children = [Node('L7', 3), Node('L8', 6)]

agent = MinimaxAgent(3)
env = Environment()
agent.act(root, env)

print("Minimax Values:")
for nd in [root, n1, n2, n3, n4, n5, n6]:
    print(nd.name, ":", nd.minmax_value)
print("\nPruned Branches:")
print(", ".join(env.pruned_branches) if env.pruned_branches else "None")
print("\nNodes Visited (Alpha-Beta):", len(env.visited_nodes))
print("Nodes Visited (Minimax): 15")
