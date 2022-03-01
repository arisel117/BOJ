# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1753-a0ea44f9a8ab4699a0230893077e7022


from sys import stdin
import heapq as H


class ShortestPath(object):
  def __init__(self, n_node, n_edge, start_node, graph_map):
    self.inf = int(1e9)
    self.n = n_node
    self.m = n_edge
    self.start = start_node
    self.graph_map = graph_map
    self.graph = {i : {} for i in range(1, self.n + 1)}
    

  def _make_graph(self):
    for o, d, w in graph_map:
      if self.graph[o].get(d) == None:
        self.graph[o][d] = w
      else:
        self.graph[o][d] = min(self.graph[o][d], w)

  def _dijkstra(self):
    que = []
    dist = {_ : self.inf for _ in self.graph}
    dist[self.start] = 0
    H.heappush(que, [dist[self.start], self.start])
    while que:
      now_dist, now_d = H.heappop(que)
      if dist[now_d] < now_dist:
        continue
      for new_dist, new_d in self.graph[now_d].items():
        cm_dist = now_dist + new_d
        if cm_dist < dist[new_dist]:
          dist[new_dist] = cm_dist
          H.heappush(que, [cm_dist, new_dist])
    return dist

  def _print(self, dist):
    for i in dist.values():
      if i == self.inf:
        print("INF")
      else:
        print(i)

  def solve(self):
    self._make_graph()
    dist = self._dijkstra()
    self._print(dist)


if __name__ == "__main__":
  n_node, n_edge = map(int, stdin.readline().split())
  start_node = int(stdin.readline())
  graph_map = [list(map(int, stdin.readline().split())) for i in range(n_edge)]
  ShortestPath_problem = ShortestPath(n_node, n_edge, start_node, graph_map)
  ShortestPath_problem.solve()
