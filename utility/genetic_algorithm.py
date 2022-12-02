from random import choices, randint, random, randrange
from utility.vestiti import body_parts, class_names

def generate_genome_range(items):
    genome = []
    for i, item in enumerate(items):
        genome.append(randrange(len(item)))
    return genome


def generate_population_range(size, items):
    return [generate_genome_range(items) for i in range(size)]

# Fitness
def fitness(genome, b_parts = body_parts, max_warmness = 70, min_fashion = 6):
    if len(genome) != len(b_parts):
        raise ValueError("Errore nelle lunghezze")
    fashion = 0
    warmness = 0

    for i, b_part in enumerate(b_parts):
        dress_index = genome[i]
        dress = b_part[dress_index]
        warmness += dress.warmness
        fashion += dress.fashion

        if warmness > max_warmness:
            return 0
    
    if fashion / len(genome) < min_fashion:
        return warmness / 2

    return warmness

# Selection
def selection_pair(population, fitness_func, max_warmness, min_fashion):
    return choices(
        population=population,
        weights=[fitness_func(genome, body_parts, max_warmness, min_fashion) for genome in population],
        k=2
    )

# Crossover
def single_pair_crossover(a, b):
    if len(a) < 2:
        return a, b

    length = len(a)
    i = randint(1, length - 1)
    return a[0:i] + b[i:], b[0:i] + a[i:]

# Mutation
def mutation(genome, num = 1, probability = 0.5):
    for i in range(num):
        index = randrange(len(genome))
        genome[index] = genome[index] if random() > probability else randrange(len(body_parts[i]))
    return genome

def run_evolution(
    temperature = 20,
    max_temperature = 40,
    min_temperature = -10,

    min_fashion = 1,

    size = 10,
    mutation_prob = 0.5,
    max_generations = 100,
    max_fitness = 100,

    verbose = False
):
    cold_level      = (temperature - max_temperature) / (min_temperature - max_temperature)
    cold_level      = abs(cold_level * 10)
    max_warmness    = cold_level * len(body_parts)


    population = generate_population_range(size, body_parts)

    for i in range(max_generations):
        population = sorted(
            population,
            key=lambda genome: fitness(genome, max_warmness=max_warmness, min_fashion=min_fashion),
            reverse=True
        )

        if fitness(population[0], max_warmness=max_warmness, min_fashion=min_fashion) >= max_fitness:
            break

        next_generation = population[0:2]

        for j in range(int(len(population) / 2)):
            parents = selection_pair(population, fitness, max_warmness=max_warmness, min_fashion=min_fashion)
            offspring_a, offspring_b = single_pair_crossover(parents[0], parents[1])
            offspring_a = mutation(offspring_a, probability=mutation_prob)
            offspring_b = mutation(offspring_b, probability=mutation_prob)
            next_generation += [offspring_a, offspring_b]
        
        population = next_generation

    population = sorted(
        population,
        key=lambda genome: fitness(genome, max_warmness=max_warmness, min_fashion=min_fashion),
        reverse=True
    )

    return population, i
