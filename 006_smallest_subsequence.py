n, k = map(int, input().split())
s = list(input())
before = 0
ans = []
for i in range(k):
    temp = min(s[before:n-k+i+1])
    ans.append(temp)
    before = s.index(temp, before)+1
print("".join(ans))