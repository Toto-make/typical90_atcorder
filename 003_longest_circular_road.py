import sys
sys.setrecursionlimit(10**6)
n = int(input())
path_list = [[] for i in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    path_list[a-1].append(b-1)
    path_list[b-1].append(a-1)

def dfs(start, graph, count = 0, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    farthest_node  = start
    longest_distance = count
    for i in graph[start]:
        if i not in visited:
            node, distance = dfs(i, graph, count+1, visited)
            if distance > longest_distance:
                farthest_node = node
                longest_distance = distance
    return farthest_node, longest_distance
        
x, _ = dfs(0, path_list)
_,y = dfs(x, path_list)
ans = y+1
print(ans)
