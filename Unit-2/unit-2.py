import random
import turtle
import math
import copy

"""
Your original attempt:
def nearest_neighbour_algorithm(x_range, y_range,locations):
    generated_map = [(random.randint(0, x_range), random.randint(0, y_range)) for _ in range(locations)]
    
    print(generated_map)
    
nearest_neighbour_algorithm(200,200,200)
"""

def nearest_neighbour_algorithm(x_range, y_range, locations):
    
    generated_map = []
    for x in range(locations):
        generated_map.insert(x, [random.randint(-x_range,x_range), random.randint(-y_range, y_range)])
        
        print(" Generated_map ", generated_map)
        
    temp_map = copy.deepcopy(generated_map)
    
    optermised_map = []
    
    optermised_map.append(temp_map.pop())
    
    turtle.setup(width=500, height=500)
    turtle.screensize(400, 400)
    turtle.speed(0)

    turtle.penup()
    turtle.goto(optermised_map[0][0], optermised_map[0][1])
    turtle.pendown()
    turtle.done()
    
    print("temp_map", temp_map)
    print("optermised_map", optermised_map
          )
nearest_neighbour_algorithm(200,200,200)