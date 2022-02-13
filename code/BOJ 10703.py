# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/10703-f3ceb25ad85c4d6f8e76f6f523a8c246


import sys


class Meteor(object):
  def __init__(self, r, s, meteor_map):
    self.r = r
    self.s = s
    self.meteor_map = meteor_map
    self.list_x = []

  def _find_fall_map(self):
    self.fell_map = list()
    for i in range(self.s):
      self.fell_map += self.meteor_map[i::self.s]

    gap_list = []
    count = self.r-1
    for i,v in enumerate(self.fell_map):
      if v == 'X':
        self.list_x.append(i)
        self.fell_map[i] = '.'
        count = 0
      elif v == '.':
        count += 1
      else:
        gap_list.append(count)

    self.gap = min(gap_list)
    for i in self.list_x:
      self.fell_map[i+self.gap] = 'X'

  def _print_map(self):
    for i in range(self.r):
      print(*self.fell_map[i::self.r],sep='')

  def solve(self):
    self._find_fall_map()
    self._print_map()


if __name__ == "__main__":
  r, s = map(int, sys.stdin.readline().split())
  meteor_map = []
  for _ in range(r):
    meteor_map += list(sys.stdin.readline().rstrip())
  meteor_problem = Meteor(r, s, meteor_map)
  meteor_problem.solve()
