# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/16466-c7bdff075df84b0da20de272893224c1


from sys import stdin
import heapq as H


class Concert(object):
  def __init__(self, n, ticket):
    self.n = n
    self.ticket = ticket
    H.heapify(self.ticket)

  def _minheap(self):
    for i in range(1, len(self.ticket)):
      if i != H.heappop(self.ticket):
        return i
    return self.n + 1

  def solve(self):
    res = self._minheap()
    print(res)


if __name__ == "__main__":
  n = int(stdin.readline().rstrip())
  ticket = list(map(int, stdin.readline().split()))
  Concert_problem = Concert(n, ticket)
  Concert_problem.solve()
