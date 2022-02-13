# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1004-012e8eef551d449daedac4a4d22e69ce


import sys


class LittlePrince(object):
  def __init__(self, origin_destination, num_planet, planet_list):
    self.x_1, self.y_1, self.x_2, self.y_2 = origin_destination
    self.num_planet = num_planet
    self.planet_list = planet_list
    self.count = 0

  def _check(self, x, y, c_x, c_y, r):
    in_x = (x - c_x) ** 2
    in_y = (y - c_y) ** 2
    in_xy = (in_x + in_y) ** 0.5
    return in_xy < r

  def _traveling(self):
    for c_x, c_y, r in self.planet_list:
      self.origin_p = self._check(self.x_1, self.y_1, c_x, c_y, r)
      self.destination_p = self._check(self.x_2, self.y_2, c_x, c_y, r)
      if self.origin_p != self.destination_p:
        self.count += 1

  def _return(self):
    print(self.count)

  def solve(self):
    self._traveling()
    self._return()


if __name__ == "__main__":
  test_case = int(sys.stdin.readline())
  for t in range(test_case):
    origin_destination = list(map(int, sys.stdin.readline().split()))
    num_planet = int(sys.stdin.readline())
    planet_list = []
    for _ in range(num_planet):
      planet_list.append(list(map(int, sys.stdin.readline().split())))
    LittlePrince_problem = LittlePrince(origin_destination, num_planet, planet_list)
    LittlePrince_problem.solve()
