# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/7576-a575f16333e944749158d8c5f6ae66fb


from collections import deque
import sys


class Tomato(object):
  def __init__(self, w, h, tomato_map):
    self.w = w
    self.h = h
    self.tomato_map = tomato_map
    self.count = -1
    self.around = [[-1,  0], [ 0, -1], [ 0,  1], [ 1,  0]]
    

  def _find_ripe_tomatoes(self):
    que = deque([])
    for y in range(1, self.h+1):
      for x in range(1, self.w+1):
        if self.tomato_map[y][x] == 1:
          que.extend([[y + i, x + j] for (i, j) in self.around])
    return que
  
  def _bfs(self, next_que):
    while len(next_que):
      que = next_que.copy()
      next_que.clear()
      while len(que):
        a, b = que.popleft()
        if self.tomato_map[a][b] == 0:
          self.tomato_map[a][b] = 1
          next_que.extend([[a + i, b + j] for (i, j) in self.around])
      self.count += 1
    for y in range(1, self.h+1):
      if 0 in self.tomato_map[y]:
        self.count = -1

  def _print(self):
    print(self.count)

  def solve(self):
    que = self._find_ripe_tomatoes()
    self._bfs(que)
    self._print()


if __name__ == "__main__":
  w, h = list(map(int, sys.stdin.readline().split()))
  tomato_map = [[-1] * (w + 2)] + [[-1] + list(map(int, sys.stdin.readline().split())) + [-1] for _ in range(h)] + [[-1] * (w + 2)]
  Tomato_problem = Tomato(w, h, tomato_map)
  Tomato_problem.solve()
