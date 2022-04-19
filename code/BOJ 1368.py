# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1368-7ddc8096fa7245c3a4c0f9e37eeb29ce


import heapq
from sys import stdin


class Waterway(object):
  def __init__(self, n, links):
    self.n = n
    self.links = links
    self.dist = 0
    self.parents = [i for i in range(n + 1)]

  def _find(self, num):
    if num != self.parents[num]:
      self.parents[num] = self._find(self.parents[num])
    return self.parents[num]

  def _union(self, nodeA, nodeB):
    rootA, rootB = self._find(nodeA), self._find(nodeB)
    if rootA == rootB:
      return False
    self.parents[rootB] = rootA
    return True

  def _kruskal(self):
    while self.links:
      dist, nodeA, nodeB = heapq.heappop(self.links)
      if self._union(nodeA, nodeB):
        self.dist += dist

  def solve(self):
    self._kruskal()
    self._print()
  
  def _print(self):
    print(self.dist)


if __name__ == "__main__":
  n = int(stdin.readline())

  links = []
  for i in range(1, n+1):
    heapq.heappush(links, (int(stdin.readline()), 0, i))

  for i in range(1, n + 1):
    path = list(map(int, stdin.readline().rstrip().split(" ")))
    for j in range(1, n + 1):
      if i == j:
        continue
      heapq.heappush(links, (path[j-1], i, j))

  Waterway_problem = Waterway(n, links)
  Waterway_problem.solve()
