# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/2109-e3ee2fd877714524bd87ed5ac6f76a53


from sys import stdin
import heapq


class TourLecture(object):
  def __init__(self, arr):
    self.arr = arr
  
  def _find(self):
    prices = []
    for d, p in arr:
      heapq.heappush(prices, p)
      if d < len(prices):
        heapq.heappop(prices)
    self.res = sum(prices)

  def _pirnt(self):
    print(self.res)

  def solve(self):
    self._find()
    self._pirnt()


if __name__ == "__main__":
  arr = sorted([tuple(map(int, stdin.readline().split()))[::-1] for i in range(int(stdin.readline()))])

  TourLecture_problem = TourLecture(arr)
  TourLecture_problem.solve()
