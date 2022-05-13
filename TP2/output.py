import ply.lex as lex

literals = "+-/*=()" ## a single char
ignore = " \t\n" 
tokens = [ 'VAR','NUMBER' ] 

def t_VAR(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	t.value = t.value
	return t

def t_NUMBER(t):
	r'\d+(\.\d+)?'
	t.value = float(t.value)
	return t

def t_error(t):
	print(f"Illegal character '{t.value[0]}', [{t.lexer.lineno}]")
	t.lexer.skip(1)

lexer = lex.lex()


import ply.yacc as yacc

precedence = [ ('left','+','-'), ('left','*','/'), ('right','UMINUS'), ] 
# symboltable : dictionary of variables
ts = {} 

def p_stat_1(t):
	"stat : VAR '=' exp"
	ts[t[1]] = t[3] 

def p_stat_2(t):
	"stat : exp"
	print(t[1]) 

def p_exp_1(t):
	"exp : exp '+' exp"
	t[0] = t[1] + t[3] 

def p_exp_2(t):
	"exp : exp '-' exp"
	t[0] = t[1] - t[3] 

def p_exp_3(t):
	"exp : exp '*' exp"
	t[0] = t[1] * t[3] 

def p_exp_4(t):
	"exp : exp '/' exp"
	t[0] = t[1] / t[3] 

def p_exp_5(t):
	"exp : '-' exp %prec UMINUS"
	t[0] = -t[2] 

def p_exp_6(t):
	"exp : '(' exp ')'"
	t[0] = t[2] 

def p_exp_7(t):
	"exp : NUMBER"
	t[0] = t[1] 

def p_exp_8(t):
	"exp : VAR"
	t[0] = getval(t[1]) 

def p_error(t):
	print(f"Syntax error at '{t.value}', [{t.lexer.lineno}]")

def getval(n):
	if n not in ts: print(f"Undefined name '{n}'")
	return ts.get(n,0)

y = yacc.yacc()
 
y.parse("3+4*7")
