# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/2240-8c7ee5eeab66447da0601c2800f61859


from sys import stdin


class PlumTree(object):
  def __init__(self, T, W, plums):
    self.T = T
    self.W = W
    self.plums = plums

  def solve(self):
    dp = [[0]*(self.W+1) for _ in range(len(self.plums))]
    for i, (_l, _n) in enumerate(self.plums):
      if _l :
        dp[i][0] = dp[i-1][0] + _n
      else:
        dp[i][0] = dp[i-1][0]
    
      for j in range(1, W+1):
        if _l and j%2 == 0:
          dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + _n
        elif not(_l) and j%2 == 1:
          dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + _n
        else:
          dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])
    print(max(dp[-1]))


def _compression_plum(T):
  _plum = []
  _now = 1
  _count = 0
  for i in range(T):
    i = int(stdin.readline().rstrip())
    if i == _now:
      _count += 1
    else:
      _plum.append([True if _now == 1 else False, _count])
      _now = i
      _count = 1
  _plum.append([True if _now == 1 else False, _count])
  return _plum


if __name__ == "__main__":
  T, W = map(int, stdin.readline().split())
  plums = _compression_plum(T)

  PlumTree_problem = PlumTree(T, W, plums)
  PlumTree_problem.solve()
