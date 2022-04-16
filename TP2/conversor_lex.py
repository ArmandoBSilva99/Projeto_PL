import ply.lex as lex

tokens = ['VAR','NUMBER']
literals = "+-/*=()"

def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

t_ignore = " \t\n\r"

def t_error(t):
    print("Illegal character: ", t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

