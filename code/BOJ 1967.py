# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1967-e6fafcb2ac9d4d16bc0d98881472764d


from sys import stdin


class TreeDiameter(object):
  def __init__(self, n, graph):
    self.n = n
    self.g = graph

  def _dfs(self, start):
    _dist = [0] * (self.n + 1)
    _visited = [True] * (self.n + 1)
    _stack = [[start, 0]]
    while _stack:
      _node, _cd = _stack.pop()
      if _visited[_node]:
        _visited[_node] = False
        _dist[_node] = _cd
        for i, _di in self.g[_node]:
          _stack.append([i, _di + _cd])
    return _dist

  def solve(self):
    point_1 = self._dfs(1)
    point_2 = self._dfs(point_1.index(max(point_1)))
    print(max(point_2))


if __name__ == "__main__":
  n = int(stdin.readline())
  graph = {i : [] for i in range(n + 1)}
  for _ in range(n - 1):
    p, c, w = map(int, stdin.readline().split())
    graph[p].append([c, w])
    graph[c].append([p, w])
  TreeDiameter_problem = TreeDiameter(n, graph)
  TreeDiameter_problem.solve()
