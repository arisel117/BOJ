# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/2644-3389798272d84ecab79a9eacf3fdce19


import sys


class KinshipDegree(object):
  def __init__(self, num_family, origin, destination, family_dic):
    self.num_family = num_family
    self.origin = origin
    self.destination = destination
    self.family_dic = family_dic
    self.res = []

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
    self.top_graph_origin = self._recursive_func(self.origin)
    self.top_graph_destination = self._recursive_func(self.destination)
    for top_graph_origin_index, top_graph_destination_index in enumerate(self.top_graph_origin):
      if top_graph_destination_index in self.top_graph_destination:
        self.res.append(top_graph_origin_index + self.top_graph_destination.index(top_graph_destination_index))
    self._return()


if __name__ == "__main__":
  num_family = int(sys.stdin.readline())
  origin, destination = map(int, sys.stdin.readline().split())
  num_link = int(sys.stdin.readline())
  family_dic = {i:-1 for i in range(1, num_family + 1)}
  for i in range(num_link):
    parent, child = map(int, sys.stdin.readline().split())
    family_dic[child] = parent
  KinshipDegree_problem = KinshipDegree(num_family, origin, destination, family_dic)
  KinshipDegree_problem.solve()
