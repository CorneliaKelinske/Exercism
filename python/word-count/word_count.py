import string

def count_words(sentence):
    sentence = sentence.lower()
    for char in string.punctuation:
        sentence = sentence.replace(char, ' ')
        sen_list = sentence.split()

    return sen_list



print(count_words("Joe can't tell between app, apple and a."))