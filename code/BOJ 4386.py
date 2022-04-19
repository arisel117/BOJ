# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/4386-f4b664be285748dbaffb107b3df8db6a


import heapq
from sys import stdin


class Constellation(object):
  def __init__(self, n, star_list):
    self.n = n
    self.stars = star_list
    self.res = 0

  def _init_map(self):
    self.map = [[] for _ in range(self.n)]
    for i in range(self.n):
      for j in range(self.n):
        if i == j:
          continue
        x, y = self.stars[i][0], self.stars[i][1]
        a, b = self.stars[j][0], self.stars[j][1]
        dist = (abs(x - a) ** 2 + abs(y - b) ** 2) ** 0.5
        self.map[i].append((dist, j))
  
  def _prim(self):
    visited = [True] * self.n
    hq = [(0, 0)]
    while hq:
      dist, node = heapq.heappop(hq)
      if visited[node]:
        self.res += dist
        visited[node] = False
      for next_dist, next_node in self.map[node]:
        if visited[next_node]:
          heapq.heappush(hq, (next_dist, next_node))

  def solve(self):
    self._init_map()
    self._prim()
    self._print()
  
  def _print(self):
    print(self.res)


if __name__ == "__main__":
  n = int(stdin.readline())
  star_list = []
  for _ in range(n):
    star_list.append(tuple(map(float, stdin.readline().split())))

  Constellation_problem = Constellation(n, star_list)
  Constellation_problem.solve()
