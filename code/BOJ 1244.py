# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1244-5f48afaa75824f51b11d057a10f3394c


import sys


class Switch(object):
  def __init__(self, num_switch, switch_list, num_student, student_list):
    self.num_switch = num_switch
    self.switch = switch_list
    self.num_student = num_student
    self.student_list = student_list

  def _men(self, location):
    for i, self.each_switch in enumerate(self.switch):
      if (i+1) % location == 0:
        self.switch[i] = not(self.each_switch)
      else:
        self.switch[i] = self.each_switch

  def _women(self, location):
    if (self.num_switch / 2) <= (self.num_switch - location):
      self.half = location
    else :
      self.half = self.num_switch - location + 1
    for i in range(self.half):
      if self.switch[location - 1 - i] == self.switch[location - 1 + i]:
        self.switch[location - 1 + i] = self.switch[location - 1 - i] = not(self.switch[location - 1 - i])
      else:
        break

  def _return(self):
    for i in range(0,self.num_switch,20):
      print(*[j.real for j in self.switch[i:i+20]])

  def solve(self):
    for sex, location in self.student_list:
      if sex == 1:
        self._men(location)
      else:
        self._women(location)
    self._return()


if __name__ == "__main__":
  num_switch = int(sys.stdin.readline())
  switch_list = list(map(bool, map(int, sys.stdin.readline().split())))
  num_student = int(sys.stdin.readline())
  student_list = []
  for _ in range(num_student):
    student_list.append(list(map(int, sys.stdin.readline().split())))
  Switch_problem = Switch(num_switch, switch_list, num_student, student_list)
  Switch_problem.solve()
