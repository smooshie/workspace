'''
Created on 10.1.2013

@author: lisagawr
'''

sequence = open("seq.txt", "r")

for line in sequence:
    if line[0] != ">":
        for letter in line:
            if letter == letter.lower():
                print line.index(letter)