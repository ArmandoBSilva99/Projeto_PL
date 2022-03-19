import re
import sys
from turtle import position
from typing import Tuple

#ER = r'"a[0-9]+","[A-Za-z éáçãíÉÁÇÃÍóô\-âï]+","[A-Z]+"[,\d]+\n'
#ER = r'(\w+{\d,*\d*}:*:*\w*)|([a-zA-Zú]+)'

def head_reader(header):
    #aggregation e.g. Notas{4,5}

    things = re.findall(r'(\w+{\d,*\d*}:*:*\w*)|([a-zA-Zú]+)',header) #adicionar maia acentos?
    print(things)
    return things
    
def converter(lines, headers):
    result = "[\n"
    i = 0
    for line in lines:
        result += "\t{\n"
        j = 0
        l = re.split(',',line)
        for h in headers:
            if (h[0]) == '': header = h[1]
            else: header = h[0]
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
aggregatedOperations = aggregatedcategories = normalCategories = []
header = head_reader(lines[0])
result = converter(lines[1:], header)
f = open("result.json","w+")
f.write(result)
f.close()

