# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/16953-A-B-fc44660cd9104eb8a287bcfb90b32011


from sys import stdin
from collections import deque


class AtoB(object):
  def __init__(self, a: int, b: int):
    self.a = a
    self.b = b
    self.res = -1
  
  def _print(self):
    print(self.res)

  def solve(self):
    stk = deque([(self.a, 1)])
    visited = set()

    while stk:
      num, cnt = stk.popleft()

      if num == self.b:
        self.res = cnt
        break

      if num > self.b or num in visited:
        continue
      visited.add(num)
      stk.extend([(num * 10 + 1, cnt + 1), (num * 2, cnt + 1)])

    self._print()


if __name__ == "__main__":
  a, b = map(int, stdin.readline().split())

  AtoB_problem = AtoB(a, b)
  AtoB_problem.solve()
