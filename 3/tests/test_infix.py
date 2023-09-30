import pytest
from infix import is_operator, to_infix


@pytest.mark.parametrize(
        "token, res",
        [("+", True),
         ("a", False),
         (1, False)]
)
def test_is_operator(token, res):
    assert is_operator(token) == res

@pytest.mark.parametrize(
        "expression, res",
        [("+ 1 2", "(1 + 2)"),
         ("+ + 1 2 3", "((1 + 2) + 3)")
        ]        
)

def test_to_infix(expression, res):
    with pytest.raises(ValueError):
        to_infix("+ + 1")
    with pytest.raises(ValueError):
        to_infix("++ 1 1")
    with pytest.raises(ValueError):
        to_infix("")
    assert to_infix(expression) == res