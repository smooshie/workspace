'''
Created on 12.6.2013

@author: lisagawr
'''

with open("testingText.txt", "r") as readFile:
    for line in readFile:
        part = line.split()
        print part[7]
        
#part[0] = contig name
#part[5] = start on reference
#part[6] = end on reference
#part[7] = orientation