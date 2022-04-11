# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/17501-e146726342354625ad3ffdabaee85a8a


from collections import deque
from sys import stdin


class FormulaTree(object):
  def __init__(self, n, nums, oprs):
    self.n = n
    self.nums = sorted(nums)
    self.oprs = oprs

  def _init_tree(self):
    called = [True] + [False for i in range(2 * self.n - 1)]
    self.tree = {i:[1, None, None] for i in range(1, 2 * self.n)}
    for (opr, left, right), p_num in zip(self.oprs, range(self.n + 1, 2 * self.n + 1)):
      left, right = int(left), int(right)
      if opr == '+':
        self.tree[p_num] = [1, left, right]
      else:
        self.tree[p_num] = [-1, left, right]
      called[left] = True
      called[right] = True
    self.top_idx = called.index(False)
    del called, self.oprs

  def _count_minus(self):
    que = deque([[self.top_idx, 1] + self.tree[self.top_idx]])
    while que:
      idx, parent, opr, left, right = que.popleft()
      if left == right == None:
        self.tree[idx] = parent * opr
        continue
      que.append([left, parent] + self.tree[left])
      que.append([right, parent * opr] + self.tree[right])

  def _print(self):
    count = 0
    for i in range(1, self.n + 1):
      if self.tree[i] == -1:
        count += 1
    print(sum(self.nums[count:]) - sum(self.nums[:count]))

  def solve(self):
    self._init_tree()
    self._count_minus()
    self._print()


if __name__ == "__main__":
  n = int(stdin.readline())
  nums = [int(stdin.readline()) for _ in range(n)]
  oprs = [stdin.readline().split() for _ in range(n - 1)]
  FormulaTree_problem = FormulaTree(n, nums, oprs)
  FormulaTree_problem.solve()
