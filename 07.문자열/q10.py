"""
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다.
예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만,
aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.
"""


def is_group(S):
    used = []  # 한 번 이상 등장한 문자는 used 리스트에 추가하자
    old = S[0]  # 순서대로 이전 문자열과 비교
    ans = True  # 리턴값 초기화

    for new in S:  # S 를 돌면서 개별 문자 체크
        if new in used:  # 만약 문자가 등장한 적이 있으면
            ans = False  # 그룹 단어가 아님
            break

        elif new == old:  # 같은 문자의 연속: 그룹 생성 중
            continue

        else:  # 같은 문자의 연속이 끝났다면
            used.append(old)  # 사용된 문자 리스트에 추가하고
            old = new  # old 문자 갱신

    return ans


N = int(input())
print(sum([is_group(input())for _ in range(N)]))