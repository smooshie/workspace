'''
Created on 27.2.2013

@author: lisagawr

            ::.
      (\./)  .-""-.
       `\'-'`      \
         '.___,_^__/

     * Whale whale whale, what have we here?

'''

masked = open("human_long_masked.fas", "r")
seq = []
print "Reading reference file..."
for line in masked:
    if line[0] != ">":
        for i in line:
            seq.append(i)
masked.close()

reads = open("paired_unmapped.sam","r")
output = open("filtered_reads.sam", "w")

print "Discarding reads with more than 50% overlap with masked area..."
for read in reads:
    counter = 0
    part = read.split()
    if read[0] == "@":
        output.write(read)
        continue
    for i in range(0, 101):
        try:
            if seq[int(part[3])-1+int(i)] == "N":
                counter += 1
                if counter > 50:
                    break
        except IndexError:
            pass
    if counter > 50:
        continue
    else:
        output.write(read)
            
print "Output in file filtered_reads.sam."

reads.close()
output.close()