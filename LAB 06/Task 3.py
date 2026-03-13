#TASK 3
import random

def binary_to_decimal(ch):
    s = ""
    for b in ch:
        s += str(b)
    return int(s, 2)
def fitness(chromosome):
    x = binary_to_decimal(chromosome)
    return x*x + 2*x
def roulette_selection(population, fitness_values):
    total = sum(fitness_values)
    probs = [f/total for f in fitness_values]
    parents = random.choices(population, probs, k=2)
    return parents
def crossover(p1, p2):
    point = random.randint(1, len(p1)-1)
    c1 = p1[:point] + p2[point:]
    c2 = p2[:point] + p1[point:]
    return c1, c2
def mutate(ch, rate):
    for i in range(len(ch)):
        if random.random() < rate:
            ch[i] = 1 - ch[i]
    return ch
def genetic_algorithm(population, generations, mutation_rate):
    for g in range(generations):
        fitness_values = [fitness(ch) for ch in population]
        parents = roulette_selection(population, fitness_values)
        offspring = [crossover(parents[0], parents[1]) for _ in range(len(population)//2)]
        offspring = [c for pair in offspring for c in pair]
        mutated = [mutate(c, mutation_rate) for c in offspring]
        population = mutated
    best = max(population, key=fitness)
    return best
population = []
for _ in range(6):
    chromosome = [random.randint(0,1) for _ in range(5)]
    population.append(chromosome)
generations = 15
mutation_rate = 0.02
best = genetic_algorithm(population, generations, mutation_rate)
x = binary_to_decimal(best)
print("Best chromosome:", best)
print("Best value of x:", x)
print("Best fitness value:", fitness(best))
