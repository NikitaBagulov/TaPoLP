from .parser import Parser
from .ast import Number, BinOp, UnOp, Variable, Assignment, Semicolon

class NodeVisitor:
    
    def visit(self):
        pass

class Interpreter(NodeVisitor):
    
    def __init__(self):
        self.parser = Parser()
        self.variables = {}

    def visit(self, node):
        if isinstance(node, Number):
            return self.visit_number(node)
        elif isinstance(node, BinOp):
            return self.visit_binop(node)
        elif isinstance(node, UnOp):
            return self.visit_unop(node)
        elif isinstance(node, Variable):
            return self.visit_variable(node)
        elif isinstance(node, Assignment):
            return self.visit_assignment(node)
        elif isinstance(node, type(None)):
            return None
        elif isinstance(node, Semicolon):
            return self.visit_semicolon(node)
       
        
    def visit_number(self, node):
        return float(node.token.value)

    def visit_binop(self, node):
        match node.op.value:
            case "+":
                return self.visit(node.left) + self.visit(node.right)
            case "-":
                return self.visit(node.left) - self.visit(node.right)
            case "*":
                return self.visit(node.left) * self.visit(node.right)
            case "/":
                return self.visit(node.left) / self.visit(node.right)
            
            case _:
                raise ValueError("Invalid operator")

    def visit_unop(self, node):
        match node.op.value:
            case "+":
                return self.visit(node.number)
            case "-":
                return self.visit(node.number)*(-1)
            case _:
                raise ValueError("Invalid operator")

    def visit_variable(self, node):
        print(node)
        variable_name = node.name.value
        if variable_name in self.variables.keys():
            return self.variables[variable_name]
        raise ValueError(f"Variable '{variable_name}' not defined")
        
    def visit_assignment(self, node):
        if node.variable.value not in self.variables.keys():
            self.variables[node.variable.value] = 0
        self.variables[node.variable.value] = self.visit(node.data)

    def visit_semicolon(self, node):
        print(node)
        self.visit(node.left)
        self.visit(node.right)

    def eval(self, code):
        tree = self.parser.parse(code)
        self.visit(tree)
        return self.variables

