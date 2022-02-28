# Given an array we can only take alternate positions, find the max value.

def max_value(arr, n, mem):
    if n in mem:
        return mem[n]
    if n == 1:
        return arr[0]
    if n == 0:
        return 0
    mem[n] = max(max_value(arr, n - 2, mem) + arr[n - 1], max_value(arr, n - 1, mem))
    return mem[n]

arr = list(map(int, input().split()))
print(max_value(arr, len(arr), {}))