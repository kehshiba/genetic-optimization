import random
import math


def fitness_func(x):
    return math.sin(10 * x) * x + math.cos(2 * x) * x


POPULATION_SIZE = 50
GENE_LENGTH = 6
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.05
GENERATIONS = 50

population = []
for i in range(POPULATION_SIZE):
    individual = []
    for j in range(GENE_LENGTH):
        individual.append(random.randint(0, 1))
    population.append(individual)


def evaluate(population):
    fitness_scores = []
    for individual in population:
        dec = int(''.join(map(str, individual)), 2) / (2 ** GENE_LENGTH - 1)
        fitness_scores.append(fitness_func(dec))
    return fitness_scores


def selection(population, fitness_scores):
    selected = []
    total_fitness = sum(fitness_scores)
    for i in range(len(population)):
        r = random.uniform(0, total_fitness)
        current_sum = 0
        for j in range(len(population)):
            current_sum += fitness_scores[j]
            if current_sum > r:
                selected.append(population[j])
                break
    return selected


def crossover(dad, mom):
    if random.random() > CROSSOVER_RATE:
        return dad, mom
    crossover_point = random.randint(1, GENE_LENGTH - 1)
    baby1 = dad[:crossover_point] + mom[crossover_point:]
    baby2 = mom[:crossover_point] + dad[crossover_point:]

    return baby1, baby2


def mutation(individual):
    for i in range(len(individual)):
        if random.random() < MUTATION_RATE:
            individual[i] = 1 - individual[i]
        return individual


for i in range(GENERATIONS):
    fitness_scores = evaluate(population)
    selected = selection(population, fitness_scores)
    offspring = []
    for j in range(0, POPULATION_SIZE - 1, 2):
        dad = random.choice(selected)
        mom = random.choice(selected)
        baby1, baby2 = crossover(dad, mom)
        baby1 = mutation(baby1)
        baby2 = mutation(baby2)
        offspring.append(baby1)
        offspring.append(baby2)
    population = offspring

for child in offspring:
    print(*child)
