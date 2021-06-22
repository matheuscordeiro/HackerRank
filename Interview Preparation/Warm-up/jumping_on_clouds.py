def jumpingOnClouds(c):
    count = i = 0
    while i < len(c)-1:
        if (i + 2) < len(c) and c[i+2] == 0:
            i += 2
        else:
            i += 1

        count += 1
    
    return count


if __name__ == "__main__":
    array = [0, 0, 0, 0, 1, 0]
    print(jumpingOnClouds(array))
