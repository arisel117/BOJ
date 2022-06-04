# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1958-LCS-3-e629a985aba442699455a03dad05b92f


from sys import stdin


class LCS3D(object):
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c
    self.la = len(self.a) + 1
    self.lb = len(self.b) + 1
    self.lc = len(self.c) + 1
    self.map = [[[0]*self.lc for _ in range(self.lb)] for _ in range(self.la)]

  def _find(self):
    for i in range(1, self.la):
      for j in range(1, self.lb):
        for k in range(1, self.lc):
          if self.a[i-1] == self.b[j-1] == self.c[k-1]:
            self.map[i][j][k] = self.map[i-1][j-1][k-1] + 1
          else:
            self.map[i][j][k] = max(self.map[i-1][j][k], self.map[i][j-1][k], self.map[i][j][k-1])

  def _pirnt(self):
    res = 0
    for i in self.map:
      for j in i:
        res = max(res, max(j))
    print(res)
  
  def solve(self):
    self._find()
    self._pirnt()


if __name__ == "__main__":
  a, b, c = [list(stdin.readline().rstrip()) for i in range(3)]
  
  LCS3D_problem = LCS3D(a, b, c)
  LCS3D_problem.solve()
