# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/14888-5740b472ef804ca7b5bce4f75d316df1


from sys import stdin


class Operators(object):
  def __init__(self, n, arr, opers):
    self.n = n
    self.arr = arr
    self.opr = opers
    self.res = []
    
  def _dfs(self, i, _res, _pl, _mi, _mu, _di):
    if _pl == 0 and _mi == 0 and _mu == 0 and _di == 0:
      self.res.append(_res)
      return 0
    
    if _pl:
      self._dfs(i+1, _res + self.arr[i], _pl-1, _mi, _mu, _di)
    if _mi:
      self._dfs(i+1, _res - self.arr[i], _pl, _mi-1, _mu, _di)
    if _mu:
      self._dfs(i+1, _res * self.arr[i], _pl, _mi, _mu-1, _di)
    if _di:
      if _res < 0:
        self._dfs(i+1, -(-_res // self.arr[i]), _pl, _mi, _mu, _di-1)
      else:
        self._dfs(i+1, _res // self.arr[i], _pl, _mi, _mu, _di-1)

  def _pirnt(self):
    print(max(self.res))
    print(min(self.res))
  
  def solve(self):
    self._dfs(1, self.arr[0], self.opr[0], self.opr[1], self.opr[2], self.opr[3])
    self._pirnt()


if __name__ == "__main__":
  n = int(stdin.readline().rstrip())
  arr = list(map(int, stdin.readline().split()))
  opers = list(map(int, stdin.readline().split()))
  
  Operators_problem = Operators(n, arr, opers)
  Operators_problem.solve()
