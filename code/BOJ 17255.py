# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/17255-N-fa4a41a32a414fce9e40735f555cec90


from sys import stdin


class ToN(object):
  def __init__(self, n):
    self.n = n
    self.res = 0
    
  def _dfs(self, _str):
    Sstr = set(_str)
    if len(Sstr) == 1:
      self.res += 1
      return 0
    else:
      self._dfs(_str[1:])
      self._dfs(_str[:-1])

  def _pirnt(self):
    print(self.res)
  
  def solve(self):
    self._dfs(self.n)
    self._pirnt()


if __name__ == "__main__":
  n = list(stdin.readline().rstrip())
  
  ToN_problem = ToN(n)
  ToN_problem.solve()
