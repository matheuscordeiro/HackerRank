def happyLadybugs(b):
    letters = {}
    order = True
    underscore = False
    for key, value in enumerate(b):
        if key > 0 and key < len(b)-1:
             if b[key-1] != value and b[key+1] != value:
                order = False
        elif key > 0 and b[key-1] != value:
            order = False
        elif key < len(b) - 1 and b[key+1] != value:
            order = False

        if value == "_":
            underscore = True
        else:
            letters[value] = letters.get(value, 0) + 1

    for key, value in letters.items():
        if value == 1 or (not underscore and not order):
            return "NO"

    return "YES"


if __name__ == "__main__":
    print(happyLadybugs("XXYYY"))
