# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1927-33ad1101e0904f9c8ff9bc8364cff61c


import heapq as H
import sys


class MinimumHeap(object):
  def __init__(self, num_list):
    self.num_list = num_list
    self.heap = []
    self.count = 0

  def _print(self):
    if len(self.heap):
      print(H.heappop(self.heap))
    else:
      print(0)

  def solve(self):
    for num in self.num_list:
      if num:
        H.heappush(self.heap, num)
      else:
        self._print()


if __name__ == "__main__":
  num_list = [int(sys.stdin.readline()) for i in range(int(sys.stdin.readline()))]
  MinimumHeap_problem = MinimumHeap(num_list)
  MinimumHeap_problem.solve()
