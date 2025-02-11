import sys
import io
_INPUT = """\
41
btwogablwetwoiehocghiewobadegwhoihegnldir
"""
sys.stdin = io.StringIO(_INPUT)
n = int(input())
s = list(input())
target = list("atcoder")
mod = 10**9 + 7
temp = [[] for _ in range(7)]

def check(p,last,ans, count):
    # 終了処理
    if count == len(temp[0]):
        return ans
    # 主処理
    for i in range(len(temp[p])):
        if temp[p][i] > last:
            if p == 6:
                ans = ans + 1
                count = count + 1
                p = 0
            check(p+1,temp[p][i],ans,count)

                          
for i in range(n):
    for j in range(7):
        if s[i] == target[j]:
            temp[j].append(i)

print(check(0,0,0,0))

