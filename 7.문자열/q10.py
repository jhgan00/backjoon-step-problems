"""
단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.
"""


def is_group(S):
    used = []
    old = S[0]
    ans = True
    for new in S:
        if new in used:
            ans = False
            break

        elif new == old:
            continue

        else:
            used.append(old)
            old = new

    return ans


N = int(input())
print(sum([is_group(input())for _ in range(N)]))