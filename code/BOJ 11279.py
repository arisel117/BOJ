# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/11279-71edc419f95d42419ce9de59ce46f309


import heapq as H
import sys


class MaximumHeap(object):
  def __init__(self, num_list):
    self.num_list = num_list
    self.heap = []
    self.count = 0

  def _print(self):
    if len(self.heap):
      print(-H.heappop(self.heap))
    else:
      print(0)

  def solve(self):
    for num in self.num_list:
      if num:
        H.heappush(self.heap, -num)
      else:
        self._print()


if __name__ == "__main__":
  num_list = [int(sys.stdin.readline()) for i in range(int(sys.stdin.readline()))]
  MaximumHeap_problem = MaximumHeap(num_list)
  MaximumHeap_problem.solve()
