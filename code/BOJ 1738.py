# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1738-26819835f6a743e38a6ccdf807fae12e


from sys import stdin
from math import inf


class Alleyway(object):
  def __init__(self, n: int, m: int, edges: list):
    self.n = n
    self.m = m
    self.edges = edges
    self.arr = [-inf]*(self.n + 1)
    self.path = [-1]*(self.n + 1)

  def _bellman(self):
    self.arr[1] = 0
    for _ in range(self.n - 1):
      for src, dst, cost in self.edges:
        new_cost = self.arr[src] + cost
        if self.arr[dst] < new_cost:
          self.arr[dst] = new_cost
          self.path[dst] = src

    for src, dst, cost in self.edges:
      if self.arr[dst] < self.arr[src] + cost:
        self.arr[dst] = inf

  def _routing(self):
    self._route = [self.n]
    if self.arr[self.n] == inf:
      self._route = [-1]
    else:
      while True:
        _idx = self.path[self._route[-1]]
        if _idx == -1:
          break
        else:
          self._route.append(_idx)

  def _print(self):
    print(*self._route[::-1])

  def solve(self):
    self._bellman()
    self._routing()
    self._print()


if __name__ == "__main__":
  n, m = map(int, stdin.readline().split())
  edges = [list(map(int, stdin.readline().split())) for _ in range(m)]

  Alleyway_problem = Alleyway(n, m, edges)
  Alleyway_problem.solve()
