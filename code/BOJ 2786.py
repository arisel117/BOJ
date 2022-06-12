# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/2786-95d348c9aa9a4399a5aafa1d191ec290


from sys import stdin


class Restaurant(object):
  def __init__(self, n, arr):
    self.n = n
    self.arr = arr
    self.arr.sort(key=lambda x : (x[1]))
    self.res = []

  def _init_cost(self):
    cost, _min = [], arr[-1][0]
    for i in [i[0] for i in arr[::-1]]:
      _min = min(_min, i)
      cost.append(_min)
    return cost[::-1]
  
  def _find(self):
    now, _min = 0, 1000001
    for i in range(self.n):
      before = now
      now += self.arr[i][1]
      _min = min(_min, self.arr[i][0] - self.arr[i][1])
      self.res.append(min(before + self.cost[i], now + _min))

  def _pirnt(self):
    print(*self.res, sep="\n")

  def solve(self):
    self.cost = self._init_cost()
    self._find()
    self._pirnt()


if __name__ == "__main__":
  n = int(stdin.readline())
  arr = [tuple(map(int, stdin.readline().split())) for _ in range(n)]

  Restaurant_problem = Restaurant(n, arr)
  Restaurant_problem.solve()
