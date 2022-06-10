# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/11509-91abaa65fcea446d941839f081b886c2


from sys import stdin


class Balloon(object):
  def __init__(self, m):
    self.map = m
    self.res = 0

  def _find(self):
    _visited = [0] * 1000001
    for v in self.map:
      if _visited[v]:
        _visited[v] -= 1
      else:
        self.res += 1
      _visited[v-1] += 1

  def _pirnt(self):
    print(self.res)
  
  def solve(self):
    self._find()
    self._pirnt()


if __name__ == "__main__":
  _ = stdin.readline()
  m = list(map(int, stdin.readline().split()))
  
  Balloon_problem = Balloon(m)
  Balloon_problem.solve()
