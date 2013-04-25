'''
Created on 14.3.2013

@author: lisagawr
'''

def writer(filename, writable):
    writeto = open(filename, "w")
    writeto.write(writable)

if __name__ == '__main__' :
    counter = 0
    cycles = 1
    alphabet = "ABCTG"
    with open ("outputfile.fas", "r") as f:
        for line in f:
            if line != "\n" and line != "" and line[1] in alphabet:
                if line[0] == ">": #headerline
                    writable = line
                    continue
                else:
                    writable += line
                    counter += 1
                    if counter % 2 != 0:
                        filename = "A_"+str(cycles)+".fas"
                        writer(filename, writable)
                        writable = ""
                    else:
                        filename = "B_"+str(cycles)+".fas"
                        writer(filename, writable)
                        cycles += 1
                        writable = ""            