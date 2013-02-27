'''
Created on 27.2.2013

@author: lisagawr
'''

masked = open("masked.txt", "r")
seq = []

for line in masked:
    if line[0] != ">":
        for i in line:
            seq.append(i)

masked.close()
reads = open("reads.txt","r")

output = open("filtered_reads.txt", "w")

for read in reads:
    part = read.split()
    if seq[int(part[3])-1] != "N":
        output.write(read)
    else:
        print "Discarded read:", read, "Because:", part[3], seq[int(part[3])-1]

reads.close()
output.close()