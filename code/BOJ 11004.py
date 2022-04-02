# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/11004-K-e4c2832d4aac4002bb72016e3b920d56


import random
random.seed(42)
from sys import stdin

class Kth(object):
  def __init__(self, n_list, k):
    self.arr = n_list
    self.k = k

  def _quick_selection(self, arr, k):
    mid_num = arr[random.randint(0, len(arr) - 1)]
#     mid_num = arr[(len(arr)+1)//2 - 1]    # 이처럼 단순히 중간값으로 하면 약 86% 정도에서 시간초과 발생..
    left, mid, right = [], [], []
    for i in arr:
      if i < mid_num:
        left.append(i)
      elif i == mid_num:
        mid.append(i)
      else:
        right.append(i)

    _len = [len(left), len(left)+len(mid)]
    if k <= _len[0]:
      del arr, mid, right    # 재귀 함수를 사용 할 때, 안쓰는 것을 삭제하면 연산 속도가 빨라지는 현상이 있음..
      return self._quick_selection(left, k)
    elif k <= _len[1]:
      del arr, left, mid, right
      return mid_num
    else:
      del arr, left, mid
      return self._quick_selection(right, k - _len[1])

  def solve(self):
    ans = self._quick_selection(self.arr, self.k)
    print(ans)


if __name__ == "__main__":
  n, k = map(int, stdin.readline().split())
  n_list = list(map(int, stdin.readline().split()))
  Kth_problem = Kth(n_list, k)
  Kth_problem.solve()
