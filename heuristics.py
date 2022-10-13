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
        


    # def manh(self, grid):
    #     sum_dist = 0
    #     for n in range(self.size * self.size):
    #         value = self.solved_grid[n // self.size][n % self.size]
    #         for k in range(self.size * self.size):
    #             if  value == grid[k // self.size][k % self.size]:
    #                 sum_dist += abs(n // self.size - k // self.size) + abs(n % self.size - k % self.size)
    #     return sum_dist

    
    def manh(self, grid):
        size = range(1, len(grid) ** 2)
        distances = [self.count_distance(num, grid) for num in size]

        return sum(distances)


    def count_distance(self, number, grid):
        for y in range(self.size):
            for x in range(self.size):
                if grid[y][x] == number:
                    position1 = [y, x]
                if self.solved_grid[y][x] == number:
                    position2 = [y, x]

        return abs(position2[0] - position1[0]) + abs(position2[1] - position1[1])


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