def beautifulDays(i, j, k):
    count = 0
    for day in range(i, j+1):
        reverse = int(str(day)[::-1])
        if abs(day-reverse) % k == 0:
            count += 1

    return count


if __name__ == "__main__":
    print(beautifulDays(20, 23, 6))