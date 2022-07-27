# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1388-d45354a525db4f70bae6c954e368d09a


from sys import stdin


class Floor(object):
  def __init__(self, n, m, arr):
    self.n = n
    self.m = m
    self.arr = arr
    self.visited = [[True]*self.m for _ in range(self.n)]
    self.res = 0

  def _chain_col(self, i, j):
    self.visited[i][j] = False
    ni = i + 1
    if ni < self.n and self.visited[ni][j] and self.arr[ni][j] == "|":
      self._chain_col(ni, j)

  def _chain_row(self, i, j):
    self.visited[i][j] = False
    nj = j + 1
    if nj < self.m and self.visited[i][nj] and self.arr[i][nj] == "-":
      self._chain_row(i, nj)

  def _finding(self):
    for i in range(self.n):
      for j in range(self.m):
        if self.visited[i][j]:
          self.res += 1
          if self.arr[i][j] == "-":
            self._chain_row(i, j)
          else:
            self._chain_col(i, j)

  def _print(self):
    print(self.res)

  def solve(self):
    self._finding()
    self._print()


if __name__ == "__main__":
  n, m = map(int, stdin.readline().split())
  arr = [list(stdin.readline().rstrip()) for i in range(n)]

  Floor_problem = Floor(n, m, arr)
  Floor_problem.solve()
