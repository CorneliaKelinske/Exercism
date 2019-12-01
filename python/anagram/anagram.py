def find_anagrams(word, candidates):
    candidates = [item.upper() for item in candidates]       
    print(candidates)

    for item in candidates:
        if item == word.upper():
            candidates.remove(item)
    if candidates[0] == word.upper():
        candidates.pop(0)
    
    print(candidates)
        
    return [item for item in candidates if sorted(item) == sorted(word.upper())]

print(find_anagrams("BANANA", ["BANANA", "Banana", "banana"]))
