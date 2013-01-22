'''
Created on 11.1.2013

@author: 

            ::.
      (\./)  .-""-.
       `\'-'`      \
         '.___,_^__/

     * Whale whale whale, what have we here?

'''

def rc(input):
    complement = { "A" : "T", "T" : "A", "C" : "G", "G" : "C"}
    result = [] 
    for i in reversed(input): 
        result.append(complement[i])
    
    return ''.join(result)

def main():
    sequence = '''GGATTACAGGTGTGAGCCACTGCGCCTGGCCTGTTGAACTTTTAACATACTTCCCTGTGCTCTAGCCACAGCCACACTGGTTCCCGTTAGCTAAATTTTTAACCATACAGTATTGTCATTTGCATGCTGTAGTTAAGAGCTTCCAGAGGTTACATGCACTAGATCTTAACAGCTTAGCCCTCATGAATAACATGTTATCTTCCACCATCTCAGGGAAGCAGTGATACCGTGGAGTGAGAAAAGTGCATTCTCTCAGGATTTCTGCCGTGTTTTCATGCTGAGGTGTGACAGAGTATTTCC'''
    reversed = rc(sequence)
    print reversed
                    

main()