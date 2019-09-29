#1. step: create a regex for each protein 
import re
m = re.compile(r'^(AUG)(\w*)') #Methionine
ph = re.compile(r'^(UUUUUC)(\w*)') #Phenylalanine
l = re.compile(r'^(UUAUUG)(\w*)') #Leucine
s = re.compile(r'^(UCUUCCUCAUCG)(\w*)') #Serine
ty = re.compile(r'^(UAUUAC)(\w*)') #Tyrosine
c = re.compile(r'^(UGUUGC)(\w*)') #Cysteine
t = re.compile(r'^(UGG)(\w*)') #Tryptophan
e = re.compile(r'^(UAA)(\w*)') #STOP

match = m.search('AUG')

print(match)
