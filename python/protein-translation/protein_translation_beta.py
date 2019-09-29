#1. step: create a regex for each protein 
import re
m = re.compile(r'^(AUG)(?P<rest>\w*)') #Methionine
ph = re.compile(r'^(UUUUUC)(?P<rest>\w*)') #Phenylalanine
l = re.compile(r'^(UUAUUG)(?P<rest>\w*)') #Leucine
s = re.compile(r'^(UCUUCCUCAUCG)(?P<rest>\w*)') #Serine
ty = re.compile(r'^(UAUUAC)(?P<rest>\w*)') #Tyrosine
c = re.compile(r'^(UGUUGC)(?P<rest>\w*)') #Cysteine
t = re.compile(r'^(UGG)(?P<rest>\w*)') #Tryptophan
e = re.compile(r'^(UAA)(?P<rest>\w*)') #STOP


code = {m : "Methionine", ph : "Phenylalanine", l : "Leucine", s : "Serine", ty : "Tyrosine", c :"Cysteine", t : "Tryptophan", e : "STOP"}

def proteins(strang):
    all_proteins = []
    for key in code:
        match = key.search(strang)
        if match:
            if key == e:
                return all_proteins
            else:
                all_proteins.append(code[key])
                strang = match.group("rest")
                proteins(strang)

print (proteins("UGGUAA"))              

