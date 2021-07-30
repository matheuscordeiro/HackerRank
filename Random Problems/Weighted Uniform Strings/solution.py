def weightedUniformStrings(s, queries):
    initial = ord("a")
    frequency = {}
    current = ""
    count = 0
    for character in s:
        weight = ord(character) - initial + 1
        if character != current:
            current = character
            count = 1
        else:
            count += 1

        frequency[weight*count] = True

    result = []
    for q in queries:
        if q in frequency:
            result.append("Yes")
        else:
            result.append("No")

    return result