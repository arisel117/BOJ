# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1016-fceb83c777d8416ba27d54836cb48040


import sys


class NonSquaredNumber(object):
  def __init__(self, min_n, max_n):
    self.min_n = min_n
    self.max_n = max_n
    self.dlist = [False] * (self.max_n - self.min_n + 1)
    self.max_root = int(self.max_n**0.5) + 1
    self.root_dlist = [False for i in range(2, self.max_root)]

  def _Sieve_of_Eratosthenes(self):
    for x in range(2, self.max_root):
      if self.root_dlist[x - 2] == False:
        for i in range(x, self.max_root , x):
          self.root_dlist[i - 2] = True
        self.x_squared = x * x
        self.start = (-1 * self.min_n // self.x_squared * -1) * self.x_squared
        for i in range(self.start, self.max_n + 1, self.x_squared):
          if self.min_n <= i:
            self.dlist[i - self.min_n] = True

  def _return(self):
    print(self.max_n - self.min_n + 1 - sum(self.dlist))

  def solve(self):
    self._Sieve_of_Eratosthenes()
    self._return()


if __name__ == "__main__":
  min_n, max_n = map(int, sys.stdin.readline().split())
  NonSquaredNumber_problem = NonSquaredNumber(min_n, max_n)
  NonSquaredNumber_problem.solve()
