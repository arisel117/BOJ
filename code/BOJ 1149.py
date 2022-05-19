# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1149-RGB-a91939686bff424a81b7ac41b0bc9bc7


from sys import stdin


class RGB(object):
  def __init__(self, n, rgbs):
    self.n = n
    self.rgb = rgbs
    self._map = [[] for _ in range(self.n)]
    self._map[0] = self.rgb[0]

  def _print(self):
    print(min(self._map[n-1]))

  def solve(self):
    for i in range(1, self.n):
      self._map[i] = [
        self.rgb[i][0] + min(self._map[i - 1][1], self._map[i - 1][2]),
        self.rgb[i][1] + min(self._map[i - 1][0], self._map[i - 1][2]),
        self.rgb[i][2] + min(self._map[i - 1][0], self._map[i - 1][1]),
      ]
    self._print()


if __name__ == "__main__":
  n = int(stdin.readline().rstrip())
  rgbs = [list(map(int, stdin.readline().split())) for i in range(n)]
  RGB_problem = RGB(n, rgbs)
  RGB_problem.solve()
