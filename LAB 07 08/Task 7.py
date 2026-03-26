from ortools.sat.python import cp_model
model = cp_model.CpModel()
n = 4
q = [model.NewIntVar(0, n - 1, f"Q{i}") for i in range(n)]
model.AddAllDifferent(q)
model.AddAllDifferent(q[i] + i for i in range(n))
model.AddAllDifferent(q[i] - i for i in range(n))

solver = cp_model.CpSolver()
res = solver.Solve(model)
if res == cp_model.OPTIMAL:
    for r in range(n):
        line = ["_"] * n
        col = solver.Value(q[r])
        line[col] = "Q"
        print(" ".join(line))
