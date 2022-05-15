# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/2042-43c0bf46e1ae4b1dbb41de7fbfbb2f1f


from sys import stdin


class IntervalSum(object):
  def __init__(self, n, m, k, arr, req):
    self.n = n
    self.m = m
    self.k = k
    self.arr = arr
    self.req = req
    self.stree = [0] * (self.n + 1)
    self.res = []

  def _update(self, idx, v):
    while idx < len(self.stree):
      self.stree[idx] += v
      idx += (idx & -idx)

  def _query(self, idx):
    res = 0
    while idx > 0:
      res += self.stree[idx]
      idx -= (idx & -idx)
    return res

  def _fenwick(self):
    for i in range(self.n):
      self._update(i + 1, self.arr[i])

    for a, b, c in self.req:
      if a == 1:
        self._update(b, c - self.arr[b - 1])
        self.arr[b-1] = c
      elif a == 2:
        self.res.append(self._query(c) - self._query(b - 1))

  def _print(self):
    for i in self.res:
      print(i)

  def solve(self):
    self._fenwick()
    self._print()


if __name__ == "__main__":
  n, m, k = map(int, stdin.readline().split())
  arr = [int(stdin.readline().rstrip()) for i in range(n)]
  req = [list(map(int, stdin.readline().split())) for i in range(m + k)]

  IntervalSum_problem = IntervalSum(n, m, k, arr, req)
  IntervalSum_problem.solve()
