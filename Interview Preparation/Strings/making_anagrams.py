def makeAnagram(a, b):
    freq_a = {}
    freq_b = {}
    for value in a:
        freq_a[value] = freq_a.get(value, 0) + 1

    for value in b:
        freq_b[value] = freq_b.get(value, 0) + 1

    total = 0
    for key, value in freq_a.items():
        dif = value - freq_b.get(key, 0)
        if dif > 0:
            total += dif

    for key, value in freq_b.items():
        dif = value - freq_a.get(key, 0)
        if dif > 0:
            total += dif

    return total


if __name__ == "__main__":
    a = "cde"
    b = "dcf"
    print(makeAnagram(a, b))