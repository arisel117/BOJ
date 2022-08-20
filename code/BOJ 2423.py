# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/2423-070cc2856b44405fbd9b07789dfd95ae


from sys import stdin
from collections import deque


class ConnectLine(object):
  def __init__(self, n: int, m: int, arr: list):
    self.n = n
    self.m = m
    self.arr = arr
    self.visited = [[int(1e6)] * (self.m) for _ in range(self.n)]
    self.around1 = [[-1,-1,True], [1,1,True], 
                    [1,0,False], [0,1,False], 
                    [-1,0,False], [0,-1,False]]
    self.around2 = [[-1,1,True], [1,-1,True], 
                    [1,0,False], [0,1,False], 
                    [-1,0,False], [0,-1,False]]
    self.dst_x = self.n - 1
    self.dst_y = self.m - 1
    self.res = -1

  def _check(self, now_v, x, y, cnt, ard):
    for i, j, v in ard:
      xi, yj = x + i, y + j
      if 0 > xi or xi > self.dst_x or 0 > yj or yj > self.dst_y:
        continue
      next_v = self.arr[xi][yj]
      if v == False:
        next_v = not next_v
      if next_v == now_v:
        self.que.appendleft([xi, yj, cnt, True])
      else:
        self.que.append([xi, yj, cnt + 1, False])

  def _find(self):
    cnt = 0
    if self.arr[0][0] == False:
      cnt += 1
      self.arr[0][0] = True

    self.que = deque([(0, 0, cnt, True)])
    while self.que:
      x, y, cnt, _axis = self.que.popleft()
      if self.visited[x][y] <= cnt:
        continue
      self.visited[x][y] = cnt

      if x == self.dst_x and y == self.dst_y:
        self.res = cnt
        return

      now_v = self.arr[x][y]
      if _axis == False:
        now_v = not now_v
      if now_v:
        self._check(now_v, x, y, cnt, self.around1)
      else:
        self._check(now_v, x, y, cnt, self.around2)
    self.res = self.visited[-1][-1]
  
  def _print(self):
    if self.res == -1:
      print("NO SOLUTION")
    else:
      print(self.res)

  def solve(self):
    if (self.n + self.m) % 2 == 0:
      self._find()
    self._print()


if __name__ == "__main__":
  n, m = map(int, stdin.readline().split())
  arr = []
  for _ in range(n):
    arr.append([True if i=="\\" else False for i in stdin.readline().rstrip()])

  ConnectLine_problem = ConnectLine(n, m, arr)
  ConnectLine_problem.solve()
