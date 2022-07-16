# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1941-e539524a2c1b43c397a0d894795cb46c


from sys import stdin
from itertools import combinations
from collections import deque
        

class Princesses(object):
  def __init__(self, arr):
    self.arr = arr
    self.map = [i for i in range(25)]
    self.res = 0

  def _check(self, adj):
    if sum([self.arr[i] for i in adj]) < 4:
      return False

    linked = 0
    deq = deque([(adj[0] // 5, adj[0] % 5)])
    vis = [[False] * 5 for _ in range(5)]
    for i in adj:
      vis[i // 5][i % 5] = True

    while deq:
      x, y = deq.popleft()
      if vis[x][y] == False:
        continue
      vis[x][y] = False
      linked += 1
      for i, j in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
        xi, yj = x + i, y + j
        if xi >= 0 and xi < 5 and yj >= 0 and yj < 5 and vis[xi][yj] == True:
          deq.append((xi, yj))

    if linked == 7:
      return True
    return False

  def _pirnt(self):
    print(self.res)

  def solve(self):
    for comb in list(combinations(self.map, 7)):
      if self._check(comb):
        self.res += 1
    self._pirnt()


if __name__ == "__main__":
  arr = []
  for _ in range(5):
    arr += [True if i=="S" else False for i in stdin.readline().rstrip()]

  Princesses_problem = Princesses(arr)
  Princesses_problem.solve()
