# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1012-23eb1411abea44a5818e531ea7af5b93


import sys
sys.setrecursionlimit(10**6)


class Cabbage(object):
  def __init__(self, m, n, k, cabbage_locs):
    self.num_k = k
    self.cab_locs = cabbage_locs
    self.field = [[False] * (n + 2) for _ in range(m + 2)]
    self.num_worms = 0
    self.dfs_check_list = [[-1, 0], [0, -1], [1, 0], [0, 1]]

  def _fill_field(self):
    for i,(x,y) in enumerate(self.cab_locs):
      self.cab_locs[i] = [x,y]
      self.field[x][y] = True

  def _dfs(self, a, b):
    for i, j in self.dfs_check_list:
      if self.field[a + i][b + j]:
        self.field[a-1][b] = False
        self._dfs(a + i, b + j)

  def _find_sub_graph(self):
    for a,b in self.cab_locs:
      if self.field[a][b]:
        self.num_worms += 1
        self.field[a][b] = False
        self._dfs(a, b)

  def _return(self):
    print(self.num_worms)

  def solve(self):
    self._fill_field()
    self._find_sub_graph()
    self._return()


if __name__ == "__main__":
  test_case = int(sys.stdin.readline())
  for T in range(test_case):
    m, n, k = list(map(int, sys.stdin.readline().split()))
    cabbage_locs = []
    for _ in range(k):
      cabbage_locs.append( list(map(lambda x : int(x)+1, sys.stdin.readline().split())) )
    Cabbage_problem = Cabbage(m, n, k, cabbage_locs)
    Cabbage_problem.solve()
