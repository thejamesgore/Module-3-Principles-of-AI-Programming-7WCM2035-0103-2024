#  Rule 90

import turtle
import random
from turtle import Screen

sizing = 1
x_stamp_spacing=9*sizing
y_stamp_spacing=18*sizing

Screen().setup(300,300)

window_width=turtle.window_width()
window_height=turtle.window_height()

columns = int(window_width/x_stamp_spacing)
rows = int(window_height/y_stamp_spacing)
current_row=[]
next_row=[]
random_values=[]
probability = 0.85

def initialise_first_row():
    print('initialise') 

    global current_row 
    current_row = []  

    for _ in range(columns):  
        rand_num = round(random.random(), 2) 
        random_values.append(rand_num)  
        
        if rand_num > probability:
            current_row.append(1)
        else:
            current_row.append(0)

    print("Current Row:", current_row)
    print("Random Values:", random_values)

initialise_first_row()