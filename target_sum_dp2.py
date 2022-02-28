def targetSum(arr, target, ans, mem):
	if mem.get(target, 0):
		return mem[target]
	if target == 0:
		return []
	if target < 0:
		return None
	for x in arr:
		remainder = target - x
		remainderResult = targetSum(arr, remainder, ans, mem) 
		if remainderResult != None:
			ans.append(x)
			mem[target] = ans
			return ans
	mem[target] = None
	return None

# returns the possible subsets.
def target_sum_tabulation(arr, target):
	dp = [None] * (target + 1)
	dp[0] = []
	for i in range(target + 1):
		if dp[i] is not None:
			for x in arr:
				if i + x < target + 1:
					dp[i + x] = [y for y in dp[i]] + [x]
	return dp


ans = []
arr = list(map(int, input().split()))
target = int(input())
# print(targetSum(arr, target, ans, {}))
print(target_sum_tabulation(arr, target))