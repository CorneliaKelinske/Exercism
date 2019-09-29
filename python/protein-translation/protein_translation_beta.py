#1. step: create a regex for each protein 
import re
Methionine = re.compile(r'^(AUG)(\w*)')
Phenylalanine = re.compile(r'UUUUUC)(\w*')
Leucine = re.compile(r'UUAUUG)(\w*')
Serine = re.compile(r'UCUUCCUCAUCG)(\w*')
Tyrosine = re.compile(r'UAUUAC)(\w*')
Cysteine = re.compile(r'UGUUGC)(\w*')
Tryptophan = re.compile(r'UGG)(\w*')
End_of_strang = re.compile(r'UAA)(\w*')

