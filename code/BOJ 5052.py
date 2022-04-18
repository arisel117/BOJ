# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/5052-7dc1201690884a859fe6bab645a06af7


from sys import stdin
from collections import deque


class PhoneBook(object):
  def __init__(self, n, num_list):
    self.n = n
    self.nums = num_list
    self.chk = False
    self.strlist = [str(i) for i in range(1, 10)]
    self.book = {i:-1 for i in self.strlist}

  def _insert(self, _nums, _book):
    num = _nums.popleft()
    if len(_nums) == 0:
      if _book[num] != -1:
        self.chk = True
      _book[num] = -2
    elif _book[num] == -2:
      self.chk = True
    elif _book[num] == -1:
      _book[num] = self._insert(_nums, {i:-1 for i in self.strlist})
    else:
      _book[num] = self._insert(_nums, _book[num])
    return _book

  def _trie(self):
    for phone_num in self.nums:
      self.book = self._insert(deque(phone_num), self.book)
      if self.chk == True:
        break

  def solve(self):
    self._trie()
    self._print()

  def _print(self):
    if self.chk:
      print("NO")
    else:
      print("YES")


if __name__ == "__main__":
  for TestCase in range(int(stdin.readline())):
    num_list = []
    for n in range(int(stdin.readline())):
      num_list.append(list(stdin.readline().rstrip()))
  
    PhoneBook_problem = PhoneBook(n, num_list)
    PhoneBook_problem.solve()
