# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/10282-3eea2248fc2b4812a2b1a9d07852225d


from sys import stdin
import heapq as H


class Hacking(object):
  def __init__(self, n_node, n_edge, start_node, graph_map):
    self.inf = int(1e9)
    self.n = n_node
    self.m = n_edge
    self.start = start_node
    self.graph_map = graph_map
    self.graph = {i : {} for i in range(1, self.n + 1)}

  def _make_graph(self):
    for d, o, t in graph_map:
      if self.graph[o].get(d) == None:
        self.graph[o][d] = t
      else:
        self.graph[o][d] = min(self.graph[o][d], t)

  def _dijkstra(self):
    que = []
    time = {_ : self.inf for _ in self.graph}
    time[self.start] = 0
    H.heappush(que, [time[self.start], self.start])
    while que:
      now_time, now_d = H.heappop(que)
      if time[now_d] < now_time:
        continue
      for new_time, new_d in self.graph[now_d].items():
        cm_time = now_time + new_d
        if cm_time < time[new_time]:
          time[new_time] = cm_time
          H.heappush(que, [cm_time, new_time])
    return time

  def _print(self, time):
    res_count, res_time = 0, 0
    for cm_time in time.values():
      if cm_time != self.inf:
        res_count += 1
        res_time = max(res_time, cm_time)
    print(res_count, res_time)

  def solve(self):
    self._make_graph()
    time = self._dijkstra()
    self._print(time)


if __name__ == "__main__":
  for _ in range(int(stdin.readline())):
    n_node, n_edge, start_node = map(int, stdin.readline().split())
    graph_map = [list(map(int, stdin.readline().split())) for i in range(n_edge)]
    Hacking_problem = Hacking(n_node, n_edge, start_node, graph_map)
    Hacking_problem.solve()
