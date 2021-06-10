def getWays(n, c):
    ways = [0] * (n+1)
    ways[0] = 1
    for i, coin in enumerate(c):
        for j in range(len(ways)):
            if coin <= j:
                ways[j] += ways[j-coin]

    return ways[-1]


if __name__ == "__main__":
    # print(getWays(4, [1,2,3]))
    print(getWays(10, [2,5,3,6]))
    