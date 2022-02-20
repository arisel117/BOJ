# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1202-bc7a619f89cd440d854b3a97d3b4a507


import heapq as H
import sys


class JewelThief(object):
  def __init__(self, num_jewel, num_bag, jewel_list, bag_list):
    self.num_jewel = num_jewel
    self.num_bag = num_bag
    self.jewel_list = jewel_list
    H.heapify(self.jewel_list)
    self.bag_list = sorted(bag_list)
    self.count = 0

  def _print(self):
    print(self.count)

  def solve(self):
    before_limit_weight = 0
    jewel_price_list = []
    for limit_weight in self.bag_list:
      if limit_weight != before_limit_weight:
        while True:
          try:
            weight, price = H.heappop(self.jewel_list)
          except:
            break
          if limit_weight < weight:
            H.heappush(self.jewel_list, [weight, price])
            break
          else:
            H.heappush(jewel_price_list, -price)
      if len(jewel_price_list):
        self.count -= H.heappop(jewel_price_list)
      before_limit_weight = limit_weight
    self._print()


if __name__ == "__main__":
  num_jewel, num_bag = map(int, sys.stdin.readline().split())
  jewel_list = [list(map(int, sys.stdin.readline().split())) for _ in range(num_jewel)]
  bag_list = [int(sys.stdin.readline().rstrip()) for _ in range(num_bag)]
  JewelThief_problem = JewelThief(num_jewel, num_bag, jewel_list, bag_list)
  JewelThief_problem.solve()
