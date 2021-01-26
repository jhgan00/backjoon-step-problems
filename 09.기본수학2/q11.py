"""
조규현의 좌표 (x1, y1)와 백승환의 좌표 (x2, y2)가 주어지고,
조규현이 계산한 류재명과의 거리 r1과 백승환이 계산한 류재명과의 거리 r2가 주어졌을 때,
류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.
x, y는 -10,000보다 크거나 같고, 10,000보다 작거나 같은 정수이고, r1, r2는 10,000보다 작거나 같은 자연수이다.
"""
import sys

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = [int(x) for x in sys.stdin.readline().strip().split()]

    if x1 == x2 and y1 == y2:  # 두 점의 좌표가 같으면
        if r1 == r2:  # 두 원의 반지름이 같으면
            print(-1)  # 동심원
        else:
            print(0)  # 겹치지 않는다

    else:
        distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2)**0.5  # 두 점 사이의 거리
        MAX = max([r1, r2, distance])  # 세 선분 중 가장 긴 선분
        rest = sum([r1, r2, distance]) - MAX  # 나머지 둘의 합

        if MAX > rest:  # 만약 가장 긴 선분의 길이가 나머지 둘의 합보다 크면
            print(0)  # 만나는 점이 없음
        elif MAX == rest:
            print(1)  # 접함
        else:
            print(2)  # 두 점에서 만남
