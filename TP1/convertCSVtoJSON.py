from ast import operator
from curses.ascii import isdigit
import re
import sys
from unicodedata import numeric

headers = []
operations = []
intervals = []
defined_op = ["sum", "media", "min", "max"]

def head_reader(header):
    hs = re.findall(r'([^,\n]+{\d,*\d*}:*:*\w*)|([^,\n]+)',header)
    for h in hs:
        if (h[0]) == '': h = h[1]
        else: h = h[0]
        if re.search(r'{\d,*\d*}:*:*\w*',h):
            interval = re.findall(r'\d',h)
            
            #Error Handling dos intervalos
            if  (len(interval) == 1 and isdigit(interval[0])) or ( len(interval) == 2 and isdigit(interval[0]) and isdigit(interval[1]) and int(interval[0]) < int(interval[1]) ):
                intervals.append(interval)
            else:
                raise NameError("Intervalo inválido!\n")

            if re.search(r'::\w+',h):
                op = re.findall(r':\w+',h)[0][1:]
                
                #Error Handling das operações (Aceita operações escritas em maiúscula)
                if (str(op).lower() in defined_op):
                    operations.append(op)
                else: 
                    raise NameError("Operação inexistente!\n") 
                

                two_headers = re.findall(r'[^{,}:\d]+',h)
                headers.append(two_headers[0] + "_" + two_headers[1])
                
            else:
                name = re.findall(r'\w+',h)[0]
                headers.append(name)
                operations.append("list")

        else:
            headers.append(h)
            operations.append("none")
            intervals.append(0)

def read_line(line):
    i = 0
    l = re.split(',',line)
    res = []
    for j in range(0,len(headers)):
        elements = []
        if operations[j] != "none":
            if len(intervals[j]) == 1: #Listas com tamanho definido
                it = int(intervals[j][0])
                while it > 0:
                    
                    if i >= len(l) or not re.search(r'\w', l[i]):
                        raise NameError("Faltam elementos!\n")   
                    
                    elements.append(l[i])
                    i = i+1
                    it = it-1
            
                if i == len(l)-1 and not re.search(r'\n', l[i]):
                    raise NameError("Faltam elementos!\n")

            else: #Listas com um intervalo de tamanhos
                it = int(intervals[j][1]) 

                while it > 0: #falta tratar dos casos em q o número é menor do q o mínimo indicado no intervalo
                    
                    if i >= len(l):
                        raise NameError("Faltam elementos!\n")      
                    
                    if re.search(r'\w', l[i]):
                        elements.append(l[i])

                    i = i+1
                    it = it-1

                if i == len(l)-1 and not re.search(r'\n', l[i]):
                    raise NameError("Faltam elementos!\n")             
                
            if operations[j] != "list":  #Funções de agregação
                
                #Error handling Aggregation Function
                for elem in elements:
                    for digit in elem:
                        if not isdigit(digit):
                            raise NameError("Impossível aplicar função de agregassão!\n")

                elements = [int(num) for num in elements]
                if operations[j] == "sum": op_res = sum(elements)
                elif operations[j] == "media": op_res = sum(elements)/len(elements)
                elif operations[j] == "min": op_res = min(elements)
                elif operations[j] == "max": op_res = max(elements)
                res.append(str(op_res))

            else:
                elements = "[" + ','.join(map(str, elements)) + "]" 
                res.append(elements)
        
        else:
            res.append("\"" + l[i] + "\"")
            i = i+1
    return res 

def converter(lines):
    result = "[\n"
    i = 0
    for line in lines:
        result += "\t{\n"
        j = 0
        l = read_line(line)
        for h in headers:
            if (j == len(headers)-1):
                result += "\t\t"
                result += "\"" + h + "\": " + l[j] + "\n"
            else:
                result += "\t\t"
                result += "\"" + h + "\": " + l[j] + ",\n"
            j = j + 1
        if (i == len(lines)-1):
            result += "\t}\n"
        else:
            result += "\t},\n"
        i = i + 1
    result += "]\n"
    return result  

f = open("teste1.csv")
lines = f.read().splitlines()
f.close()
header = head_reader(lines[0])
result = converter(lines[1:])
f = open("result.json","w+")
f.write(result)
f.close()

