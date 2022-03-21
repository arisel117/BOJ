# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1991-a43a72945f994fc38facc3c31e3d418a


from sys import stdin


class TreeSearch(object):
  def __init__(self, tree):
    self.tree = tree
    self.start = 'A'
    self._pre_res = ''
    self._in_res = ''
    self._post_res = ''

  def _pre_order(self, node):
    if node == '.':
      return
    self._pre_res += node
    self._pre_order(tree[node][0])
    self._pre_order(tree[node][1])

  def _in_order(self, node):
    if node == '.':
      return
    self._in_order(tree[node][0])
    self._in_res += node
    self._in_order(tree[node][1])

  def _post_order(self, node):
    if node == '.':
      return
    self._post_order(tree[node][0])
    self._post_order(tree[node][1])
    self._post_res += node

  def _print(self):
    print(self._pre_res, self._in_res, self._post_res, sep="\n")

  def solve(self):
    self._pre_order(self.start)
    self._in_order(self.start)
    self._post_order(self.start)
    self._print()


if __name__ == "__main__":
  tree = {}
  for _ in range(int(stdin.readline())):
    parent, left, right = stdin.readline().split()
    tree[parent] = [left, right]
  TreeSearch_problem = TreeSearch(tree)
  TreeSearch_problem.solve()
