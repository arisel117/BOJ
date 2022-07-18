# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/2405-M-4e3a4debdf5e4f3f95b6ace1fdf008ce


from sys import stdin


class TwoM(object):
  def __init__(self, arr):
    self.arr = sorted(arr)
    self.res = 0

  def _find(self):
    a = self.arr[0]
    for b, c in zip(self.arr[1:-1], self.arr[2:]):
      self.res = max(self.res, abs(2 * b - a - c))

    c = self.arr[-1]
    for a, b in zip(self.arr[:-2], self.arr[1:-1]):
      self.res = max(self.res, abs(2 * b - a - c))

  def _print(self):
      print(self.res)

  def solve(self):
    self._find()
    self._print()


if __name__ == "__main__":
  n = int(stdin.readline())
  arr = [int(stdin.readline()) for _ in range(n)]

  TwoM_problem = TwoM(arr)
  TwoM_problem.solve()
