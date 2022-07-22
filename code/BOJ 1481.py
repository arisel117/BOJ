# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1481-a342223d8a84457a92cad5149688a6c0


from sys import stdin


class SSquare(object):
  def __init__(self, n, d):
    self.n = n
    self.d = d
    self._map = [[-1]*d for _ in range(d)]
    self._row = [[False]*d for _ in range(d)]
    self._col = [[False]*d for _ in range(d)]
    self._f = False

  def _next(self, x, y, n):
    if self._row[x][n] or self._col[y][n]:
      return True
    self._map[x][y] = n
    self._row[x][n] = self._col[y][n] = True
    return False

  def _back(self, x, y, n):
    self._map[x][y] = -1
    self._row[x][n] = self._col[y][n] = False

  def _checking(self, x, y, i):
    if self.d - y-1 >= self.d - sum(self._row[x]) or self.d - x-1 >= self.d - sum(self._col[y]):
      return False
    self._back(x, y, i)
    return True

  def _mapping(self, x, y):
    if x == self.d:
      self._f = True
      return

    for i in range(d):
      if self._next(x, y, i):
        continue

      if self._checking(x, y, i):
        continue
      self._mapping((y+1)//self.d + x, (y+1)%self.d)

      if self._f:
        return
      self._back(x, y, i)

  def _expending(self):
    self.res = []
    for i in range(self.n - self.d):
      self.res.append([0 for i in range(self.n - self.d)] + [i for i in range(self.d)])

    for i in range(self.d):
      self.res.append([i]*(self.n - self.d) + self._map[i])

  def _print(self):
    for i in self.res:
      print(*i)

  def solve(self):
    self._mapping(0, 0)
    self._expending()
    self._print()


if __name__ == "__main__":
  n, d = map(int, stdin.readline().split())

  SSquare_problem = SSquare(n, d)
  SSquare_problem.solve()
