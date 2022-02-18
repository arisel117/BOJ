# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1927-33ad1101e0904f9c8ff9bc8364cff61c


import sys


class Heapq(object):
  def __init__(self, num_list):
    self.heap = [None]
    self.num_list = num_list

  def heappush(self, value):
    last_idx = node = len(self.heap)
    self.heap.append(value)
    while node > 1:
      node //= 2
      if self.heap[node] > value :
        self.heap[last_idx] = self.heap[node]
        last_idx = node
      else:
        break
    self.heap[last_idx] = value
    return 0

  def heappop(self):
    _len = len(self.heap) - 1
    if _len:
      return_value = self.heap[1]
      last_data = self.heap[-1]
      node = 1
      while True:
        if _len >= node * 2 + 1:
          if self.heap[node * 2] > self.heap[node * 2 + 1]:
            pri_node = node * 2 + 1
          else:
            pri_node = node * 2
        elif _len == node * 2:
          pri_node = node * 2
        else:
          break
        if last_data > self.heap[pri_node]:
          self.heap[node] = self.heap[pri_node]
          node = pri_node
        else:
          break
      self.heap[node] = last_data
      self.heap.pop()
      return return_value
    else:
      return 0

  def solve(self):
    for num in self.num_list:
      if num:
        self.heappush(num)
      else:
        print(self.heappop())


if __name__ == "__main__":
  num_list = [int(sys.stdin.readline()) for i in range(int(sys.stdin.readline()))]
  MinimumHeap_problem = Heapq(num_list)
  MinimumHeap_problem.solve()
