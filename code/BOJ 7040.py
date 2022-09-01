# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/7040-ef60b82cc3b14dff848741071334bcbe


from sys import stdin


class CowMealTime(object):
  def __init__(self, n: int, edges: list):
    self.n = n
    self.edges = edges
    for _ in range(2, self.n):
      edges.append([_, _-1, 0])
    self.inf = int(1e9)
    self.arr = [0, 0] + [self.inf for _ in range(1, self.n)]
    self.pos = 0

  def _bellman(self):
    for _ in range(self.n - 1):
      for src, dst, cost in self.edges:
        if self.arr[src] < self.inf:
          self.arr[dst] = min(self.arr[dst], self.arr[src] + cost)
      if self.arr[1] < 0:
        self.pos = -1
        return

    _chk = self.arr[-1]
    for src, dst, cost in self.edges:
      if self.arr[dst] > self.arr[src] + cost:
        self.arr[dst] = self.arr[src] + cost
        self.pos = -1
    if _chk < self.arr[-1] or _chk == self.inf:
      self.pos = -2

  def _print(self):
    if self.pos != 0:
      print(self.pos)
    else:
      print(self.arr[-1])

  def solve(self):
    self._bellman()
    self._print()


if __name__ == "__main__":
  N, ML, MD = map(int, stdin.readline().split())
  edges = []
  for _ in range(ML):
    a, b, k = map(int, stdin.readline().split())
    edges.append([a, b, k])
  for _ in range(MD):
    a, b, k = map(int, stdin.readline().split())
    edges.append([b, a, -k])


  CowMealTime_problem = CowMealTime(N, edges)
  CowMealTime_problem.solve()
