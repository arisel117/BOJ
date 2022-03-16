# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/1032-b2c3a4548cd74f6ca4eb203dd5def26c


from sys import stdin


class Prompt(object):
  def __init__(self, n, txt):
    self.n = n
    self.txt = txt
    self.len = len(txt[0])
    self.res = ''

  def _check(self, chk):
    t = ''
    for i in chk:
      if t == '':
        t = i
      if t != i:
        return '?'
    return t
  
  def _get_pattern(self):
    for j in range(self.len):
      chk = []
      for i in range(self.n):
        chk.append(txt[i][j])
      self.res += self._check(chk)

  def solve(self):
    self._get_pattern()
    print(self.res)


if __name__ == "__main__":
  n = int(stdin.readline().rstrip())
  txt = [list(stdin.readline().rstrip()) for _ in range(n)]
  Prompt_problem = Prompt(n, txt)
  Prompt_problem.solve()
