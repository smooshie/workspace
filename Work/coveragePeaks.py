'''
Created on 14.1.2013

@author: lisagawr


depth = open("mate_depth", "r")

for line in depth:
    column = line.split()

depth.close()
'''
depth = open("mate_depth", "r")
location = []
coverage = []


for line in depth:
    part = line.split()
    location.append(part[1])
    coverage.append(part[2])

print len(coverage), len(location)

print location[0], location[-1]

    depth = open("mate_depth", "r")
    location = []
    coverage = []

    for line in depth:
        part = line.split()
        location.append(part[1])
        coverage.append(part[2])