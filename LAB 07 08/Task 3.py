import math
class Node:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value
        self.children = []
        self.minmax_value = None

class MinimaxAgent:
    def act(self, node, environment):
        return environment.alpha_beta_search(node, 3, -math.inf, math.inf, True)

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
            for index, child in enumerate(node.children):
                result = self.alpha_beta_search(child, depth - 1, alpha, beta, False)
                if result > best:
                    best = result
                if best > alpha:
                    alpha = best
                if beta <= alpha:
                    for remaining in node.children[index + 1:]:
                        self.pruned_branches.append(remaining.name)
                    break
            node.minmax_value = best
            return best
        else:
            best = math.inf
            for index, child in enumerate(node.children):
                result = self.alpha_beta_search(child, depth - 1, alpha, beta, True)
                if result < best:
                    best = result
                if best < beta:
                    beta = best
                if beta <= alpha:
                    for remaining in node.children[index + 1:]:
                        self.pruned_branches.append(remaining.name)
                    break
            node.minmax_value = best
            return best

    def find_optimal_path(self, node):
        path = [node.name]
        current = node

        while current.children:
            next_node = None
            for child in current.children:
                if child.minmax_value == current.minmax_value:
                    next_node = child
                    break

            if next_node is None:
                break

            path.append(next_node.name)
            current = next_node

        return " -> ".join(path)


root = Node('Root')
n1 = Node('N1')
n2 = Node('N2')
n3 = Node('N3')
root.children = [n1, n2, n3]
n4 = Node('N4')
n5 = Node('N5')
n1.children = [n4, n5]
n4.children = [Node('L1', 3), Node('L2', 5)]
n5.children = [Node('L3', 2), Node('L4', 9)]
n6 = Node('N6')
n7 = Node('N7')
n2.children = [n6, n7]
n6.children = [Node('L5', 1), Node('L6', 4)]
n7.children = [Node('L7', 8), Node('L8', 2)]

n8 = Node('N8')
n9 = Node('N9')
n3.children = [n8, n9]
n8.children = [Node('L9', 10), Node('L10', 12)]
n9.children = [Node('L11', 1), Node('L12', 0)]
env = Environment()
agent = MinimaxAgent()
agent.act(root, env)
print("Minimax Values:")
print("Root:", root.minmax_value)
for child in root.children:
    print(child.name + ":", child.minmax_value)
print("\nPruned:")
print(", ".join(env.pruned_branches) if env.pruned_branches else "None")
print("\nOptimal Path:")
print(env.find_optimal_path(root))
