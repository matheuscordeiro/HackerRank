def connectedCell(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False] * cols for i in range(rows)]
    max_area = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and not visited[i][j]:
                max_area = max(max_area, count_islands(i,j,matrix,visited))

    return max_area


def is_bound(i, j, matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    return i >= 0 and j >= 0 and i < rows and j < cols


def count_islands(i, j, matrix, visited):
    islands = [(i,j)]
    visited[i][j] = True
    count = 0
    while islands:
        count += 1
        i, j = islands.pop()
        positions = [(i,j+1), (i,j-1), (i+1,j), (i-1,j), (i+1,j+1), (i-1,j-1), (i+1,j-1), (i-1, j+1)]
        for pi, pj in positions:
            if is_bound(pi,pj, matrix) and matrix[pi][pj] == 1 and not visited[pi][pj]:
                islands.append((pi,pj))
                visited[pi][pj] = True

    return count


if __name__ == "__main__":
    matrix = [
        [1,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [1,0,0,0]
    ]
    print(connectedCell(matrix))
