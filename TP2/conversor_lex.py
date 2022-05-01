import re
import ply.lex as lex
from urllib3 import Retry

tokens = ['ID', 'STRING', 'PERC', "ER", "SPACE", "RETURN", "TOK", "RET_ELEM", "ERROR"]
literals = ['=', '(', ')', '[', ']', ',']
states = [("lex", "exclusive"), ("yacc", "exclusive"), ("var", "inclusive"), ("func", "inclusive")]

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_STRING(t):
    r'".+"'
    return t

def t_PERC(t):
    r'%'
    #t.lexer.push_state("var")
    return t
    
def t_var_PERC(t):
    r'^%[a-z]*'
    #t.lexer.push_state("var")
    return t

def t_ER(t): #isto fica estranho pq pode ser qualquer coisa
    r'.+'
    return t

def t_SPACE(t):
    r' '
    return t

def t_RETURN(t):
    r'return'
    return t

def t_TOK(t):
    #?
    pass

def t_RET_ELEM(t):
    #????
    pass

def t_ERROR(t):
    r'error'
    return t

def t_lex(t):
    r'%% LEX'
    t.lexer.push_state("lex")

def t_yacc(t):
    r'%% YACC'
    t.lexer.push_state("yacc")

t_ignore = " \t\n\r"

def t_lex_error(t):
    print("Illegal character: ", t.value[0])
    t.lexer.skip(1)

def t_yacc_error(t):
    print("Illegal character: ", t.value[0])
    t.lexer.skip(1)   

def t_error(t):
    print("Illegal character: ", t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

