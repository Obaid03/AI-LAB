# TASK 3 – Iterative Deepening Search (IDS)
class Goalbasedagent:
    def __init__(self, goal):
        self.goal = goal
    def check_goal(self, current):
        return current == self.goal
    def dls(self, graph, node, depth, path):
        if depth == 0:
            return False
        if node == self.goal:
            path.append(node)
            return True
        for child in graph.get(node, []):
            if self.dls(graph, child, depth - 1, path):
                path.append(node)
                return True
        return False
    def iterative_deepening(self, graph, start, max_depth):
        for depth in range(max_depth + 1):
            print("Depth:", depth)
            path = []
            if self.dls(graph, start, depth, path):
                final_path = list(reversed(path))
                print("Path to Goal:", end=" ")
                for i in range(len(final_path)):
                    if i == len(final_path) - 1:
                        print(final_path[i], end="")
                    else:
                        print(final_path[i], end=" -> ")
                print()
                return
        print("Goal not found withing depth limit")
    def run(self, percept, graph, depth_limit):
        if self.check_goal(percept):
            return "Already at Goal"
        return self.iterative_deepening(graph, percept, depth_limit)
class Environment:
    def __init__(self, graph_data):
        self.graph = graph_data
    def perceive(self, node):
        return node
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': ['H'],
    'G': [],
    'H': []
}
def run(agent, env, start, depth_limit):
    percept = env.perceive(start)
    agent.run(percept, env.graph, depth_limit)

start_node = 'A'
goal_node = 'G'
env = Environment(tree)
agent = Goalbasedagent(goal_node)
run(agent, env, start_node, 4)
