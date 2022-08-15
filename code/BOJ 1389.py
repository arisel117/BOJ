# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1389-6-9578488bac8a405e840a711b02269418


from sys import stdin


class SixHopRule(object):
  def __init__(self, n: int, m: int, arr: list):
    self.n = n
    self.m = m
    self.arr = arr
    self.res = None

  def _floyd(self):
    for k in range(1, self.n + 1):
      for i in range(1, self.n + 1):
        for j in range(1, self.n + 1):
          _sum = self.arr[i][k] + self.arr[k][j]
          if self.arr[i][j] > _sum:
            self.arr[i][j] = _sum

  def _get_cnt(self):
    _min_idx, _min_sum = None, int(1e6)
    for i in range(1, self.n + 1):
      self.arr[i][i] = 0
      _sum = sum(self.arr[i][1:])
      if _min_sum > _sum:
        _min_idx = i
        _min_sum = _sum
    self.res = _min_idx

  def _print(self):
    print(self.res)

  def solve(self):
    self._floyd()
    self._get_cnt()
    self._print()


if __name__ == "__main__":
  _inf = int(1e6)
  n, m = map(int, stdin.readline().split())
  arr = [[_inf]*(n+1) for _ in range(n+1)]
  for _ in range(m):
    i, j = map(int, stdin.readline().split())
    arr[i][j] = 1
    arr[j][i] = 1

  SixHopRule_problem = SixHopRule(n, m, arr)
  SixHopRule_problem.solve()
