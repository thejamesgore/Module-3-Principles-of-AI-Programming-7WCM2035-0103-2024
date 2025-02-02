import random
import turtle
import math
import copy

def nearest_neighbour_algorithm(x_range, y_range,locations):
    generated_map = [(random.randint(0, x_range), random.randint(0, y_range)) for _ in range(locations)]
    
    print(generated_map)
    
nearest_neighbour_algorithm(200,200,200)