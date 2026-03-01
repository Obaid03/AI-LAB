# TASK 5 – Best First Search (Graph with Multiple Goals)
class Goalbasedagent:
    def __init__(self, goals):
        self.goals = goals
    def best_first(self, graph, start, goal):
        frontier = [(0, start)]
        visited = set()
        parent = {start: None}
        while frontier:
            frontier.sort()
            current_cost, current_node = frontier.pop(0)
            if current_node in visited:
                continue
            visited.add(current_node)
            print("Node:", current_node, "Priority:", current_cost)
            if current_node == goal:
                path = []
                node = current_node
                while node is not None:
                    path.append(node)
                    node = parent[node]
                path = path[::-1]
                print("Path to", goal, ":", path)
                return path
            for neighbour, weight in graph.get(current_node, []):
                if neighbour not in visited:
                    parent[neighbour] = current_node
                    frontier.append((weight, neighbour))
        print("Goal not reachable")
        return None
    def run(self, graph, start):
        current = start
        remaining_goals = self.goals.copy()
        full_path = [start]
        while remaining_goals:
            best_segment = None
            best_goal = None
            shortest_length = float('inf')

            for goal in remaining_goals:
                print("\nSearching path to goal:", goal)
                segment = self.best_first(graph, current, goal)
                if segment and len(segment) < shortest_length:
                    best_segment = segment
                    best_goal = goal
                    shortest_length = len(segment)
            if best_segment is None:
                print("Cannot reach remaining goals:", remaining_goals)
                return None
            full_path.extend(best_segment[1:])
            current = best_goal
            remaining_goals.remove(best_goal)
            print("Reached goal:", best_goal)
            print("Path so far:", full_path)
        return full_path

class Environment:
    def __init__(self, graph_data):
        self.graph = graph_data
    def perceive(self, node):
        return node

def run(agent, env, start):
    percept = env.perceive(start)
    result = agent.run(env.graph, percept)
    if result:
        print("\nAll goals visited! Final Path:", result)
    else:
        print("No path found")

graph = {
    'S': [('A', 3), ('B', 6), ('C', 5)],
    'A': [('D', 9), ('E', 8)],
    'B': [('F', 12), ('G', 14)],
    'C': [('H', 7)],
    'H': [('I', 5), ('J', 6)],
    'I': [('K', 1), ('L', 10), ('M', 2)],
    'D': [], 'E': [], 'F': [], 'G': [],
    'J': [], 'K': [], 'L': [], 'M': []
}
start_node = 'S'
goals = ['K', 'M', 'E']
env = Environment(graph)
agent = Goalbasedagent(goals)
run(agent, env, start_node)
