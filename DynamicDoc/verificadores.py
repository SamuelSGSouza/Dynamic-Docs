import ast

def safe_eval(code,kwargs:dict={}) -> bool:
    # Converte a string da condição em uma expressão AST
    tree = ast.parse(code, mode='eval')
    
    # Verifica se a expressão contém apenas operações seguras
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and node.id not in list(kwargs.keys()):
            raise ValueError(f"Invalid variable found: {node.id}")

        elif not isinstance(node, (ast.Name,ast.Eq, ast.Expression, ast.Compare, ast.Constant, ast.BinOp, ast.UnaryOp, ast.BoolOp, ast.Lt, ast.LtE, ast.Gt, ast.GtE, ast.NotEq, ast.In, ast.NotIn, ast.Is, ast.IsNot, ast.And, ast.Or, ast.List,ast.Load)):
            raise ValueError(f"Insecure or unsupported operation found: {type(node).__name__}")
    # Avalia a expressão de forma segura
    return eval(code, {'__builtins__': None}, kwargs)

