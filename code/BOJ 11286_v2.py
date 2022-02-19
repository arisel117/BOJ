# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/11286-cb8f16a99e1d4e548b53abf02fe3dca7


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
      if self.heap[node] > value:
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
        doubled_node = node * 2
        if _len >= doubled_node + 1:
          if self.heap[doubled_node] > self.heap[doubled_node + 1]:
            pri_node = doubled_node + 1
          else:
            pri_node = doubled_node
        elif _len == doubled_node:
          pri_node = doubled_node
        else:
          break
        if last_data > self.heap[pri_node]:
          self.heap[node] = self.heap[pri_node]
          node = pri_node
        else:
          break
      self.heap[node] = last_data
      self.heap.pop()
      return return_value[1]
    else:
      return 0

  def solve(self):
    for num in self.num_list:
      if num[0]:
        self.heappush(num)
      else:
        print(self.heappop())


if __name__ == "__main__":
  num_list = []
  for _ in range(int(sys.stdin.readline())):
    i = int(sys.stdin.readline())
    num_list.append((abs(i), i))
  AbsHeap_problem = Heapq(num_list)
  AbsHeap_problem.solve()
