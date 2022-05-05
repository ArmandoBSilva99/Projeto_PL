import re
import ply.lex as lex
from urllib3 import Retry

tokens = ['ID', 'STRING', 'PERC', "ER", "RETURN", "PAL", "RETELEM", "ERROR", "COMMENT", "LIST", "FUNCTIONS", "END", "EMPTYLIST", "EXP"]
literals = ['=', '(', ')', '[', ']', ',']
states = [("var", "exclusive"), ("func", "exclusive"), ("er", "exclusive")]

def t_lex(t):
    r'%%\sLEX'
    print("LEX: " + t.value)
    #t.lexer.begin("lex")

def t_yacc(t):
    r'%%\sYACC'
    print("YACC: " + t.value)
    #t.lexer.begin("yacc")

def t_functions(t):
    r'%%\sFUNCTIONS'
    print("FUNCTIONS: " + t.value)
    t.lexer.begin("func")

def t_ers(t):
    r'%%\sERS'
    print("ERS: " + t.value)
    t.lexer.begin("er")

def t_PERC(t):
    r'%'
    t.lexer.begin("var")
    print("PERC: " + t.value)
    return t

def t_COMMENT(t):
    r'\#.*'
    print("COMMENT: " + t.value)
    return t

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

def t_var_COMMENT(t):
    r'\#.*'
    print("COMMENT: " + t.value)
    return t

def t_var_EMPTYLIST(t):
    r'\{\}'
    print("EMPTYLIST: " + t.value)
    t.lexer.begin("INITIAL")
    return t

#def t_PERC(t):
#    r'%'
    #t.lexer.push_state("var")
#    print("PERC: " + t.value)
#    return t

def t_func_RETURN(t):
    r'return'
    print("RETURN: " + t.value)
    return t

def t_func_ERROR(t):
    r'error'
    print("ERROR: " + t.value)
    return t

def t_func_END(t):
    r'%%\sEND'
    print("END: " + t.value)
    t.lexer.begin("INITIAL")
    return t

def t_func_STRING(t):
    r'\".*\"'
    print("STRING: " + t.value)
    return t

def t_func_PAL(t):
    r'[a-zA-Z0-9\.\(\)]+'
    print("PAL: " + t.value)
    return t

def t_func_ER(t): 
    r'[^\s]+'
    print("ER: " + t.value)
    #t.lexer.begin("func")
    return t

def t_er_STRING(t):
    r'\".*\"'
    print("STRING: " + t.value)
    return t

def t_er_EXP(t):
    r'[^\}]+'
    print("EXP: " + t.value)
    return t

#def t_TOK(t):
    #?
#    pass

#def t_RET_ELEM(t):
    #????
#    pass


t_ignore = " \t\n\r"
t_var_ignore = " \t\n\r"
t_func_ignore = " \t\n\r,'()"
t_er_ignore = " \t\n\r}{"

#def t_lex_error(t):
#    print("Illegal character: ", t.value[0])
#    t.lexer.skip(1)

def t_var_error(t):
    print("Illegal character: ", t.value[0])
    t.lexer.skip(1)

def t_func_error(t):
    print("Illegal character: ", t.value[0])
    t.lexer.skip(1) 

def t_er_error(t):
    print("Illegal character: ", t.value[0])
    t.lexer.skip(1) 

def t_error(t):
    print("Illegal character: ", t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
file = open("sintaxe.txt")
for line in file:
    lexer.input(line)
    for tok in lexer:
        pass

