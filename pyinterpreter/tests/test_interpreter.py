import pytest
from interpreter import Interpreter
from interpreter import Number, BinOp, UnOp, Variable, Assignment, Semicolon
from interpreter import Token, TokenType



@pytest.fixture(scope="function")
def interpreter():
    return Interpreter()

class TestInterpreter:
    interpreter = Interpreter()

    def test_token(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("1-=-1")
    def test_check_token(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("(2+1")

    def test_binop(self, interpreter):
        with pytest.raises(ValueError):
            interpreter.visit_binop(BinOp(Number(Token(TokenType.NUMBER, 2)), Token(TokenType.OPERATOR, "^"), Number(Token(TokenType.NUMBER, 3))))

    def test_unop(self, interpreter):
        assert interpreter.eval("BEGIN x:=1++++1 END.") == {"x":2}
        assert interpreter.eval("BEGIN x:=1----1 END.") == {"x":2}

    def test_wrong_unop(self, interpreter):
        with pytest.raises(ValueError):
            interpreter.visit_unop(UnOp(Token(TokenType.OPERATOR, "^"), Number(Token(TokenType.NUMBER, 3))))

    def test_assign(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("BEGIN   b:   -1 END.")

    def test_bad_token(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("BEGIN a:3END.")

    def test_visit_variable(self, interpreter):
        with pytest.raises(ValueError):
            interpreter.eval("BEGIN x:=y END.")

    def test_invalid_factor(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.parser.factor()

    def test_invalid_token_order(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("x")
    def test_factor(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("1+-")

    def test_add_with_letter(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("2+a")

    def test_wrong_operator(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("2&3")

    def test_empty(self, interpreter):
        assert interpreter.eval("BEGIN END.") == {}
    def test_easy(self, interpreter):
        assert interpreter.eval("BEGIN x:= 2 + 3 * (2 + 3); y:= 2 / 2 - 2 + 3 * ((1 + 1) + (1 + 1)); END.") == {'x': 17.0, 'y': 11.0}
    def test_medium(self, interpreter):
        assert interpreter.eval("BEGIN y:= 2; BEGIN a := 3; a := a; b := 10 + a + 10 * y / 4; c := a - b; END; x := 11; END.") == {'x': 11.0, 'y': 2.0, 'a': 3.0, 'b': 18.0, 'c': -15.0}

class TestAst:

    def test_number_str(self):
        num = Number("1")
        assert num.__str__()=='Number (1)'

    def test_binop_str(self):
        binop = BinOp(Number(Token(TokenType.NUMBER, 1)), Token(TokenType.OPERATOR, "+"), Number (Token(TokenType.NUMBER, 1)))
        assert binop.__str__() == "BinOp+ (Number (Token(TokenType.NUMBER, 1)), Number (Token(TokenType.NUMBER, 1)))"

    def test_unop_str(self):
        unop = UnOp(Token(TokenType.OPERATOR, "-"), Number(Token(TokenType.NUMBER, 1)))
        assert unop.__str__() == "UnOp-Number (Token(TokenType.NUMBER, 1))"

    def test_var_str(self):
        variable = Variable("x")
        assert variable.__str__() == "Variable(x)"

    def test_assign_str(self):
        assign = Assignment(Variable("x"), Number(Token(TokenType.NUMBER, 1)))
        assert assign.__str__() == "AssignmentVariable(x):=Number (Token(TokenType.NUMBER, 1))"

    def test_semicolon_str(self):
        semicol = Semicolon(Variable("x"), Variable("y"))
        assert semicol.__str__() == "Semicolon (Variable(x), Variable(y))"


