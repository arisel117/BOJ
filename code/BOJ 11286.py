# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/11286-cb8f16a99e1d4e548b53abf02fe3dca7


import heapq as H
import sys


class AbsHeap(object):
  def __init__(self, num_list):
    self.num_list = num_list
    self.heap = []
    self.count = 0

  def _print(self):
    if len(self.heap):
      print(H.heappop(self.heap)[1])
    else:
      print(0)

  def solve(self):
    for num in self.num_list:
      if num[0]:
        H.heappush(self.heap, num)
      else:
        self._print()


if __name__ == "__main__":
  num_list = []
  for _ in range(int(sys.stdin.readline())):
    i = int(sys.stdin.readline())
    num_list.append((abs(i), i))
  AbsHeap_problem = AbsHeap(num_list)
  AbsHeap_problem.solve()
