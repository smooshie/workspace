'''
Created on 24.1.2013

@author: lisagawr
'''

comparable = {}

with open('try.sam', 'r') as matesw:
    for line in matesw:
        mateparts = line.split()
        comparable[mateparts[0]] = mateparts[3]
    
writeto = open("uniqmates.sam", "w")

with open('mapped12.sam', 'r') as mapped:
    for find in mapped:
        mappedparts = find.split()
        if comparable.has_key(mappedparts[0]) :
            if mappedparts[3] == mateparts[3]:
                print "same loc"

writeto.close()