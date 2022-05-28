# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/2096-2cfe333f9b74465d9b56e2159f803d18


from sys import stdin


class SwapDP(object):
  def __init__(self, n):
    self.n = n

  def solve(self):
    _max, _min = [0] * 3, [0] * 3

    for _ in range(self.n):
      # Received input due to memory
      a,b,c = map(int, stdin.readline().split())

      _max = a + max(_max[:2]), b + max(_max), c + max(_max[1:])
      _min = a + min(_min[:2]), b + min(_min), c + min(_min[1:])

    print(max(_max), min(_min))


if __name__ == "__main__":
  n = int(stdin.readline().rstrip())

  SwapDP_problem = SwapDP(n)
  SwapDP_problem.solve()
