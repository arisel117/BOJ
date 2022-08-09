# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1655-a5e8bc58e2054adbaae496ccd06007f3


from sys import stdin
import heapq as H


class MedianValue(object):
  def __init__(self, n: int, arr: list):
    self.n = n
    self.arr = arr
    self.MinH = [10001]
    self.MaxH = [10001]
    self.nlist = []
    self.res = []

  def _heappush(self, num: int):
    self.nlist.extend([num, -H.heappop(self.MaxH), H.heappop(self.MinH)])
    self.nlist.sort()

    if len(self.nlist) == 3:
      self.res.append(self.nlist[1])
    else:
      self.res.append(min(self.nlist[1:3]))
      H.heappush(self.MaxH, -self.nlist.pop(0))
      H.heappush(self.MinH, self.nlist.pop())
    H.heappush(self.MaxH, -self.nlist.pop(0))
    H.heappush(self.MinH, self.nlist.pop())

  def _print(self):
    print(*self.res, sep="\n")

  def solve(self):
    for num in self.arr:
      self._heappush(num)

    self._print()


if __name__ == "__main__":
  n = int(stdin.readline().rstrip())
  arr = [int(stdin.readline().rstrip()) for i in range(n)]

  MedianValue_problem = MedianValue(n, arr)
  MedianValue_problem.solve()
