# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/5719-011c39d887c847c0922f95196ab20997


from sys import stdin
import heapq as H
from math import inf


class AlmostShortPath(object):
  def __init__(self, n: int, edges: list, src: int, dst: int):
    self.n = n
    self.edges = edges
    self.src = src
    self.dst = dst

    self.visited = [[False] * self.n for _ in range(self.n)]

  def _init_map(self):
    self.adj = [[] for _ in range(self.n)]
    self.rev_adj = [[] for _ in range(self.n)]
    for i, j, v in self.edges:
      self.adj[i].append((j, v))
      self.rev_adj[j].append((i, v))

  def _get_shortest_path(self):
    self.dist = [inf] * self.n
    self.dist[self.src] = 0
    que = [(0, self.src)]
    while que:
      now_dist, _src = H.heappop(que)
      if now_dist > self.dist[_src]:
        continue

      for _dst, next_dist in self.adj[_src]:
        _dist = now_dist + next_dist
        if self.visited[_src][_dst] or _dist >= self.dist[_dst]:
          continue

        self.dist[_dst] = _dist
        H.heappush(que, (_dist, _dst))

  def _erase_path(self):
    que = [self.dst]
    while que:
      _dst = H.heappop(que)
      if _dst == self.src:
        continue

      for _src, _dist in self.rev_adj[_dst]:
        if self.visited[_src][_dst] == True:
          continue

        if self.dist[_src] == self.dist[_dst] - _dist:
          self.visited[_src][_dst] = True
          H.heappush(que, _src)

  def _print(self):
    if self.dist[self.dst] == inf:
      print(-1)
    else:
      print(self.dist[self.dst])

  def solve(self):
    self._init_map()

    self._get_shortest_path()
    self._erase_path()

    self._get_shortest_path()
    self._print()


if __name__ == "__main__":
  while True:
    n, m = map(int, stdin.readline().split())
    if n == m == 0:
      break
    src, dst = map(int, stdin.readline().split())
    edges = [list(map(int, stdin.readline().split())) for _ in range(m)]

    AlmostShortPath_problem = AlmostShortPath(n, edges, src, dst)
    AlmostShortPath_problem.solve()
