import random

def create_grid(size=20, fill_value=0):
    return [[fill_value for _ in range(size)] for _ in range(size)]

def place_mines(grid, probability=0.2):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if random.random() < probability:
                grid[i][j] = 9

def set_values(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 9:
                continue
            count = 0
            for x in range(max(0, i-1), min(len(grid), i+2)):
                for y in range(max(0, j-1), min(len(grid[i]), j+2)):
                    if grid[x][y] == 9:
                        count += 1
            grid[i][j] = count

def print_grid(grid):
    for row in grid:
        print(" ".join(f"{num:2}" for num in row))


grid = create_grid()
place_mines(grid)
set_values(grid)
print_grid(grid)



