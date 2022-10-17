import sys
from parser import FileParser
from solvability import is_solvable
import time
from ida_search import Solver as ida_solver
from other_algorithm import Solver as other_solver


def npuzzle(file_name, heuristic_name, search_type):
    parser = FileParser(file_name)
    parser.parse()
    solved_grid = is_solvable(parser.map)
    if search_type == "ida-star":
        solution = ida_solver(parser.map["grid"], parser.map["size"], solved_grid, heuristic_name)
    else:
        solution = other_solver(parser.map["grid"], parser.map["size"], solved_grid, heuristic_name, search_type)
    start = time.time()
    solution.solve()
    print(time.time() - start)

if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2 or len(args) > 3:
        raise Exception("python3 n_puzzle.py [self.map_name] optional: [functiontion_name]")
    file_name = args[1]
    heuristic_name = "manh"
    search_type = "ida-star"
    if len(args) == 3:
        heuristic_name = args[2]
    npuzzle(file_name, heuristic_name, search_type)