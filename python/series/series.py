#maybe slice from 0 to length -1 while len(series) >= length


def slices(series, length):
    result = []
    if len(series) < length:
        raise ValueError ("slice is too large")
    if length <= 0:
        raise ValueError ("slice cannot be negative or zero")
    if len(series) == 0:
        raise ValueError ("cannot input empty string")
    while len(series) >= length:
        s = series[:length]
        result.append(s)
        series = series[1:len(series)]
    return result

#print(slices("777777", 100))
