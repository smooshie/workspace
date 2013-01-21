'''
Created on 21.1.2013

@author: lisagawr
'''

def rc(reversable):
    complement = { "A" : "T", "T" : "A", "C" : "G", "G" : "C"}
    result = [] 
    for i in reversed(reversable): 
        result.append(complement[i])
    
    return ''.join(result)

def main():
    readflags = {}
    
    reads = open("batman_reads.fq", "w")
    
    with open('batman.sam', 'r') as matesw:
        for line in matesw:
            line.rstrip()
            mateparts = line.split()
            reversedSeq = rc(mateparts[9])
            readflags[mateparts[10]] = reversedSeq
    
    trying = open('try.fq', 'w')
    for i in readflags.iterkeys() :
        trying.write(i+"\n")
    trying.close()
        
    newtry = open('try.fq', "r")
    for line in newtry:
        line.rstrip()
        if readflags.has_key(line):
            print "found"
    
    newtry.close() 
    reads.close()

main()