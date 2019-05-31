def is_pangram(sentence):
    ABC = ["a", "b","c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    sentence = sentence.lower()
    count = 0
    for let in ABC:
        if let in sentence:
            count +=1
        else:
            count = count
    if count == 26:
        return True
    else:
        return False

