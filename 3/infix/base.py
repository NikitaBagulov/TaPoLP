def is_operator(token):
    return token in ['+', '-', '*', '/']

def to_infix(expression):
    tokens = expression.split()
    stack = []

    for token in reversed(tokens):
        if token.isdigit():
            stack.append(token)
        elif is_operator(token):
            if len(stack) < 2:
                raise ValueError("Недостаточно операндов для оператора")
            operand1 = stack.pop()
            operand2 = stack.pop()
            infix_expr = f"({operand1} {token} {operand2})"
            stack.append(infix_expr)
        else:
            raise ValueError("Недопустимый токен: {}".format(token))

    if len(stack) != 1:
        raise ValueError("Недопустимое выражение")

    return stack[0]


