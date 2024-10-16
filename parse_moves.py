import re
from parse_info import ChessGameInfo

def split_moves(data: str) -> [str]:
    moves = []
    re_turns = re.compile("[0-9]+\.")
    turns = list(map(lambda s: s.strip(), re_turns.split(data.replace("\n", " "))[1:]))
    for t in turns:
        ts = list(filter(lambda s: s != '', t.split(" ")))
        moves.append(ts[0])
        moves.append(ts[1])

    return moves

def read_moves(info: ChessGameInfo, moves: [str]):
    # print(info)
    # print(moves)

    for (i, mv) in enumerate(moves[:-1]):
        if i % 2 == 0:
            color = "WHITE"
            names = info.white.split(" ")
        else:
            color = "BLACK"
            names = info.black.split(" ")

        try:
            player = f"{names[0][0]}. {names[1]}"
        except IndexError:
            player = names[0]
        action = Action(mv)

        print(f"[{color} {i // 2 + 1}] {player} {action}")

    print(f"[Game End] {info.white} {info.result} {info.black}")
        
def parse_figure(fig: str) -> str:
        match fig:
            case 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h':
                return f"{fig} pawn"
            case "R":
                return "Rook"
            case "N":
                return "Knight"
            case "B":
                return "Bishop"
            case "Q":
                return "Queen"
            case "K" | "O":
                return "King"
            case u:
                raise Exception(f"Figure unknown {u}")

class Action():
    def __init__(self, move: str):

        move_expr = re.compile("[a-z][1-8]")
        promote_expr = re.compile("=[A-Z]")

        self.figure = parse_figure(move[0])

        if len(promote_expr.findall(move)) == 1:
            self.promotion = parse_figure(promote_expr.findall(move)[0][1])
        else:
            self.promotion = None
        
        if move == "O-O":
            self.pos_str = "Short Castle position"
        elif move == "O-O-O":
            self.pos_str = "Long Castle position"
        else:
            self.pos_str = move_expr.findall(move)[0]
        
        if move[-1] == '+':
            self.check = 'check'
        elif move[-1] == '#':
            self.check = 'checkmate'
        else:
            self.check = None
        
        if 'x' in move:
            self.capture = True
        else:
            self.capture = False

    def __str__(self):
        rs = ""
        if self.capture:
            rs += f"captures with {self.figure} on"
        else:
            rs += f"moves {self.figure} to"
        rs += f" {self.pos_str}"

        if self.promotion:
            rs += f" and promotes it to a {self.promotion}"

        if self.check != None:
            rs += " with "+self.check

        return rs
      
