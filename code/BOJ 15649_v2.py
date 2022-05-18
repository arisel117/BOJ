# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/15649-N-M-1-256bbf3eb091483da286e961894a6a65


from sys import stdin

class Permutations(object):
  def __init__(self, n, m):
    self.n = n
    self.m = m
    self.arr = list(range(1, self.n + 1))

  def _gen(self, arr, m):
    for i in range(len(arr)):
      if m == 1:
        yield [arr[i]]
      else:
        for next in self._gen(arr[:i] + arr[i+1:], m-1):
          yield [arr[i]] + next

  def _print(self):
    for i in self.res:
      print(*i)

  def solve(self):
    self.res = self._gen(self.arr, self.m)
    self._print()

if __name__ == "__main__":
  n, m = map(int, stdin.readline().split())

  Permutations_problem = Permutations(n, m)
  Permutations_problem.solve()
