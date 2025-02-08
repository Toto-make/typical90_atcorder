n = int(input())
a = sorted(list(map(int, input().split())))
q = int(input())
for _ in range(q):
    b = int(input())
    left = 0
    right = n-1
    before_mid = 0
    judge = True
    while judge:
        mid = (left + right) // 2
        if a[mid] < b:
            left = mid
        elif a[mid] > b:
            right = mid
        if before_mid == mid:
          judge = False
        else:
          before_mid = mid
    if mid < n-1:
      print(min(abs(a[mid]-b),abs(a[mid+1]-b)))
    else:
      print(abs(a[mid]-b))