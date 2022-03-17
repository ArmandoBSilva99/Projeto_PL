import re
import sys
from turtle import position

#ER = r'"a[0-9]+","[A-Za-z éáçãíÉÁÇÃÍóô\-âï]+","[A-Z]+"[,\d]+\n'

def head_reader(header):
    return re.split(r',',header)

def converter(lines, headers):
    result = "[\n"
    i = 0
    for line in lines:
        result += "\t{\n"
        j = 0
        l = re.split(',',line)
        for header in headers:
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

f = open("alunos.csv")
lines = f.read().splitlines()
f.close()
header = head_reader(lines[0]) #HEADER
result = converter(lines[1:], header)
f = open("result.json","w+")
f.write(result)
f.close()

