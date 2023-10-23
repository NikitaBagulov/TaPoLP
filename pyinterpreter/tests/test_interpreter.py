import pytest
from interpreter import Interpreter
from interpreter import Number, BinOp
from interpreter import Token, TokenType



@pytest.fixture(scope="function")
def interpreter():
    return Interpreter()

class TestInterpreter:
    interpreter = Interpreter()

    def test_add(self, interpreter):
        assert interpreter.eval("2+2") == 4
    
    def test_sub(self, interpreter):
        assert interpreter.eval("2-2") == 0

    def test_mult(self, interpreter):
        assert interpreter.eval("2*2") == 4
    
    def test_div(self, interpreter):
        assert interpreter.eval("2/2") == 1

    def test_priority(self, interpreter):
        assert interpreter.eval("2+2*2-100") == -94

    def test_parens(self, interpreter):
        assert interpreter.eval("(2+2)*2-100") == -92

    def test_token(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("2**2")
            interpreter.eval("2++2")

    def test_factor(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("1+1+")

    def test_expr(self, interpreter):
        assert interpreter.eval("2*2/2+2")==4

    def test_add_with_letter(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("2+a")
            interpreter.eval("t+2")

    def test_wrong_operator(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("2&3")

    @pytest.mark.parametrize(
            "interpreter, code", [(interpreter, "2 + 2"),
                                  (interpreter, "2 +2 "),
                                  (interpreter, " 2+2")]
    )
    def test_add_spaces(self, interpreter, code):
        assert interpreter.eval(code) == 4

class TestAst:

    def test_number_str(self):
        num = Number("1")
        assert num.__str__()=='Number (1)'

    def test_binop_str(self):
        binop = BinOp(Number(Token(TokenType.NUMBER, 1)), Token(TokenType.OPERATOR, "+"), Number (Token(TokenType.NUMBER, 1)))
        assert binop.__str__() == "BinOp+ (Number (Token(TokenType.NUMBER, 1)), Number (Token(TokenType.NUMBER, 1)))"

