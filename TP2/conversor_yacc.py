import ply.yacc as yacc
import sys

from conversor_lex import tokens
from conversor_lex import literals
from conversor_lex import states

def p_programa(p):
    'programa : vars funcs ers python' 
    p[0] = p[1] + p[2] + p[3] + p[3]

def p_vars_list(p):
    'vars : vars var'
    p[0] = p[1] + p[2]

def p_vars_empty(p):
    'vars : '
    p[0] = ''

def p_var_string(p):
    "var : PERC ID '=' STRING"
    p[0] = p[2] + '=' + p[4] + "\n"

def p_var_lista(p):
    "var : PERC ID '=' LISTA"
    p[0] = p[2] + '=' + p[4] + "\n"

def p_var_emptylista(p):
    "var : PERC ID '=' EMPTYLIST"
    p[0] = p[2] + '=' + p[4] + "\n"   

def p_var_yacc(p):
    "var : PERC ID '=' YACC"
    p[0] = p[2] + '=' + "yacc." + p[4] + "\n"     

def p_funcs_list(p):
    'funcs : funcs func'
    #p[0] = p[1] + p[2]

def p_funcs_empty(p):
    'funcs : '
    p[0] = ""

def p_func_list(p):
    'func : ER return'
    p[0] = p[2] + p[1]

def p_func_end(p):
    'func : END'
    p[0] = p[1]    

def p_return_ret(p):
    "return : RETURN '(' PAL ',' PAL ')'"
    p[0] = "def " + "t_" + p[3] + "(t):" + "\n"

def p_return_errorf(p):
    "return : ERROR '(' PAL STRING ',' PAL ')'"
    p[0] = "def t_error(t):\n\t" + p[3] + p[4] + "\n\t" + p[6] + "\n"   

def p_return_error(p):
    "return : ERROR '(' STRING ',' PAL ')'"
    p[0] = "def t_error(t):\n\t" + p[3] + "\n\t" + p[5] + "\n";    

def p_python_list(p):
    "python : python TEXT"
    p[0] = p[1] + p[2] + "\n\t"

def p_python_perc(p):
    "python : PERC"
    p[0] = p[1]          

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


def p_error(p):
    print("Erro sintático!")

parser = yacc.yacc()
parser.ts = {}

f = open('sintaxe.txt', 'r')

content = f.read()
result = parser.parse(content)

f.close()