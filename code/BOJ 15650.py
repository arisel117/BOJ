# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/15650-N-M-2-fb741c571b9f4328996f4b4657896804


from itertools import combinations as _c
n, m = map(int, input().split())
for i in _c(range(1, n+1), m):
  print(*i)
