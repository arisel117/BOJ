# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/9251-LCS-29961fc9b35a4c7a86c891d999b5523c


from sys import stdin


class LCS(object):
  def __init__(self, m, n):
    self.m = m
    self.n = n
    self.lm = len(self.m)
    self.ln = len(self.n)
    self.map = [[0] * (self.ln+1) for i in range(self.lm+1)]

  def _find(self):
    for i, a in enumerate(self.m):
      for j, b in enumerate(self.n):
        if a == b:
          self.map[i+1][j+1] = self.map[i][j] +1
        else:
          self.map[i+1][j+1] = max(self.map[i][j+1], self.map[i+1][j])

  def _pirnt(self):
    print(self.map[self.lm][self.ln])
  
  def solve(self):
    self._find()
    self._pirnt()


if __name__ == "__main__":
  m = list(stdin.readline().rstrip())
  n = list(stdin.readline().rstrip())

  LCS_problem = LCS(m, n)
  LCS_problem.solve()
