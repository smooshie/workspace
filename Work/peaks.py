
def read_file(f) :
    return map(int, filter(lambda x: x.strip() != '', open(f).readlines()))

def window(c, width) :
    global histogram
    #return filter(lambda x : x > -1, range(c-width, c+width+1))
    return filter(lambda x : (x > -1) and (x < len(histogram)), range(c-width, c+width+1))


values = read_file("positions.txt")
values.sort()

library_size = 500
breaks = (values[-1] - values[0]) / library_size
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
    print >> f, h * library_size, histogram[h]

f.close()


from scipy.signal import find_peaks_cwt
import numpy as np

peaks = find_peaks_cwt(np.array(histogram, np.int32), np.arange(1,10))

peak_set = {}
base = values[0]

f = open("peaks", 'w')

for p in peaks :
    freq,ind = sorted(map(lambda x : (histogram[x], x), window(p, 2)), reverse=1)[0] # PhD-level bullshit  :-P
    location = base + library_size * ind

    if location in peak_set :
        continue
    
    print >> f, location, freq
    
    peak_set[location] = freq

f.close()

thresh = sorted(peak_set.values())[3*(len(peak_set)/4)]

f = open("high_peaks", 'w')

for p in peak_set :
    if peak_set[p] > thresh :
        print >> f, p, peak_set[p]

f.close()


