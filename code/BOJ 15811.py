# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/15811-f3df2fdc6cc648708d93c6d45a57f585
# Python3 시간초과 / PyPy3 통과

from sys import stdin
from itertools import permutations

class Cryptarithms(object):
  def __init__(self, A, B, C):
    self.a, self.b, self.c = A, B, C
    self.strs = sorted(list(set(a + b + c)))
    self.lstr = len(self.strs)
    self.res = False

  def _find(self):
    for k in permutations([_ for _ in range(10)], self.lstr):
      _dic = {self.strs[i]:k[i] for i in range(self.lstr)}

      a, b, c = 0, 0, 0
      for i in self.a:
        a = (a * 10) + _dic[i]
      for i in self.b:
        b = (b * 10) + _dic[i]
      for i in self.c:
        c = (c * 10) + _dic[i]
      if a + b == c:
        self.res = True
        return 0

  def _print(self):
    if self.res:
      print("YES")
    else:
      print("NO")

  def solve(self):
    if self.lstr < 11:
      self._find()
    self._print()

if __name__ == "__main__":
  a, b, c = stdin.readline().split()

  Cryptarithms_problem = Cryptarithms(a, b, c)
  Cryptarithms_problem.solve()
