# TASK 2 – Depth-Limited Search (DLS
class Goalbasedagent:
    def __init__(self, goal):
        self.goal = goal
    def check_goal(self, current):
        return current == self.goal
    def dls(self, graph, start, limit):
        visited_order = []
        def depth_search(node, depth, path):
            if depth > limit:
                return None
            visited_order.append(node)
            path.append(node)
            if node == self.goal:
                return path.copy()
            for neighbour in graph.get(node, []):
                if neighbour not in path:
                    result = depth_search(neighbour, depth + 1, path)
                    if result:
                        return result
            path.pop()
            return None
        result_path = depth_search(start, 0, [])
        print("Depth Limit:", limit)
        print("Traversal Order:", visited_order)
        if result_path:
            print("Path to Goal:", result_path)
        else:
            print("Goal not found withing depth limit")
        return result_path
    def run(self, percept, graph, depth_limit):
        if self.check_goal(percept):
            return "Already at Goal"
        return self.dls(graph, percept, depth_limit)

class Environment:
    def __init__(self, graph_data):
        self.graph = graph_data
    def perceive(self, node):
        return node  
graph = {
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
goal_node = 'H'
env = Environment(graph)
agent = Goalbasedagent(goal_node)
run(agent, env, start_node, 2)
print()
run(agent, env, start_node, 3)
