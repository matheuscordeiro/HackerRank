
# 3D Surface Area
# Difficulty: Medium

def surfaceArea(A):
    rows = len(A)
    cols = len(A[0])
    area = 0
    for i in range(rows):
        for j in range(cols):

            top = 1
            bottom = 1
            
            # front
            if i > 0:
                if A[i][j] > A[i-1][j]:
                    front = A[i][j] - A[i-1][j]
                else:
                    front = 0
            else:
                front = A[i][j]

            # back
            if i + 1 < rows:
                if A[i][j] > A[i+1][j]:
                    back = A[i][j] - A[i+1][j]
                else:
                    back = 0
            else:
                back = A[i][j]

            # left
            if j > 0:
                if A[i][j] > A[i][j-1]:
                    left = A[i][j] - A[i][j-1]
                else:
                    left = 0
            else:
                left = A[i][j]

            # right
            if j + 1 < cols:
                if A[i][j] > A[i][j+1]:
                    right = A[i][j] - A[i][j+1]
                else:
                    right = 0
            else:
                right = A[i][j]

            area += top + bottom + front + back + left + right

    return area


if __name__ == "__main__":
    print(surfaceArea([[1,3,4],[2,2,3],[1,2,4]]))