from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from play_npuzzle import play_npuzzle
import argparse
from parser import FileParser
from solvability import is_solvable
import time
from ida_search import Solver as ida_solver
from other_algorithm import Solver as other_solver
from display_solution import draw_solution





def npuzzle(file_name, heuristic_name, search_type, play):
    parser = FileParser(file_name)
    parser.parse()
    solved_grid = is_solvable(parser.map)
    if play:
        play_npuzzle(parser.map["grid"], parser.map["size"], solved_grid)
    if search_type == 1:
        solution = ida_solver(parser.map["grid"], parser.map["size"], solved_grid, heuristic_name)
    else:
        solution = other_solver(parser.map["grid"], parser.map["size"], solved_grid, heuristic_name, search_type)
    start = time.time()
    path = solution.solve()
    print("Solved in ", "%.4f" % (time.time() - start), "seconds")
    draw_solution(path, parser.map["size"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--map", help="put a valid file")
    parser.add_argument("-play", "--play", help="play to solve yourself", action="store_true")
    args = parser.parse_args()

    if not args.map:
        raise Exception("python3 n_puzzle.py -m [map_name]")
    file_name = args.map
    search_type = 0
    heuristic_name = 0
    if not args.play:
        while search_type not in ["1", "2", "3", "4"]:
            search_type = input("\n\nSelect your search algorithm:\n1. ida*\n2. a*\n3. greedy\n4. uniform\n\nYour choice : ")
        while heuristic_name not in ["1", "2", "3"]:
            heuristic_name = input("\n\nSelect your heuristic function:\n1. Manhattan distance\n2. Euclidean distance\n3. Hamming distance\n\nYour choice : ")

    npuzzle(file_name, int(heuristic_name), int(search_type), args.play)