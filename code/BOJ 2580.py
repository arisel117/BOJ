# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/2580-08503bb0ac4a4a1db002de72ce8ad338


import sys


class Sudoku(object):
  def __init__(self, sudoku_map):
    self.su_map = sudoku_map
    self.dim_x = [[True] * 10 for _ in range(9)]
    self.dim_y = [[True] * 10 for _ in range(9)]
    self.dim_z = [[True] * 10 for _ in range(9)]
    self.blank = []

  def _find_blank(self):
    for x in range(9):
      for y in range(9):
        if self.su_map[x][y]==0:
          self.blank.append([x, y])
        else:
          self.dim_x[x][self.su_map[x][y]] = False
          self.dim_y[y][self.su_map[x][y]] = False
          self.dim_z[x//3*3 + y//3][self.su_map[x][y]] = False
    self.len_blank = len(self.blank)

  def _fill_map(self, Count):
    if Count == self.len_blank:
      self._print()
      exit(0)    # if Python3  exit(0),    PyPy3  sys.exit(0),    가급적 이 방법 비추천
    a, b = self.blank[Count]
    for i in range(1, 10):
      if self.dim_x[a][i] & self.dim_y[b][i] & self.dim_z[a//3*3 + b//3][i]:
        self.su_map[a][b] = i
        self.dim_x[a][i] = self.dim_y[b][i] = self.dim_z[a//3*3 + b//3][i] = False
        self._fill_map(Count + 1)
        self.su_map[a][b] = 0
        self.dim_x[a][i] = self.dim_y[b][i] = self.dim_z[a//3*3 + b//3][i] = True

  def _solve(self):
    self._find_blank()
    self._fill_map(0)

  def _print(self):
    for i in self.su_map:
      print(*i)


if __name__ == "__main__":
  sudoku_map = [list(map(int, sys.stdin.readline().split())) for i in range(9)]
  sudoku_problem = Sudoku(sudoku_map)
  sudoku_problem._solve()
