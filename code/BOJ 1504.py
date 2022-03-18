# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1504-ef300dcc32c9476f8c40a98bed84db32


from sys import stdin
import heapq as H


class SpecialShortestPath(object):
  def __init__(self, n_node, n_edge, graph_map, point_node1, point_node2):
    self.inf = int(1e9)
    self.n = n_node
    self.m = n_edge
    self.v1 = point_node1
    self.v2 = point_node2
    self.graph_map = graph_map
    self.g = {i : {} for i in range(1, self.n + 1)}

  def _init_graph(self):
    for o, d, w in self.graph_map:
      if self.g[o].get(d) == None:
        self.g[o][d] = w
      else:
        self.g[o][d] = min(self.g[o][d], w)
      if self.g[d].get(o) == None:
        self.g[d][o] = w
      else:
        self.g[d][o] = min(self.g[d][o], w)

  def _dijkstra(self, start_node):
    que = []
    dist = {_ : self.inf for _ in self.g}
    dist[start_node] = 0
    H.heappush(que, [dist[start_node], start_node])
    while que:
      now_dist, now_d = H.heappop(que)
      if dist[now_d] < now_dist:
        continue
      for next_d, next_dist in self.g[now_d].items():
        cm_dist = now_dist + next_dist
        if cm_dist < dist[next_d]:
          dist[next_d] = cm_dist
          H.heappush(que, [cm_dist, next_d])
    return dist

  def _print(self, min_dist):
    if min_dist < self.inf:
      print(min_dist)
    else:
      print(-1)
    

  def solve(self):
    self._init_graph()
    dist1 = self._dijkstra(1)
    dist2 = self._dijkstra(self.v1)
    dist3 = self._dijkstra(self.v2)
    path1 = dist1[self.v1] + dist2[self.v2] + dist3[self.n]
    path2 = dist1[self.v2] + dist3[self.v1] + dist2[self.n]
    self._print(min(path1, path2))


if __name__ == "__main__":
  n_node, n_edge = map(int, stdin.readline().split())
  graph_map = [list(map(int, stdin.readline().split())) for i in range(n_edge)]
  point_node1, point_node2 = map(int, stdin.readline().split())
  SpecialShortestPath_problem = SpecialShortestPath(n_node, n_edge, graph_map, point_node1, point_node2)
  SpecialShortestPath_problem.solve()
