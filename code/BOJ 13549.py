# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/13549-3-e4f0a45d651f42a5a754718a2fd11f0d


from sys import stdin
from collections import deque


class HideSeek(object):
  def __init__(self, n: int, m: int):
    self.n = n
    self.m = m
    self._max = self.m + 1
    self.res = 0

  def _get_cnt(self):
    visited = [False] * (self._max + 1)
    que = deque([(self.n, 0)])
    while que:
      num, cnt = que.popleft()
      if 0 > num or num > self._max or visited[num]:
        continue
      visited[num] = True

      if num == self.m:
        self.res = cnt
        break

      que.appendleft([2 * num, cnt])
      que.append([num + 1, cnt + 1])
      que.append([num - 1, cnt + 1])

  def _print(self):
    print(self.res)

  def solve(self):
    if self.n > self.m:
      self.res = self.n - self.m
    else:
      self._get_cnt()
    self._print()


if __name__ == "__main__":
  n, k = map(int, stdin.readline().split())

  HideSeek_problem = HideSeek(n, k)
  HideSeek_problem.solve()
