'''
Created on 23.4.2013

@author: lisagawr
'''
peak_set = {}
with open ("high_peaks", "r") as high_peaks:
    for line in high_peaks:
        part = line.split()
        peak_set[part[0]] = part[1]

places = []
for key in peak_set.iterkeys():
    places.append(key)

sorted = sorted(places)
finished = {}
diff_range = []

for entry in sorted:
    index = sorted.index(entry)
    if index+1 < len(sorted):
        if (int(entry) + 1500) >= int(sorted[index+1])-500:
            print "!", entry, int(entry)+1500, int(sorted[index+1])-500, sorted[index+1]
            entry_s = int(entry)-500
            entry_e = int(sorted[index+1])+1500
            diff_range.append(str(entry_s)+"-"+str(entry_e))
        else:
            finished[entry] = peak_set[entry]
            
print len(peak_set)
print len(finished)

for each in diff_range:
    parts = each.split("-")
    print parts[0], parts[1]