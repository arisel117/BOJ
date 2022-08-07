# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/6597-c0e794883a5449048a700d16f38309bb


from sys import stdin


class ReTree(object):
  def __init__(self, a: str, b: str):
    self.a = list(a)
    self.b = b
    self.res = ""

  def _find(self, strs: str):
    _parent = self.a.pop(0)
    if strs == _parent:
      self.res += strs
      return

    _left, _right = strs.split(_parent)
    if _left:
      self._find(_left)
    if _right:
      self._find(_right)
    self.res += _parent

  def _print(self):
    print(self.res)

  def solve(self):
    self._find(self.b)
    self._print()


if __name__ == "__main__":
  while True:
    try:
      a, b = stdin.readline().split()
    except:
      break

    ReTree_problem = ReTree(a, b)
    ReTree_problem.solve()
