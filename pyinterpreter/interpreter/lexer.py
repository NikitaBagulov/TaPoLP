from .token import Token, TokenType

class Lexer():

    def __init__(self):
        self._pos = 0
        self._text = ""
        self._current_char = None

    def init(self, text):
        self._text = text
        self._pos = 0
        self._current_char = self._text[self._pos]


    def forward(self):
        self._pos += 1
        if self._pos > len(self._text) - 1:
            self._current_char = None
        else:
            self._current_char = self._text[self._pos]

    def skip(self):
        while (self._current_char is not None and 
               self._current_char.isspace()):
            self.forward()

    def number(self):
        result  = []
        while (self._current_char is not None and 
               (self._current_char.isdigit() or
                self._current_char == ".")):
            result.append(self._current_char)
            self.forward()
        return "".join(result)

    def variable(self):
        result = []
        while self._current_char is not None and (self._current_char.isalpha() or
                self._current_char == "_" or self._current_char.isdigit()):
            result.append(self._current_char)
            self.forward()
        return "".join(result)

    def assignment(self):
        while self._current_char:
            self.forward()
            if self._current_char.isspace():
                self.skip()
                continue
            if self._current_char == "=":
                self.forward()
                return ":="
            raise SyntaxError("bad token")

    def next(self):
        while self._current_char:
            if self._current_char.isspace():
                self.skip()
                continue
            if self._current_char.isdigit():
                num = self.number()
                if self._current_char is None or \
                    (self._current_char != '_' and not(self._current_char.isalpha())):
                    return Token(TokenType.NUMBER, num)
            if self._current_char in ["+", "-", "/", "*"]:
                op = self._current_char
                self.forward()
                return Token(TokenType.OPERATOR, op)
            if self._current_char == "(":
                op = self._current_char
                self.forward()
                return Token(TokenType.LPAREN, op)
            if self._current_char == ")":
                op = self._current_char
                self.forward()
                return Token(TokenType.RPAREN, op)
            if self._current_char == ":":
                return Token(TokenType.ASSIGNMENT, self.assignment())
            if self._current_char == ";":
                semicolon = self._current_char
                self.forward()
                return Token(TokenType.SEMICOLON, semicolon)
            if self._current_char == "B":
                while self._current_char and self._current_char in list("BEGIN"):
                    self.forward()
                return Token(TokenType.BEGIN, "BEGIN")
            if self._current_char == "E":
                while self._current_char and self._current_char in list("END"):
                    self.forward()
                return Token(TokenType.END, "END")
            if self._current_char == ".":
                return Token(TokenType.DOT, self._current_char)
            if self._current_char.isalpha() or self._current_char == "_":
                return Token(TokenType.IDENTIFIER, self.variable())
            
            raise SyntaxError("bad token")
