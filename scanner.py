
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

def check_number(value):
    return re.fullmatch(r'[0-9]{1,10}(?:\.[0-9]+)?',value) is not None

def check_identifier(name):
    return len(name) <= 16

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
            #checking text
            if char == '"':
                text_match = re.match(TOKEN_PATTERNS[0][1] , line[position:])
                if text_match is None : 
                    errors.append( f"Line {line_number}: Unclosed text literal" )
                    break
            
            #checking num
            if char in "0123456789":
                number_match = re.match( r'[0-9][A-Za-z0-9_.]*', line[position:])
                word=number_match.group()

                if not check_number(word):
                    errors.append( f"Line {line_number}: Malformed number {word}")
                    position += len(word)
                    continue
            #checking idn
            if char.isalpha() and char.isascii():
                name_match = re.match(  r'[A-Za-z][A-Za-z0-9_]*', line[position:] )
                word=name_match.group()

                if not check_identifier(word):
                    errors.append(  f"Line {line_number}: Identifier too long: {word}" )
                    position += len(word)
                    continue

            #find token
            token_type = None
            lexeme = ""

            for current_type, pattern in TOKEN_PATTERNS:
                match = re.match(pattern, line[position:])

                if match and len(match.group())>len(lexeme):
                    token_type = current_type
                    lexeme = match.group()

            if token_type is None :
                errors.append(f"Line {line_number}: Unknown symbol: {char}")
                position += 1
                continue

            # tables
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
          
    return tokens, symbols, errors
