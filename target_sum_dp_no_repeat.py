# A target value is given and an array of numbers is given, find if target is sum is achieveable by using subset of 
# array.
def targetSum(target, arr, n, mem):
	if target in mem:
		return mem[target]
	if target == 0:
		return True
	if target < 0 or n == 0:
		return False
	if target - arr[n - 1] < 0:
		mem[target] = targetSum(target, arr, n - 1, mem)
		return mem[target]
	mem[target] = targetSum(target, arr, n - 1, mem) or targetSum(target - arr[n - 1], arr, n - 1, mem)
	return mem[target]

arr = list(map(int, input().split()))
target = int(input())
print(targetSum(target, arr, len(arr), {}))