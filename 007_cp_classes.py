n = int(input())
a = list(map(int, input().split()))
q = int(input())
for _ in range(q):
    b = int(input())
    left = 0
    right = n
    while left < right:
        mid = (left + right) // 2
        if a[mid] < b:
            left = mid + 1
        else:
            right = mid