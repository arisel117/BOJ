# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/13141-Ignition-d5eddef898124eddb732d75b982d0e8c


from sys import stdin
from math import inf

class Ignition(object):
  def __init__(self, n: int, edges: list):
    self.n = n
    self.edges = edges
    self.arr = [[inf]*(self.n+1) for _ in range(self.n+1)]

  def _init_map(self):
    for i, j, v in self.edges:
      self.arr[i][j] = min(self.arr[i][j], v)
      self.arr[j][i] = self.arr[i][j]

    for i in range(1, self.n + 1):
      self.arr[i][i] = 0

  def _floyd(self):
    for k in range(1, self.n + 1):
      for i in range(1, self.n + 1):
        for j in range(1, self.n + 1):
          self.arr[i][j] = min(self.arr[i][j], self.arr[i][k] + self.arr[k][j])

  def _get_burn_time(self, src):
    fire_times = [0] * (self.n+1)
    for i in range(1, self.n+1):
      fire_times[i] = self.arr[src][i]

    max_time = -inf
    for i, j, v in edges:
      fi, fj = fire_times[i], fire_times[j]
      max_time = max(max_time, fi + fj + v)
    return max_time

  def _print(self):
    print("{:.1f}".format(self.diff / 2))

  def solve(self):
    self._init_map()
    self._floyd()

    self.diff = inf
    for i in range(1, self.n+1):
      self.diff = min(self._get_burn_time(i), self.diff)

    self._print()


if __name__ == "__main__":
  n, m = map(int, stdin.readline().split())
  edges = [list(map(int, stdin.readline().split())) for _ in range(m)]

  Ignition_problem = Ignition(n, edges)
  Ignition_problem.solve()
