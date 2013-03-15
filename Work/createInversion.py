'''
Created on 11.1.2013

@author: 

            ::.
      (\./)  .-""-.
       `\'-'`      \
         '.___,_^__/

     * Whale whale whale, what have we here?

'''

def rc(reversable):
    complement = { "A" : "T", "T" : "A", "C" : "G", "G" : "C"}
    result = "" 
    for i in reversed(reversable): 
        result += complement[i]
    
    return result

def main():
    seq = []
    with open("human_relative.fas", 'rU') as f:
        for line in f:
            line.rstrip('\r\n')
            if line[0] != ">":
                for i in line:
                    if i != '\n':
                        seq.append(i)
    
    indexes = open("indexes.txt", "w")
    for i in range (1, 130):
        if i % 30 == 0:
            reversd = rc(seq[i:i+5])
            indexes.write("from " + str(i) + " took " + str(seq[i:i+5]) + " --> " + str(i-20) + "-" + str(i-18) + " inserted " + reversd + " \n")
            seq.pop(i-20)
            seq.pop(i-19)
            seq.insert(i-21, reversd)
        
    
    done = open("human_altered.fas", "w")
    
    done.write(''.join(seq))
                    

main()