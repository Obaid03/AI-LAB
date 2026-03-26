from ortools.sat.python import cp_model
class SolutionPrinter(cp_model.CpSolverSolutionCallback):
    def __init__(self, vars_list):
        super().__init__()
        self.vars = vars_list
        self.count = 0
    def OnSolutionCallback(self):
        self.count += 1
        for var in self.vars:
            print(f"{var.Name()} = {self.Value(var)}", end=" ")
        print()
    def get_count(self):
        return self.count

def solve_all():
    model = cp_model.CpModel()
    limit = 4
    A = model.NewIntVar(0, limit - 1, "A")
    B = model.NewIntVar(0, limit - 1, "B")
    C = model.NewIntVar(0, limit - 1, "C")
    model.Add(A != B)
    model.Add(B != C)
    model.Add(A + B <= 4)
    solver = cp_model.CpSolver()
    printer = SolutionPrinter([A, B, C])
    solver.parameters.enumerate_all_solutions = True
    status = solver.Solve(model, printer)
    print("Status =", solver.StatusName(status))
    print("Total Solutions:", printer.get_count())
solve_all()
