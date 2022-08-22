# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1719-252e0362d32c4cb88d11e8b8d9d45a4c


from sys import stdin


class Parcel(object):
  def __init__(self, n: int, m: int, arr: list):
    self.n = n
    self.m = m
    self.arr = arr
    self.INF = int(1e7)
    self._map = [[self.INF]*(self.n+1) for _ in range(self.n+1)]
    self._back = [[-1]*(self.n+1) for _ in range(self.n+1)]

  def _init_map(self):
    for src, dst, k in self.arr:
      if self._map[src][dst] > k:
        self._map[src][dst] = k
        self._back[src][dst] = dst
      if self._map[dst][src] > k:
        self._map[dst][src] = k
        self._back[dst][src] = src
    

  def _floyd(self):
    for k in range(1, self.n+1):
      for i in range(1, self.n+1):
        for j in range(1, self.n+1):
          if self._map[i][j] > self._map[i][k] + self._map[k][j]:
            self._map[i][j] = self._map[i][k] + self._map[k][j]
            self._back[i][j] = self._back[i][k]

    for i in range(1, self.n+1):
      self._back[i][i] = "-"

  def _print(self):
    for _l in self._back[1:]:
      print(*_l[1:])

  def solve(self):
    self._init_map()
    self._floyd()
    self._print()


if __name__ == "__main__":
  n, m = map(int, stdin.readline().split())
  arr = [list(map(int, stdin.readline().split())) for _ in range(m)]

  Parcel_problem = Parcel(n, m, arr)
  Parcel_problem.solve()
