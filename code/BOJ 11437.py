# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/11437-LCA-916c605e73d543a78c4b85b6cb4fc8e7


import sys
sys.setrecursionlimit(100000)

class Lca(object):
  def __init__(self, n, graph, req):
    self.n = n
    self.g = graph
    self.req = req
    self.visited = [0] * (n + 1)
    self.parent = [0] * (n + 1)
    self.d = [0] * (n + 1)
    self.res = []

  def _dfs(self, x, depth):
    self.visited[x] = True
    self.d[x] = depth
    for node in graph[x]:
      if self.visited[node]:
        continue
      self.parent[node] = x
      self._dfs(node, depth + 1)

  def _lca(self, a, b):
    while self.d[a] != self.d[b]:
      if self.d[a] > self.d[b]:
        a = self.parent[a]
      else:
        b = self.parent[b]
    while a != b:
      a = self.parent[a]
      b = self.parent[b]
    return a

  def _print(self):
    for i in self.res:
      print(i)

  def solve(self):
    self._dfs(1, 0)
    for a, b in self.req:
      self.res.append(self._lca(a, b))
    self._print()


if __name__ == "__main__":
  n = int(sys.stdin.readline().rstrip())
  graph = [[] for _ in range(n + 1)]
  for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

  m = int(sys.stdin.readline().rstrip())
  req = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
  
  Lca_problem = Lca(n, graph, req)
  Lca_problem.solve()
