# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1944-b1f6887df0e342adadd1ab0b6b1312a3
# 개선된 코드로 수정됨 - _loc의 i to j 를 찾을 때, 한 i에 대해 모든 위치에 대해 구한 후, j들에 대해 한 번에 채우는 개념을 사용함

from collections import deque
from sys import stdin


class Robots(object):
  def __init__(self, n, m, graph):
    self.n = n
    self.m = m
    self.g = graph
    self._loc = []
    self._around = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    self.parents = [i for i in range(self.m + 1)]
    self.tree = []
    self.res = 0

  def _find_loc(self):
    for i, _ in enumerate(self.g):
      for j, k in enumerate(_):
        if k == "S" or k == "K":
          self._loc.append([i, j])

  def _dfs(self, _link):
    que = deque([_link])
    visited = [[0 for j in range(self.n)] for i in range(self.n)]
    while(que):
      r, c = que.popleft()      
      for i, j in self._around:
        nR, nC = r + i, c + j
        if 0 <= nR < self.n and 0 <= nC < self.n and visited[nR][nC] == 0 and self.g[nR][nC] != "1":
          visited[nR][nC] = visited[r][c] + 1
          que.append([nR, nC])
    return visited

  def _build_tree(self):
    for i in range(self.m + 1):
      _visited = self._dfs(self._loc[i])
      for j in range(i + 1, self.m + 1):
        min_d = _visited[self._loc[j][0]][self._loc[j][1]]
        if min_d == 0:
          self.res = -1
          return 0
        self.tree.append((min_d, i, j))

  def _find(self, num):
    if num != self.parents[num]:
      self.parents[num] = self._find(self.parents[num])
    return self.parents[num]

  def _union(self, nodeA, nodeB):
    rootA, rootB = self._find(nodeA), self._find(nodeB)
    if rootA == rootB:
      return False
    self.parents[rootB] = rootA
    return True

  def _kruskal(self):
    self.tree.sort()
    cnt = 0
    for dist, nodeA, nodeB in self.tree:
      if self._union(nodeA, nodeB):
        self.res += dist
        cnt += 1
      if cnt == self.m:
        break

  def solve(self):
    self._find_loc()
    self._build_tree()
    if self.res == 0:
      self._kruskal()
    self._print()
  
  def _print(self):
    print(self.res)


if __name__ == "__main__":
  n, m = map(int, stdin.readline().split())
  graph = [list(stdin.readline().rstrip()) for i in range(n)]

  Robots_problem = Robots(n, m, graph)
  Robots_problem.solve()
