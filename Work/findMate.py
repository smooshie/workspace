'''
Created on 10.1.2013
            ::.
      (\./)  .-""-.
       `\'-'`      \
         '.___,_^__/

     * Whale whale whale, what have we here?
  
'''
comparable = {}

with open('paired_unmapped.sam', 'r') as matesw:
    for line in matesw:
        mateparts = line.split()
        comparable[mateparts[0]] = 1
    
writeto = open("uniqmates.sam", "w")

with open('mapped12.sam', 'r') as mapped:
    for find in mapped:
        mappedparts = find.split()
        if comparable.has_key(mappedparts[0]) :
            writeto.write(find)

writeto.close()