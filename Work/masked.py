'''
Created on 27.2.2013

@author: lisagawr

            ::.
      (\./)  .-""-.
       `\'-'`      \
         '.___,_^__/

     * Whale whale whale, what have we here?

'''
seq = []
cutoff = int(raw_input("Insert cut off point in full percentages. (e.g. 50) :"))

print "Reading reference file..."
with open("human_long_masked.fas", "r") as masked:
    next(masked)
    for line in masked:
        for i in line:
            seq.append(i)

reads = open("paired_unmapped.sam","r")
output = open("filtered_reads.sam", "w")

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


