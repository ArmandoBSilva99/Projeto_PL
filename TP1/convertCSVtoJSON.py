import re
import sys

#ER = r'"a[0-9]+","[A-Za-z éáçãíÉÁÇÃÍóô\-âï]+","[A-Z]+"[,\d]+\n'


def head_reader(header):
    return header


def converter(lines, headers):
    result = "[\n"
        


f = open("alunos.csv")
lines = f.read()

header = head_reader(lines.splitlines()[0]) #HEADER

converter(lines, header)
