import yaml

from typing import Any


def load_config(path: str) -> dict[str, Any]:
    with open(path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    return config

def print_table():
    table = [
        ["SYMBOL", "VALUE"],
        ["KEYWORD", "int"],
        ["IDENTIFIER", "main"],
        ["LP", "("],
        ["RP", ")"],
        ["LB", "{"],
        ["KEYWORD", "int"],
        ["IDENTIFIER", "a"],
        ["ASSIGN_OP", "="],
        ["IDENTIFIER", "a"],
        ["ADD_OP", "+"],
        ["INTEGER", "1"],
        ["SEMICOLON", ";"],
        ["IDENTIFIER", "cout"],
        ["LSTREAM", "<<"],
        ["IDENTIFIER", "a"],
        ["LSTREAM", "<<"],
        ["IDENTIFIER", "endl"],
        ["SEMICOLON", ";"],
        ["KEYWORD", "return"],
        ["INTEGER", "0"],
        ["SEMICOLON", ";"],
        ["RB", "}"]
    ]

    max_lengths = [max(len(str(cell)) for cell in col) for col in zip(*table)]
    row_format = "|".join(" {{:<{}}} ".format(length) for length in max_lengths)

    print("+{}+".format("+".join("-" * (length + 2) for length in max_lengths)))
    for row in table:
        print("|{}|".format(row_format.format(*row)))
        if row[0] == "SYMBOL":
            print("+{}+".format("+".join("-" * (length + 2) for length in max_lengths)))
    print("+{}+".format("+".join("-" * (length + 2) for length in max_lengths)))

print_table()
