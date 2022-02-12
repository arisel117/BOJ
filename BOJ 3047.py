# -*- coding: utf-8 -*-
# 자세한 설명 링크 : https://arisel.notion.site/3047-ABC-58ff01339ecf481c828627e5f7c32200


import sys


class ABC(object):
  def __init__(self, ints, strs):
    self.ints = sorted(ints)
    self.strs = strs
    self.res = ''

  def reorder_ascii(self):
    for s in self.strs:
      self.res += str(self.ints[ord(s) - 65])

  def return_(self):
    print(self.res)

  def solve(self):
    self.reorder_ascii()
    self.return_()


if __name__ == "__main__":
  ints = list(map(int, sys.stdin.readline().split()))
  strs = str(sys.stdin.readline()).rstrip()

  abc_problem = ABC(ints, strs)
  abc_problem.solve()


if __name__ == "__main__":
  response()