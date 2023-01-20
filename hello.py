def numCells(grid):
    dominant_value = 0
    no_of_dominant = 0
    dom_ls = []
    rows = len(grid)
    cols = len(grid[0])
    
    for i in range(0,rows-1):
        for j in range(0, cols-1):
            element = grid[i][j]
            if element > grid[min(rows-1, i+1)][j] and element > grid[i][min(cols-1, j+1)] and element > grid[min(rows-1, i+1)][min(cols-1, j+1)] and element > grid[max(i-1, 0)][j] and element > grid[i][max(j-1, 0)] and element > grid[max(i-1, 0)][max(j-1, 0)] and element > grid[max(i-1, 0)][min(cols-1, j+1)] and element > grid[i+1][j-1]: