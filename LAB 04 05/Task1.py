# TASK 1 – Breadth-First Search (BFS)
class Goalbasedagent:
    def __init__(self, exit_point):
        self.exit_point = exit_point
    def check_goal(self, current):
        return current == self.exit_point
    def create_graph(self, floor):
        graph = {}
        rows = len(floor)
        cols = len(floor[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        for i in range(rows):
            for j in range(cols):
                if floor[i][j] == 1:
                    neighbours = []
                    for dx, dy in directions:
                        x, y = i + dx, j + dy
                        if 0 <= x < rows and 0 <= y < cols and floor[x][y] == 1:
                            neighbours.append((x, y))
                    graph[(i, j)] = neighbours
        return graph
    def bfs(self, graph, start):
        queue = [(start, [start])]
        visited = {start}
        traversal_order = []
        while queue:
            current, path = queue.pop(0)
            traversal_order.append(current)
            if current == self.exit_point:
                print("Traversing Order:", traversal_order)
                print("Shortest Path:", path)
                return "Emergency Exit fond "
            for nxt in graph.get(current, []):
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, path + [nxt]))
        print("Traversing order Order:", traversal_order)
        return "No Exit Available"
    def run(self, percept, grid):
        if self.check_goal(percept):
            return "Already at Emergency Exit"
        graph = self.create_graph(grid)
        return self.bfs(graph, percept)
class Environment:
    def __init__(self, layout):
        self.layout = layout
    def perceive(self, position):
        return position

def run(agent, env, start):
    perception = env.perceive(start)
    result = agent.run(perception, env.layout)
    print(result)

building = [
    [1, 1, 0, 1],
    [0, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 0, 1, 1]
]
start_position = (0, 0)
exit_position = (3, 3)
agent = Goalbasedagent(exit_position)
env = Environment(building)
run(agent, env, start_position)
