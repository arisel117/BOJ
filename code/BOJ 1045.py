# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1045-06e56d6bc65d4467842085d16fe166e2


from sys import stdin
from collections import deque


class NLoad(object):
  def __init__(self, n: int, m: int, edges: list):
    self.n = n
    self.m = m
    self.edges = edges
    self.parents = [i for i in range(self.n)]
    self.mst = [0] * self.n
    self.pos = True

  def _init_map(self):
    cnt = 0
    self.que = deque()
    for src in range(self.n):
      for dst in range(src + 1, self.n):
        if self.edges[src][dst] == "Y":
          self.que.append((src, dst))
          cnt += 1

    if cnt < self.m:
      self.pos = False

  def _find(self, node):
    if self.parents[node] == node:
      return node
    else:
      self.parents[node] = self._find(self.parents[node])
      return self.parents[node]

  def _union(self, src, dst):
    src, dst = sorted([self._find(src), self._find(dst)])
    if src == dst:
      return False
    else:
      self.parents[dst] = src
      return True

  def _kruskal(self):
    cnt = 0
    extra = self.m - self.n + 1
    while self.que:
      src, dst = self.que.popleft()
      if self._union(src, dst):
        cnt += 1
      else:
        if extra > 0:
          extra -= 1
        else:
          continue
      self.mst[src] += 1
      self.mst[dst] += 1

    if cnt < self.n - 1:
      self.pos = False

  def _print(self):
    if self.pos:
      print(*self.mst, sep=" ")
    else:
      print(-1)

  def solve(self):
    self._init_map()
    if self.pos:
      self._kruskal()
    self._print()


if __name__ == "__main__":
  n, m = map(int, stdin.readline().rstrip().split())
  edges = [list(stdin.readline().rstrip()) for _ in range(n)]

  NLoad_problem = NLoad(n, m, edges)
  NLoad_problem.solve()
