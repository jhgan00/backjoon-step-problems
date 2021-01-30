"""
N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.
첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다.
둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을 넘지 않는 양의 정수이다.
합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.
"""

import sys
from itertools import combinations

N, M = [int(x) for x in sys.stdin.readline().strip().split()]
cards = [int(x) for x in sys.stdin.readline().strip().split() if int(x) < M]
MAX = -1
for comb in combinations(cards, 3):
    s = sum(comb)
    if s > M:
        continue
    elif s > MAX:
        MAX = s
print(MAX)