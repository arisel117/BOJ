# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1931-925de4fa0ce749a097f3b51eb8a15e3d


from sys import stdin


class Meeting(object):
  def __init__(self, arr):
    self.arr = sorted(arr, key= lambda x: [x[1], x[0]])
    self.cnt = 0

  def _count(self):
    meet_time = -1
    for start, end in self.arr:
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
  arr = [tuple(map(int, stdin.readline().split())) for _ in range(n)]

  Meeting_problem = Meeting(arr)
  Meeting_problem.solve()
