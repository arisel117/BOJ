# -*- coding: utf-8 -*-
# 자세한 설명 링크 : https://arisel.notion.site/1946-822cfd96a9d64c91b209a8e1d751c1f3


import sys


class New_Recruits(object):
  def __init__(self):
    self.inf = 1e+7

  def _solve_init(self, num_person, dic_list):
    self.person = num_person
    self.dic_list = dic_list
    self.max_num = self.inf
    self.count = 0
    self.dic = dict()
    for a, b in self.dic_list:
      self.dic[a] = b

  def _count(self):
    for p in range(1, self.person + 1):
      if self.dic[p] < self.max_num:
        self.max_num = self.dic[p]
        self.count += 1
      if self.max_num == 1:
        break

  def _return(self):
    print(self.count)

  def solve(self, num_person, dic_list):
    self._solve_init(num_person, dic_list)
    self._count()
    self._return()


if __name__ == "__main__":
  test_case = int(sys.stdin.readline())
  New_Recruits_problem = New_Recruits()
  for _ in range(test_case):
    dic_list = []
    num_person = int(sys.stdin.readline())
    for p in range(num_person):
      dic_list.append(list(map(int, sys.stdin.readline().split())))
    New_Recruits_problem.solve(num_person, dic_list)