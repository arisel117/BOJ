# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/3778-8902029bf1734c8bb6af4f229dbefee1


import sys


class Anagram(object):
  def __init__(self, test_num, word_a, word_b):
    self.test_num = test_num
    self.a = word_a
    self.b = word_b
    self.count = 0
        
  def _count(self):
    for i in range(97, 123):
      ascii = chr(i)
      self.count += abs(self.a.count(ascii) - self.b.count(ascii))
  
  def _print(self):
    print("Case #{}: {}".format(self.test_num, self.count))
    
  def solve(self):
    self._count()
    self._print()


if __name__ == "__main__":
  for test_num in range(1, int(sys.stdin.readline()) + 1):
    word_a = list(sys.stdin.readline().rstrip())
    word_b = list(sys.stdin.readline().rstrip())
    Anagram_problem = Anagram(test_num, word_a, word_b)
    Anagram_problem.solve()
