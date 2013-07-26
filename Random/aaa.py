'''
Created on 12.6.2013

@author: lisagawr
'''
store = []
star = False
temp = ""

with open("testixi.txt", "r") as readFile:
    for line in readFile:
        line = line.rstrip()
        if line == "*" and star == False:
            star = True
        elif line == "*" and star == True:
            store.append(temp)
            temp = ""
            star = False
        elif star == True and line != "*" and len(line) > 1:
            if "query" in line or "contig" in line or "target" in line:
                temp += line
            else:
                temp += line.upper()

for each in store:
        part = each.split()
        if len(part) != 15:
            print "Erronous read."
            print each
            pass
    
#part[0] = contig name
#part[5] = start on reference
#part[6] = end on reference
#part[7] = orientation
#part[10] = mm
#part[11] = ">query"
#part[12] = query sequence
#part[13] = ">target"
#part[14] = target sequence