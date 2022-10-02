# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/4792-9f91c67d4eb342d594d08e4895ab83d2


from sys import stdin


class RedBlueTree(object):
  def __init__(self, n: int, m: int, k: int, edges: list):
    self.n = n
    self.m = m
    self.k = k
    self.edges = sorted(edges)
    self.res = []

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
    self.parents = [i for i in range(self.n + 1)]
    for color, src, dst in self.edges:
      if self._union(src, dst) and color:
        cnt += 1
    self.res.append(cnt)

  def _print(self):
    self.res.sort()
    if self.res[0] <= self.k <= self.res[1]:
      print(1)
    else:
      print(0)

  def solve(self):
    self._kruskal()
    self.edges = self.edges[::-1]
    self._kruskal()
    self._print()


if __name__ == "__main__":
  while True:
    n, m, k = map(int, stdin.readline().rstrip().split())
    if n == m == k == 0:
      break

    edges = []
    for _ in range(m):
      color, src, dst = stdin.readline().rstrip().split()
      edges.append([True if color == "B" else False, int(src), int(dst)])

    RedBlueTree_problem = RedBlueTree(n, m, k, edges)
    RedBlueTree_problem.solve()
