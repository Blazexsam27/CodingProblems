# A target value is given and an array of numbers is given, find if target is sum is achieveable by using subset of 
# array.
# RETURN THE ACTUAL SUBSET.

def target_sum_subset(arr, target, n, mem):
	if target in mem:
		return mem[target]
	ans = []
	if target == 0:
		return []
	if n == 0:
		return None
	if target - arr[n - 1] >= 0:
		result = target_sum_subset(arr, target - arr[n - 1], n - 1, mem)
	else:
		result = target_sum_subset(arr, target, n - 1, mem)
	if result is not None:
		ans = [x for x in result]
		ans.append(arr[n - 1])
		mem[target] = ans
		return ans
	return None

arr = list(map(int, input().split()))
target = int(input())
ans = []
print(target_sum_subset(arr, target, len(arr), {}))