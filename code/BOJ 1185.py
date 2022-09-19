# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1185-a75259023d1a41d590994e6e3e491492


from sys import stdin
import heapq as H


class EUTrip(object):
  def __init__(self, n: int, m: int, nodes: list, edges: list):
    self.n = n
    self.m = m
    self.nodes = [0] + nodes
    self.edges = edges
    self.res = min(nodes)

  def _init_map(self):
    self.arr = {i:[] for i in range(self.n + 1)}
    for i, j, k in self.edges:
      weight = (2 * k) + self.nodes[i] + self.nodes[j]
      self.arr[i].append((weight, i, j))
      self.arr[j].append((weight, j, i))

    del self.nodes, self.edges

  def _prim(self, src: int):
    visited = [False] * (self.n + 1)
    visited[src] = True

    que = self.arr[src]
    H.heapify(que)
    while que:
      dist, _src, _dst = H.heappop(que)
      if visited[_dst]:
        continue
      visited[_dst] = True
      self.res += dist

      for next_dist, _, _next in self.arr[_dst]:
        if visited[_next]:
          continue
        H.heappush(que, (next_dist, _dst, _next))

  def _print(self):
    print(self.res)

  def solve(self):
    self._init_map()
    self._prim(src = 1)
    self._print()


if __name__ == "__main__":
  n, m = map(int, stdin.readline().rstrip().split())
  nodes = [int(stdin.readline().rstrip()) for _ in range(n)]
  edges = [map(int, stdin.readline().rstrip().split()) for _ in range(m)]

  EUTrip_problem = EUTrip(n, m, nodes, edges)
  EUTrip_problem.solve()
