# -*- coding: utf-8 -*-
# 자세한 설명 링크 : https://arisel.notion.site/1753-a0ea44f9a8ab4699a0230893077e7022


import sys
import heapq as H


class ShortestPath(object):
  def __init__(self, nodes, lines, start_node, dic_list):
    self.inf = int(1e9)
    self.nodes = nodes
    self.lines = lines
    self.start_node = start_node
    self.dic_list = dic_list
    self.graph = {i : {} for i in range(1, self.nodes + 1)}
    self.dist = {_ : self.inf for _ in self.graph}

  def _make_graph(self):
    for origin, destination, weight in dic_list:
      if self.graph[origin].get(destination) == None:
        self.graph[origin][destination] = weight
      else:
        self.graph[origin][destination] = min(self.graph[origin][destination], weight)

  def _dijkstra(self):
    self.que = []
    self.dist[self.start_node] = 0
    H.heappush(self.que, [self.dist[self.start_node], self.start_node])
    while self.que:
      current_distance, current_destination = H.heappop(self.que)
      if self.dist[current_destination] < current_distance:
        continue
      for new_distance, new_destination in self.graph[current_destination].items():
        cumulative_distance = current_distance + new_destination
        if cumulative_distance < self.dist[new_distance]:
          self.dist[new_distance] = cumulative_distance
          H.heappush(self.que, [cumulative_distance, new_distance])

  def _return(self):
    for i in self.dist.values():
      if i == self.inf:
        print("INF")
      else:
        print(i)

  def solve(self):
    self._make_graph()
    self._dijkstra()
    self._return()


if __name__ == "__main__":
  nodes, lines = map(int, sys.stdin.readline().split())
  start_node = int(sys.stdin.readline())
  dic_list = []
  for i in range(lines):
    dic_list.append(list(map(int, sys.stdin.readline().split())))
  ShortestPath_problem = ShortestPath(nodes, lines, start_node, dic_list)
  ShortestPath_problem.solve()