def separateNumbers(s):
    max_value = round(len(s)/2)
    for i in range(1, max_value+1):
        value = s[0:i]
        if len(value) > 1 and value[0] == "0":
            break
        elif check(s, value, i):
            print(f"YES {value}")
            return

    print("NO")


def check(s:str, before:str, initial:int) -> bool:
    before_number = int(before)
    found = False
    value = ""
    for i in range(initial, len(s)):
        value = s[initial:i+1]
        if len(value) > 1 and value[0] == "0":
            break

        if len(value) - len(before) > 1:
            break

        if int(value) == before_number + 1:
            found = True
            break

    if found:
        if i == len(s)-1:
            return True
        else:
            return check(s, value, i+1)
    else:
        return False


if __name__ == "__main__":
    separateNumbers("010203")
