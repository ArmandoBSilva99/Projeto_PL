import ply.yacc as yacc
import sys

from conversor_lex import tokens
from conversor_lex import literals

def p_programa(p):
    'programa : lex' #yacc
    p[0] = p[1] + p[2]

def p_lex(p):
    'lex : vars funcs'
    p[0] = p[1] + p[2]

def p_vars_list(p):
    'vars : vars var'
    p[0] = p[1] + p[2]

def p_vars_empty(p):
    'vars : '
    p[0] = ''

def p_var_string(p):
    "var : PERC ID '=' STRING"
    p[0] = p[2] + '=' + p[4] #not sure

def p_var_lista(p):
    "var : PERC ID '=' lista"
    p[2] = p[4] #also not sure

def p_funcs_list(p):
    'funcs : funcs func'
    print("0")
    print(p[0])
    print("1")
    print(p[1])
    print("2")
    print(p[2])
    #p[0] = p[1] + p[2]

def p_funcs_empty(p):
    'funcs : '
    p[0] = ""

def p_func(p):
    'func : ER return'

def p_lista_elems(p) :
    "lista : '[' elementos ']'"

def p_lista_empty(p):
    'lista : '
    p[0] = ""

def p_elementos_tok(p):
    'elementos : TOK'
    p[0] = p[1]

def p_elementos_list(p):
    "elementos : TOK ',' elementos"
    p[0] = p[1] + p[3]

def p_return_elems(p):
    "return : RETURN '(' TOK ',' RET_ELEM ')'"
    p[0] = p[3] + p[5] #not sure

def p_return_error(p):
    "return : "
    #falta acabar

def p_error(p):
    print("Erro sintático!")

parser = yacc.yacc()
parser.ts = {}

f = open('sintaxe.txt', 'r')

content = f.read()
result = parser.parse(content)

f.close()

