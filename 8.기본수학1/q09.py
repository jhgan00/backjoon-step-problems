"""
김우현을 위해 x지점부터 정확히 y지점으로 이동하는데 필요한 공간 이동 장치 작동 횟수의 최솟값을 구하는 프로그램을 작성하라
"""


def solution(a, b):
    distance = b - a
    step_size = 1
    distance -= 2 * step_size

    while distance > 0:  # 남은 거리가 0 혹은 음수가 되면 반복 종료

        step_size += 1  # 스텝 사이즈를 하나 올리고
        distance -= 2 * step_size  # 양쪽에서 가운데로 이동

    # 반복이 끝나면 남은 거리는 0이거나 음수

    if distance == 0:  # 만약 남은 거리가 0이면

        ans = 2 * step_size  # 현재의 스텝 크기 * 2 가 이동 횟수와 같음

    else:  # 만약 남은 거리가 음수이면

        distance += 2 * step_size  # 마지막 스텝을 되돌리고
        ans = 2 * (step_size - 1)  # 해당 스텝까지 이동한 횟수 기록

        if distance <= step_size:  # s + 1 보다 남은 거리가 작으면
            ans += 1  # 남은 거리는 한번에 이동 가능

        else:  # s + 1 보다 남은 거리가 크면
            ans += 2  # 남은 거리는 두 번에 걸쳐 이동 가능

    return ans


T = int(input())
for _ in range(T):
    x, y = [int(i) for i in input().split()]
    print(solution(x, y))
