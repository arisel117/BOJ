# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1915-984c64d3b2d248cc845199d7475366f7


from sys import stdin


class LargeSquare(object):
  def __init__(self, n, m, arr):
    self.n = n
    self.m = m
    self.arr = arr

  def _calc(self):
    for i in range(1, self.n):
      for j in range(1, self.m):
        if self.arr[i][j] > 0:
          self.arr[i][j] += min(self.arr[i-1][j-1], self.arr[i-1][j], self.arr[i][j-1])

  def _print(self):
    print(max([max(i) for i in self.arr])**2)

  def solve(self):
    self._calc()
    self._print()


if __name__ == "__main__":
  n, m = map(int, stdin.readline().split())
  arr = [list(map(int, stdin.readline().rstrip())) for i in range(n)]

  LargeSquare_problem = LargeSquare(n, m, arr)
  LargeSquare_problem.solve()
