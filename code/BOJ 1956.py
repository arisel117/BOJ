# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1956-fa4287990e494a8b94110efd03dabd4a


from sys import stdin


class ExerciseCycle(object):
  def __init__(self, n_node, n_edge, graph_map):
    self.inf = int(1e9)
    self.n = n_node
    self.m = n_edge
    self.graph_map = graph_map
    self.graph = [[self.inf] * self.n for i in range(self.n)]

  def _make_graph(self):
    for o, d, dist in self.graph_map:
      self.graph[o-1][d-1] = dist

  def _floyd(self):
    for k in range(self.n):
      for i in range(self.n):
        for j in range(self.n):
          min_root = self.graph[i][k] + self.graph[k][j]
          if self.graph[i][j] > min_root:
            self.graph[i][j] = min_root

  def _print(self):
    res = self.inf
    for i in range(self.n):
      res = min(res, self.graph[i][i])
    if res == self.inf:
      print(-1)
    else:
      print(res)

  def solve(self):
    self._make_graph()
    self._floyd()
    self._print()


if __name__ == "__main__":
  n_node, n_edge = map(int, stdin.readline().split())
  graph_map = [list(map(int, stdin.readline().split())) for _ in range(n_edge)]
  ExerciseCycle_problem = ExerciseCycle(n_node, n_edge, graph_map)
  ExerciseCycle_problem.solve()
