h,w = map(int, input().split())
a_list = []
a_i = []
a_j = [0 for i in range(w)]
for i in range(h):
    a = list(map(int, input().split()))
    a_i.append(sum(a))
    a_j = [a_j[j]+a[j] for j in range(w)]
    a_list.append(a)
ans_all = []
for i in range(h):
    ans = []
    for j in range(w):
        ans.append(a_i[i]+a_j[j]-a_list[i][j])
    ans_all.append(ans)
for i in range(h):
    print(*ans_all[i])