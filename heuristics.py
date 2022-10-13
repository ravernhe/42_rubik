class Heuristics:
    
    def __init__(self, size, solved_grid, name):
        self.size = size
        self.solved_grid = solved_grid
        self.name = name
        self.function = self.manh
        if self.name == "nbmis":
            self.function = self.nbmis
        # elif self.name == "nbmis_row_col":
            # self.function = self.nbmis_row_col
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
        for n in range(len(grid)):
            if  self.solved_grid[n] != grid[n]:
                sum_miss += 1
        return sum_miss
