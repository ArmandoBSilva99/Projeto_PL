import ply.yacc as yacc
import sys

from conversor_lex import tokens
from conversor_lex import literals

precedence = [('left','+','-'),
              ('left','*','/'),
              ('right','UMINUS'),]

def p_stat_atrib(p):
    "stat : VAR '=' exp"
    parser.ts[p[1]] = p[3]

def p_stat_exp(p):
    "stat : exp"
    print(p[1])

def p_exp_add(p):
    "exp : exp '+' exp"
    p[0] = p[1] + p[3]

def p_exp_sub(p):
    "exp : exp '-' exp"
    p[0] = p[1] - p[3]

def p_exp_mul(p):
    "exp : exp '*' exp"
    p[0] = p[1] * p[3]

def p_exp_div(p):
    "exp : exp '/' exp"
    p[0] = p[1] / p[3]

def p_exp_uminus(p):
    "exp : '-' exp %prec UMINUS"
    p[0] = -p[2]

def p_exp_par(p):
    "exp : '(' exp ')'"
    p[0] = p[2]

def p_exp_NUMBER(p):
    "exp : NUMBER"
    p[0] = p[1]

def p_exp_VAR(p):
    "exp : VAR"
    var = p[1]
    if var in parser.ts:
        p[0] = parser.ts[var]
    else:
        print("Variável '{var}' não definida!")
        exit()

def p_error(p):
    print("Erro sintático!")

parser = yacc.yacc()
parser.ts = {}

for line in sys.stdin:
    parser.parse(line)
