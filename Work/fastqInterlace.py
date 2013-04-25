'''
Created on 5.4.2013

@author: lisagawr
'''

firstFile = open("toFq_reads.1", "r")
secondFile = open("toFq_reads.2", "r")

namesOne = {}
namesTwo = {}

readsOne = []
readsTwo = []

for line in firstFile:
    if line[0] == "@":
        