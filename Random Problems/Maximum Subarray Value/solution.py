import math

def solution(arr):
    sum_even = sum_odd = 0
    max_value = 0
    for key, value in enumerate(arr):
        if key % 2 == 0:  # even
            sum_even += value
            result = int(math.pow(sum_even-sum_odd, 2))
            if result > max_value:
                max_value = result
            elif result < 0:
                sum_even = sum_odd = 0
        else:  # odd
            sum_odd += value
            result = int(math.pow(sum_even-sum_odd, 2))
            if result > max_value:
                max_value = result
            elif result < 0:
                sum_even = sum_odd = 0

    return max_value


if __name__ == "__main__":
    # arr = [2, -1, -4, 5]
    # arr = [-1, 2, 3, 4, -5]
    arr = [1, -1, 1, -1, 1]
    print(solution(arr))