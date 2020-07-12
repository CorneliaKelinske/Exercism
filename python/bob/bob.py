def response(hey_bob):
    if hey_bob.isupper():
        if hey_bob[-1] == "?":
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"
    elif hey_bob[-1] == "?":
        return "Sure"
    return "Whatever"

print(response("HELLO?"))
print(response("HELLO"))

print(response("How?"))
