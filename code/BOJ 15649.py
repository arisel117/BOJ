# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/15649-N-M-1-256bbf3eb091483da286e961894a6a65


from itertools import permutations as _p
n, m = map(int, input().split())
for i in _p(range(1, n+1), m):
  print(*i)
