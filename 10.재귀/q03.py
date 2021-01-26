"""
재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.
크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.
"""


def star(x):

    if x == 3:
        return [["*", "*", "*"], ["*", " ", "*"], ["*", "*", "*"]]
    else:
        prior = star(x//3)
        result = []
        for i in range(len(prior)):
            result.append(prior[i] * 3)
        for i in range(len(prior)):
            result.append(prior[i] + [" "] * (x // 3) + prior[i])
        for i in range(len(prior)):
            result.append(prior[i] * 3)

        return result


n = int(input())
for line in star(n):
    print("".join(line))