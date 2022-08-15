# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/23563-db84db2ea72a4eb6b93bc3b82072f6cf


from sys import stdin
from collections import deque


class Lucio(object):
  def __init__(self, n: int, m: int, arr: list):
    self.n = n
    self.m = m
    self.arr = arr
    self.visited = [[False] * self.m for _ in range(self.n)]
    self.if_wall = [[False] * self.m for _ in range(self.n)]
    self.around = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    self.res = 0

  def _init_map(self):
    for x, _l in enumerate(self.arr):
      for y, v in enumerate(_l):
        if v == "#":
          self.visited[x][y] = True
        else:
          if v == "S":
            self.srt = (x, y)
          for i, j in self.around:
            if self.arr[x + i][y + j] == "#":
              self.if_wall[x][y] = True
              break

  def _get_cnt(self, _x: int, _y: int):
    _pos = self.if_wall[_x][_y]
    que = deque([(_x, _y, 0, _pos)])
    while que:
      x, y, cnt, wall = que.popleft()
      if self.visited[x][y]:
        continue
      self.visited[x][y] = True

      if self.arr[x][y] == "E":
        self.res = cnt
        return

      for i, j in self.around:
        xi, yj = x + i, y + j
        if self.visited[xi][yj]:
          continue
        _pos = self.if_wall[xi][yj]
        if wall and _pos:
          que.appendleft((xi, yj, cnt, _pos))
        else:
          que.append((xi, yj, cnt + 1, _pos))

  def _print(self):
    print(self.res)

  def solve(self):
    self._init_map()
    self._get_cnt(self.srt[0], self.srt[1])
    self._print()


if __name__ == "__main__":
  n, m = map(int, stdin.readline().split())
  arr = [list(stdin.readline().rstrip()) for _ in range(n)]

  Lucio_problem = Lucio(n, m, arr)
  Lucio_problem.solve()
