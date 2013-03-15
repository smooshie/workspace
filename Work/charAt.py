'''
Created on 13.3.2013

@author: lisagawr
'''
seq = ""

first = raw_input("First value: ")
second = raw_input("Second value: ")

with open("human_altered.fas", "r") as f:
    for line in f:
        if line[0] != ">":
            seq += line

wanted = seq[first:second]

output = open("location_in_altered", "w")

output.write(wanted)