# -*- coding: utf-8 -*-
# 링크 : https://arisel.notion.site/11508-2-1-ce2e05079cd74cc0b44d47c698d8bcc0


from sys import stdin


N = int(stdin.readline())
A = [int(stdin.readline()) for _ in range(N)]
A.sort(reverse=True)

print(sum(A) - sum(A[2::3]))
