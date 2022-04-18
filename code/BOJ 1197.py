# -*- coding: utf-8 -*-
# 링크 : https://www.notion.so/arisel/1197-19ad731c8a9544aebe42e4c30c25e64c


from sys import stdin


class MST(object):
  def __init__(self, n, m, edges):
    self.n = n
    self.m = m
    self.edges = sorted(edges)
    self.parents = {i:i for i in range(1, self.n+1)}
    self.total_dist = 0

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
        self.total_dist += _dist

  def _print(self):
    print(self.total_dist)

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
