# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1162-13164d0c70e24554ac3d3bba52111d7c


from sys import stdin
import heapq as H
from math import inf


class Pavement(object):
  def __init__(self, n: int, m: int, k: int, edges: list):
    self.n = n
    self.m = m
    self.k = k
    self.edges = edges
    self.res = -1

  def _init_map(self):
    self.arr = dict()
    for i in range(1, self.n + 1):
      self.arr[i] = []

    for src, dst, cost in self.edges:
      self.arr[src].append((dst, cost))
      self.arr[dst].append((src, cost))

  def _dijkstra(self):
    visited = [[inf]*(self.k+1) for _ in range(self.n+1)]
    que = [(0, 1, 0, 0)]
    while que:
      _cost, _src, _back, _cnt = H.heappop(que)
      if _cost > visited[_src][_cnt]:
        continue

      if _cnt < self.k:
        for _dst, cost in self.arr[_src]:
          if _dst == _back or _cost >= visited[_dst][_cnt+1]:
            continue
          H.heappush(que, (_cost, _dst, _src, _cnt + 1))
          visited[_dst][_cnt+1] = _cost

      for _dst, cost in self.arr[_src]:
        if _dst == _back or _cost+cost >= visited[_dst][_cnt]:
          continue
        H.heappush(que, (_cost + cost, _dst, _src, _cnt))
        visited[_dst][_cnt] = _cost + cost

    self.res = min(visited[-1])

  def _print(self):
    print(self.res)

  def solve(self):
    self._init_map()
    self._dijkstra()
    self._print()


if __name__ == "__main__":
  n, m, k = map(int, stdin.readline().split())
  edges = [map(int, stdin.readline().split()) for _ in range(m)]  

  Pavement_problem = Pavement(n, m, k, edges)
  Pavement_problem.solve()
