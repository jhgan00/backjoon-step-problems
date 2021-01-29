"""
재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.
크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.
"""


def star(x):
    """
    패턴을 2차원 리스트로 반환. x=3 이면 3 by 3, x=9 이면 9 by 9 ...
    :param x: int
    :return: list[list[str]]
    """

    if x == 3:  # x 의 최소값 3
        return [["*", "*", "*"], ["*", " ", "*"], ["*", "*", "*"]]  # 패턴을 2차원 리스트로 반환
    else:  # 만약 3보다 크면
        prior = star(x//3)  # 이전의 패턴을 구한다. 이전의 패턴은 2차원 리스트임. 만약
        result = []  # 결과를 저장할 리스트 초기화.

        # 3 by 3 배열의 첫째 행: 이전 패턴을 세 번 채워넣어야 함
        for i in range(len(prior)):  # 이전 패턴의 행마다
            result.append(prior[i] * 3)  # 패턴을 3번 반복

        # 3 by 3 배열의 둘째 행: 이전 패턴, 공백, 이전 패턴 순서로 채워넣어야 함
        for i in range(len(prior)):  # 이전 패턴의 행마다
            result.append(prior[i] + [" "] * (x // 3) + prior[i])  # 패턴 - 공백 - 패턴

        # 3 by 3 배열의 셋째 행: 첫째 행과 같음
        for i in range(len(prior)):
            result.append(prior[i] * 3)

        return result


n = int(input())
for line in star(n):
    print("".join(line))