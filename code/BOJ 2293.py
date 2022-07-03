# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/2293-1-2175243021cb47ad8ccdefc497bcab2e


from sys import stdin


class CoinDP(object):
  def __init__(self, k, coins):
    self.k = k
    self.coins = coins
    self.map = [1] + [0 for _ in range(self.k)]

  def _dp(self):
    for c in self.coins:
      for i in range(c, self.k + 1):
        if i - c >= 0:
          self.map[i] += self.map[i - c]

  def _pirnt(self):
    print(self.map[-1])

  def solve(self):
    self._dp()
    self._pirnt()


if __name__ == "__main__":
  n, k = map(int, stdin.readline().split())
  arr = [int(stdin.readline()) for _ in range(n)]

  CoinDP_problem = CoinDP(k, arr)
  CoinDP_problem.solve()
