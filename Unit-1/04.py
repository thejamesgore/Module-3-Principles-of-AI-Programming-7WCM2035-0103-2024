import random

def nested_for_loop(v):
    grid = []
    for x in range(v):
        grid.append([random.randint(0,10),random.randint(-50,100),random.randint(10,20)])
    print(grid)
    
nested_for_loop(10)