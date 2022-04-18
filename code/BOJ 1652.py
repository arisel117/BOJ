# -*- coding: utf-8 -*-
# 링크 : https://www.notion.so/arisel/1652-e0997d49ff16482f82a3e906eea0bda0


from sys import stdin


class LyingPlace(object):
  def __init__(self, n, graph):
    self.n = n
    self.g = graph

  def _check(self, g):
    count = 0
    for line in g:
      for space in line.split('X'):
        if len(space) > 1:
          count += 1
    return count

  def solve(self):
    transpose_g = list("".join(list(x)) for x in zip(*graph))
    print(self._check(self.g), self._check(transpose_g))


if __name__ == "__main__":
  n = int(stdin.readline())
  graph = [stdin.readline().rstrip() for _ in range(n)]
  LyingPlace_problem = LyingPlace(n, graph)
  LyingPlace_problem.solve()
