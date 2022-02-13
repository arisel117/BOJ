# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/11724-859d7561f3414362a61cba9c8707fd98


from collections import deque
import sys


class ConnectedComponent(object):
  def __init__(self, n, m, graph_list):
    self.node = n
    self.link = m
    self.graph_list = graph_list
    self.graph = {i:[] for i in range(n+1)}
    self.graph[0] = False
    self.count = 0

  def _make_graph(self):
    for i,j in self.graph_list:
      self.graph[i].append(j)
      self.graph[j].append(i)

  def _bfs(self):
    bfs_que = deque([])
    for i in self.graph:
      temp = self.graph[i]
      if temp == []:    # Connected Component는 연결 관계가 없는 노드도 카운트 해야 함
        self.count += 1
      if temp:
        self.count += 1
        bfs_que += temp
        while bfs_que:
          que = bfs_que.popleft()
          if self.graph[que]:
            bfs_que += self.graph[que]
            self.graph[que] = False

  def _return(self):
    print(self.count)

  def solve(self):
    self._make_graph()
    self._bfs()
    self._return()


if __name__ == "__main__":
  n, m = list(map(int, sys.stdin.readline().split()))
  graph = []
  for _ in range(m):
    graph.append(list(map(int, sys.stdin.readline().split())))
  ConnectedComponent_problem = ConnectedComponent(n, m, graph)
  ConnectedComponent_problem.solve()
