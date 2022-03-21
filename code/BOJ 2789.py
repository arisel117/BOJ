# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/2789-834b496d7d1d465c98371e886206cfc6


from sys import stdin


class Censor(object):
  def __init__(self, txt):
    self._str = "CAMBRIDGE"
    self.txt = txt
    self.res = ""
    
  def _censor(self):
    for i in self.txt:
      if i not in self._str:
        self.res += i

  def _print(self):
    print(self.res)

  def solve(self):
    self._censor()
    self._print()


if __name__ == "__main__":
  txt = stdin.readline().rstrip()
  Censor = Censor(txt)
  Censor.solve()
