# dp program to find minimum length of array to find target sum (repetition allowed)

def shortest_target_sum(arr, target, mem):
	if target in mem:
		return mem[target]
	if target == 0:
		return []
	if target < 0:
		return None
	shortest = None
	for x in arr:
		remainder = target - x
		remainder_combination = shortest_target_sum(arr, remainder, mem)
		if remainder_combination is not None:
			ans = [x for x in remainder_combination]
			ans.append(x)
			combination = ans
			if shortest is None or len(shortest) > len(combination):
				shortest = combination
	mem[target] = shortest
	return shortest

arr = list(map(int, input().split()))
target = int(input())
ans = []
print(shortest_target_sum(arr, target, mem))