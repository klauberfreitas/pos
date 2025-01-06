import random
import numpy as np

def generate_random_population(cities_locations, population_size):
    population = []
    for _ in range(population_size):
        individual = cities_locations[:]
        random.shuffle(individual)
        population.append(individual)
    return population

def nearest_neighbour(cities_locations):
    start_city = random.choice(cities_locations)
    unvisited = cities_locations[:]
    unvisited.remove(start_city)
    tour = [start_city]
    
    while unvisited:
        nearest_city = min(unvisited, key=lambda city: distance(tour[-1], city))
        tour.append(nearest_city)
        unvisited.remove(nearest_city)
    
    return tour

def distance(city1, city2):
    # Implementação da função de distância (por exemplo, distância euclidiana)
    return ((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2) ** 0.5

def generate_population(cities_locations, population_size):
    half_population_size = population_size // 2
    
    # Gerar metade da população aleatoriamente
    random_population = generate_random_population(cities_locations, half_population_size)
    
    # Gerar a outra metade usando Nearest Neighbour
    nn_population = [nearest_neighbour(cities_locations) for _ in range(half_population_size)]
    
    # Combinar as duas metades
    population = random_population + nn_population
    
    return population