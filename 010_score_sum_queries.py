n = int(input())
one_list = [0]
two_list = [0]
one = 0
two = 0
for i in range(n):
    c, p = map(int, input().split())
    if c == 1:
        one = one + p
    elif c == 2:
        two = two + p
    one_list.append(one)
    two_list.append(two)
q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    print(one_list[r] - one_list[l-1], two_list[r] - two_list[l-1])