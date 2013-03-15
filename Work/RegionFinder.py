'''
Created on 7.2.2013
@author: lisagawr

            ::.
      (\./)  .-""-.
       `\'-'`      \
         '.___,_^__/

     * Whale whale whale, what have we here?

'''
import os
import sys

class RegionFinder() :
    
    def __init__(self) :
	try:
		args = sys.argv
		self.matesaved = args[1]
		self.sorted = args[2]
        	self.library_size = int(args[3])
        	self.header = ""
	except IndexError:
		print "\n\n"
		print "ERROR. Wrong input." 
		print "\n Usage: python RegionFinder.py matesavedSamFile sortedMappedSamFile  librarySize ."
		print "\n   (e.g.) python RegionFinder.py matesaved.sam sorted_mapped.sam 500"
		print "\n\n"		
		sys.exit(0)

    def read_file(self, f) :
        return map(int, filter(lambda x: x.strip() != '', open(f).readlines()))

    def window(self, c, width) :
        global histogram
        #return filter(lambda x : x > -1, range(c-width, c+width+1))
        return filter(lambda x : (x > -1) and (x < len(histogram)), range(c-width, c+width+1))
    
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
            writeto.write(rf.header)		
        writeto.write(line)
        writeto.close()    
        
if __name__ == '__main__' :
    rf = RegionFinder()
    values = []
    
    #read matesw-reads from file store their pairs location
    with open(rf.matesaved, 'r') as matesw:
        for line in matesw:
            line.rstrip()
            if line[0] != "@":
                mateparts = line.split()
                values.append(int(mateparts[7])) #pos-of-next
    values.sort()

    breaks = (values[-1] - values[0]) / rf.library_size
    bin_length = (values[-1] - values[0]) / (breaks - 1)
    histogram = [0] * breaks
    
    for i in values :
        try :
            histogram[(i - values[0]) / bin_length] += 1
        except IndexError :
            pass
            #print (i - values[0]) / bin_length
    
    f = open("histogram", 'w')
    for h in range(len(histogram)) :
        print >> f, h * rf.library_size, histogram[h]
    f.close()
    
    from scipy.signal import find_peaks_cwt
    import numpy as np
    
    peaks = find_peaks_cwt(np.array(histogram, np.int32), np.arange(1,10))
    
    peak_set = {}
    base = values[0]
    
    f = open("peaks", 'w')
    for p in peaks :
        freq,ind = sorted(map(lambda x : (histogram[x], x), rf.window(p, 2)), reverse=1)[0] # PhD-level bullshit  :-P
        location = base + rf.library_size * ind
    
        if location in peak_set :
            continue
        
        print >> f, location, freq
        
        peak_set[location] = freq
    f.close()
    
    thresh = sorted(peak_set.values())[3*(len(peak_set)/4)] #the threshold peaks should go over
    
    f = open("high_peaks", 'w')
    for p in peak_set :
        if peak_set[p] > thresh :
            print >> f, p, peak_set[p]
    f.close()
    
    regions = []
    high_peaks = open("high_peaks", "r") #read from the high peaks, produce two indexes from between which to search for reads
    for line in high_peaks:
        part = line.split()
        regions.append((int(part[0])-rf.library_size, int(part[0])+3*rf.library_size)) #arbitrary values
    regions.sort()
    
    current = 0
    writable = ""
    allreads = open(rf.sorted, "r")#java -jar ../../picard-tools-1.84/SortSam.jar I=mapped12.sam O=sorted_mapped12.sam SO$
    for line in allreads:
        allparts = line.split()
        if line[0] == "@":
            rf.header += line 
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

