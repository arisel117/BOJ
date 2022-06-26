# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/10999-2-b9307c31cce141e1a8cb9138132e7340


from sys import stdin


class IntervalSum(object):
  def __init__(self, n, m, k, arr, req):
    self.n = n
    self.m = m
    self.k = k
    self.arr = arr
    self.req = [[True, i[1]-1, i[2]-1, i[3]] if i[0] == 1 else [False, i[1]-1, i[2]-1, 0] for i in req]
    self.segtree = [0] * (self.n * 4)
    self.lazy = [0] * (self.n * 4)
    self.res = []

  def init_segtree(self, start, end, node):
    if start == end:
      self.segtree[node] = self.arr[start]
    else:
      mid = (start + end) // 2
      self.init_segtree(start,   mid, node * 2)
      self.init_segtree(mid + 1, end, node * 2 + 1)
      self.segtree[node] = self.segtree[node * 2] + self.segtree[node * 2 + 1]

  def _propagation(self, node, start, end):
    if self.lazy[node] != 0:
      self.segtree[node] += (end - start + 1) * self.lazy[node]
      if start != end:
        self.lazy[node * 2    ] += self.lazy[node]
        self.lazy[node * 2 + 1] += self.lazy[node]
      self.lazy[node] = 0

  def _update(self, start, end, node, idx_start, idx_end, dif):
    self._propagation(node, start, end)

    if idx_start > end or start > idx_end:
      return
    if start >= idx_start and idx_end >= end:
      self.segtree[node] += (end - start + 1) * dif
      if start != end:
        self.lazy[node * 2    ] += dif
        self.lazy[node * 2 + 1] += dif
      return

    mid = (start + end) // 2
    self._update(start,   mid, node * 2,     idx_start, idx_end, dif)
    self._update(mid + 1, end, node * 2 + 1, idx_start, idx_end, dif)
    self.segtree[node] = self.segtree[node * 2] + self.segtree[node * 2 + 1]
  
  def _sum(self, start, end, node, left, right):
    self._propagation(node, start, end)

    if left > end or start > right:
      return 0
    if start >= left and right >= end:
      return self.segtree[node]

    mid = (start + end) // 2
    return self._sum(start, mid, node * 2, left, right) + self._sum(mid + 1, end, node * 2 + 1, left, right)

  def _print(self):
    print(*self.res, sep="\n")

  def solve(self):
    self.init_segtree(0, self.n - 1, 1)

    for a, b, c, d in self.req:
      if a:
        self._update(0, self.n - 1, 1, b, c, d)
      else:
        self.res.append(self._sum(0, self.n - 1, 1, b, c))

    self._print()


if __name__ == "__main__":
  n, m, k = map(int, stdin.readline().split())
  arr = [int(stdin.readline().rstrip()) for _ in range(n)]
  req = [list(map(int, stdin.readline().split())) for _ in range(m + k)]

  IntervalSum_problem = IntervalSum(n, m, k, arr, req)
  IntervalSum_problem.solve()
