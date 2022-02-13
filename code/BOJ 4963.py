# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/4963-1dfd4a6db7ab41b09c20bf43a3ca7e7b


from collections import deque
import sys


class Island(object):
  def __init__(self, w, h, island_map):
    self.w = w
    self.h = h
    self.island_map = island_map
    self.count = 0
    self.around = [[-1, -1], [-1,  0], [-1,  1],
                   [ 0, -1],           [ 0,  1],
                   [ 1, -1], [ 1,  0], [ 1,  1]]

  def _bfs(self):
    for y in range(1, self.w+1):
      for x in range(1, self.h+1):
        if self.island_map[x][y]:
          self.count += 1
          que = deque([[x, y]])
          while len(que):
            a, b = que.popleft()
            if self.island_map[a][b]:
              self.island_map[a][b] = 0
              que.extend([[a + i, b + j] for (i, j) in self.around])

  def _return(self):
    print(self.count)

  def solve(self):
    self._bfs()
    self._return()


if __name__ == "__main__":
  while True:
    w, h = list(map(int, sys.stdin.readline().split()))
    if w == h == 0:
      break
    island_map = [[0]*(w + 2)] + [[0] + list(map(int, sys.stdin.readline().split())) + [0] for _ in range(h)] + [[0] * (w + 2)]
    Island_problem = Island(w, h, island_map)
    Island_problem.solve()
