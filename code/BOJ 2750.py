# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/2750-8dd4e44e32ef4c4480fc13e586479a20


import sys


class SortNum(object):
  def __init__(self, num_list):
    self.nums = num_list

  def _print(self):
    for i in self.nums:
      print(i)

  def _sort(self):
    self.nums.sort()
  
  def solve(self):
    self._sort()
    self._print()


if __name__ == "__main__":
  _len = int(sys.stdin.readline())
  num_list = [int(sys.stdin.readline()) for _ in range(_len)]
  SortNum_problem = SortNum(num_list)
  SortNum_problem.solve()
