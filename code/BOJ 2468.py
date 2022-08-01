# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/2468-6abda3e72f8a4f8d83632351b6f89a75


from sys import stdin


class SafetyZone(object):
  def __init__(self, n: int, arr: list):
    self.n = n
    self.arr = arr
    self.nums = sorted(list(set(self.arr)), reverse=True)
    self.groups = [[-1]*self.n for _ in range(self.n)]
    self.group_member = {-1:False}
    self.around = [[-1, 0], [0, -1],[1, 0],[0, 1]]
    self.res = 1

  def _next_map(self, h: int):
    self._map = [[False]*self.n for _ in range(self.n)]
    for idx, v in enumerate(self.arr):
      if v == h:
        self._map[idx//self.n][idx%self.n] = True

  def _get_new_member(self):
    for num in range(max(self.group_member)+2):
      if num not in self.group_member:
        return num

  def _change(self, x, y):
    g = []
    for a, b in self.around:
      xa, yb = x+a, y+b
      if xa < 0 or xa >= self.n or yb < 0 or yb >= self.n:
        continue
      if self.groups[xa][yb] == -1:
        continue
      g.append(self.groups[xa][yb])
    g = sorted(list(set(g)))

    if len(g):
      self.group_member[g[0]] += [(x, y)]
      while len(g) > 1:
        _cg = self.group_member.pop(g[-1])
        self.group_member[g[0]].extend(_cg)
        for i, j in _cg:
          self.groups[i][j] = g[0]
        g.pop(-1)
    else:
      g.append(self._get_new_member())
      self.group_member[g[0]] = [(x, y)]
    self.groups[x][y] = g[0]

  def _find(self):
    for h in self.nums:
      self._next_map(h)
      for x in range(self.n):
        for y in range(self.n):
          if self._map[x][y]:
            self._change(x, y)
      self.res = max(self.res, len(self.group_member)-1)

  def _print(self):
    print(self.res)

  def solve(self):
    self._find()
    self._print()


if __name__ == "__main__":
  n = int(stdin.readline().rstrip())
  arr = []
  for i in range(n):
    arr += list(map(int, stdin.readline().split()))

  SafetyZone_problem = SafetyZone(n, arr)
  SafetyZone_problem.solve()
