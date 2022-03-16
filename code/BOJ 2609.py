# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/2609-048bee74d0954ac5acc960ca526ffebc


from sys import stdin


class GCDandLCM(object):
  def __init__(self, num_a, num_b):
    self.a = max(num_a, num_b)
    self.b = min(num_a, num_b)

  def _gcd(self): # 최대공약수 Greatest Common Divisor
    a, b = self.a, self.b
    while b > 0:
      a, b = b, a % b
    self.gcd = a
    return self.gcd
  
  def _lcm(self): # 최소공배수 Least Common Multiple
    return int(self.gcd * (self.a / self.gcd) * (self.b / self.gcd))

  def solve(self):
    print(self._gcd())
    print(self._lcm())


if __name__ == "__main__":
  num_a, num_b = map(int, stdin.readline().split())
  GCDandLCM_problem = GCDandLCM(num_a, num_b)
  GCDandLCM_problem.solve()
