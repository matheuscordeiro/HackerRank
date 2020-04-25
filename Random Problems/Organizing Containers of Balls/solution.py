#!/usr/local/bin/python3

import math

# Complete the organizingContainers function below.
def organizingContainers(container):
	count_container = [sum(row) for row in container]
	count_color = [0] * len(container)
	n = len(container)
	for i in range(n):
		for j in range(n):
			count_color[j] += container[i][j] 

	count_container = sorted(count_container)
	count_color = sorted(count_color)
	return 'Possible' if count_container == count_color else 'Impossible'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
