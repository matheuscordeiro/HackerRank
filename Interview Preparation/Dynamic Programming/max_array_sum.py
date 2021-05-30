# Option 1 (recursion) - Time Error
# def maxSubsetSum(arr):
#     max_sum = 0
#     cache = {}
#     for key, _ in enumerate(arr):
#         max_sum = max(max_sum, max_subset(arr, key, cache))

#     return max_sum


# def max_subset(arr, pos, cache):
#     if pos >= len(arr):
#         return 0

#     if pos in cache:
#         return cache[pos]
#
#     cache[pos] = arr[pos] + max(max_subset(arr, pos+2, cache), max_subset(arr, pos+3, cache))
#     return cache[pos]

def maxSubsetSum(arr):
    memo = [0]*(len(arr)+2)
    for key in range(len(arr)-1, -1, -1):
        memo[key] = max(arr[key]+memo[key+2], memo[key+1])

    return memo[0]


if __name__ == "__main__":
    # array = [-2,1,3,-4,5]
    # array = [3,7,4,6,5]
    # array = [2,1,5,8,4]
    array = [3,5,-7,8,10]
    print(maxSubsetSum(array))
    