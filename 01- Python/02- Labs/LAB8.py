import csv
Data = csv.reader(open("file.csv","r"))

Dict = {}

for line in Data :
    print(line[0],line[1],line[2])
    Dict[line[0]] = {'clk':line[1],'Type':line[2]}
    
print(Dict[line[0]])