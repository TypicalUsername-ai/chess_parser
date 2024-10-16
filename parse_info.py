import re

class ChessGameInfo:
    
    def __init__(self, data: str):
        # expr = re.compile("(?<=\[).+?(?=\])")
        expr = re.compile("\[(.*)\]")
        par = re.compile("\"(.*)\"")
        splits = list(filter(lambda a: a != '\n' and a != '',expr.split(data))) 
        assert len(splits) >= 7, "Seven-tag rule violated"
        # due to the seven-tag rule everything appears in order
        self.event = par.split(splits[0])[1]
        self.site = par.split(splits[1])[1]
        self.date = par.split(splits[2])[1]
        self.round = par.split(splits[3])[1]
        self.white = par.split(splits[4])[1]
        self.black = par.split(splits[5])[1]
        self.result = par.split(splits[6])[1]

    def __str__(self):
        return f"{self.white} (white) vs {self.black} (black) at {self.event} {self.date}"
            
def parse_info(info_part: str):
    return ChessGameInfo(info_part)
