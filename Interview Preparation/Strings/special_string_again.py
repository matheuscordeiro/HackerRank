def substrCount(n, s):
    total = n
    for i in range(1, n):
        left = i-1
        right = i+1
        if s[i] != s[left]:
            j = left
            k = right
            previous = s[left]
            while j >= 0 and k < n and s[j] == s[k] == previous:
                total += 1
                j -= 1
                k += 1
        else:
            j = left
            while j >= 0 and s[i] == s[j]:
                total += 1
                j -= 1

    return total


if __name__ == "__main__":
    s = ""
    print(substrCount(7, "abcbaba"))