# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1463-1-2c1aea9e52f24170b549e52280ea31e4


from sys import stdin


class ToOne(object):
  def __init__(self, n):
    self.n = n
    self._map = [0 for _ in range(self.n+1)]

  def _find(self):
    for i in range(2, self.n+1):
      self._map[i] = self._map[i-1]+1

      if i%2 == 0:
        self._map[i] = min(self._map[i], self._map[i//2]+1)

      if i%3 == 0:
        self._map[i] = min(self._map[i], self._map[i//3]+1)

  def _pirnt(self):
    print(self._map[-1])
  
  def solve(self):
    self._find()
    self._pirnt()


if __name__ == "__main__":
  n = int(stdin.readline().rstrip())

  ToOne_problem = ToOne(n)
  ToOne_problem.solve()
