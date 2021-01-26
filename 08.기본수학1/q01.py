"""
A, B, C가 주어졌을 때, 손익분기점을 구하는 프로그램을 작성하시오.
"""


A, B, C = [int(x) for x in input().split()]
if C <= B:
    print(-1)
else:
    print(A // (C - B) + 1)