'''
Created on 6.3.2013

@author: lisagawr
'''
def find_overlaps(dataset):
    maxlen = 0
    results = []
    for contig in dataset:
        if len(contig) > maxlen:
            maxlen = len(contig)
            maxcontig = contig
    for contig in dataset:
        if contig == maxcontig:
            continue
        else:
            if contig[0:10] in maxcontig:
                whereFound = maxcontig.index(contig[0:10])
                tempcontig = list(maxcontig)
                mismatchLoc = ["x", "x"]
                for i in range (0, len(contig)):
                    try:
                        if contig[i] == maxcontig[whereFound+i]:
                            continue
                        else:
                            if mismatchLoc[0] == "x":
                                mismatchLoc[0] = i
                            else:
                                if contig[i:i+5] != maxcontig[whereFound+mismatchLoc[0]:whereFound+mismatchLoc[0]+5]:
                                    continue
                                    #print contig[i:i+5], maxcontig[whereFound+mismatchLoc[0]:whereFound+mismatchLoc[0]+5]
                                else:
                                    mismatchLoc[1] = i+5
                        if mismatchLoc[0] != "x" and mismatchLoc[1] != "x":
                            tempcontig[whereFound+mismatchLoc[0]] = contig[mismatchLoc[0]:mismatchLoc[1]]
                            results.append(''.join(tempcontig))
                            mismatchLoc = ["x", "x"]
                    except IndexError:
                        if ''.join(tempcontig) == maxcontig:
                            result = maxcontig+contig[i:len(contig)]
                            results.append(result)
                        else:
                            results.append(''.join(tempcontig))
                        break
    print '\n\n'.join(results)

if __name__ == "__main__":
    dataset = []
    with open ("default-contigs.txt", "r") as f:
        for line in f:
            if line[0] == ">":
                continue
            else:
                dataset.append(line.rstrip())
    find_overlaps(dataset)