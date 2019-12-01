letters = ["A", "a", "A"]

letters = [letter.upper() for letter in letters]
print(letters)
for letter in letters:
        if letter == "A":
            letters.remove(letter)
            print(letters)
if letters[0] == "A":
    letters.pop(0)
print(letters)