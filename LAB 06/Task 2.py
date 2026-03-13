#TASK 2
goal = 20
beam_width = 2

def heuristic(n):
    return abs(goal - n)

def get_successors(x):
    return [x + 2, x + 3, x * 2]

def beam_search(start, goal, beam_width=2):
    beam = [(heuristic(start), [start])]
    level = 0
    while beam:
        print("Levele", level, "Statse:", [path[-1] for h, path in beam])
        candidates = []
        for h_val, path in beam:
            current = path[-1]
            if current == goal:
                return path

            for n in get_successors(current):
                if n <= goal:
                    new_path = path + [n]
                    candidates.append((heuristic(n), new_path))

        candidates.sort(key=lambda x: x[0])
        beam = candidates[:beam_width]
        level += 1
    return None
start = 1
path = beam_search(start, goal, beam_width)
print("\nFinal Path to 20:", path)
