'''
Created on 8.5.2013

@author: lisagawr
'''
#os.path.abspath(filename)

import glob
import os
writable = ["", ""]
writeFile = open("longContigs.txt", "w")
contigNames = open("namesOfLongContigs.txt", "w")

pathToScript = os.path.dirname(os.path.realpath(__file__))
os.chdir(pathToScript)
for oneFile in glob.glob("*.fa"):
    with open(oneFile, "r") as readFile:
        for line in readFile:
            if line[0] == ">":
                columns = line.split("    ")
                if int(columns[1]) >= 300:
                    writable[0] = line
                    writable[1] = readFile.next()
                    writeFile.write(writable[0] + writable[1] + "\n")
                    contigNames.write(columns[0] + "\n")
                    writable = ["", ""]
                else:
                    continue