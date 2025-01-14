n, l = map(int,input().split())
k = int(input())
a = list(map(int,input().split()))
left = 0
right = l
num = 0
mid = 0
while mid != (left+right)//2:
 mid = (left+right)//2
 num = 0
 cut = 0
 for i in range(len(a)):
  if a[i]-cut-mid >= 0:
   cut = a[i]
   num += 1
  if i == len(a)-1:
   if l-cut < mid:
    num = num-1 
 if num < k:
  right = mid
 elif num >= k:
  left = mid
print(mid)
