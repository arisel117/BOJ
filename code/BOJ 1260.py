# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1260-DFS-BFS-cd6efe20107744c8810298405555523e


from collections import deque
import sys


class DFSAndBFS(object):
  def __init__(self, n, m, v, map_links):
    self.n_node = n
    self.n_link = m
    self.start_node = v
    self.map_links = map_links
    self.graph = [[] for _ in range(n+1)]
    self.dfs_linked = []
    self.bfs_linked = []

  def _make_map(self):
    for i,j in self.map_links:
      self.graph[i].append(j)
      self.graph[j].append(i)
    for i,v in enumerate(self.graph):
      v.sort()

  def _dfs(self):
    dfs_check_list = [False]*(self.n_node + 1)
    dfs_stack = [self.start_node]
    while dfs_stack:
      i = dfs_stack.pop()
      if not dfs_check_list[i]:
        dfs_check_list[i] = True
        self.dfs_linked.append(i)
        dfs_stack += list(reversed(self.graph[i]))

  def _bfs(self):
    bfs_check_list = [False]*(self.n_node + 1)
    bfs_queue = deque([self.start_node])
    bfs_check_list[self.start_node] = True
    while bfs_queue:
      i = bfs_queue.popleft()
      self.bfs_linked.append(i)
      for j in self.graph[i]:
        if not bfs_check_list[j]:
          bfs_queue.append(j)
          bfs_check_list[j] = True

  def _return(self):
    print(*self.dfs_linked)
    print(*self.bfs_linked)

  def solve(self):
    self._make_map()
    self._dfs()
    self._bfs()
    self._return()


if __name__ == "__main__":
  n, m, v = list(map(int, sys.stdin.readline().split()))
  map_links = []
  for _ in range(m):
    map_links.append(list(map(int, sys.stdin.readline().split())))
  DFSAndBFS_problem = DFSAndBFS(n, m, v, map_links)
  DFSAndBFS_problem.solve()
