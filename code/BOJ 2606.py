# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/2606-779100ca1668448f90624a6068a3225f


import sys
sys.setrecursionlimit(10**9)


class Virus(object):
  def __init__(self, n, m, virus_locs):
    self.dim_x = n
    self.dim_y = m
    self.virus_locs = virus_locs
    self.virus_dic = {i:set() for i in range(1,self.dim_x+1)}
    self.infected = {1}

  def _fill_map(self):
    for i,j in self.virus_locs:
      self.virus_dic[i].add(j)
      self.virus_dic[j].add(i)

  def _bfs(self, carrier):
    next_carrier = set()
    for i in carrier:
      next_carrier.update(self.virus_dic[i])
    carrier = next_carrier - self.infected    # n이 100 이하로 적어서 괜찮은데, visited를 통해 진행하는게 좋음!
    self.infected = self.infected | carrier
    if len(carrier):
      self._bfs(carrier)

  def _return(self):
    print(len(self.infected)-1)

  def solve(self):
    self._fill_map()
    self._bfs(self.infected)
    self._return()



if __name__ == "__main__":
  n = int(sys.stdin.readline())
  m = int(sys.stdin.readline())
  virus_locs = []
  for _ in range(m):
    virus_locs.append(list(map(int, sys.stdin.readline().split())))
  Virus_problem = Virus(n, m, virus_locs)
  Virus_problem.solve()
