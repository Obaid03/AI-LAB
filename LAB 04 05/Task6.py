# TASK 6 – A* Search
class Goalbasedagent:
    def __init__(self, goal):
        self.goal = goal
    def astar(self, graph, start, heuristic):
        frontier = [(heuristic[start], 0, start)]
        visited = set()
        parent = {start: None}
        cost_record = {start: 0}
        while frontier:
            frontier.sort()
            f_cost, g_cost, current_node = frontier.pop(0)
            if current_node in visited:
                continue
            visited.add(current_node)
            print("Node:", current_node, "g:", g_cost, "f:", f_cost)
            if current_node == self.goal:
                path = []
                node = current_node
                while node is not None:
                    path.append(node)
                    node = parent[node]
                path = path[::-1]
                print("A* Path:", path, "Total Cost:", g_cost)
                return path, g_cost
            for neighbour, weight in graph.get(current_node, {}).items():
                new_g = g_cost + weight
                new_f = new_g + heuristic[neighbour]
                if neighbour not in cost_record or new_g < cost_record[neighbour]:
                    cost_record[neighbour] = new_g
                    parent[neighbour] = current_node
                    frontier.append((new_f, new_g, neighbour))
        print("Goal not reachable")
        return None, float('inf')
    def star(self, graph, start, heuristic, changes):
        path, cost = self.astar(graph, start, heuristic)
        print("\nInitial Path:", path, "Cost:", cost)
        for edge, new_cost in changes:
            node_a, node_b = edge
            if node_b in graph.get(node_a, {}):
                old_cost = graph[node_a][node_b]
                graph[node_a][node_b] = new_cost
                print("\nEdge", node_a, "-", node_b,
                      "changed from", old_cost, "to", new_cost)
                print("Recomputing path after change...")
                path, cost = self.astar(graph, start, heuristic)
        return path, cost
    def run(self, graph, start, heuristic, changes):
        if start == self.goal:
            return "Already at Goal"
        return self.astar(graph, start, heuristic, changes)
class Environment:
    def __init__(self, graph_data, heuristic_data):
        self.graph = graph_data
        self.heuristic = heuristic_data
    def perceive(self, node):
        return node
def run(agent, env, start, changes):
    percept = env.perceive(start)
    result = agent.run(env.graph, percept, env.heuristic, changes)
    print("\nFinal Result:", result)

graph = {
    'A': {'B': 4, 'C': 3},
    'B': {'E': 12, 'F': 5},
    'C': {'D': 7, 'E': 10},
    'D': {'E': 2},
    'E': {'G': 5},
    'F': {'G': 16},
    'G': {}
}
heuristic = {
    'A': 14, 'B': 12, 'C': 11,
    'D': 6, 'E': 4, 'F': 11, 'G': 0
}
start_node = 'A'
goal_node = 'G'
changes = [
    (('A', 'B'), 8),
    (('B', 'E'), 7)
]
env = Environment(graph, heuristic)
agent = Goalbasedagent(goal_node)
run(agent, env, start_node, changes)
