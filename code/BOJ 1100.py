# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1100-6c292625794e4e77a36ba986c3eeee95


import sys


class Chess(object):
  def __init__(self, chess_map):
    self.map = chess_map
    self.count = 0
        
  def _count(self):
    for i in self.map[::2]:
      self.count += i[::2].count("F")
    for i in self.map[1::2]:
      self.count += i[1::2].count("F")
  
  def _print(self):
    print(self.count)
    
  def solve(self):
    self._count()
    self._print()


if __name__ == "__main__":
  chess_map = [list(sys.stdin.readline().rstrip()) for _ in range(8)]
  Chess_problem = Chess(chess_map)
  Chess_problem.solve()
