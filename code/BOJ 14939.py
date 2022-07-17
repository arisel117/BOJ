# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/14939-ccaa4be936b34c97965f58431daa4a0a


# 14939 - python 통과 코드


from sys import stdin
from copy import deepcopy


class TurnOff(object):
  def __init__(self, arr):
    self.arr = arr
    self.res = int(1e9)

  def _switch(self, _map, x, y):
    for i, j in [[0, 0], [-1, 0], [0, -1], [0, 1], [1, 0]]:
      xi, yj = x + i, y + j
      if xi >= 0 and xi < 10 and yj >= 0 and yj < 10:
        _map[xi][yj] = not _map[xi][yj]
    return _map

  def _find(self):
    for i in range(1024):
      cnt = 0
      _map = deepcopy(self.arr)

      for y in range(10):
        if i & (1 << y) > 0:
          _map = self._switch(_map, 0, y)
          cnt += 1

      for x in range(9):
        for y in range(10):
          if _map[x][y]:
            _map = self._switch(_map, x+1, y)
            cnt += 1

      if sum(_map[-1]) == 0:
        self.res = min(self.res, cnt)

  def _print(self):
    if self.res == int(1e9):
      print(-1)
    else:
      print(self.res)

  def solve(self):
    self._find()
    self._print()


if __name__ == "__main__":
  arr = []
  for _ in range(10):
    arr.append([True if i=="O" else False for i in stdin.readline().rstrip()])

  TurnOff_problem = TurnOff(arr)
  TurnOff_problem.solve()
