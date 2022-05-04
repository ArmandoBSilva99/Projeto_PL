import re
import ply.lex as lex
from urllib3 import Retry

tokens = ['ID', 'STRING', 'PERC', "ER", "RETURN", "TOK", "RETELEM", "ERROR", "COMMENT", "LIST"]
literals = ['=', '(', ')', '[', ']', ',']
states = [("var", "exclusive"), ("func", "exclusive")]

def t_lex(t):
    r'%%\sLEX'
    print("LEX: " + t.value)
    #t.lexer.push_state("lex")

def t_yacc(t):
    r'%%\sYACC'
    print("YACC: " + t.value)
    #t.lexer.push_state("yacc")

def t_var_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    print("ID: " + t.value)
    return t

def t_var_STRING(t):
    r'\".*\"'
    print("STRING: " + t.value)
    t.lexer.begin("INITIAL")
    return t

def t_var_LIST(t):
    r'\[.*\]'
    print("LISTA: " + t.value)
    t.lexer.begin("INITIAL")
    return t

#def t_PERC(t):
#    r'%'
    #t.lexer.push_state("var")
#    print("PERC: " + t.value)
#    return t
    
def t_PERC(t):
    r'%'
    t.lexer.begin("var")
    print("PERC: " + t.value)
    return t

def t_COMMENT(t):
    r'\#.*'
    print("COMMENT: " + t.value)
    return t

def t_ER(t): #isto fica estranho pq pode ser qualquer coisa
    r'[^\s]+'
    print("ER: " + t.value)
    t.lexer.begin("func")
    return t

def t_func_RETURN(t):
    r'return\('
    print("RETURN: " + t.value)
    return t

def t_func_RETELEM(t):
    r'[a-zA-Z\(\)\.]+\)'
    print("RETELEM: " + t.value)
    t.lexer.begin("INITIAL")
    return t

def t_func_TOK(t):
    r'[a-zA-Z]+'
    print("TOK: " + t.value)
    return t


#def t_TOK(t):
    #?
#    pass

#def t_RET_ELEM(t):
    #????
#    pass

def t_ERROR(t):
    r'error'
    print("ERROR: " + t.value)
    return t

t_ignore = " \t\n\r"
t_var_ignore = " \t\n\r"
t_func_ignore = " \t\n\r,'"

#def t_lex_error(t):
#    print("Illegal character: ", t.value[0])
#    t.lexer.skip(1)

def t_var_error(t):
    print("Illegal character: ", t.value[0])
    t.lexer.skip(1)   

def t_error(t):
    print("Illegal character: ", t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
file = open("grammar.txt")
for line in file:
    lexer.input(line)
    for tok in lexer:
        pass

