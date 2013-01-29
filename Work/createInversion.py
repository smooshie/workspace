'''
Created on 11.1.2013

@author: lisagawr
'''

def rc(reversable):
    complement = { "A" : "T", "T" : "A", "C" : "G", "G" : "C"}
    result = "" 
    for i in reversed(reversable): 
        result += complement[i]
    
    return result

def main():
    sequence = "GGAGGCGCTGGGTATGGTGGCTCACTCCTGTAATCCCAGCACTTTGGGAGGCCAAGGAGG"    
    reversd = rc(sequence)
    print reversd
                    

main()