# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/2327-c2d30e39e4734833ac009f60aacfbf63


from sys import stdin
import heapq

class Marathon(object):
  def __init__(self, h, n, arr):
    self.H = h + 1
    self.n = n
    self.arr = arr
    self.map = [False for _ in range(self.H)]
    self.map[0] = True

  def _matching(self):
    while self.arr:
      s, h = heapq.heappop(self.arr)
      for i in range(self.H - h)[::-1]:
        if self.map[i] and not self.map[i + h]:
          self.map[i + h] = s
      if self.map[-1]:
        break

  def _pirnt(self):
    print(-self.map[-1])

  def solve(self):
    self._matching()
    self._pirnt()


if __name__ == "__main__":
  H, N = map(int, stdin.readline().split())
  arr = []
  for _ in range(N):
    h, s = map(int, stdin.readline().split())
    arr.append((-s, h))
  heapq.heapify(arr)

  Marathon_problem = Marathon(H, N, arr)
  Marathon_problem.solve()
