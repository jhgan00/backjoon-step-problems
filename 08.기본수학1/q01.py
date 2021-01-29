"""
A, B, C가 주어졌을 때, 손익분기점을 구하는 프로그램을 작성하시오.
"""


A, B, C = [int(x) for x in input().split()]
if C <= B:  # 매출보다 비용이 같거나 크면 항상 손해
    print(-1)
else:  # 그렇지 않다면
    print(A // (C - B) + 1)