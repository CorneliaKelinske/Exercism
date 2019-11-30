def find_anagrams(word, candidates):
        
    return [item for item in candidates if sorted(item) == sorted(word)]

print(find_anagrams("listen", ["enlists", "google", "inlets", "banana"]))   

