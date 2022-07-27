# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/11559-Puyo-Puyo-1ce51f983beb450ea5ce78c775a770e3


from sys import stdin
from collections import deque


class PuyoPuyo(object):
  def __init__(self, n, arr):
    self.n = n
    self.m = 6
    self.arr = arr
    self.around = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    self.res = 0

  def _scan(self):
    self.visited = [[False]*self.m for i in range(self.n)]
    self._ffmap = deque([])
    for i in range(self.n):
      for j in range(self.m):
        k = self.arr[i][j]
        if k == ".":
          continue
        _fmap = self._find(i, j, k)
        if len(_fmap) >= 4:
          self._ffmap.extend(_fmap)

    if self._ffmap:
      self._down(sorted(self._ffmap, reverse=True))
      self.res += 1
      self._scan()

  def _find(self, i, j, k):
    _dp = deque([(i, j)])
    _fmap = deque([])
    while _dp:
      i, j = _dp.pop()
      if self.arr[i][j] == "." or self.visited[i][j]:
        continue
      self.visited[i][j] = True
      _fmap.append((i, j))
      for a, b in self.around:
        ia, jb = i + a, j + b
        if ia < 0 or ia >= self.n or jb < 0 or jb >= self.m:
          continue
        if self.arr[ia][jb] == k:
          _dp.append((ia, jb))
    return _fmap

  def _down(self, _fmap):
    while _fmap:
      i, j = _fmap.pop()
      for a in range(i, 0, -1):
        self.arr[a][j] = self.arr[a-1][j]
      self.arr[0][j] = "."

  def _print(self):
    print(self.res)

  def solve(self):
    self._scan()
    self._print()


if __name__ == "__main__":
  n = 12
  arr = [list(stdin.readline().rstrip()) for i in range(n)]
  PuyoPuyo_problem = PuyoPuyo(n, arr)
  PuyoPuyo_problem.solve()
