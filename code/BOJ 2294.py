# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/2294-2-e81063f624f843cdab2ca4af1cee4df3


from sys import stdin


class CoinDP(object):
  def __init__(self, k, coins):
    self.inf = int(1e6+1)
    self.k = k
    self.coins = coins
    self.map = [self.inf for _ in range(max(max(self.coins), self.k) + 1)]

  def _dp(self):
    for c in self.coins:
      self.map[c] = 1
      for i in range(c + 1, self.k + 1):
        if i - c >= 0:
          self.map[i] = min(self.map[i], 1 + self.map[i - c])

  def _pirnt(self):
    if self.map[self.k] >= self.inf:
      print(-1)
    else:
      print(self.map[self.k])

  def solve(self):
    self._dp()
    self._pirnt()


if __name__ == "__main__":
  n, k = map(int, stdin.readline().split())
  arr = [int(stdin.readline()) for _ in range(n)]

  CoinDP_problem = CoinDP(k, arr)
  CoinDP_problem.solve()
