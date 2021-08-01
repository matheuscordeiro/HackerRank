def is_odd(value):
    return value % 2 != 0

def fairRations(B):
    loaf = 0
    while True:
        odd = 0
        for b in B:
            if is_odd(b):
                odd += 1

        if odd == 0:
            return f"{loaf}"
        elif is_odd(odd):
            return "NO"
        else:
            for key, value in enumerate(B):
                if is_odd(value):
                    B[key] = value + 1
                    B[key+1] = B[key+1] + 1
                    loaf += 2
                    break

if __name__ == "__main__":
    print(fairRations([1,2,3]))