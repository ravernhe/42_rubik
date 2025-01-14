from math import sqrt


class Heuristics:
    
    def __init__(self, size, solved_grid, name):
        self.size = size
        self.solved_grid = solved_grid
        self.name = name
        if self.name == 1:
            self.function = self.manh
        elif self.name == 2:
            self.function = self.eucl
        elif self.name == 3:
            self.function = self.nbmis
        
    
    def count_manh_distance(self, number, grid):
        position1 = grid.index(number)
        position2 = self.solved_grid.index(number)

        return abs(position2 // self.size - position1 // self.size) + abs(position2 % self.size - position1 % self.size)
    

    def manh(self, grid):
        size = range(1, len(grid))
        distances = [self.count_manh_distance(num, grid) for num in size]

        return sum(distances)


    def count_eucl_distance(self, number, grid):
        position1 = grid.index(number)
        position2 = self.solved_grid.index(number)

        return sqrt((position2 // self.size - position1 // self.size) ** 2 + (position2 % self.size - position1 % self.size) ** 2)
    
    def eucl(self, grid):
        size = range(1, len(grid))
        distances = [self.count_eucl_distance(num, grid) for num in size]
        return sum(distances)

    
    def nbmis(self, grid):
        sum_miss = 0
        for n in range(len(grid)):
            if  self.solved_grid[n] != grid[n]:
                sum_miss += 1
        return sum_miss