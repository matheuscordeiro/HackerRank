def funnyString(s):
    for i in range(len(s)-1):
        j = len(s)-2-i
        if abs(ord(s[i])-ord(s[i+1])) != abs(ord(s[j+1])-ord(s[j])):
            return "Not Funny"

    return "Funny"


if __name__ == "__main__":
    print(funnyString("lmnop"))
