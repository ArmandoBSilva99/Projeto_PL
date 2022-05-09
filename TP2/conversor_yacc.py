import ply.yacc as yacc
import sys

from conversor_lex import tokens
from conversor_lex import literals
from conversor_lex import states

def p_programa(p):
    'programa : vars FUNCTION' 
    p[0] = "import ply.lex as lex\n" + p[1]
    
def p_vars_empty(p):
    'vars : '
    p[0] = ''

def p_vars_var(p):
    'vars : vars var'
    p[0] = p[1] + p[2]
    parser.output += p[0]

def p_var_string(p):
    "var : PERC ID '=' STRING comments"
    p[0] = p[2] + '=' + p[4] + "\t" + p[5] + "\n"
    #print(p[0])

def p_var_lista(p):
    "var : PERC ID '=' LIST comments"
    p[0] = p[2] + '=' + p[4] + "\t" + p[5] + "\n"
    #print(p[0])

def p_var_emptylista(p):
    "var : PERC ID '=' EMPTYLIST comments"
    p[0] = p[2] + '=' + p[4] + "\t" + p[5] + "\n"
    #print(p[0])

def p_var_yacc(p):
    "var : PERC ID '=' YACC comments"
    p[0] = p[2] + '=' + "yacc." + p[4] + "\t" + p[5] + "\n" 
    #print(p[0]) 

def p_var_empty(p):
    "var : "
    p[0] = ''    

def p_functions_empty(p):
    'functions : '
    p[0] = '' 

def p_functions_funcs(p):
    'functions : FUNCTION funcs'
    p[0] = p[1] + p[2]
    ##print(p[0])

def p_funcs_empty(p):
    'funcs : '
    p[0] = ''

def p_funcs_list(p):
    'funcs : funcs func comments'
    p[0] = p[1] + p[2] + p[3]    

def p_func_ret(p):
    "func : ER RETURN '(' PAL ',' PAL ')'"
    p[0] = "def " + "t_" + p[4] + "(t):" + "\n" + f"r'{p[1]}'\n" + f"{p[2]} {p[6]}\n"
    #print(p[0])

def p_func_errorf(p):
    "func : ERROR '(' PAL STRING ',' PAL ')'"
    p[0] = "def t_error(t):\n\t" + p[3] + p[4] + "\n\t" + p[6] + "\n" 
    #print(p[0])

def p_func_error(p):
    "func : ERROR '(' STRING ',' PAL ')'"
    p[0] = "def t_error(t):\n\t" + p[3] + "\n\t" + p[5] + "\n"  
    #print(p[0])

def p_func_end(p):
    'func : END'
    p[0] = ''     
"""
def p_python_perc(p):
    "python : PERC"
    p[0] = ''

def p_python_list(p):
    "python : python TEXT comments"
    p[0] = p[1] + "\n\t" + p[2]
    #print(p[0])     

def p_ers_empty(p):
    "ers : "
    p[0] = ''

def p_ers_er(p):
    "ers : ers er comments"
    p[0] = p[1] + p[2] + p[3]
    ##print(p[0])

def p_er_e(p):
    "er : EXP ':' STRING '{' EXP '}'"
    p[0] = f"def p_{p[1]}(p):\n\t" + f"\"{p[3]}\n\t{p[5]}\n"
    #print(p[0])
"""
def p_comments_empty(p):
    "comments : "
    p[0] = ''

def p_comments_list(p):
    "comments : comments com"
    p[0] = p[1] + p[2]


def p_error(p):
    print("Erro sintático!")
    #print(p)


parser = yacc.yacc()
parser.output = ""
f = open('sintaxe2.txt', 'r')

content = f.read()
result = parser.parse(content)
print("HERE WE GO")
print(parser.output)

f.close()