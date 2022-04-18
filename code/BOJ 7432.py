# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/7432-fb7b6d503b454b9c93b6e0337007f960


from sys import stdin
from collections import deque


class DiskTree(object):
  def __init__(self, n, dir_list):
    self.n = n
    self.dirs = dir_list
    self.dirtree = dict()

  def _insert(self, _dirs, _dirtree):
    dir = _dirs.popleft()
    if len(_dirs) == 0:
      if dir not in _dirtree:
        _dirtree[dir] = dict()
      return _dirtree
    elif dir not in _dirtree:
      _dirtree[dir] = dict()
    _dirtree[dir] = self._insert(_dirs, _dirtree[dir])
    return _dirtree

  def _trie(self):
    for dir in self.dirs:
      self.dirtree = self._insert(deque(dir), self.dirtree)

  def solve(self):
    self._trie()
    self._print()

  def _inner_print(self, _dirtree, cnt):
    if len(_dirtree) == 0:
      return 0
    for _inner_tree in sorted(_dirtree.keys()):
      print(" "*cnt + _inner_tree)
      cnt += 1
      self._inner_print(_dirtree[_inner_tree], cnt)
      cnt -= 1
  
  def _print(self):
    self._inner_print(self.dirtree, 0)


if __name__ == "__main__":
  n = int(stdin.readline())
  dir_list = []
  for n in range(n):
    dir_list.append(tuple(stdin.readline().rstrip().split("\\")))

  DiskTree_problem = DiskTree(n, dir_list)
  DiskTree_problem.solve()
