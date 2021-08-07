def strangeCounter(t):
    initial = 3
    j = 3 + 1
    time = 0
    while True:
        time += 1
        j -= 1
        if t > time -1 + initial:
            time += initial -1
            initial = initial * 2
            j = initial + 1
            continue
            
        return j - (t - time)

if __name__ == "__main__":
    print(strangeCounter(17))