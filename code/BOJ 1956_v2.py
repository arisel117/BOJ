# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1956-fa4287990e494a8b94110efd03dabd4a


from sys import stdin
import heapq as H


class ExerciseCycle(object):
  def __init__(self, n_node, n_edge, graph_map):
    self.inf = int(1e9)
    self.n = n_node
    self.m = n_edge
    self.graph_map = graph_map
    self.graph = {i : [] for i in range(self.n + 1)}
    self.dist = [[self.inf] * (self.n + 1) for i in range(self.n + 1)]
    self.que = []

  def _init_graph(self):
    for o, d, dist in self.graph_map:
      self.graph[o].append([d, dist])
      self.dist[o][d] = dist
      H.heappush(self.que, (dist, o, d))

  def _heapfloyd(self):
    while self.que:
      dist, o, d = H.heappop(self.que)
      if o == d:
        return dist
      if self.dist[o][d] >= dist:
        for next_node, next_dist in self.graph[d]:
          next_dist += dist
          if self.dist[o][next_node] > next_dist:
            self.dist[o][next_node] = next_dist
            H.heappush(self.que, (next_dist, o, next_node))
    return -1

  def _print(self, res):
    print(res)

  def solve(self):
    self._init_graph()
    res = self._heapfloyd()
    self._print(res)


if __name__ == "__main__":
  n_node, n_edge = map(int, stdin.readline().split())
  graph_map = [list(map(int, stdin.readline().split())) for _ in range(n_edge)]
  ExerciseCycle_problem = ExerciseCycle(n_node, n_edge, graph_map)
  ExerciseCycle_problem.solve()
