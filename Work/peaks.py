coverages = open("coverage_unmapped.sam", "r")
A = []

print "Reading from file..."

first = True
for line in coverages:
    parts = line.split()
    if first == True:
        pos = int(parts[1])
        first = False
    A.append(int(parts[2]))
coverages.close()

print "Finding peaks..."
B = []
firstover5 = True
for i in range(0, len(A)-1):
    if A[i] >= 5:
        if firstover5 == True:
            B.append(i+pos)
            firstover5 = False
        if A[i+1] < 5:
            B.append(i+pos)
            firstover5 = True

peaks = open("peaks_unmapped.txt", "w")

for i in range(0, len(B)):
    if i % 2 == 0:
        line = str(B[i]) + "-"
    else:
        line += str(B[i])
        peaks.write(line+"\n")
        line = ""
peaks.close()

print "Peaks stored in peaks_unmapped.txt."

range = open("peaks_unmapped.txt", "r")
snps = open("RAL_samtools.vcf", "r")

found = open("peaks_and_snps.txt", "w")

for line in range:
    linepart = line.split("-")
    for snp in snps:
        if snp[0] == "#":
            continue
        count = 0
        snpart = snp.split()
        if snpart[1] > linepart[0] and snpart[1] < linepart[1]:
            count+=1
        found.write(linepart[0] , "-" , linepart[1] , "||" , count , "SNPs")
            