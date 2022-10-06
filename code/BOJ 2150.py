# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/2150-Strongly-Connected-Component-1c1f7a957c3a4fa8b91f845d15d61b5c


from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)


class StrongConnectComp(object):
  def __init__(self, n: int, m: int, edges: list):
    self.n = n
    self.m = m
    self.edges = edges
    self.idx = 0
    self.history = []
    self.low = [-1] * (self.n + 1)
    self.ids = [-1] * (self.n + 1)
    self.visited = [False] * (self.n + 1)
    self.sccs = []

  def _init_map(self):
    self.arr = {i:[] for i in range(self.n + 1)}
    for src, dst in self.edges:
      self.arr[src].append(dst)
    del self.edges

  def rec(self, dst):
    self.ids[dst] = self.idx
    self.low[dst] = self.idx
    self.idx += 1
    self.visited[dst] = True
    self.history.append(dst)

    for ndst in self.arr[dst]:
      if self.ids[ndst] == -1:
        self.rec(ndst)
        self.low[dst] = min(self.low[dst], self.low[ndst])
      elif self.visited[ndst]:
        self.low[dst] = min(self.low[dst], self.ids[ndst])

    w = -1
    scc = []
    if self.low[dst] == self.ids[dst]:
      while w != dst:
        w = self.history.pop()
        scc.append(w)
        self.visited[w] = False
      self.sccs.append(sorted(scc))

  def _print(self):
    print(len(self.sccs))
    for i in sorted(self.sccs):
      print(*sorted(i), -1)

  def solve(self):
    self._init_map()
    for i in range(1, self.n + 1):
      if self.ids[i] == -1:
        self.rec(i)
    self._print()


if __name__ == "__main__":
  n, m = map(int, stdin.readline().rstrip().split())
  edges = [list(map(int, stdin.readline().rstrip().split())) for _ in range(m)]

  StrongConnectComp_problem = StrongConnectComp(n, m, edges)
  StrongConnectComp_problem.solve()
