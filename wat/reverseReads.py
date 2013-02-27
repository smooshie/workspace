'''
Created on 21.1.2013

@author: 

            ::.
      (\./)  .-""-.
       `\'-'`      \
         '.___,_^__/

     * Whale whale whale, what have we here?

'''

def rc(reversable):
    complement = { "A" : "T", "T" : "A", "C" : "G", "G" : "C"}
    result = "" 
    for i in reversed(reversable): 
        result += complement[i]
    
    return result

def main():
    readflags = {}
    linecount = 0
    lastFour = [0,0,0,0]

    print "Starting with paired reads."
    with open('paired_unmapped.sam', 'r') as matesw:
        for line in matesw:
            line.rstrip()
            if line[0] != "@":
                mateparts = line.split()
                reversedSeq = rc(mateparts[9])
                readflags[mateparts[10]] = reversedSeq
                
    print "Paired reads reversed."
    
    reads1 = open('reads1.fq', "r")
    reads2 = open('reads2.fq', "r")
    reads = open("unmapped_paired_reversed.fq", "w")
    
    print "Finding reads1..."
    for line in reads1:
        linecount += 1
        line = line.rstrip()
        if linecount == 1:
            lastFour[0] = line
        elif linecount == 2:
            lastFour[1] = line
        elif linecount == 3:
            lastFour[2] = line
        elif linecount == 4:
            lastFour[3] = line
            linecount = 0
        if readflags.has_key(line):
            lastFour[1] = readflags[line].rstrip()
            reads.write('\n'.join(lastFour))
            reads.write("\n")
    print "Done!"
    print "Data from paired reads is in file reversed_unmapped_reads.fq !"
    #linecount = 0 #maybe needed?
    
    print "Finding reads2..."
    for line in reads2:
        linecount += 1
        line = line.rstrip()
        if linecount == 1:
            lastFour[0] = line
        elif linecount == 2:
            lastFour[1] = line
        elif linecount == 3:
            lastFour[2] = line
        elif linecount == 4:
            lastFour[3] = line
            linecount = 0
        if readflags.has_key(line):
            lastFour[1] = readflags[line].rstrip()
            reads.write('\n'.join(lastFour))
            reads.write("\n")
    print "Done!"
    #linecount = 0 #maybe needed?    

    reads1.close()
    reads2.close() 
    reads.close()
    
    singleFlags = {}
    open('unmapped_singles_reversed.fq', "w").close() #to make sure output file is empty
    singl_reads = open('unmapped_singles_reversed.fq', "w")

    with open('singles_unmapped.sam', 'r') as singles:
        for line in singles:
            if line[0] != "@":
                line.rstrip()
                mateparts = line.split()
                reversedSeq = rc(mateparts[9])
                singleFlags[mateparts[10]] = reversedSeq
    print "Rerversed reads."
    
    print "Reading reads.fq..."
    with open('reads.fq', "r") as readss:
        for line in readss:
            linecount += 1
            line = line.rstrip()
            if linecount == 1:
                lastFour[0] = line
            elif linecount == 2:
                lastFour[1] = line
            elif linecount == 3:
                lastFour[2] = line
            elif linecount == 4:
                lastFour[3] = line
                linecount = 0
            if singleFlags.has_key(line):
                lastFour[1] = singleFlags[line].rstrip()
                singl_reads.write('\n'.join(lastFour))
                singl_reads.write("\n")
    print "Data from single reads in unmapped_singles_reversed.fq !"
    singl_reads.close()
    
main()


