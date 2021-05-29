def candies(n, arr):
    candie = [1]*n
    for key in range(1, n):
        if arr[key] > arr[key-1]:
            candie[key] = candie[key-1] + 1

    for key in range(n-1, 0, -1):
        if arr[key] < arr[key-1]:
            candie[key-1] = max(candie[key-1], candie[key]+1) 

    return sum(candie)

if __name__ == "__main__":
    # arr = [3,2,1]
    # arr = [9,4,4,5,4,3,2,1,6]
    # arr = [2,4,3,5,2,6,4,5]
    arr = [2,4,2,6,1,7,8,9,2,1]
    print(candies(10, arr))