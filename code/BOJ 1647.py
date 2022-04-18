# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1647-c96bcdce5e284c909ab1d9a804d681b0


from sys import stdin


class MST(object):
  def __init__(self, n, m, edges):
    self.n = n
    self.m = m
    self.edges = sorted(edges)
    self.parents = {i:i for i in range(1, self.n+1)}
    self.total_dist = []

  def _find(self, num):
    if num != self.parents[num]:
      self.parents[num] = self._find(self.parents[num])
    return self.parents[num]

  def _union(self, pA, pB):
    if pA < pB :
      self.parents[pB] = pA
    else:
      self.parents[pA] = pB

  def _kruskal(self):
    for _dist, _nodeA, _nodeB in self.edges:
      pA = self._find(_nodeA)
      pB = self._find(_nodeB)
      if pA != pB:
        self._union(pA, pB)
        self.total_dist.append(_dist)

  def _print(self):
    print(sum(self.total_dist) - max(self.total_dist))

  def solve(self):
    self._kruskal()
    self._print()


if __name__ == "__main__":
  n, m = map(int, stdin.readline().split())
  edges = []
  for _ in range(m):
    edge = list(map(int, stdin.readline().split()))
    edges.append((edge[2], edge[0], edge[1]))
  
  MST_problem = MST(n, m, edges)
  MST_problem.solve()
