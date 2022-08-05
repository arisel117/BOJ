# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1963-59c11f5232ae43e6993e212bf93d69b5


from sys import stdin
from copy import deepcopy


class PrimePath(object):
  def __init__(self, T: int, arr: list):
    self.T = T
    self.arr = arr
    self.res = []

  def _get_eratos(self) -> dict:
    n = 10000
    a = [True] * (n + 1)
    m = int(n**0.5)
    eratos = dict()

    for i in range(2, m + 1):
      if a[i] == True:
        for j in range(i + i, n + 1, i):
          a[j] = False

    for i in range(2, n + 1):
      if a[i] and i > 1000:
        eratos[i] = False
    del n, a, m
    return eratos

  def _comparison(self, a: str, b: str):
    chk = True
    for i, j in zip(list(a), list(b)):
      if i == j:
        continue
      elif chk:
        chk = False
      else:
        return False
    return True

  def _find(self, src: int, dst: int) -> int:
    if src == dst:
      return 0

    visited = deepcopy(self.eratos)
    visited[src] = True
    stk = [(src, 0)]
    while stk:
      v, cnt = stk.pop(0)
      if v == dst:
        return cnt

      for i in visited:
        if visited[i]:
          continue
        if self._comparison(str(v), str(i)):
          visited[i] = True
          stk.append((i, cnt + 1))
    return None

  def _print(self):
    print(*["Impossible" if i == None else i for i in self.res], sep="\n")

  def solve(self):
    self.eratos = self._get_eratos()
    for src, dst in self.arr:
      self.res.append(self._find(src, dst))
    self._print()


if __name__ == "__main__":
  T = int(stdin.readline().rstrip())
  arr = [list(map(int, stdin.readline().split())) for i in range(T)]

  PrimePath_problem = PrimePath(T, arr)
  PrimePath_problem.solve()
