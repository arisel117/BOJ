# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/21317-b6c85a6255314765b9bf86f21a6d1075


from sys import stdin


class SteppingStone(object):
  def __init__(self, n, _map, k):
    self.n = n
    self._last = self.n - 1
    self._map = _map
    self.k = k
    self._res = 1e9

  def _dp(self, idx, sjump, curv):
    if (curv >= self._res) or (idx > self._last):
      return 0

    if idx == self._last:
      self._res = min(self._res, curv)
      return 0

    self._dp(idx+1, sjump, self._map[idx][0] + curv)
    self._dp(idx+2, sjump, self._map[idx][1] + curv)
    if sjump:
      self._dp(idx+3, False, self.k + curv)
    
  def _print(self):
    print(self._res)

  def solve(self):
    self._dp(0, True, 0)
    self._print()


if __name__ == "__main__":
  n = int(stdin.readline().rstrip())
  _map = [list(map(int, stdin.readline().split())) for _ in range(n-1)]
  k = int(stdin.readline().rstrip())

  SteppingStone_problem = SteppingStone(n, _map, k)
  SteppingStone_problem.solve()
