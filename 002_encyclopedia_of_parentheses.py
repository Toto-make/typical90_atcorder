n = int(input())
ans = []
for i in range(2**n):
    count = 0
    temp = []
    for x in range(n):
        if ((i >> x) & 1):
            count += 1
            temp.append("(")
        else:
            count -= 1
            temp.append(")")
        if count < 0:
            break
        elif (x == n-1)&(count == 0):
            ans.append("".join(temp))
ans = sorted(ans)
for i in ans:
    print(i)
