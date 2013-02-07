'''
Created on 7.2.2013

@author: lisagawr
'''
import sys

class RegionFinder(object) :
    def __init__(self, library_size, multiplier=2.1) :
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

if __name__ == '__main__' :
    rf = RegionFinder(10)
    print rf.get_regions([0,5,6,8,10,35,36,40,45,48,78,79,80])
