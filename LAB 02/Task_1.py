# Task 1: Vehicle Rental System
# Design a Vehicle Rental System using OOP.
# Requirements:
# 1. Create a class Vehicle
# 2. Attributes: vehicle_id, brand, rent_per_day
# 3. Methods: display_details(), calculate_rent(days)
# 4. Create at least two vehicle objects
# 5. Calculate rent for different days

class Vehicle:
    def __init__(self, vehicle_id, brand, rent_per_day):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.rent_per_day = rent_per_day
    def display_details(self):
        print(self.vehicle_id, self.brand, self.rent_per_day)
    def calculate_rent(self, days):
        return self.rent_per_day * days

v1 = Vehicle(1,"civic",500)
v2 = Vehicle(2,"city",400)

v1.display_details()
print(v1.calculate_rent(3))

v2.display_details()
print(v2.calculate_rent(5))
  
