"""
지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.
하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.
첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다
"""

BW = "BW" * 4
WB = "WB" * 4
BW_BOARD = "".join(BW if i % 2 == 0 else WB for i in range(8))
WB_BOARD = "".join(WB if i % 2 == 0 else BW for i in range(8))


def count_n(b):
    bw_score = sum(x != y for x, y in zip(b, BW_BOARD))
    wb_score = sum(x != y for x, y in zip(b, WB_BOARD))
    if wb_score > bw_score:
        return bw_score
    else:
        return wb_score


N, M = [int(x) for x in input().split()]
board = [input() for _ in range(N)]
best_score = 64
for r in range(N - 8 + 1):
    for c in range(M - 8 + 1):
        b = [row[c:c+8] for row in board[r:r+8]]
        b = "".join(b)
        score = count_n(b)
        if score < best_score:
            best_score = score

print(best_score)