# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/5545-2c2fe3f031dc4fc186773442d489564d


from sys import stdin


class Pizza(object):
  def __init__(self, Ap, Bp, Ac, Bc):
    self.Sp = Ap
    self.Bp = Bp
    self.Sc = Ac
    self.Bc = sorted(Bc, reverse = True)
    self.res = self.Sc / self.Sp

  def _find(self):
    for c in self.Bc:
      self.Sc += c
      self.Sp += self.Bp
      self.res = max(self.res, self.Sc / self.Sp)

  def _pirnt(self):
    print(int(self.res))

  def solve(self):
    self._find()
    self._pirnt()


if __name__ == "__main__":
  n = int(stdin.readline())
  Ap, Bp = map(int, stdin.readline().split())
  Ac = int(stdin.readline())
  Bc = [int(stdin.readline()) for i in range(n)]

  Pizza_problem = Pizza(Ap, Bp, Ac, Bc)
  Pizza_problem.solve()
