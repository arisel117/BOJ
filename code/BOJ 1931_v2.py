# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1931-925de4fa0ce749a097f3b51eb8a15e3d


from sys import stdin
import heapq


class Meeting(object):
  def __init__(self, n, hq):
    self.n = n
    self.hq = hq
    self.cnt = 0

  def _count(self):
    meet_time = -1
    for _ in range(n):
      end, start = heapq.heappop(self.hq)
      if meet_time <= start:
        self.cnt += 1
        meet_time = end

  def _pirnt(self):
    print(self.cnt)

  def solve(self):
    self._count()
    self._pirnt()


if __name__ == "__main__":
  n = int(stdin.readline())
  hq = []
  for _ in range(n):
    a, b = map(int, stdin.readline().split())
    heapq.heappush(hq, (b, a))

  Meeting_problem = Meeting(n, hq)
  Meeting_problem.solve()
