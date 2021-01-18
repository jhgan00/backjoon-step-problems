"""
대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
"""
import sys


def evaluate(n, scrs):
    m = sum(scrs) / n
    return (sum(scr > m for scr in scrs) / N) * 100


C = int(input())
for _ in range(C):
    test_case = [int(x) for x in sys.stdin.readline().rstrip().split()]
    N = test_case[0]
    scores = test_case[1:]
    percentage = evaluate(N, scores)
    print("{:.3f}%".format(percentage))