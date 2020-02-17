import string
from collections import Counter


def count_words(sentence):
    sentence = sentence.lower()
    for char in string.punctuation:        
        if char != "'":
            sentence = sentence.replace(char, ' ')

    sen_list = [word.strip("'") for word in sentence.split()]
    cnt = Counter(sen_list)   
      
    return cnt


print(count_words("Joe can't tell between 'large' and large."))

