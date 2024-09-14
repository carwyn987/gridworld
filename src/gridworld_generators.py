import numpy as np

def generate_gridworld_dataset(n,m,num_pairs):
    x = []
    y = []
    for i in range(num_pairs):
        grid = generate_single_gridworld(n,m,4,np.random.randint(0,17))
        x.append(grid)
        y.append(step_gridworld(grid))
    return x, y

def generate_single_gridworld(n, m, num_actions = 4, num_movers = 4):
    grid = np.zeros((n, m))
    
    # choose random starting positions for the movers
    for i in range(num_movers):
        x = np.random.randint(n)
        y = np.random.randint(m)
        while grid[x, y] != 0:
            x = np.random.randint(n)
            y = np.random.randint(m)
        grid[x, y] = np.random.choice(list(range(1, num_actions + 1)))

    return grid

def step_gridworld(grid):
    # 1 = up, 2 = down, 3 = left, 4 = right
    n, m = grid.shape
    new_grid = np.zeros((n, m))

    for i in range(n):
        for j in range(m):
            if grid[i, j] == 1:
                if i > 0:
                    new_grid[i - 1, j] = 1
            elif grid[i, j] == 2:
                if i < n - 1:
                    new_grid[i + 1, j] = 2
            elif grid[i, j] == 3:
                if j > 0:
                    new_grid[i, j - 1] = 3
            elif grid[i, j] == 4:
                if j < m - 1:
                    new_grid[i, j + 1] = 4

    return new_grid