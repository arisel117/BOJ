# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1697-5e7d2908b6874f99ae5fb4557a0b7780


from collections import deque
import sys


class HideSeek(object):
  def __init__(self, origin, destination):
    self.o = origin
    self.d = destination
    self.visited = [True for _ in range(150001)]

  def _bfs(self):
    time = 0
    next_que = deque([self.o])
    while len(next_que):
      que = next_que.copy()
      next_que.clear()
      while len(que):
        x = que.popleft()
        if x == self.d:
          return time
        if self.visited[x]:
          self.visited[x] = False
          if x > 0:
            next_que.append(x - 1)
          if x < 150000:
            next_que.append(x + 1)
          if x < 75000:
            next_que.append(x * 2)
      time += 1

def solve(self):
    if self.o > self.d:
      time = self.o - self.d
    else:
      time = self._bfs()
    print(time)


if __name__ == "__main__":
  origin, destination = list(map(int, sys.stdin.readline().split()))
  HideSeek_problem = HideSeek(origin, destination)
  HideSeek_problem.solve()
