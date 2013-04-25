'''
Created on 27.2.2013

@author: lisagawr

            ::.
      (\./)  .-""-.
       `\'-'`      \
         '.___,_^__/

     * Whale whale whale, what have we here?

'''

import sys

try: 
	args = sys.argv
	seq = []
	cutoff = int(args[3])
	masked_file = args[1]
	reads_file = args[2]
except IndexError:
	print "ERROR!"
	print "Usage: python removeMasked.py masked_file reads_file cutoff_point"
	sys.exit(0)

print "Reading reference file..."
with open(masked_file, "r") as masked:
    next(masked)
    for line in masked:
        for i in line:
            seq.append(i)

reads = open(reads_file,"r")
output = open("filtered_paired_unmapped.sam", "w")

print "Discarding reads with >= than ", cutoff," overlap with masked area..."
for read in reads:
    counter = 0
    part = read.split()
    if read[0] == "@":
        output.write(read)
        continue
    for i in range(0, len(part[9])):
        try:
            if seq[int(part[3])-1+int(i)] == "N":
                counter += 1
                if counter >= cutoff:
                    break
        except IndexError:
            pass
    if counter >= cutoff:
        continue
    else:
        output.write(read)
        
reads.close()
output.close()

print "Output in file filtered_reads.sam."



