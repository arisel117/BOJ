# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/12015-2-1393d770c7d94e66aa10f2a79a86db0c


from sys import stdin
from bisect import bisect_left


class Subsequence(object):
  def __init__(self, n, arr):
    self.n = n
    self.arr = arr
    self.map = [0]
  
  def _pirnt(self):
    print(len(self.map) - 1)

  def solve(self):
    for v in self.arr:
      if self.map[-1] < v:
        self.map.append(v)
      else:
        self.map[bisect_left(self.map, v)] = v
    self._pirnt()


if __name__ == "__main__":
  n = int(stdin.readline())
  arr = list(map(int, stdin.readline().split()))

  Subsequence_problem = Subsequence(n, arr)
  Subsequence_problem.solve()
