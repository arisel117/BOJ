# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1414-3bdb02f61f664f8ba5012b45c0af0d06


# Python3 통과 코드


from sys import stdin
import heapq as H


class ShortLAN(object):
  def __init__(self, n: int, edges: list):
    self.n = n
    self.edges = edges
    self.n_edges = 0
    self.res = 0

  def _ascii2int(self):
    for i, v in enumerate(self.edges):
      _edge = []
      for k in v:
        weight = ord(k)
        if 65 <= weight <= 90:
          weight = weight - 38 # A=27, Z=52
        elif 97 <= weight <= 122:
          weight = weight - 96 # a=1, z=26
        else: # 0
          weight = 0
        self.res += weight
        _edge.append(weight)
      self.edges[i] = _edge

  def _init_map(self):
    self.arr = {i:[] for i in range(self.n)}
    for i in range(self.n):
      for j in range(i+1, self.n):
        ab = sorted([self.edges[i][j], self.edges[j][i]])
        if ab[0] == 0:
          if ab[1] == 0:
            continue
          else:
            weight = ab[1]
        else:
          weight = ab[0]
        
        self.arr[i].append((weight, i, j))
        self.arr[j].append((weight, j, i))

    if self.n > 1:
      for i in self.arr:
        if len(self.arr[i]) == 0:
          self.res = -1

    del self.edges

  def _prim(self, src: int):
    visited = [False] * (self.n)
    visited[src] = True

    que = self.arr[src]
    H.heapify(que)
    while que:
      dist, _src, _dst = H.heappop(que)
      if visited[_dst]:
        continue
      visited[_dst] = True
      self.res -= dist
      self.n_edges += 1

      for next_dist, _, _next in self.arr[_dst]:
        if visited[_next]:
          continue
        H.heappush(que, (next_dist, _dst, _next))

  def _print(self):
    if self.n_edges == self.n - 1:
      print(self.res)
    else:
      print(-1)

  def solve(self):
    self._ascii2int()
    self._init_map()
    if self.n > 1 and self.res != -1:
      self._prim(src = 0)
    self._print()


if __name__ == "__main__":
  n = int(stdin.readline().rstrip())
  edges = [list(stdin.readline().rstrip()) for _ in range(n)]

  ShortLAN_problem = ShortLAN(n, edges)
  ShortLAN_problem.solve()
