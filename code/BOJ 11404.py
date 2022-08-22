# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/11404-5036d9a060fe41bb929b0185444f2a95


from sys import stdin


class Floyd(object):
  def __init__(self, n: int, m: int, arr: list):
    self.n = n
    self.m = m
    self.arr = arr
    self.INF = int(1e7)
    self._map = [[self.INF]*(self.n+1) for _ in range(self.n+1)]

  def _init_map(self):
    for src, dst, k in self.arr:
      self._map[src][dst] = min(self._map[src][dst], k)

  def _floyd(self):
    for k in range(1, self.n+1):
      for i in range(1, self.n+1):
        for j in range(1, self.n+1):
          self._map[i][j] = min(self._map[i][j], self._map[i][k] + self._map[k][j])

    for i in range(1, self.n+1):
      self._map[i][i] = 0

  def _print(self):
    for _l in self._map[1:]:
      print(*_l[1:])

  def solve(self):
    self._init_map()
    self._floyd()
    self._print()


if __name__ == "__main__":
  n = int(stdin.readline())
  m = int(stdin.readline())
  arr = [list(map(int, stdin.readline().split())) for _ in range(m)]

  Floyd_problem = Floyd(n, m, arr)
  Floyd_problem.solve()
