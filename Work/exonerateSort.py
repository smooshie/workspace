#for file in `ls *.fa`; do filename=${file##*/}; name=${filename%.fa}; outputname=$name".txt"; exonerate --percent 90 --verbose 0 --showalignment no --showvulgar no  --ryo "\n*\n%S mm %em \n >query %qas \n >target %tas*" $file ../chr10.fa > exonerate/$outputname; done

from operator import itemgetter
import glob
import os

contigs_by_mm = {}
contigs_by_position = {}
contigs_and_sequence = {}
contigs_and_orientation = {}
contigs_and_reference = {}
store = []
star = False
temp = ""

pathToScript = os.path.dirname(os.path.realpath(__file__))
os.chdir(pathToScript)
for oneFile in glob.glob("*.txt"):
    with open(oneFile, "r") as readFile:
        try: #read from files
                for line in readFile:
                    line = line.rstrip()
                    if line == "*" and star == False:
                        star = True
                    elif line == "*" and star == True:
                        store.append(temp)
                        temp = ""
                        star = False
                    elif star == True and line != "*" and len(line) > 1:
                        if "query" in line or "contig" in line or "target" in line:
                            temp += line
                        else:
                            temp += line.upper()
                #store from files       
                for each in store:
                        part = each.split()
                        contigs_by_mm[part[0]] = int(part[10])
                        contigs_and_orientation[part[0]] = part[7]
                        contigs_by_position[part[0]] = str(part[5])+"-"+str(part[6])
                        contigs_and_sequence[part[0]] = part[12]
                        contigs_and_reference[part[0]] = part[14]
                        
        except IndexError:
            print "Error in file", oneFile
            print "On line", line
            
#part[0] = contig name
#part[5] = start on reference
#part[6] = end on reference
#part[7] = orientation
#part[10] = mm
#part[11] = ">query"
#part[12] = query sequence
#part[13] = ">target"
#part[14] = target sequence
'''
rtemp = ""
with open("chr10.fa", "r") as reference:
    for line in reference:
        if line[0] != ">":
                rtemp += line.rstrip()
seq_ref = rtemp
'''
sortedFile = open("sortedContigs.txt", "w")

#sort and print to separate files "<name>_query" and "<name>_target".
for key, value in sorted(contigs_by_mm.items(), key=itemgetter(1), reverse=True):
    print >> sortedFile, key, value
    if key in contigs_and_sequence and value >= 2:
        position = contigs_by_position[key]
        pos = position.split("-")
        with open(pathToScript+"/complete/"+key+"_query", "w") as queryFile:
            print >> queryFile, ">CONTIG from ", pos[0]+"-"+pos[1], key, "\n", contigs_and_sequence[key]
        with open(pathToScript+"/complete/"+key+"_target", "w") as targetFile:
            if contigs_and_orientation[key] == "+":
                print >> targetFile, ">REFERENCE from ", pos[0]+"-"+pos[1], key
                print >> targetFile, contigs_and_reference[key]
                #seq_ref[int(pos[0])+100:int(pos[1])+100]
            else:
                print >> targetFile, contigs_and_reference[key]

print "Query and Target files are in folder complete."
sortedFile.close()