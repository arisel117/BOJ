# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/14442-2-ad2a5b4e928342bbac862a8436e6ff39


from sys import stdin
from collections import deque


class WallBreaker(object):
  def __init__(self, n: int, m: int, k: int, arr: list):
    self.n = n
    self.m = m
    self.k = k
    self.arr = arr
    self.around = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    self.dst_x = self.n - 1
    self.dst_y = self.m - 1
    self.res = -1

  def _find(self):
    dq = deque([(0, 0, 0, 0, -1, -1)])
    visited = [[self.k+1 for i in range(self.m)] for i in range(self.n)]
    while dq:
      wcnt, cnt, x, y, bx, by = dq.popleft()
      if visited[x][y] <= wcnt:
        continue
      visited[x][y] = wcnt
      cnt += 1

      if x == self.dst_x and y == self.dst_y:
        self.res = cnt
        return

      for i, j in self.around:
        xi, yj = x + i, y + j
        if xi == bx and yj == by:
          continue
        if xi >= self.n or xi < 0 or yj >= self.m or yj < 0:
          continue

        if self.arr[xi][yj] == 1:
          dq.append((wcnt + 1, cnt, xi, yj, x, y))
        else:
          dq.append((wcnt, cnt, xi, yj, x, y))

  def _print(self):
    print(self.res)

  def solve(self):
    self._find()
    self._print()


if __name__ == "__main__":
  n, m, k = map(int, stdin.readline().split())
  arr = [list(map(int, list(stdin.readline().rstrip()))) for i in range(n)]

  WallBreaker_problem = WallBreaker(n, m, k, arr)
  WallBreaker_problem.solve()
