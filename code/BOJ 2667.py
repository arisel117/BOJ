# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/2667-606a25b61fe94f9f8741fd31d7887a8d


import sys
sys.setrecursionlimit(10**9)


class Apart(object):
  def __init__(self, n, apart_locations):
    self.dim = n
    self.apart_locs = apart_locations
    self.apart_map = [[False] * (self.dim + 3) for _ in range(self.dim + 3)]
    self.num_aparts = []
    self.num_apart = 0
    self.del_list = [[-1, 0], [0, -1], [0, 1], [1, 0]]

  def _fill_danji(self):
    for i,v in zip(range(1, self.dim + 2), self.apart_locs):
      self.apart_map[i][1 : self.dim + 2] = list(map(bool, list(map(int, v))))

  def _dfs(self, a, b):
    for i,j in self.del_list:
      if self.apart_map[a + i][b + j]:
        self.apart_map[a + i][b + j] = False
        self.num_apart += 1
        self._dfs(a + i, b + j)

  def _find_danji(self):
    for a in range(1, self.dim + 1):
      for b in range(1, self.dim + 1):
        if self.apart_map[a][b]:
          self.num_apart += 1
          self.apart_map[a][b] = False
          self._dfs(a, b)
          self.num_aparts.append(self.num_apart)
          self.num_apart = 0

  def _return(self):
    print(len(self.num_aparts))
    for i in sorted(self.num_aparts):
      print(i)

  def solve(self):
    self._fill_danji()
    self._find_danji()
    self._return()


if __name__ == "__main__":
  n = int(sys.stdin.readline())
  Apart_locations = []
  for n in range(n):
    Apart_locations.append(list(sys.stdin.readline().rstrip()))
  Apart_problem = Apart(n, Apart_locations)
  Apart_problem.solve()
