# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1309-0cc20b949f3a466b9a481b9c1da39bb5


class Zoo(object):
  def __init__(self, n):
    self.n = n - 1
    self._mod = 9901
    self._res = 0

  def _find(self):
    a, b = 1, 3
    for _ in range(self.n):
      a, b = b, (2*b + a) % self._mod
    self._res = b

  def _pirnt(self):
    print(self._res)
  
  def solve(self):
    self._find()
    self._pirnt()


if __name__ == "__main__":
  n = int(input())
  
  Zoo_problem = Zoo(n)
  Zoo_problem.solve()
