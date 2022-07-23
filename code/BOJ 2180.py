# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/2180-8b6347e6d05c4e67afb7850fb8617bb5


from sys import stdin


class FireStation(object):
  def __init__(self, n, arr):
    self.n = n
    self.arr = arr
    self._div = 40000
    self.res = 0
    self._end = 0
    self.parr = []

  def _preprocessing(self):
    for a, b in self.arr:
      if a == 0:
        self._end += b
      elif b == 0:
        continue
      else:
        self.parr.append((b/a, a, b))

  def _sort(self):
    for _, a, b in sorted(self.parr):
      self.res += self.res * a + b
      self.res %= self._div
    self.res += self._end
    self.res %= self._div

  def _print(self):
    print(self.res)

  def solve(self):
    self._preprocessing()
    self._sort()
    self._print()


if __name__ == "__main__":
  n = int(stdin.readline())
  arr = [tuple(map(int, stdin.readline().split())) for _ in range(n)]

  FireStation_problem = FireStation(n, arr)
  FireStation_problem.solve()
