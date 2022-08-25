# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/16118-41445fce869f49f9aac231a0cc463c6d
# 이 코드는 통과 시간이 아슬아슬해서, 추가적인 개선이 필요함


from sys import stdin
from heapq import heappush, heappop


INF = int(1e9)
n, m = map(int, stdin.readline().split())
_map = [[] for _ in range(n+1)]
for _ in range(m):
  src, dst, k = map(int, stdin.readline().split())
  k *= 2
  _map[src].append((k, dst))
  _map[dst].append((k, src))

dist_f = [INF]*(n+1)
dist_f[1] = 0
que = [(0, 1)]
while que:
  _dist, _loc = heappop(que)
  if _dist > dist_f[_loc]:
    continue
  for ndist, nloc in _map[_loc]:
    dist = _dist + ndist
    if dist < dist_f[nloc]:
      dist_f[nloc] = dist
      heappush(que, (dist, nloc))

dist_w = [[INF]*2 for _ in range(n+1)]
dist_w[1][1] = 0
que = [(0, 1, False)]
while que:
  _dist, _loc, _odd = heappop(que)
  if _odd:
    if _dist > dist_w[_loc][0]:
      continue
  else:
    if _dist > dist_w[_loc][1]:
      continue

  for ndist, nloc in _map[_loc]:
    if _odd:
      dist = _dist + ndist * 2
      if dist < dist_w[nloc][1]:
        dist_w[nloc][1] = dist
        heappush(que, (dist, nloc, False))
    else:
      dist = _dist + ndist // 2
      if dist < dist_w[nloc][0]:
        dist_w[nloc][0] = dist
        heappush(que, (dist, nloc, True))


res = 0
for f, w in zip(dist_f, dist_w):
  if f < min(w):
    res += 1
print(res)
