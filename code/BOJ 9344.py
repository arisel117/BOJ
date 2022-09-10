# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/9344-5f00ca58c66c4fd18c0e8530ee8c2c8c


from sys import stdin
import heapq as H


class LoadMST(object):
  def __init__(self, n: int, p: int, q: int, edges: list):
    self.n = n
    self.edges = edges
    self.src = p
    self.dst = q
    self.res = "NO"

  def _init_map(self):
    self.arr = {i:[] for i in range(self.n + 1)}
    for i, j, k in self.edges:
      self.arr[i].append((k, i, j))
      self.arr[j].append((k, j, i))

  def _prim(self):
    visited = [False] * (self.n + 1)
    visited[self.src] = True

    que = self.arr[self.src]
    H.heapify(que)
    mst = set()

    while que:
      now_dist, _src, _dst = H.heappop(que)
      if visited[_dst]:
        continue
      visited[_dst] = True
      mst.add((_src, _dst))

      for next_dist, _, _next in self.arr[_dst]:
        if visited[_next]:
          continue
        H.heappush(que, (next_dist, _dst, _next))

    if (self.src, self.dst) in mst:
      self.res = "YES"
    return 0

  def _print(self):
    print(self.res)

  def solve(self):
    self._init_map()
    self._prim()
    self._print()


if __name__ == "__main__":
  for i in range(int(stdin.readline())):
    n, m, p, q = map(int, stdin.readline().split())
    edges = [list(map(int, stdin.readline().split())) for _ in range(m)]

    LoadMST_problem = LoadMST(n, p, q, edges)
    LoadMST_problem.solve()
