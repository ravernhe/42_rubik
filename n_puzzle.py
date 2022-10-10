import sys
from parser import file_parser
from solvability import is_solvable

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