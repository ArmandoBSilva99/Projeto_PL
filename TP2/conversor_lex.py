import re
import ply.lex as lex
from urllib3 import Retry

tokens = ['LEX', 'YACC', 'FUNCTIONS', 'ERS', "COMMENT", 'ID', 'STRING', 'PERC', "ER", "RETURN", "PAL", "ERROR", "LIST", "END", "EMPTYLIST", "EXP", "TEXT", "PYTHON", "PONTO", "DEF", "VCOMMENT"]
literals = ['=', '(', ')', '[', ']', ',']
states = [("var", "exclusive"), ("func", "exclusive"), ("er", "exclusive"), ("python", "exclusive")]

def t_LEX(t):
    r'%%\sLEX'
    ##print("LEX: " + t.value)
    return t

def t_YACC(t):
    r'%%\sYACC'
    #print("YACC: " + t.value)
    return t

def t_FUNCTIONS(t):
    r'%%\sFUNCTIONS'
    #print("FUNCTIONS: " + t.value)
    t.lexer.begin("func")
    return t

def t_ERS(t):
    r'%%\sERS'
    #print("ERS: " + t.value)
    t.lexer.begin("er")
    return t

def t_VCOMMENT(t):
    r'\#{2}.*'
    #print("VAR_COMMENT: " + t.value)
    return t

def t_COMMENT(t):
    r'\#.*'
    #print("COMMENT: " + t.value)
    return t

def t_PERC(t):
    r'%'
    t.lexer.begin("var")
    #print("PERC: " + t.value)
    return t

def t_var_YACC(t):
    r'yacc\(\)'
    #print("YACC: " + t.value)
    t.lexer.begin("python")
    return t      

def t_var_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    #print("ID: " + t.value)
    return t    

def t_var_STRING(t):
    r'\".*\"'
    #print("STRING: " + t.value)
    t.lexer.begin("INITIAL")
    return t
    
def t_var_LIST(t):
    r'\[.*\]'
    #print("LIST: " + t.value)
    t.lexer.begin("INITIAL")
    return t

def t_var_EMPTYLIST(t):
    r'\{\}'
    #print("EMPTYLIST: " + t.value)
    t.lexer.begin("INITIAL")
    return t
  
def t_func_RETURN(t):
    r'return'
    #print("RETURN: " + t.value)
    return t

def t_func_ERROR(t):
    r'error'
    #print("ERROR: " + t.value)
    return t

def t_func_YACC(t):
    r'%%\sYACC'
    #print("END: " + t.value)
    t.lexer.begin("INITIAL")
    return t

def t_func_STRING(t):
    r'\".*\"'
    #print("STRING: " + t.value)
    return t

def t_func_PONTO(t):
    r'\.'
    return t

def t_func_PAL(t):
    r'[a-zA-Z0-9\.\(\)]+'
    #print("PAL: " + t.value)
    return t

def t_func_ER(t): 
    r'[^\s]+'
    #print("FUNC_ER: " + t.value)
    return t

def t_er_STRING(t):
    r'\".*\"'
    #print("STRING: " + t.value)
    return t

def t_er_PYTHON(t):
    r'%%\sPYTHON'
    #print("PYTHON BEGIN: " + t.value)
    t.lexer.begin("python")
    return t 

def t_er_EXP(t):
    r'[^\}\"\:]+'
    #print("EXP: " + t.value)
    return t

def t_python_END(t):
    r'%%'
    #print("END: " + t.value)
    t.lexer.begin("INITIAL")
    return t

def t_python_PERC(t):
    r'%'
    #print("PYTHON PERC: " + t.value)
    t.lexer.begin("var")
    return t

def t_python_DEF(t):
    r'def.+'
    return t

def t_python_TEXT(t):
    r'.+'
    #print("TEXT: " + t.value)
    return t    

t_ignore = " \t\n\r"
t_var_ignore = " \t\n\r"
t_func_ignore = " \t\n\r,'()"
t_er_ignore = " \t\n\r}{:"
t_python_ignore = " \t\n\r"

def t_var_error(t):
    print("Illegal character: ", t.value[0])
    t.lexer.skip(1)

def t_func_error(t):
    print("Illegal character: ", t.value[0])
    t.lexer.skip(1) 

def t_er_error(t):
    print("Illegal character: ", t.value[0])
    t.lexer.skip(1) 

def t_python_error(t):
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

