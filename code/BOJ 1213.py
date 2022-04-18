# -*- coding: utf-8 -*-
# 링크 : https://www.notion.so/arisel/1213-fbbe789472614476a50b53cd9a2e88ec


from sys import stdin


class Pelindrome(object):
  def __init__(self, strs):
    self.s = strs
    self.ords = {}

  def solve(self):
    for i in range(ord("A"), ord("Z") + 1):
      i = chr(i)
      bef_len = len(self.s)
      self.s = self.s.replace(i, "")
      aft_len = len(self.s)
      self.ords[i] = bef_len - aft_len

    cnt = 1
    _left, _mid, _right = "", "", ""
    for i in self.ords.keys():
      if self.ords[i] % 2 == 1:
        cnt -= 1
        _mid = i
        if cnt == -1:
          self._print(-1)
          return 0
      _len = self.ords[i] // 2
      _left = _left + i * _len
      _right = i * _len + _right
    self._print(_left + _mid + _right)

  def _print(self, x):
    if x == -1:
      print("I'm Sorry Hansoo")
    else:
      print(x)


if __name__ == "__main__":
  strs = stdin.readline().rstrip()
  
  Pelindrome_problem = Pelindrome(strs)
  Pelindrome_problem.solve()
