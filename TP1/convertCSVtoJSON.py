from ast import operator
import re
import sys
from turtle import position
from typing import Tuple

#ER = r'"a[0-9]+","[A-Za-z éáçãíÉÁÇÃÍóô\-âï]+","[A-Z]+"[,\d]+\n'
#ER = r'(\w+{\d,*\d*}:*:*\w*)|([a-zA-Zú]+)'

def head_reader(header):
    #aggregation e.g. Notas{4,5}

    things = re.findall(r'(\w+{\d,*\d*}:*:*\w*)|([a-zA-Zú]+)',header) #adicionar mais acentos?
    print(things)
    return things

def read_line(line,headers):
    i = 0
    l = re.split(',',line)
    res = []
    for h in headers:
        if (h[0]) == '': header = h[1]
        else: header = h[0]
        print("header: " + header)
        if re.search(r'{\d}',header): 
                it = int(re.findall(r'\d',header)[0])
                header = re.search(r'\w+',header)
                numbers = []
                while it > 0:
                    numbers.append(l[i])
                    i = i+1
                    it = it-1
                res.append(numbers)
        else: 
            res.append(l[i])
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
            if (j == len(headers)-1):
                result += "\t\t"
                if isinstance(l[j],list):
                    l[j] = ','.join(map(str, l[j]))
                    result += "\"" + header + "\": " + "[" + l[j] + "]\n"
                else: result += "\"" + header + "\": " + "\"" + l[j] + "\"\n"
            else:
                result += "\t\t"
                if isinstance(l[j],list):
                    l[j] = ','.join(map(str, l[j]))
                    result += "\"" + header + "\": " + "[" + l[j] + "],\n"
                else: result += "\"" + header + "\": " + "\"" + l[j] + "\",\n"
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
aggregatedOperations = aggregatedcategories = normalCategories = []
header = head_reader(lines[0])
#res = read_line("7777,Cristiano Ronaldo,Desporto,17,12,20,11,12",header)
#print(res)
result = converter(lines[1:], header)
f = open("result.json","w+")
f.write(result)
f.close()

