import sys
from split_data import split_data
from parse_info import parse_info
from parse_moves import split_moves, read_moves

def main():
    if len(sys.argv) < 2:
        print("Invalind argument count (game file path must be provided)")
        exit(1)

    with open(sys.argv[1], 'r') as file:
        info_part, moves_part = split_data(file.read())
        info = parse_info(info_part)
        print(info)
        moves_list = split_moves(moves_part)
        read_moves(info, moves_list);

if __name__ == '__main__':
    main()
    
