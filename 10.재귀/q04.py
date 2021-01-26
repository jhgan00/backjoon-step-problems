"""
세 개의 장대가 있고 첫 번째 장대에는 반경이 서로 다른 n개의 원판이 쌓여 있다. 각 원판은 반경이 큰 순서대로 쌓여있다.
이제 수도승들이 다음 규칙에 따라 첫 번째 장대에서 세 번째 장대로 옮기려 한다.
한 번에 한 개의 원판만을 다른 탑으로 옮길 수 있다.
쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.
이 작업을 수행하는데 필요한 이동 순서를 출력하는 프로그램을 작성하라. 단, 이동 횟수는 최소가 되어야 한다.
아래 그림은 원판이 5개인 경우의 예시이다.
"""


def move(x, src=1, dst=3):
    if x == 1:
        return [(src, dst)]
    else:
        side_dst = ({1, 2, 3} - {src, dst}).pop()
        return move(x-1, src, side_dst) + [(src, dst)] + move(x-1, side_dst, dst)


n = int(input())
steps = move(n)
print(len(steps))
for step in steps:
    print(step[0], step[1])