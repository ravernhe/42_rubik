class Heuristics:
    
    def __init__(self, size, solved_grid, name):
        self.size = size
        self.solved_grid = solved_grid
        self.name = name
        self.function = self.manh
        if self.name == "nbmis":
            self.function = self.nbmis
        elif self.name == "nbmis_row_col":
            self.function = self.nbmis_row_col
        elif self.name != "manh":
            print("Heuristic function self.name was not found. Default used = manh")
        
    
    def manh(self, grid):
        size = range(1, len(grid))
        distances = [self.count_distance(num, grid) for num in size]

        return sum(distances)


    def count_distance(self, number, grid):
        position1 = grid.index(number)
        position2 = self.solved_grid.index(number)

        return abs(position2 // self.size - position1 // self.size) + abs(position2 % self.size - position1 % self.size)


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