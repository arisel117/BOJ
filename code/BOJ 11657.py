# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/11657-caf8e49785034955bb9c004a2a1997f7


from sys import stdin


class TimeMachine(object):
  def __init__(self, n_node, graph_map):
    self.inf = int(1e9)
    self.n = n_node
    self.graph = graph_map
    self.time = [self.inf] * (self.n + 1)
    self.time[1] = 0

  def _bellmanford(self):
    for i in range(self.n):
      for o, d, t in self.graph:
        next_t = self.time[o] + t
        if self.time[o] != self.inf and self.time[d] > next_t:
          if i == self.n - 1:
            return [-1]
          self.time[d] = next_t
    return self.time[2:]

  def _print(self, res):
    for i in res:
      if i == self.inf:
        print(-1)
      else:
        print(i)

  def solve(self):
    res = self._bellmanford()
    self._print(res)


if __name__ == "__main__":
  n_node, n_edge = map(int, stdin.readline().split())
  graph_map = [list(map(int, stdin.readline().split())) for _ in range(n_edge)]
  TimeMachine_problem = TimeMachine(n_node, graph_map)
  TimeMachine_problem.solve()
