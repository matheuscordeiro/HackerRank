def superReducedString(s):
    found = True
    while found:
        found = False
        name = ""
        i = 0
        while i < len(s):
            if i+1 < len(s) and s[i] == s[i+1]:
                found = True
                i += 1
            else:
                name += s[i]

            i += 1

        s = name

    return s if s else "Empty String"


if __name__ == "__main__":
    print(superReducedString("abba"))