# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1506-dbf160e2b2044c079fe44179d16a8b37


from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)


class PoliceStation(object):
  def __init__(self, n: int, prices: list, edges: list):
    self.n = n
    self.prices = prices
    self.edges = edges
    self.idx = 0
    self.history = []
    self.low = [-1] * (self.n)
    self.ids = [-1] * (self.n)
    self.visited = [False] * (self.n)
    self.sccs = []
    self.res = 0

  def _init_map(self):
    self.arr = {i:[] for i in range(self.n)}
    for src, v in enumerate(self.edges):
      for dst, k in enumerate(v):
        if k == '1':
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
      self.sccs.append(scc)

  def _print(self):
    for v in self.sccs:
      self.res += min([self.prices[i] for i in v])
    print(self.res)

  def solve(self):
    self._init_map()
    for i in range(self.n):
      if self.ids[i] == -1:
        self.rec(i)
    self._print()


if __name__ == "__main__":
  n = int(stdin.readline().rstrip())
  prices = list(map(int, stdin.readline().rstrip().split()))
  edges = [list(stdin.readline().rstrip()) for _ in range(n)]

  PoliceStation_problem = PoliceStation(n, prices, edges)
  PoliceStation_problem.solve()
