
import re

KEYWORDS = {
    "analysis", "end", "load", "from", "with",
    "let", "keep", "where", "sort", "by",
    "asc", "desc", "show", "plot", "bar",
    "line", "if", "then", "otherwise",
    "done", "number", "text"
}

TOKEN_PATTERNS = [
    ("TEXT", re.compile(r'"[^"\r\n]*"')),
    ("NUMBER", re.compile(r'[0-9]{1,10}(?:\.[0-9]+)?')),
    ("IDENTIFIER", re.compile(r'[A-Za-z][A-Za-z0-9_]*')),
    ("OPERATOR", re.compile(r'==|!=|<=|>=|[=+\-*/<>]')),
    ("DELIMITER", re.compile(r'[(),.]')),
]

def scan(source):
    tokens = []
    symbols = {}
    errors = []

    for line_number, line in enumerate(source.splitlines(), 1):
        position = 0

        while position < len(line):
            char = line[position]

            if char.isspace():
                position += 1
                continue

            if char == "#":
                break

            if char == '"':
                match = TOKEN_PATTERNS[0][1].match(line, position)
                if not match:
                    errors.append(
                        f"Line {line_number}: Unclosed text literal"
                    )
                    break

            if char.isdigit():
                candidate = re.match(
                    r'[0-9][A-Za-z0-9_.]*',
                    line[position:]
                ).group()

                if not re.fullmatch(
                    r'[0-9]{1,10}(?:\.[0-9]+)?',
                    candidate
                ):
                    errors.append(
                        f"Line {line_number}: Malformed number {candidate}"
                    )
                    position += len(candidate)
                    continue

            if char.isalpha():
                candidate = re.match(
                    r'[A-Za-z][A-Za-z0-9_]*',
                    line[position:]
                ).group()

                if len(candidate) > 16:
                    errors.append(
                        f"Line {line_number}: Identifier too long: {candidate}"
                    )
                    position += len(candidate)
                    continue

            matches = []

            for token_type, pattern in TOKEN_PATTERNS:
                match = pattern.match(line, position)
                if match:
                    matches.append(
                        (len(match.group()), token_type, match.group())
                    )

            if matches:
                _, token_type, lexeme = max(
                    matches, key=lambda item: item[0]
                )

                if token_type == "IDENTIFIER":
                    lexeme = lexeme.lower()

                    if lexeme in KEYWORDS:
                        token_type = "KEYWORD"
                    elif lexeme not in symbols:
                        symbols[lexeme] = line_number

                tokens.append({
                    "Type": token_type,
                    "Line": line_number,
                    "Lexeme": lexeme
                })

                position += len(lexeme)
            else:
                errors.append(
                    f"Line {line_number}: Unknown symbol '{char}'"
                )
                position += 1

    return tokens, symbols, errors
