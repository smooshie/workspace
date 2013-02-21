import os
import os.path
import sys
from subprocess import call

def main():
    linecount = 0
    lastFour = [0,0,0,0]
    count = 0
    path = 'sams/'
    filenames = [filename for filename in os.listdir(path)
                 if filename.endswith('.sam') and filename.startswith('mapped12_')]

    for filename in filenames:
        with open(os.path.join(path, filename), "r") as f:
                readflags = {}
                print readflags
                print len(readflags)               
                for line in f:
                    line.rstrip()
                    if line[0] != "@":
                        mateparts = line.split()
                        readflags[mateparts[10]] = 1
                    print readflags
                    print len(readflags)
                    storename = str(filename)+'.fq'
                    storefile = open(storename, "w")
                    
                with open("reads.fq", "r") as reads:
                    for line in reads:
                            linecount += 1
                            line = line.rstrip()
                            if linecount == 1:
                                    lastFour[0] = line
                            elif linecount == 2:
                                    lastFour[1] = line
                            elif linecount == 3:
                                    lastFour[2] = line
                            elif linecount == 4:
                                    lastFour[3] = line
                                    linecount = 0
                            if readflags.has_key(line):
                                    print "found"
                                    storefile.write('\n'.join(lastFour))
                                    storefile.write("\n")

if __name__ == '__main__':
    status = main()
    sys.exit(status)