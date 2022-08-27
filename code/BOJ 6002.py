# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/6002-Job-Hunt-e5d1c45dfcbd453b8a80cdae7eec285a


from sys import stdin


class JobHunt(object):
  def __init__(self, D: int, C: int, S: int, arr: list):
    self.D = D
    self.n = C
    self.srt = S
    self.arr = arr
    self.m = len(self.arr)

  def _init_map(self):
    self._map = [0]*(self.n + 1)
    self._map[0] = -1
    self._map[self.srt] = self.D

  def _bellman(self):
    for _ in range(self.n - 1):
      for a, b, c in self.arr:
        new_cost = self._map[a] + c
        if self._map[b] < new_cost:
          self._map[b] = new_cost

    for a, b, c in self.arr:
      if self._map[b] < self._map[a] + c:
        return True
    return False

  def _print(self):
    if self.pos:
      print(-1)
    else:
      print(max(self._map))

  def solve(self):
    self._init_map()
    self.pos = self._bellman()
    self._print()
    return


if __name__ == "__main__":
  D, P, C, F, S = map(int, stdin.readline().split())
  arr = []
  for _ in range(P):
    i, j = map(int, stdin.readline().split())
    arr.append((i, j, D))
  for _ in range(F):
    i, j, k = map(int, stdin.readline().split())
    arr.append((i, j, D - k))


  JobHunt_problem = JobHunt(D, C, S, arr)
  JobHunt_problem.solve()
