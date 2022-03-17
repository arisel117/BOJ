# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1507-6b473a20ceb348fcbdae235903e263f6


from sys import stdin


class MinHoW(object):
  def __init__(self, n_node, graph_map):
    self.n = n_node
    self.g = graph_map

  def _floyd(self):
    visited = [[1] * self.n for i in range(self.n)]
    for k in range(self.n):
      for i in range(self.n):
        for j in range(self.n):
          if i == j or j == k or i == k:
            continue
          if self.g[i][j] == self.g[i][k] + self.g[k][j]:
            visited[i][j] = 0
          elif self.g[i][j] > self.g[i][k] + self.g[k][j]:
            return -1
    result = 0
    for i in range(self.n):
      for j in range(i + 1, self.n):
        if visited[i][j]:
          result += self.g[i][j]
    return result

  def solve(self):
    print(self._floyd())


if __name__ == "__main__":
  n_node = int(stdin.readline().rstrip())
  graph_map = [list(map(int, stdin.readline().split())) for _ in range(n_node)]
  MinHoW_problem = MinHoW(n_node, graph_map)
  MinHoW_problem.solve()
