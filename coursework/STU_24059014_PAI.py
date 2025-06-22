"""

James Gore STU_24059014 course work - Simulated epidemic spread using Cellular Automata

"""

import random
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# 
GRID_SIZE = 20
INFECTION_RATE = 0.1
RECOVERY_RATE = 0.2
VACCINATION_RATE = 0.1
STEPS = 20

HEALTHY, INFECTED, RECOVERED = 'H', 'I', 'R'
STATE_MAP = {HEALTHY: 0, INFECTED: 1, RECOVERED: 2}
COLORS = ['green', 'red', 'blue']  

# Helps manage social distancing numbers that can be tweaked
INITIAL_SPREAD = 0.4
REDUCTION_RATE = 0.02
MINIMUM_SPREAD = 0.1

def initialize_grid():
    grid = [[HEALTHY for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    
    for _ in range(int(GRID_SIZE * GRID_SIZE * INFECTION_RATE)):
        x = random.randint(0, GRID_SIZE - 1)
        y = random.randint(0, GRID_SIZE - 1)
        grid[y][x] = INFECTED

    for _ in range(int(GRID_SIZE * GRID_SIZE * VACCINATION_RATE)):
        x = random.randint(0, GRID_SIZE - 1)
        
        y = random.randint(0, GRID_SIZE - 1)
        if grid[y][x] == HEALTHY:
            grid[y][x] = RECOVERED

    return grid

# This function returns the neighbours of cell by looking at the left, top, right, and bottom adjacent cells
def get_neighbors(x, y):
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    return [(x+dx, y+dy) for dx, dy in directions if 0 <= x+dx < GRID_SIZE and 0 <= y+dy < GRID_SIZE]

# This function is what is simulating the spread of the virus and how effective vaccination and recovery is
def step(grid, time_step):
    new_grid = []
    for i in range(GRID_SIZE):
        new_grid.append([])
        for j in range(GRID_SIZE):
            new_grid[i].append(grid[i][j])

    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            state = grid[y][x]
            neighbors = get_neighbors(x, y)
            infected_neighbors = sum(1 for nx, ny in neighbors if grid[ny][nx] == INFECTED)

            spread_chance = INITIAL_SPREAD - (REDUCTION_RATE * time_step)
            if spread_chance < MINIMUM_SPREAD:
                spread_chance = MINIMUM_SPREAD

            if state == HEALTHY and infected_neighbors > 0 and random.random() < spread_chance:
                new_grid[y][x] = INFECTED
            elif state == INFECTED and random.random() < RECOVERY_RATE:
                new_grid[y][x] = RECOVERED

    return new_grid

#  A simple function to display the progress of simulation using our visualisation package matplotlib
def show_grid(grid, step):
    numeric_grid = [[STATE_MAP[cell] for cell in row] for row in grid]
    cmap = mcolors.ListedColormap(COLORS)  
    plt.figure(figsize=(5, 5))
    plt.imshow(numeric_grid, cmap=cmap, interpolation='nearest')
    plt.title(f"Step {step}")
    plt.axis('off')
    plt.show()

# This is the final function that displays a line graph of the infection rate versus recovered over time
def plot_trends(infection_counts, recovery_counts):
    
    plt.figure(figsize=(8, 4))
    plt.plot(infection_counts, label="Infected", color='red')
    plt.plot(recovery_counts, label="Recovered", color='blue')
    plt.title("Epidemic Progression Over Time")  
    plt.xlabel("Time Step")
    plt.ylabel("Number of Individuals")  
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def run_simulation():

    grid = initialize_grid()
    infection_counts = []
    recovery_counts = []

    for t in range(STEPS):
        grid = step(grid, t)
        infected = sum(row.count(INFECTED) for row in grid)
        recovered = sum(row.count(RECOVERED) for row in grid)

        infection_counts.append(infected)
        recovery_counts.append(recovered)

        if t % 5 == 0 or t == STEPS - 1:
            show_grid(grid, t)

    plot_trends(infection_counts, recovery_counts)


if __name__ == "__main__":
    run_simulation()
