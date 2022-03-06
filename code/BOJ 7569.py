# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/7569-f777630583c04ef0ba202f11fe4aa852


from collections import deque
from sys import stdin


class Tomato(object):
  def __init__(self, w, h, f, tomato_map):
    self.w = w
    self.h = h
    self.f = f
    self.tmap = tomato_map
    self.count = -1
    self.around = [[ 0, 0,-1],[ 0, 0, 1],
                   [ 0,-1, 0],[ 0, 1, 0],
                   [-1, 0, 0],[ 1, 0, 0]]

  def _check(self, _z, _y, _x):
    return_list = []
    for (a, b, c) in self.around:
      za, yb, xc = _z + a, _y + b, _x + c
      if za < 0 or za >= self.f:
        continue
      elif yb < 0 or yb >= self.h:
        continue
      elif xc < 0 or xc >= self.w:
        continue
      else:
        return_list.append([za, yb, xc])
    return return_list
  
  def _bfs(self):
    next_que = deque([])
    for z in range(self.f):
      for y in range(self.h):
        for x in range(self.w):
          if self.tmap[z][y][x] == 1:
            next_que.extend(self._check(z, y, x))

    while next_que:
      que = next_que.copy()
      next_que.clear()
      while que:
        z, y, x = que.popleft()
        if self.tmap[z][y][x] == 0:
          self.tmap[z][y][x] = 1
          next_que.extend(self._check(z, y, x))
      self.count += 1

  def _print(self):
    for z in range(self.f):
      for y in range(self.h):
        if 0 in self.tmap[z][y]:
          self.count = -1
    print(self.count)

  def solve(self):
    self._bfs()
    self._print()


if __name__ == "__main__":
  w, h, f = list(map(int, stdin.readline().split()))
  tomato_map = []
  for _f in range(f):
    _floor = []
    for _h in range(h):
      _floor.append(list(map(int, stdin.readline().split())))
    tomato_map.append(_floor)

  Tomato_problem = Tomato(w, h, f, tomato_map)
  Tomato_problem.solve()
