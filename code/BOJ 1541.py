# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1541-b6c66f36ce0740838df3c5bb849e5f16


from sys import stdin


class LostBracket(object):
  def __init__(self, txt):
    self.txt = txt.split("-")
    self.res = []
    
  def _split_sum(self):
    for i in self.txt:
      self.res.append(sum([int(j) for j in i.split("+")]) )

  def _print(self):
    print(self.res[0] - sum(self.res[1:]))

  def solve(self):
    self._split_sum()
    self._print()


if __name__ == "__main__":
  txt = stdin.readline().rstrip()
  LostBracket_problem = LostBracket(txt)
  LostBracket_problem.solve()
