# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/2327-c2d30e39e4734833ac009f60aacfbf63


from sys import stdin

class Marathon(object):
  def __init__(self, h, n, arr):
    self.H = h + 1
    self.n = n
    self.arr = sorted(arr, key=lambda x:x[1], reverse=True)
    self.map = [False for _ in range(self.H)]
    self.map[0] = True

  def _matching(self):
    for h, s in self.arr:
      for i in range(self.H - h)[::-1]:
        if self.map[i] and not self.map[i + h]:
          self.map[i + h] = s
      if self.map[-1]:
        break

  def _pirnt(self):
    print(self.map[-1])

  def solve(self):
    self._matching()
    self._pirnt()


if __name__ == "__main__":
  H, N = map(int, stdin.readline().split())
  arr = [tuple(map(int, stdin.readline().split())) for _ in range(N)]

  Marathon_problem = Marathon(H, N, arr)
  Marathon_problem.solve()
