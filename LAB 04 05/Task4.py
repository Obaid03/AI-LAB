# TASK 4 – Uniform Cost Search (UCS)
class Goalbasedagent:
    def __init__(self, goal):
        self.goal = goal
    def check_goal(self, current):
        return current == self.goal
    def ucs(self, graph, start):
        frontier = [(0, start)]
        visited = set()
        parent = {start: None}
        cost_record = {start: 0}
        while frontier:
            frontier.sort()
            current_cost, current_node = frontier.pop(0)
            if current_node in visited:
                continue
            visited.add(current_node)
            print("Node:", current_node, "Cost:", current_cost)
            if current_node == self.goal:
                path = []
                node = current_node
                while node is not None:
                    path.append(node)
                    node = parent[node]
                path = path[::-1]
                print("UCS Path:", path, "Total Cost:", current_cost)
                return path, current_cost
            for neighbour, weight in graph.get(current_node, {}).items():
                new_cost = current_cost + weight
                if neighbour not in cost_record or new_cost < cost_record[neighbour]:
                    cost_record[neighbour] = new_cost
                    parent[neighbour] = current_node
                    frontier.append((new_cost, neighbour))
        print("Goal not reachable")
        return None, None
    def run(self, percept, graph):
        if self.check_goal(percept):
            return "Already at Goal"
        return self.ucs(graph, percept)
class Environment:
    def __init__(self, graph_data):
        self.graph = graph_data
    def perceive(self, node):
        return node
graph = {
    'S': {'A': 4, 'B': 2},
    'A': {'C': 5, 'D': 10},
    'B': {'E': 3},
    'C': {'G': 4},
    'D': {'G': 1},
    'E': {'D': 4},
    'G': {}
}
def run(agent, env, start):
    percept = env.perceive(start)
    agent.run(percept, env.graph)

start_node = 'S'
goal_node = 'G'
env = Environment(graph)
agent = Goalbasedagent(goal_node)
run(agent, env, start_node)
