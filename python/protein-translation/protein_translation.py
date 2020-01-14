#I wanted to solve this using regex. If I run each test individually, my solution passes all of them. 
#However, if I run more than 1 test at the same time, my code only passes the first test.
#I am wondering why that is and if there is a better regex solution.

import re


m = re.compile(r'(^AUG)(?P<rest>\w*)') #Methionine
ph = re.compile(r'(^UUU|^UUC)(?P<rest>\w*)') #Phenylalanine
l = re.compile(r'(^UUA|^UUG)(?P<rest>\w*)') #Leucine
s = re.compile(r'(^UCU|^UCC|^UCA|^UCG)(?P<rest>\w*)') #Serine
ty = re.compile(r'(^UAU|^UAC)(?P<rest>\w*)') #Tyrosine
c = re.compile(r'(^UGU|^UGC)(?P<rest>\w*)') #Cysteine
t = re.compile(r'(^UGG)(?P<rest>\w*)') #Tryptophan
e = re.compile(r'(^UAA|^UAG|^UGA)(?P<rest>\w*)') #STOP


code = {m : "Methionine", ph : "Phenylalanine", l : "Leucine", s : "Serine", ty : "Tyrosine", c :"Cysteine", t : "Tryptophan", e : "STOP"}
all_proteins = []
used_keys = []

def proteins(strand):
    for key in code:
        match = key.search(strand)
        

        if match and key != e and key not in used_keys:
            all_proteins.append(code[key])
            used_keys.append(key)
            rest =  match.group("rest")
            strand = rest
            proteins(strand)
                                    
      
    return all_proteins

print(proteins("UGGUGUUAUUAAUGGUUU"))
