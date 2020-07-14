def response(hey_bob):
    hey_bob = hey_bob.replace(" ", "")
    if len(hey_bob) != 0:
        if hey_bob.isupper():
            if hey_bob[-1] == "?":
                return "Calm down, I know what I'm doing!"
            return "Whoa, chill out!"
        elif hey_bob[-1] == "?":
            return "Sure."
        elif len([letter for letter in hey_bob if letter.isalnum()]) == 0:
            return "Fine. Be that way!"
        return "Whatever."
    return "Fine. Be that way!"



