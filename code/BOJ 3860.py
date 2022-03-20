# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/3860-a1303abcc19d4bb28daa2a75e8995463


from sys import stdin


class Halloween(object):
  def __init__(self, width, height, graves, holes):
    self.inf = 1e9
    self.w = width
    self.h = height
    self.graves = graves
    self.holes = holes
    self.around = [[-1, 0], [ 1, 0], [ 0,-1], [ 0, 1]]
    self.map = [[0] * self.h for i in range(self.w)]
    self.nodes = [[self.inf] * self.h for i in range(self.w)]
    self.nodes[0][0] = 0
    self.edges = self.holes[:]
    self.end_w, self.end_h = self.w - 1, self.h - 1

  def _init_map(self):
    for i, j in self.graves:
      self.map[i][j] = 1
    for x1, y1, x2, y2, t in self.holes:
      self.map[x1][y1] = 2
    for i in range(self.w):
      for j in range(self.h):
        if i == self.end_w and j == self.end_h:
          continue
        if self.map[i][j] == 0:
          for a, b in self.around:
            ia, jb = i + a, j + b
            if ia >= 0 and jb >= 0 and ia < self.w and jb < self.h and self.map[ia][jb] != 1:
                self.edges.append((i, j, ia, jb, 1))

  def _bellmanford(self):
    for _ in range(self.w * self.h - 1):
      for edge in self.edges:
        x1, y1, x2, y2, t = edge
        if self.nodes[x1][y1] == self.inf:
          continue
        new_t = self.nodes[x1][y1] + t
        before_t = self.nodes[x2][y2]
        if new_t < before_t:
          self.nodes[x2][y2] = new_t
    for edge in self.edges:
      x1, y1, x2, y2, t = edge
      if self.nodes[x1][y1] == self.inf:
        continue
      new_t = self.nodes[x1][y1] + t
      before_t = self.nodes[x2][y2]
      if new_t < before_t:
        self.res = -self.inf
        return 0
    self.res = self.nodes[self.end_w][self.end_h]

  def _print(self):
    if self.res == -self.inf:
      print("Never")
    elif self.res == self.inf:
      print("Impossible")
    else:
      print(self.res)

  def solve(self):
    self._init_map()
    self._bellmanford()
    self._print()


if __name__ == "__main__":
  while True:
    width, height = map(int, stdin.readline().split())
    if width == height == 0:
      break
    graves = [list(map(int, stdin.readline().split())) for i in range(int(stdin.readline().rstrip()))]
    holes = [tuple(map(int, stdin.readline().split())) for i in range(int(stdin.readline().rstrip()))]

    Halloween_problem = Halloween(width, height, graves, holes)
    Halloween_problem.solve()
