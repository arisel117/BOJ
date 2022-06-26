# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/12015-2-1393d770c7d94e66aa10f2a79a86db0c


from sys import stdin


class Subsequence(object):
  def __init__(self, n, arr):
    self.n = n
    self.arr = arr
    self.map = [0]

  def _find(self, x):
    _len, _height = 1, len(self.map) - 1
    while _len < _height:
      m = (_len + _height) // 2
      if self.map[m] < x:
        _len = m + 1
      elif self.map[m] > x:
        _height = m
      else:
        _len = _height = m
    return _height

  def _pirnt(self):
    print(len(self.map) - 1)

  def solve(self):
    for v in self.arr:
      if self.map[-1] < v:
        self.map.append(v)
      else:
        self.map[self._find(v)] = v
    self._pirnt()


if __name__ == "__main__":
  n = int(stdin.readline())
  arr = list(map(int, stdin.readline().split()))

  Subsequence_problem = Subsequence(n, arr)
  Subsequence_problem.solve()
