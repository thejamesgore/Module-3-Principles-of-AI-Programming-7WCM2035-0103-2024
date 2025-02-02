# turtle isn't working so debugging here

import random
import turtle
import copy

def nearest_neighbour_algorithm(x_range, y_range, locations):
    # Setup turtle window size to prevent scrolling
    turtle.setup(800, 800)  # This sets the window to a larger 800x800 pixels.

    turtle.screensize(400, 400)
    turtle.setworldcoordinates(-200, -200, 200, 200)
    
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)


    
    generated_map = []
    for x in range(locations):
        generated_map.insert(x, [random.randint(-x_range, x_range), random.randint(-y_range, y_range)])
        
    temp_map = copy.deepcopy(generated_map)
    optermised_map = []
    
    optermised_map.append(temp_map.pop())
    turtle.penup()
    turtle.goto(optermised_map[0][0], optermised_map[0][1])
    turtle.pendown()
    
    # Keep window open
    turtle.done()

nearest_neighbour_algorithm(200, 200, 200)
