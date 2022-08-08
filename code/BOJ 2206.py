# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/2206-e57a471824dd423cb6cf953cd6214979


from sys import stdin
from collections import deque


class WallBreaker(object):
  def __init__(self, n: int, m: int, arr: list):
    self.n = n
    self.m = m
    self.arr = arr
    self.around = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    self.dst_x = self.n - 1
    self.dst_y = self.m - 1
    self.res = -1

  def _find(self):
    dq = deque([(1, 0, 0, 0)])
    visited = [[[False]*2 for i in range(self.m)] for i in range(self.n)]
    while dq:
      cnt, x, y, z = dq.popleft()
      if visited[x][y][z]:
        continue

      if x == self.dst_x and y == self.dst_y:
        self.res = cnt
        return

      visited[x][y][z] = True
      cnt += 1

      if self.arr[x][y] == 1:
        z += 1
        if z > 1:
          continue
      for i, j in self.around:
        xi, yj = x + i, y + j
        if xi >= self.n or xi < 0 or yj >= self.m or yj < 0:
          continue
        dq.append((cnt, xi, yj, z))

  def _print(self):
    print(self.res)

  def solve(self):
    self._find()
    self._print()


if __name__ == "__main__":
  n, m = map(int, stdin.readline().split())
  arr = [list(map(int, list(stdin.readline().rstrip()))) for i in range(n)]

  WallBreaker_problem = WallBreaker(n, m, arr)
  WallBreaker_problem.solve()
