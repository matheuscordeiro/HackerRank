
# Larry's Array
# Difficulty: Medium

# Algorithm based on 15 Puzzle

def larrysArray(A):
    size_a = len(A)
    inversions = 0
    for i in range(size_a):
        for j in range(i+1, size_a):
            if A[i] > A[j]:
                inversions += 1

    return "YES" if inversions % 2 == 0 else "NO"


if __name__ == "__main__":
    print(larrysArray([1,2,3,5,4]))