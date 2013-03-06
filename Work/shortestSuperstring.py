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
                for i in range (0, len(contig)):
                    try:
                        if contig[i] == maxcontig[whereFound+i]:
                            continue
                        else:
                            continue
                            #print tempcontig[whereFound+i], contig[i]
                            #tempcontig[maxcontig.index(contig[0:10])+i] = contig[i]
                    except IndexError:
                        if ''.join(tempcontig) == maxcontig:
                            result = maxcontig+contig[i:len(contig)]
                            results.append(result)
                        #else:
                        #    results.append(''.join(tempcontig))
                        break
    print '\n\n'.join(results)

if __name__ == "__main__":
    dataset = []
    with open ("default-contigs.fa", "r") as f:
        for line in f:
            if line[0] == ">":
                continue
            else:
                dataset.append(line.rstrip())
    find_overlaps(dataset)