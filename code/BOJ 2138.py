# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/2138-13e7ba394e0a42fcbdcbd1a1ffa67869


from sys import stdin
from copy import deepcopy as dcopy


class Switching(object):
  def __init__(self, n: int, arr1: list, arr2: list):
    self.n = n
    self.a1 = arr1
    self.a2 = arr2
    self.inf = int(1e9)

  def _click(self, i: int, arr: list):
    for idx in range(i, i + 3):
      if idx >= 0 and idx < self.n:
        arr[idx] = not arr[idx]
    return arr

  def _find(self, cnt: int, a1: list, a2: list):
    for i in range(n - 1):
      if a1[i] == a2[i]:
        continue
      cnt += 1
      a1 = self._click(i, a1)

    if a1[-1] == a2[-1]:
      return cnt
    return self.inf

  def _print(self):
    if self.res == self.inf:
      print(-1)
    else:
      print(self.res)

  def solve(self):
    self.res = self._find(0, dcopy(self.a1), dcopy(self.a2))

    _a = self._click(-1, dcopy(self.a1))
    self.res = min(self.res, self._find(1, _a, dcopy(self.a2)))

    self._print()


if __name__ == "__main__":
  n = int(stdin.readline().rstrip())
  arr1 = [True if i == '1' else False for i in stdin.readline().rstrip()]
  arr2 = [True if i == '1' else False for i in stdin.readline().rstrip()]

  Switching_problem = Switching(n, arr1, arr2)
  Switching_problem.solve()
