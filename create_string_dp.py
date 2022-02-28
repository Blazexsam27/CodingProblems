# given a target string and list of strings/chars. write program to find whether string can be created using 
# contents of string or not.

def can_create_string(target_string, arr, mem):
	if target_string in mem:
		return mem[target_string]
	if target_string == "":
		return True
	for x in arr:
		if target_string.find(x) == 0:
			remainder = target_string[len(x):]
			if can_create_string(remainder, arr):
				mem[target_string] = True
				return True
	mem[target_string] = False
	return False



target_string = input()
arr = list(map(str, input().split()))
print(can_create_string(target_string, arr, {}))