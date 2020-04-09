#!/usr/local/bin/python3


"""Task

Alice is playing an arcade game and wants to climb to the top of the leaderboard and wants to track her ranking. 
The game uses Dense Ranking, so its leaderboard works like this:

	The player with the highest score is ranked number  on the leaderboard.
	Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.

For example, the four players on the leaderboard have high scores of 100, 100, 90, and 80. Those players will have ranks 1, 2, 2, and 3, respectively. 
If Alice's scores are 70, 80 and 105, her rankings after each game are 4, 3 and 1.

Function Description
Complete the climbingLeaderboard function in the editor below. It should return an integer array where each element represents Alice's rank after the  game.
climbingLeaderboard has the following parameter(s):
	scores: an array of integers that represent leaderboard scores
	alice: an array of integers that represent Alice's scores

"""


# Complete the climbingLeaderboard function below.

def perform_rank(scores):
	ranking = {}
	actual = 0
	for index, s in enumerate(scores):
		if not ranking.get(s):
			ranking[s] = actual + 1
			actual += 1

	return ranking

def binary_search(scores, value, ranking):
	init = 0
	end = len(scores) - 1
	result = 1
	while(init <= end):
		middle = int((init+end)/2)
		if scores[init] == value:
			return ranking[scores[init]]
		elif scores[end] == value:
			return ranking[scores[end]]
		elif scores[middle] == value:
			return ranking[scores[middle]]

		if scores[middle] > value:
			init = middle + 1			
			result = ranking[scores[middle]] + 1
		else:
			end = middle - 1
			result = ranking[scores[middle]]

	return result


def climbingLeaderboard(scores, alice):
	ranking = perform_rank(scores)
	return [binary_search(scores, value, ranking) for value in alice]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)
    
    fptr.write('\n'.join(map(str, result)))
    
    fptr.write('\n')

    fptr.close()
