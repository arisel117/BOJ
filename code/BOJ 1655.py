# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1655-a5e8bc58e2054adbaae496ccd06007f3


from sys import stdin
import heapq as H


class MedianValue(object):
  def __init__(self, n: int, arr: list):
    self.n = n
    self.arr = arr
    self.MaxH, self.MinH = [], []
    self.res = []

  def _heappush(self, num: int):
    if len(self.MaxH) > len(self.MinH):
      H.heappush(self.MinH, num)
    else:
      H.heappush(self.MaxH, -num)

  def _if_swap(self):
    if -self.MaxH[0] > self.MinH[0]:
      H.heappush(self.MinH, -H.heappop(self.MaxH))
      H.heappush(self.MaxH, -H.heappop(self.MinH))

  def _get_median(self):
    self.MaxH.append(-self.arr[0])
    self.res.append(self.arr[0])

    for num in self.arr[1:]:
      self._heappush(num)
      self._if_swap()
      self.res.append(-self.MaxH[0])
  
  def _print(self):
    print(*self.res, sep="\n")

  def solve(self):
    self._get_median()
    self._print()


if __name__ == "__main__":
  n = int(stdin.readline().rstrip())
  arr = [int(stdin.readline().rstrip()) for i in range(n)]

  MedianValue_problem = MedianValue(n, arr)
  MedianValue_problem.solve()
