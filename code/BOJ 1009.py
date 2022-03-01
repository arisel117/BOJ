# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1009-868e82044db64c2e8d1f3e6dea1e89fc


from sys import stdin


class DistPrcs(object):
  def __init__(self, num_list):
    self.nums = num_list
    self.res = []

  def _print(self):
    for i in self.res:
      print(i)

  def _quotient(self):
    for x, a in self.nums:
      x %= 10
      a %= 4
      a = 4 if a == 0 else a
      ans = (x ** a) % 10
      self.res.append(10 if ans == 0 else ans)
  
  def solve(self):
    self._quotient()
    self._print()


if __name__ == "__main__":
  num_list = [list(map(int, stdin.readline().split())) for _ in range(int(stdin.readline()))]
  DistPrcs_problem = DistPrcs(num_list)
  DistPrcs_problem.solve()
