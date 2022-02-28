# given array numbers that can be used repetitively .
# this is similar to coin change problem.
def targetSum(arr, target, mem):
	if target in mem:
		return mem[target]
	if target == 0:
		return True
	if target < 0:
		return False

	for x in arr:
		remainder = target - x
		if targetSum(arr, remainder, mem):
			mem[target] = True
			return True
	mem[target] = False
	return False

arr = list(map(int, input().split()))
target = int(input())
print(targetSum(arr, target, {}))