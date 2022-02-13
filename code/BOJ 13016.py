# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/13016-6ef5cc51502d499cad716570d457fb8a


from collections import deque
import sys


class Black_Flame_Dragon(object):
  def __init__(self, n, world):
    self.n = n + 1
    self.world = world
    self.tree = {i:[] for i in range(1, self.n)}

  def _make_tree(self):
    for (from_, to_, dist) in self.world:
      self.tree[from_].append([to_, dist])
      self.tree[to_].append([from_, dist])
        
  def _bfs(self, start_node):
    max_dist = 0
    dist_dict = {i:[] for i in range(1, self.n)}
    dist_dict[start_node] = max_dist
    que = deque([[start_node, max_dist]])
    visited = [True] * self.n
    while len(que):
      from_, before_dist = que.popleft()
      visited[from_] = False
      for to_, dist in self.tree[from_]:
        if visited[to_]:
          dist += before_dist
          dist_dict[to_] = dist
          que.append([to_, dist])
    return dist_dict

  def _find_diameter(self):
    first_dict = self._bfs(1)
    node_a = max(first_dict, key = first_dict.get)
    dist_a = self._bfs(node_a)
    node_b = max(dist_a, key = dist_a.get)
    dist_b = self._bfs(node_b)
    return dist_a, dist_b
    
  def _return(self, dist_a, dist_b):
    for i in range(1, self.n):
      print(max(dist_a[i], dist_b[i]))

  def solve(self):
    self._make_tree()
    dist_a, dist_b = self._find_diameter()
    self._return(dist_a, dist_b)


if __name__ == "__main__":
  n = int(sys.stdin.readline().rstrip())
  world = [list(map(int, sys.stdin.readline().split())) for i in range(n - 1)]
  Black_Flame_Dragon_problem = Black_Flame_Dragon(n, world)
  Black_Flame_Dragon_problem.solve()
