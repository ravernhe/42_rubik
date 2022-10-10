from nis import match
import sys
from parser import file_parser
from unittest import case

from matplotlib.pyplot import switch_backend
from solvability import is_solvable


def manh(grid, size, solved_grid):
    sum_dist = 0
    for n in range(size * size):
        value = solved_grid[n // size][n % size]
        for k in range(size * size):
            if  value == grid[k // size][k % size]:
                sum_dist += abs(n // size - k // size) + abs(n % size - k % size)
    return sum_dist

def nbmis(grid, size, solved_grid):
    sum_miss = 0
    for n in range(size * size):
        if  solved_grid[n // size][n % size] != grid[n // size][n % size]:
            sum_miss += 1
    return sum_miss

def nbmis_row_col(grid, size, solved_grid):
    sum_miss_row_col = 0
    for n in range(size * size):
        if  solved_grid[n // size][n % size] not in grid[n // size]:
            sum_miss_row_col += 1
        if  solved_grid[n // size][n % size] not in [grid[y][n % size] for y in range(size)]:
            sum_miss_row_col += 1
        
    return sum_miss_row_col

def heuristic_func(grid, size, solved_grid, name):
    if name == "manh":
        return manh(grid, size, solved_grid)
    elif name == "nbmis":
        return nbmis(grid, size, solved_grid)
    elif name == "nbmis_row_col":
        return nbmis_row_col(grid, size, solved_grid)

    print("Heuristic function name was not found. Default used = manh")
    return manh(grid, size, solved_grid)



class solver:
    node = {
    "grid":[],
    "cost":0,
    "h": 0,
    "parent": None,
    }

    solution = []

    def __init__(self, grid, size, solved_grid, heuristic_name):
        self.grid = grid
        self.size = size
        self.solved_grid = solved_grid
        self.heuristic_name = heuristic_name
    
    def solve(self):
        heuristic = heuristic_func(self.grid, self.size, self.solved_grid, self.heuristic_name)
        # astar =/
        print(heuristic)
        self.solution = ["blabla"]
        pass

def npuzzle(file_name, heuristic_name):
    parser = file_parser(file_name)
    parser.parse()
    solved_grid = is_solvable(parser.map)
    solution = solver(parser.map["grid"], parser.map["size"], solved_grid, heuristic_name)
    solution.solve()

if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2 or len(args) > 3:
        raise Exception("python3 n_puzzle.py [self.map_name] optional: [heuristic_function_name]")
    file_name = args[1]
    heuristic_name = "manh"
    if (len(args) == 3):
        heuristic_name = args[2]
    npuzzle(file_name, heuristic_name)