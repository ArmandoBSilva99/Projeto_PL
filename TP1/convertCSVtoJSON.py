from ast import operator
import re
import sys
from unicodedata import numeric

headers = []
operations = []
intervals = []

def head_reader(header):
    hs = re.findall(r'([^,\n]+{\d,*\d*}:*:*\w*)|([^,\n]+)',header)
    for h in hs:
        if (h[0]) == '': h = h[1]
        else: h = h[0]
        if re.search(r'{\d,*\d*}:*:*\w*',h):
            if re.search(r'::\w+',h):
                two_headers = re.findall(r'[^{,}:\d]+',h)
                headers.append(two_headers[0] + "_" + two_headers[1])
                op = re.findall(r':\w+',h)[0][1:]
                operations.append(op)
            else:
                name = re.findall(r'\w+',h)[0]
                headers.append(name)
                operations.append("list")
            interval = re.findall(r'\d',h)
            intervals.append(interval)
        else:
            headers.append(h)
            operations.append("none")
            intervals.append(0)

def read_line(line):
    i = 0
    l = re.split(',',line)
    res = []
    for j in range(0,len(headers)):
        numbers = []
        if operations[j] != "none":
            if len(intervals[j]) == 1: #Listas com tamanho definido
                it = int(intervals[j][0])
                while it > 0:
                    numbers.append(l[i])
                    i = i+1
                    it = it-1
            else: #Listas com um intervalo de tamanhos
                it = int(intervals[j][1])
                while it > 0 and re.search('\d',l[i]): #falta tratar dos casos em q o número é menor do q o mínimo indicado no intervalo
                    numbers.append(l[i])
                    i = i+1
                    it = it-1
                i = it + i

            if operations[j] != "list":  #Funções de agregação
                numbers = [int(num) for num in numbers]
                if operations[j] == "sum": op_res = sum(numbers)
                elif operations[j] == "media": op_res = sum(numbers)/len(numbers)
                elif operations[j] == "min": op_res = min(numbers)
                elif operations[j] == "max": op_res = max(numbers)
                res.append(str(op_res))

            else:
                numbers = "[" + ','.join(map(str, numbers)) + "]" 
                res.append(numbers)
        
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

f = open("teste.csv")
lines = f.read().splitlines()
f.close()
header = head_reader(lines[0])
result = converter(lines[1:])
f = open("result.json","w+")
f.write(result)
f.close()

