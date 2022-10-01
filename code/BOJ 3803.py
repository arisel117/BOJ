# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/3803-Networking-048c2fea95c3463faa00185aa1f6216f


from sys import stdin
import heapq as H


class Networking(object):
  def __init__(self, n: int, m: int, edges: list):
    self.n = n
    self.m = m
    self.edges = edges
    self.parents = [i for i in range(self.n + 1)]
    self.res = 0

  def _init_map(self):
    self.que = []
    for src, dst, dist in self.edges:
      H.heappush(self.que, (dist, src, dst))
    H.heapify(self.que)

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
    while self.que:
      dist, src, dst = H.heappop(self.que)
      if self._union(src, dst):
        self.res += dist

  def _print(self):
      print(self.res)

  def solve(self):
    self._init_map()
    self._kruskal()
    self._print()


if __name__ == "__main__":
  while True:
    nm = stdin.readline().rstrip()
    if nm == "0":
      break
    n, m = map(int, nm.split())
    edges = [list(map(int, stdin.readline().rstrip().split())) for _ in range(m)]
    stdin.readline()

    Networking_problem = Networking(n, m, edges)
    Networking_problem.solve()
