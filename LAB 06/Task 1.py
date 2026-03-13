#TASK1
import random

def calculate_value(x):
    return -x**2 + 6*x

def get_neighbors(x):
    neighbors = []
    if x - 1 >= 0:
        neighbors.append(x - 1)
    if x + 1 <= 6:
        neighbors.append(x + 1)
    return neighbors

def simple_hill_climbing():
    
    current = random.randint(0, 6)
    print("Initial x:", current)
    print("f(x) =", calculate_value(current))
    while True:
        neighbors = get_neighbors(current)
        best = current
        best_value = calculate_value(current)
        
        for n in neighbors:
            value = calculate_value(n)
            print("Check neighbor x =", n, " f(x) =", value)
            if value > best_value:
                best = n
                best_value = value
        if best == current:
            break
        current = best
        print("Move x =", current)
        print("f(x) =", calculate_value(current))
        print()
    print("Final Otpimal x =", current)
    print("Maximum f(x) =", calculate_value(current))

simple_hill_climbing()
