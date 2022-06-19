# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1417-b6de60d5bf1c4a50b7081928a561bd90


from sys import stdin
import heapq


class Capitalism(object):
  def __init__(self, arr):
    self.arr = arr
    self.res = 0
  
  def _find(self):
    me = self.arr.pop(0)
    heapq.heapify(self.arr)
    while True:
      _min = heapq.heappop(self.arr)
      if me < _min:
        break
      self.res += 1
      me -= 1
      heapq.heappush(self.arr, _min + 1)

  def _pirnt(self):
    print(self.res)

  def solve(self):
    if len(self.arr) > 1:
      self._find()
    self._pirnt()


if __name__ == "__main__":
  arr = [-int(stdin.readline()) for _ in range(int(stdin.readline()))]

  Capitalism_problem = Capitalism(arr)
  Capitalism_problem.solve()
