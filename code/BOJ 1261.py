# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1261-e7c1d60de06f462892a50c0d16d46874


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
    self.inf = int(1e6)

  def _find(self):
    dq = deque([(0, 0, 0, -1, -1)])
    visited = [[self.inf for i in range(self.m)] for i in range(self.n)]
    while dq:
      cnt, x, y, bx, by = dq.popleft()
      if visited[x][y] <= cnt:
        continue
      visited[x][y] = cnt
      
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
          dq.append((cnt + 1, xi, yj, x, y))
        else:
          dq.appendleft((cnt, xi, yj, x, y))

  def _print(self):
    print(self.res)

  def solve(self):
    self._find()
    self._print()


if __name__ == "__main__":
  m, n = map(int, stdin.readline().split())
  arr = [list(map(int, list(stdin.readline().rstrip()))) for i in range(n)]

  WallBreaker_problem = WallBreaker(n, m, arr)
  WallBreaker_problem.solve()
