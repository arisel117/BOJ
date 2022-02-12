# -*- coding: utf-8 -*-
# 자세한 설명 링크 : https://arisel.notion.site/2644-3389798272d84ecab79a9eacf3fdce19


import sys


class KinshipDegree(object):
  def __init__(self, num_family, origin, destination, num_link):
    self.num_family = num_family
    self.origin = origin
    self.destination = destination
    self.num_link = num_link
    self.family_dic = {i:-1 for i in range(1, self.num_family + 1)}
    self.res = []

  def _make_family_dic(self):
    for i in range(self.num_link):
      self.parent, self.child = map(int, sys.stdin.readline().split())
      self.family_dic[self.child] = self.parent

  def _recursive_func(self, x):
    if x != -1:
      return [x] + self._recursive_func(self.family_dic[x])
    else:
      return []

  def _return(self):
    if len(self.res) > 0:
      print(min(self.res))
    else:
      print(-1)

  def solve(self):
    self._make_family_dic()
    self.top_graph_origin = self._recursive_func(self.origin)
    self.top_graph_destination = self._recursive_func(self.destination)
    for top_graph_origin_index, top_graph_destination_index in enumerate(self.top_graph_origin):
      if top_graph_destination_index in self.top_graph_destination:
        self.res.append(top_graph_origin_index + self.top_graph_destination.index(top_graph_destination_index))
    self._return()


if __name__ == "__main__":
  num_family = int(sys.stdin.readline())
  family_dic = {i:-1 for i in range(1, num_family + 1)}
  origin, destination = map(int, sys.stdin.readline().split())
  num_link = int(sys.stdin.readline())
  
  KinshipDegree_problem = KinshipDegree(num_family, origin, destination, num_link)
  KinshipDegree_problem.solve()