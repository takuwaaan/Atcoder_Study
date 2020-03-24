n, k = map(int, input().split())

arr = [int(input()) for _ in range(n)]

arr.sort()

print(arr)
print(arr[k-1:])
print(min(abs(y - x) for x, y in zip(arr, arr[k-1:])))
