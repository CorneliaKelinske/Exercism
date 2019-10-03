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
        print(f"this is the input {strand}")

        if match and key != e and key not in used_keys:
            all_proteins.append(code[key])
            used_keys.append(key)
            rest =  match.group("rest")
            print(f"this is the rest {rest}")
            

            strand = rest
            proteins(strand)
        #else:                            
      
    return all_proteins

print(proteins("UGGUUU"))
