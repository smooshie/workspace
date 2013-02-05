'''
Created on 1.2.2013

@author: lisagawr
'''
from itertools import islice

def window(seq, n):            
    it = iter(seq)
    result = tuple(islice(it, n))
    #if len(result) == n:
        #yield result
    for elem in it:
        result = result[1:] + (elem,)
        print result

def main():
    sorted = open("coverage_mapped.txt", "r")
    sorted12 = open("coverage_mapped12.txt", "r")
    
    sorteds = []
    sortedp = []
    
    for line in sorted:
        part = line.split()
        sorteds.append(part[2])
    
    for line in sorted12:
        part = line.split()
        sortedp.append(part[2])
        
    window(sorteds, 1000) # 1000bp window

main()