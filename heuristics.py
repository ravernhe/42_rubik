class Heuristics:
    
    def __init__(self, size, solved_grid, name):
        self.size = size
        self.solved_grid = solved_grid
        self.name = name


    def manh(self, grid):
        sum_dist = 0
        for n in range(self.size * self.size):
            value = self.solved_grid[n // self.size][n % self.size]
            for k in range(self.size * self.size):
                if  value == grid[k // self.size][k % self.size]:
                    sum_dist += abs(n // self.size - k // self.size) + abs(n % self.size - k % self.size)
        return sum_dist

    def nbmis(self, grid):
        sum_miss = 0
        for n in range(self.size * self.size):
            if  self.solved_grid[n // self.size][n % self.size] != grid[n // self.size][n % self.size]:
                sum_miss += 1
        return sum_miss

    def nbmis_row_col(self, grid):
        sum_miss_row_col = 0
        for n in range(self.size * self.size):
            if  self.solved_grid[n // self.size][n % self.size] not in grid[n // self.size]:
                sum_miss_row_col += 1
            if  self.solved_grid[n // self.size][n % self.size] not in [grid[y][n % self.size] for y in range(self.size)]:
                sum_miss_row_col += 1
        return sum_miss_row_col

    def heuristic_func(self, grid):
        if self.name == "manh":
            return self.manh(grid)
        elif self.name == "nbmis":
            return self.nbmis(grid)
        elif self.name == "nbmis_row_col":
            return self.nbmis_row_col(grid)
        print("Heuristic function self.name was not found. Default used = manh")
        return self.manh(grid)
