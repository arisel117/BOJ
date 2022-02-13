# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/2178-4759d888dee544beb7705c6120f2de29


from collections import deque
import sys

sys.setrecursionlimit(10 ** 9)


class Maze(object):
  def __init__(self, n, m, maze_map):
    self.dim_x = n
    self.dim_y = m
    self.maze_map = maze_map
    self.count = 0
    self.end_sig = True
    self.bfs_check_list = [[-1, 0],[0, -1],[1, 0],[0, 1]]

  def _make_map(self):
    self.map = [[False] + list(map(bool, map(int, list(i)))) + [False] for i in self.maze_map]
    self.map.insert(0, [False] * (self.dim_y + 2))
    self.map.append([False] * (self.dim_y + 2))

  def _bfs(self):
    que = deque([[1, 1, 1]])
    while len(que):
      x, y, c = que.popleft()
      if x == self.dim_x and y == self.dim_y:
        self.count = c
        return 0
      if self.map[x][y]:
        self.map[x][y] = False
        for i, j in self.bfs_check_list:
          que.append([x + i, y + j, c + 1])

  def _solve(self):
    self._make_map()
    self._bfs()
    self._print()

  def _print(self):
    print(self.count)


if __name__ == "__main__":
  n, m = list(map(int, sys.stdin.readline().split()))
  maze_map = [sys.stdin.readline().rstrip() for _ in range(n)]
  Maze_problem = Maze(n, m, maze_map)
  Maze_problem._solve()
