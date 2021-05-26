cache = {}

def stepPerms(n):
    if n == 0:
        return 1

    if n in cache:
        return cache[n]

    with_one = with_two = with_three = 0
    if n >= 1:
        with_one = stepPerms(n-1)

    if n >= 2:
        with_two = stepPerms(n-2)

    if n >= 3:
        with_three = stepPerms(n-3)

    cache[n] = with_one + with_two + with_three
    return cache[n]


if __name__ == "__main__":
    print(stepPerms(7))