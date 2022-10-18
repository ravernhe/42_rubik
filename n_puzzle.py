import sys
from parser import FileParser
from solvability import is_solvable
import time
from ida_search import Solver as ida_solver
from other_algorithm import Solver as other_solver
from display_solution import draw_solution


def npuzzle(file_name, heuristic_name, search_type):
    parser = FileParser(file_name)
    parser.parse()
    solved_grid = is_solvable(parser.map)
    if search_type == 1:
        solution = ida_solver(parser.map["grid"], parser.map["size"], solved_grid, heuristic_name)
    else:
        solution = other_solver(parser.map["grid"], parser.map["size"], solved_grid, heuristic_name, search_type)
    start = time.time()
    path = solution.solve()
    print("Solved in ", "%.4f" % (time.time() - start), "seconds")
    draw_solution(path, parser.map["size"])

if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        raise Exception("python3 n_puzzle.py [map_name]")
    file_name = args[1]
    search_type = 0
    heuristic_name = 0

    while search_type not in ["1", "2", "3", "4"]:
        search_type = input("\n\nSelect your search algorithm:\n1. ida*\n2. a*\n3. greedy\n4. uniform\n\nYour choice : ")
    while heuristic_name not in ["1", "2", "3"]:
        heuristic_name = input("\n\nSelect your heuristic function:\n1. Manhattan distance\n2. Euclidean distance\n3. Hamming distance\n\nYour choice : ")

    npuzzle(file_name, int(heuristic_name), int(search_type))