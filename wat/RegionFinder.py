'''
Created on 7.2.2013

@author: lisagawr
'''
import sys
import os
global header

class RegionFinder(object) :
    def __init__(self, library_size, multiplier=1.5) :
        self.library_size = library_size
        self.multiplier = multiplier
        self.threshold = library_size * multiplier

    # data is assumed to be [pos, pos ...]
    def get_regions(self, data) :
        data.sort()
        boundaries = [data[0]]

        for i in range(1, len(data)) :
            if (data[i] - data[i-1]) > self.threshold :
                boundaries += [data[i-1], data[i]]

        boundaries.append(data[-1])

        regions = []

        for i in range(0, len(boundaries), 2) :
            regions.append((boundaries[i], boundaries[i+1]))

        return regions

    def test(self, regions, current, value):
        temp  = regions[current]
        boundaries = temp[0], temp[1]
        if boundaries[0] <= int(value) and int(value) <= boundaries[1]:
            return True
        else:
            return False

    def writer(self, filename, line):
        writeto = open(filename, "w")
        if os.stat(filename)[6]==0:
		writeto.write(header)		
	writeto.write(line)
        writeto.close()
    
if __name__ == '__main__' :
    readflags = {}
    
    with open('paired_unmapped.sam', 'r') as matesw:
        for line in matesw:
            line.rstrip()
            if line[0] != "@":
                mateparts = line.split()
                readflags[mateparts[0]] = mateparts[7] #name:pos of next
        
    positions = []
    for entry in readflags.iterkeys():
        positions.append(int(readflags[entry]))
    
    rf = RegionFinder(500, 1.5)
    regions = rf.get_regions(positions)
    current = 0
    writable = ""
    header = ""
    allreads = open("sorted_mapped12.sam", "r")#java -jar ../../picard-tools-1.84/SortSam.jar I=mapped12.sam O=sorted_mapped12.sam SO$
    for line in allreads:
        allparts = line.split()
	if line[0] == "@":
	    header += line 
        else:
            temp  = regions[current]
            boundaries = temp[0], temp[1]
            filename = "mapped12_"+str(boundaries[0])+"-"+str(boundaries[1])+".sam"
            if rf.test(regions, current, allparts[3]):
                writable += line
            else:
		if len(regions)>current+1:
			if rf.test(regions, current+1, allparts[3]):
                		if len(writable) != 0:
                    			rf.writer(filename, writable)
                    			writable = ""
               			current += 1
                		writable = line
           	else:
                	if len(writable) != 0:
                    		rf.writer(filename, writable)
                    		writable = ""

    allreads.close()
