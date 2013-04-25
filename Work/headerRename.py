'''
Created on 10.4.2013

@author: lisagawr
'''
# for dir in `ls -d contigs_*`; do for file in `ls $dir/*.fa`; do python headerRename.py $file; done; done
# cat *.txt > all_contigs_renamed.fa

import sys
import os

args = sys.argv

try:
    f = open(args[1], "r")
    enteredFile = args[1]
    parts = enteredFile.split("/")
    filename = parts[1]
    run_and_range = filename.rstrip(".fa")
    contig_id = run_and_range.lstrip("contigs")
    txtname = str(run_and_range)+".txt"
    abspath_and_name = os.path.abspath(filename)
    abspath = abspath_and_name.rstrip(filename)+parts[0]+"/"
    
    w = open(abspath+txtname, "w")
    
    counter = 0
    contigs = []
    
    for line in f:
        if line[0] == ">":
            part = line.split()
            newHeader = ">contig"+str(counter)+str(contig_id)+"    "+part[1]+"    "+part[2]
            contigs.append(newHeader)
            counter += 1
        else:
            contigs.append(line)
            
    w.write('\n'.join(contigs))
    
except IndexError:
    print "ERROR: You must insert second command in the command line. e.g. python headerRename.py filename.fa ."



        