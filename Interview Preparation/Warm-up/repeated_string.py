def repeatedString(s, n):
    count_as = s.count("a")
    total = (n // len(s)) * count_as
    rest = n % len(s) if n > len(s) else n
    for i in range(rest):
        if s[i] == "a":
            total += 1

    return total


if __name__ == "__main__":
    print(repeatedString("aaaa", 1))
