'''
Created on 10.4.2013

@author: lisagawr
'''
#for file in `ls contigs/*.fa`; do python rmDup.py $file; done
import sys
import os

try:
    args = sys.argv
    f = open(args[1], "r")
    enteredFile = args[1]
    parts = enteredFile.split("/")
    filename = parts[1]
    run_and_range = filename.rstrip(".fa")
    abspath_and_name = os.path.abspath(filename)
    abspath = abspath_and_name.rstrip(filename)+parts[0]+"/"
    outputname = str(run_and_range)+".fa"
    newPath = abspath+"../blat/"
    w = open(newPath+outputname, "w")
    
    contigs = {}
    
    for line in f:
        if line[0] == ">":
            header = line.rstrip("\n")
            parts = header.split()
        elif line != " " and len(line) > 2:
            if line not in contigs.itervalues():
                if int(parts[1]) > 70:
                    contigs[header] = line
    f.close()
    
    for (key, value) in contigs.iteritems():
        w.write(key)
        w.write("\n")
        w.write(value)
    w.close()
    
except IndexError:
    print "ERROR: You must insert second command in the command line. e.g. python rmDup.py filename.fa ."

