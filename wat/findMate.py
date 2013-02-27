'''
Created on 10.1.2013
            ::.
      (\./)  .-""-.
       `\'-'`      \
         '.___,_^__/

     * Whale whale whale, what have we here?

'''
readflags = {}

with open('paired_unmapped.sam', 'r') as matesw:
    for line in matesw:
        line.rstrip()
        if line[0] != "@":
            mateparts = line.split()
            readflags[mateparts[0]] = mateparts[7] #name:pos of next

writeto = open("identifier_pos.sam", "w")

with open('mapped12.sam', 'r') as mapped:
    for entry in mapped:
        mappedparts = entry.split()
        if entry[0] != "@":
            if readflags.has_key(mappedparts[0]) and mappedparts[3] == readflags[mappedparts[0]]:
                writeto.write(entry)

writeto.close()




