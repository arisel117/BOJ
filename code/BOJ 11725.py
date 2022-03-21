# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/11725-de21561f8f564d098c8f661335663a24


from sys import stdin


class ParentTree(object):
  def __init__(self, n, graph):
    self.n = n
    self.graph = graph
    self.g = {i : [] for i in range(1, n + 1)}
    self.parents = [0] * (self.n + 1)

  def _init_graph(self):
    for i, j in self.graph:
      self.g[i].append(j)
      self.g[j].append(i)

  def _dfs(self):
    _visited = [True] * (self.n + 1)
    _stack = [[1, 0]]
    while _stack:
      _node, _p = _stack.pop()
      if _visited[_node]:
        _visited[_node] = False
        self.parents[_node] = _p
        for i in self.g[_node]:
          _stack.append([i, _node])

  def _print(self):
    print(*self.parents[2:], sep="\n")

  def solve(self):
    self._init_graph()
    self._dfs()
    self._print()


if __name__ == "__main__":
  n = int(stdin.readline())
  graph = []
  for _ in range(n - 1):
    graph.append(list(map(int, stdin.readline().split())))
  ParentTree_problem = ParentTree(n, graph)
  ParentTree_problem.solve()
