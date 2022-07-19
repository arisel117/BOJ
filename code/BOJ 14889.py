# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/14889-042afaa42d5c4b208ce9eba33b7e2f36


from sys import stdin
from itertools import combinations


class GoldenBalance(object):
  def __init__(self, n, arr):
    self.n = n
    self.arr = arr
    self._map = {i : [self.arr[i][j] + self.arr[j][i] for j in range(n)] for i in range(n)}
    self._half = sum([sum(self._map[i]) for i in range(n)]) // 2
    self.res = self._half

  def _find(self):
    member = [i for i in range(n)]
    for TA in combinations(member, n // 2):
      PA = sum([self._map[a][b] for i, a in enumerate(TA) for b in TA[i:]])

      TB = [m for m in member if m not in TA]
      PB = sum([self._map[a][b] for i, a in enumerate(TB) for b in TB[i:]])

      self.res = min(self.res, abs(PA - PB))

  def _print(self):
      print(self.res)

  def solve(self):
    self._find()
    self._print()


if __name__ == "__main__":
  n = int(stdin.readline())
  arr = [list(map(int, stdin.readline().split())) for _ in range(n)]

  GoldenBalance_problem = GoldenBalance(n, arr)
  GoldenBalance_problem.solve()
