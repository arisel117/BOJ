# -*- coding: utf-8 -*-
# 자세한 설명 링크 : https://arisel.notion.site/1244-5f48afaa75824f51b11d057a10f3394c


import sys


class Switch(object):
  def __init__(self, num_switch, switch_list, num_student):
    self.num_switch = num_switch
    self.switch = switch_list
    self.num_student = num_student

  def _men(self):
    for i, self.each_switch in enumerate(self.switch):
      if (i+1) % self.location == 0:
        self.switch[i] = not(self.each_switch)
      else:
        self.switch[i] = self.each_switch

  def _women(self):
    if (self.num_switch / 2) <= (self.num_switch - self.location):
      self.half = self.location
    else :
      self.half = self.num_switch - self.location + 1
    for i in range(self.half):
      if self.switch[self.location - 1 - i] == self.switch[self.location - 1 + i]:
        self.switch[self.location - 1 + i] = self.switch[self.location - 1 - i] = not(self.switch[self.location - 1 - i])
      else:
        break

  def _return(self):
    for i in range(0,self.num_switch,20):
      print(*[j.real for j in self.switch[i:i+20]])

  def solve(self):
    for _ in range(self.num_student):
      self.sex, self.location = map(int, sys.stdin.readline().split())
      if self.sex == 1:
        self._men()
      else:
        self._women()
    self._return()


if __name__ == "__main__":
  num_switch = int(sys.stdin.readline())
  switch_list = list(map(bool, map(int, sys.stdin.readline().split())))
  num_student = int(sys.stdin.readline())
  Switch_problem = Switch(num_switch, switch_list, num_student)
  Switch_problem.solve()
