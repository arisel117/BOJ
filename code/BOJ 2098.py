# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/2098-06710a02a221450fb741cd6463d2b364


from sys import stdin


class TSP(object):
  def __init__(self, n, _map):
    self.inf = 1e9
    self.n = n
    self._map = _map
    self._fmap = [[0] * (1 << (self.n - 1)) for _ in range(self.n)]
    self._last = (1 << (self.n - 1)) - 1

  def _dp(self, i, route):
    if self._fmap[i][route] != 0:
      return self._fmap[i][route]

    if route == self._last:
      if self._map[i][0]:
        return self._map[i][0]
      else:
        return self.inf

    _minv = self.inf
    for j in range(1, n):
      if (not self._map[i][j]) or (route & (1 << (j - 1))):
        continue
      _minv = min(_minv, self._map[i][j] + self._dp(j, route | (1 << (j - 1))))
    self._fmap[i][route] = _minv
    return _minv

  def solve(self):
    print(self._dp(0, 0))


if __name__ == "__main__":
  n = int(stdin.readline().rstrip())
  _map = [list(map(int, stdin.readline().split())) for _ in range(n)]

  TSP_problem = TSP(n, _map)
  TSP_problem.solve()
