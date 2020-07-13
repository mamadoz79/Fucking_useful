def dfs(v):
  res = a[v]
  vis[v]=1
  for u in adj[v]:
    if vis[u] == 0:
      res = min(res,dfs(u))
  return res

n, m, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
vis=[0]*n
ans=0
for i in range(n):
  ans+=min(k,a[i])
adj=[[] for i in range(n)]
for i in range(m):
  x,y = [int(i) for i in input().split()]
  adj[x-1].append(y-1)
  adj[y-1].append(x-1)
for i in range(n):
  if vis[i] == 0:
    d=dfs(i)
    if d>k:
      ans+=d-k
print(ans)
