#1. step: create a regex for each protein 
import re
m = re.compile(r'(^AUG)(?P<rest>\w*)') #Methionine
ph = re.compile(r'(^UUUUUC)(?P<rest>\w*)') #Phenylalanine
l = re.compile(r'(^UUAUUG)(?P<rest>\w*)') #Leucine
s = re.compile(r'(^UCUUCCUCAUCG)(?P<rest>\w*)') #Serine
ty = re.compile(r'(^UAUUAC)(?P<rest>\w*)') #Tyrosine
c = re.compile(r'(^UGUUGC)(?P<rest>\w*)') #Cysteine
t = re.compile(r'(^UGG)(?P<rest>\w*)') #Tryptophan
e = re.compile(r'(^UAA)(?P<rest>\w*)') #STOP


code = {m : "Methionine", ph : "Phenylalanine", l : "Leucine", s : "Serine", ty : "Tyrosine", c :"Cysteine", t : "Tryptophan", e : "STOP"}
all_proteins = []

def proteins(strand):
   
    for key in code:
        match = key.search(strand)

        
        if match and key == e:
            print("BREAK")
            break
        elif match and key != e:
            print(match.group())
            
            
            print("CONTINUE")
            all_proteins.append(code[key])
            print(f"all proteins: {all_proteins}")
            rest = match.group("rest")
            if rest:
                strand = rest
                print(strand)
                proteins(strand)
            else:
                print("NO_REST")
                break
    return all_proteins

print (proteins("AUGUUUUUCUAA"))
#print (proteins("UGGAUGF"))
                           
   

