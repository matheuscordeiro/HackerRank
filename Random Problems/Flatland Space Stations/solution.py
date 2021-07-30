def flatlandSpaceStations(n, c):
    c = sorted(c)
    maximum = c[0]
    for i in range(1, len(c)):
        maximum = max(maximum, int((c[i]-c[i-1])/2))

    lastGap = n-1-c[-1]
    return max(maximum, lastGap)


if __name__ == "__main__":
    print(flatlandSpaceStations(5, [0, 4]))