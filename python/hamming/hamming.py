def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError ("strand_a and strand_b must have the same length")
    hamming_distance = 0
    y = 0
    for char in strand_a:
        if char != strand_b[y]:
            hamming_distance += 1
        y += 1
    return hamming_distance

#print(distance("GGACGGATTCTG", "AGGACGGATTCT"))



