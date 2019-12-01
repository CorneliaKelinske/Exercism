def find_anagrams(word, candidates):
    
    return [item for item in candidates if item.upper() != word.upper() and sorted(item.upper()) == sorted(word.upper())]

print(find_anagrams("BANANA", ["BANANA", "Banana", "banana"]))
