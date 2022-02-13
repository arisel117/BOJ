# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/2798-65904bdd0ec34cf8a445560a56c4fdc8


from itertools import combinations
import sys


class Blackjack(object):
  def __init__(self, m, cards):
    self.max_sum = m
    self.cards = cards
    self.count = 0

  def _comb(self):
    self.comb_list = list(combinations(self.cards, 3))
    for i,v in enumerate(self.comb_list):
      comb_sum = sum(v)
      if comb_sum == self.max_sum :
        self.count = comb_sum
        break
      elif (comb_sum > self.count) & (comb_sum <= self.max_sum):
        self.count = comb_sum

  def _return(self):
    print(self.count)

  def solve(self):
    self._comb()
    self._return()


if __name__ == "__main__":
  n, m = map(int, sys.stdin.readline().split())
  cards = list(map(int, sys.stdin.readline().split()))
  Blackjack_problem = Blackjack(m, cards)
  Blackjack_problem.solve()
