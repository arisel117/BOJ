# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/2665-c5f080dfc21f4c4ab4b65c941880cf22


from collections import deque
import sys


class Make_Maze(object):
  def __init__(self, num_len, maze_map):
    self.num_len = num_len - 1
    self.maze_map = maze_map
    self.count = 0
    self.bound = [[-1, 0], [ 1, 0], [ 0,-1], [ 0, 1]]

  def _print(self):
    print(self.count)

  def _bfs(self):
    visited = [[-1]*(self.num_len+1) for i in range(self.num_len+1)]
    visited[0][0] = 0
    que = deque([(0,0)])
    while True:
      y, x = que.popleft()
      if (y == self.num_len) and (x == self.num_len):
        return visited[y][x]
      for a, b in self.bound:
        y_a, x_b = y + a, x + b
        if (y_a<0) or (y_a>self.num_len) or (x_b<0) or (x_b>self.num_len):
          continue
        if visited[y_a][x_b] == -1:
          if self.maze_map[y_a][x_b] == '1':
            que.appendleft((y_a,x_b))
            visited[y_a][x_b] = visited[y][x]
          else:
            que.append((y_a,x_b))
            visited[y_a][x_b] = visited[y][x] + 1

  def solve(self):
    self.count = self._bfs()
    self._print()


if __name__ == "__main__":
  num_len = int(sys.stdin.readline().rstrip())
  maze_map = [list(sys.stdin.readline().rstrip()) for _ in range(num_len)]
  Make_Maze_problem = Make_Maze(num_len, maze_map)
  Make_Maze_problem.solve()
