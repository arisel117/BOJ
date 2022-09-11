# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/17472-2-652fcd5c0b8a4f468061392ed54f803f


from sys import stdin
import heapq as H
from collections import deque
from math import inf


class BridgeMaker(object):
  def __init__(self, n: int, m: int, _map: list):
    self.n = n
    self.m = m
    self._map = _map
    self.group_num = 2
    self.around = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    self.res = 0

  def _grouping(self, idx: tuple):
    que = deque( [idx] )
    self._map[idx[0]][idx[1]] = self.group_num
    while que:
      x, y = que.popleft()
      for i, j in self.around:
        xi, yj = x + i, y + j
        if xi < 0 or xi >= self.n or yj < 0 or yj >= self.m:
          continue
        if self._map[xi][yj] == True:
          self._map[xi][yj] = self.group_num
          que.append( (xi, yj) )

  def _find_map(self):
    for i in range(self.n):
      for j in range(self.m):
        if self._map[i][j] != True:
          continue

        self._grouping( (i, j) )
        self.group_num += 1

  def _connecting(self, _group_num: int, idx_x: int, idx_y: int):
    que = deque([])
    for i, j in self.around:
      que.append( (0, idx_x + i, idx_y + j, i, j) )
    while que:
      cnt, x, y, i, j = que.popleft()
      if x < 0 or x >= self.n or y < 0 or y >= self.m:
        continue
      if self._map[x][y] == False:
        que.append( (cnt + 1, x + i, y + j, i, j) )
      else:
        if cnt > 1:
          self._arr[_group_num][self._map[x][y]] = min(cnt, self._arr[_group_num][self._map[x][y]])

  def _find_edges(self):
    self._arr = [[inf] * self.group_num for _ in range(self.group_num)]
    for i in range(self.n):
      for j in range(self.m):
        if self._map[i][j] == False:
          continue

        self._connecting( self._map[i][j], i, j )

    del self._arr[:2]
    self._arr = [i[2:] for i in self._arr]
    self.group_num -= 2

    del self.n, self.m, self.around, self._map

  def _find(self, node: int):
    if self.parents[node] == node:
      return node
    else:
      self.parents[node] = self._find(self.parents[node])
      return self.parents[node]

  def _union(self, src: int, dst: int):
    src, dst = self._find(src), self._find(dst)
    if src == dst:
      return False
    else:
      self.parents[max(src, dst)] = min(src, dst)
      return True

  def _kruskal(self):
    que = []
    for src in range(self.group_num):
      for dst in range(self.group_num):
        cost = self._arr[src][dst]
        if cost != inf:
          H.heappush(que, [cost, src, dst])

    self.parents = [i for i in range(self.group_num)]
    self.mst = [[] for _ in range(self.group_num)]
    while que:
      cost, src, dst = H.heappop(que)
      if self._union(src, dst):
        self.res += cost
        self.mst[src].append(dst)
        self.mst[dst].append(src)

    for idx, v in enumerate(self.parents):
      if v != 0:
        self._find(idx)

  def _print(self):
    print(self.res)

  def solve(self):
    self._find_map()
    self._find_edges()

    if len(self._arr) == 0:
      self.res = -1
    else:
      for i in self._arr:
        if min(i) == inf:
          self.res = -1

    if self.res == 0:
      self._kruskal()
      if len(set(self.parents)) > 1:
        self.res = -1
    self._print()


if __name__ == "__main__":
  n, m = map(int, stdin.readline().rstrip().split())
  _map = []
  for _ in range(n):
    _map.append( [True if i == "1" else False for i in stdin.readline().rstrip().split()] )

  BridgeMaker_problem = BridgeMaker(n, m, _map)
  BridgeMaker_problem.solve()
