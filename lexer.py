from typing import Any
import re


class Lexer:

    def tokenize(self, config, program) :
        tokens = []
        for token_type, pattern in config.items():
            if isinstance(pattern, str):
                for match in re.finditer(pattern, program):
                    value = match.group(0)
                    tokens.append((token_type, value))
        return tokens