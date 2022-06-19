# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/11053-f692e2085fed46f7b7b51d52ed467507


from sys import stdin


class Subsequence(object):
  def __init__(self, n, arr):
    self.n = n
    self.a = arr
    self.map = [0] * self.n

  def _find(self):
    for i in range(self.n):
      for j in range(i):
        if self.a[i] > self.a[j] and self.map[i] < self.map[j]:
          self.map[i] = self.map[j]
      self.map[i] += 1

  def _pirnt(self):
    print(max(self.map))

  def solve(self):
    self._find()
    self._pirnt()


if __name__ == "__main__":
  n = int(stdin.readline())
  arr = list(map(int, stdin.readline().split()))

  Subsequence_problem = Subsequence(n, arr)
  Subsequence_problem.solve()
