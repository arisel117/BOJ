# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/6091-5d3ee927b1114176892e4a298c9aae71


from sys import stdin
import heapq as H


class PinkFloyd(object):
  def __init__(self, n: int, _map: list):
    self.n = n
    self._map = _map
    self.parents = [i for i in range(self.n + 1)]
    self.mst = [[] for _ in range(self.n + 1)]

  def _find(self, node):
    if self.parents[node] == node:
      return node
    else:
      self.parents[node] = self._find(self.parents[node])
      return self.parents[node]

  def _union(self, src, dst):
    src, dst = self._find(src), self._find(dst)
    if src == dst:
      return False
    else:
      self.parents[dst] = src
      return True

  def _kruskal(self):
    que = []
    for src in range(1, self.n):
      for dst, cost in zip(range(src + 1, self.n + 1), self._map[src - 1]):
        H.heappush(que, [cost, src, dst])

    while que:
      cost, src, dst = H.heappop(que)
      if self._union(src, dst):
        self.mst[src].append(dst)
        self.mst[dst].append(src)

  def _print(self):
    for _idx in range(1, self.n + 1):
      print(len(self.mst[_idx]), *(sorted(self.mst[_idx])), sep=' ')

  def solve(self):
    self._kruskal()
    self._print()


if __name__ == "__main__":
  n = int(stdin.readline().rstrip())
  _map = [list(map(int, stdin.readline().rstrip().split())) for src in range(n - 1)]

  PinkFloyd_problem = PinkFloyd(n, _map)
  PinkFloyd_problem.solve()
