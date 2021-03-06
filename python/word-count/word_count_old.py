import string
import re

pattern = re.compile(r'(\')(\w+)(\')')


def counter(list, input_word):
    count = 0

    for item in list:
        if item == input_word:
            count += 1
    return count


def count_words(sentence):
    sentence = sentence.lower()
    for char in string.punctuation:
        
        if char != "'":
            sentence = sentence.replace(char, ' ')
    
    eliminate = pattern.sub("\g<2>", sentence)   

    sen_list = eliminate.split()

    words = []
    results = {}
    for word in sen_list:
        if word not in words:
            words.append(word)
            results.update({word:  counter(sen_list, word)})

    return results


print(count_words("Joe can't tell between 'large' and large."))
