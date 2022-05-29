# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/9663-N-Queen-36d7736abe2b46059a4eb0ef004e0c84


def _check(x):
  for i in range(x):
    if v[x] == v[i] or abs(v[x] - v[i]) == x - i:
      return False
  return True

def _chess(x):
  global res
  if x == n:
    res += 1
    return
  for i in range(n):
    v[x] = i
    if _check(x):
      _chess(x + 1)

n = int(input())
res = 0
v = [0] * n
_chess(0)
print(res)
