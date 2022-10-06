import sys
from copy import deepcopy

class file_parser:

    def __init__(self, file_name=str):
        self.file_name = file_name
        self.map = {'size': 0, 'grid': []}


    def parse(self):
        self.parse_file()
        self.catch_error()
        self.normalized_grid(self.map["size"])

    def normalized_grid(self, size):
        self.map["grid"] = [self.map["grid"][i * size : i * size + size] for i in range(size)]
    
    def parse_file(self):
        try:
            file = open(self.file_name,"r")
        except:
            raise FileNotFoundError(f"File {self.file_name} cannot be oppened.")
        
        lines = file.readlines()
        for line in lines:
            line = line.split("#")[0]
            if line:
                line = line.split()
                if self.map["size"] == 0:
                    if len(line) != 1:
                        raise ValueError("self.map size must specified correctly")
                    if not line[0].isnumeric():
                        raise ValueError("self.map size must be numeric")
                    if int(line[0]) < 2:
                        raise Exception("self.map size cannot be less than 2")
                    self.map["size"] = int(line[0]) 
                else:
                    for x in line:
                        if not x.isnumeric():
                            raise ValueError("self.map must only contain numbers")
                        self.map["grid"].append(int(x))

    def catch_error(self):
        self.map_lenght = self.map["size"] * self.map["size"]
        if len(self.map["grid"]) != self.map_lenght:
            raise Exception("self.map does not match the self.map size specified")
        grid_set = set(self.map["grid"])
        if len(grid_set) != self.map_lenght:
            raise Exception("self.map must not contain duplicates")
        if min(grid_set) != 0 or max(grid_set) != self.map_lenght - 1:
            raise ValueError("self.map values out of range")


def in_bound(i, j, border):
    return i >= border[2] and i <= border[3] and j >= border[0] and j <= border[1]

def swap_numbers(i, j, value, moves, size, grid):
    if not grid[i][j] == value:
        for n in range(size * size - 1) :
            if (grid[n // size][n % size] == value):
                grid[i][j], grid[n // size][n % size] = grid[n // size][n % size], grid[i][j]
                moves += 1
                break
    return grid, moves

def step_zero(i, j, map):
    for n in range(map["size"] * map["size"] - 1):
            if (map["grid"][n // map["size"]][n % map["size"]] == 0):
                return abs(n // map["size"] - i) + abs(n % map["size"] - j)

def is_solvable(map):
    directions = [
    lambda i, j: (i, j + 1),
    lambda i, j: (i + 1, j),
    lambda i, j: (i, j - 1),
    lambda i, j: (i - 1, j),
    ]

    border_reshape = [
    lambda l, r, t, b: (l, r, t + 1, b),
    lambda l, r, t, b: (l, r - 1, t, b),
    lambda l, r, t, b: (l, r, t, b - 1),
    lambda l, r, t, b: (l + 1, r, t, b),
    ]

    border = [0, map["size"] - 1, 0, map["size"] -1]

    turn = 0
    i, j = 0, 0
    index = 1
    moves = 0
    grid_cpy = deepcopy(map["grid"])
    while True:
        direction_func = directions[turn % 4]
        tmp_i, tmp_j = direction_func(i, j)
        if (not in_bound(tmp_i, tmp_j, border)):
            border = [*border_reshape[turn % 4](*border)]
            turn += 1
        else:
            grid_cpy, moves = swap_numbers(i, j, index, moves, map["size"], grid_cpy)
            i, j = tmp_i, tmp_j

            index += 1
            if index >= map["size"] * map["size"]:
                if step_zero(i, j, map) % 2 != moves % 2:
                    print("The map requested is not solvable.")
                    exit()
                return 


def npuzzle(file_name):
    parser = file_parser(file_name)
    parser.parse()
    is_solvable(parser.map)
    print(parser.map)

if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        raise Exception("python3 n_puzzle.py [self.map_name]")
    file_name = args[1]
    npuzzle(file_name)