# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/14002-4-777d7b936cea4d7eb57fc177a0a77d21


from sys import stdin


class Subsequence(object):
  def __init__(self, n, arr):
    self.n = n
    self.a = arr
    self.map = [0] * self.n
    self.back = [-1] * self.n

  def _find(self):
    for i in range(self.n):
      for j in range(i):
        if self.a[i] > self.a[j] and self.map[i] < self.map[j]:
          self.map[i] = self.map[j]
          self.back[i] = j
      self.map[i] += 1

  def _print(self):
    _maxI, _maxV = -1, -1
    for idx, v in enumerate(self.map):
      if _maxV < v:
        _maxI, _maxV = idx, v
    print(_maxV)

    _path = [_maxI]
    while True:
      _back = self.back[_path[-1]]
      if _back == -1:
        break
      _path.append(_back)
    print(*[self.a[i] for i in reversed(_path)])


  def solve(self):
    self._find()
    self._print()


if __name__ == "__main__":
  n = int(stdin.readline())
  arr = list(map(int, stdin.readline().split()))

  Subsequence_problem = Subsequence(n, arr)
  Subsequence_problem.solve()
