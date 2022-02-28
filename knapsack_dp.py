# knapsack problem refers to two arrays, one for weight of object and other for its profit. And a bag which 
# has some capacity, our goal is to maximize profit by choosing optimal objects.

def knapsack(wt_arr, capacity, profit_arr, n):
	dp = [[0 for x in range(n + 1)] for y in range(capacity + 1)]

	for i in range(capacity + 1):
		for j in range(n + 1):
			if i == 0 or j == 0:
				continue
			if wt_arr[i - 1] > capacity:
				dp[i][j] = dp[i - 1][j]
			else:
				dp[i][j] = max(dp[i][j - wt_arr[i - 1]] + profit_arr[i - 1], dp[i - 1][j])
	return dp[capacity][n]