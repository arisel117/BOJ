# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/9252-LCS-2-14290d45ce92448da12f122b763931e8


from sys import stdin


class LCS(object):
  def __init__(self, m, n):
    self.m = m
    self.n = n
    self.lm = len(self.m)
    self.ln = len(self.n)
    self.map = [[0] * (self.ln+1) for i in range(self.lm+1)]
    self.fmap = [[""] * (self.ln+1) for i in range(self.lm+1)]

  def _find(self):
    for i, a in enumerate(self.m):
      for j, b in enumerate(self.n):
        if a == b:
          self.map[i+1][j+1] = self.map[i][j] +1
          self.fmap[i+1][j+1] = self.fmap[i][j] + a
        else:
          if self.map[i][j+1] > self.map[i+1][j]:
            self.map[i+1][j+1] = self.map[i][j+1]
            self.fmap[i+1][j+1] = self.fmap[i][j+1]
          else:
            self.map[i+1][j+1] = self.map[i+1][j]
            self.fmap[i+1][j+1] = self.fmap[i+1][j]


  def _pirnt(self):
    res = self.map[self.lm][self.ln]
    print(res)
    if res:
      print(self.fmap[self.lm][self.ln])
  
  def solve(self):
    self._find()
    self._pirnt()


if __name__ == "__main__":
  m = list(stdin.readline().rstrip())
  n = list(stdin.readline().rstrip())
  
  LCS_problem = LCS(m, n)
  LCS_problem.solve()
