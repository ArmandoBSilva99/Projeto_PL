import re
import sys

#ER = r'"a[0-9]+","[A-Za-z éáçãíÉÁÇÃÍóô\-âï]+","[A-Z]+"[,\d]+\n'
#ER = r'(\w+{\d,*\d*}:*:*\w*)|([a-zA-Zú]+)'

def head_reader(header):
    res = re.findall(r'([^,\n]+{\d,*\d*}:*:*\w*)|([^,\n]+)',header)
    return res

def read_line(line,headers):
    i = 0
    l = re.split(',',line)
    res = []
    for h in headers:
        if (h[0]) == '': header = h[1]
        else: header = h[0]
        print("header: " + header)
        if re.search(r'{\d}',header): #Listas com tamanho definido 
            it = int(re.findall(r'\d',header)[0])
            numbers = []
            while it > 0:
                numbers.append(l[i])
                i = i+1
                it = it-1
            res.append(numbers)
        elif re.search(r'{\d,\d}',header): #Listas com um intervalo de tamanhos
            it = int(re.findall(r'\d',header)[1])
            numbers = []
            while it > 0 and re.search('\d',l[i]): #falta tratar dos casos em q o número é menor do q o mínimo indicado no intervalo
                numbers.append(l[i])
                i = i+1
                it = it-1
            
            if re.search(r'::\w+',header):  #Funções de agregação
                op = re.findall(r':\w+',header)[0][1:]
                numbers = [int(num) for num in numbers]
                if op == "sum": op_res = sum(numbers)
                elif op == "media": op_res = sum(numbers)/len(numbers)
                res.append(str(op_res))

            else:
                numbers = "[" + ','.join(map(str, numbers)) + "]" 
                res.append(numbers)
        else: 
            res.append("\"" + l[i] + "\"")
            i = i + 1
    return res

def converter(lines, headers):
    result = "[\n"
    i = 0
    for line in lines:
        result += "\t{\n"
        j = 0
        l = read_line(line,headers)
        for h in headers:
            if (h[0]) == '': header = h[1]
            else: header = h[0]
            if re.search(r'{\d,*\d*}:*:*\w*',header):
                if re.search(r'::\w+',header):
                    two_headers = re.findall(r'[^{,}:\d]+',header)
                    header = two_headers[0] + "_" + two_headers[1]
                else: header = re.findall(r'\w+',header)[0]
            if (j == len(headers)-1):
                result += "\t\t"
                result += "\"" + header + "\": " + l[j] + "\n"
            else:
                result += "\t\t"
                result += "\"" + header + "\": " + l[j] + ",\n"
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
result = converter(lines[1:], header)
f = open("result.json","w+")
f.write(result)
f.close()

