def hackerrankInString(s):
    name = "hackerrank"
    i = 0
    for character in s:
        if character == name[i]:
            i += 1

        if i == len(name):
            return "YES"

    return "NO"


if __name__ == "__main__":
    print(hackerrankInString("rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt"))