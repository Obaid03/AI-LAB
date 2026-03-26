from ortools.sat.python import cp_model
model = cp_model.CpModel()
limit = 4
A = model.NewIntVar(0, limit - 1, "A")
B = model.NewIntVar(0, limit - 1, "B")
C = model.NewIntVar(0, limit - 1, "C")
model.Add(A != B)
model.Add(B != C)
model.Add(A + B <= 4)
solver = cp_model.CpSolver()
result = solver.Solve(model)
if result in (cp_model.OPTIMAL, cp_model.FEASIBLE):
    print("A:", solver.Value(A))
    print("B:", solver.Value(B))
    print("C:", solver.Value(C))
else:
    print("No feasible solution")
