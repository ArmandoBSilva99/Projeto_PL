import re
import sys
from turtle import position

#ER = r'"a[0-9]+","[A-Za-z éáçãíÉÁÇÃÍóô\-âï]+","[A-Z]+"[,\d]+\n'

def head_reader(header, categories):
    #aggregation e.g. Notas{4,5}
    aggregatedcategories = re.findall(r'(\w+{[\d,]+}(::\w+)*|\w+{[\d,]+})', header)
    print("aggregated categories: ")
    print(aggregatedcategories)
    aggregation = re.sub(r'\w+{[\d,]+}(::\w+)*', r'',header)
    print("normal categories: ")
    print(aggregation)
    """
    if(aggregation):
        for cat in aggregation:
            categories.append( (re.findall(r'^\w+', cat)[0], re.findall(r'\d+', cat)) )
        print(categories)
    res = re.split(r',',header)
    """
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

f = open("teste.csv")
lines = f.read().splitlines()
f.close()
categories = []
header = head_reader(lines[0], categories) #HEADER
#result = converter(lines[1:], header)
#f = open("result.json","w+")
#f.write(result)
#f.close()

