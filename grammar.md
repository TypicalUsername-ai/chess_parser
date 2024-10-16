<pgn_game> ::= <tag_section> <move_section>

<tag_section> ::= "[" <tag_pair> { <tag_pair> } "]"

<tag_pair> ::= <tag_name> <tag_value>

<tag_name> ::= <string>

<tag_value> ::= <string>

<string> ::= '"' <characters> '"'

<characters> ::= { <character> }

<character> ::= <any ASCII character except " and control characters>

<move_section> ::= <san_move> { <san_move> }

<san_move> ::= <move_number> <san_move_text>

<move_number> ::= <digit> { <digit> } "."

<digit> ::= "1" | "2" | ... | "9" | "0"

<san_move_text> ::= <san_move_element> { <san_move_element> }

<san_move_element> ::= <piece_designator> | <square_designator> | <special_move> | <check_indicator>

<piece_designator> ::= "K" | "Q" | "R" | "B" | "N"

<square_designator> ::= <file_letter> <rank_number>

<file_letter> ::= "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h"

<rank_number> ::= "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8"

<special_move> ::= "O-O" | "O-O-O"

<check_indicator> ::= "+" | "#"
