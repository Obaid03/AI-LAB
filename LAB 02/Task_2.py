# Design an Employee Payroll System using inheritance.
# Requirements:
# 1. Base class Employee (name, emp_id)
# 2. Child classes:
# - FullTimeEmployee (monthly_salary)
# - PartTimeEmployee (hours_worked, hourly_rate)
# 3. Override calculate_salary() method
# 4. Create objects and display salary

class Employee:
    def __init__(self,name,emp_id):
        self.name= name
        self.emp_id = emp_id
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, monthly_salary):
        super().__init__(name, emp_id)
        self.monthly_salary = monthly_salary
    def calculate_salary(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, hours_worked, hourly_rate):
        super().__init__(name, emp_id)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate

e1 = FullTimeEmployee("obaid", 101,500)
e2 = PartTimeEmployee("jawad", 102, 40, 500)

print(e1.name, e1.calculate_salary())
print(e2.name, e2.calculate_salary())
