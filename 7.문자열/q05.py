"""
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
"""

S = input().upper()
unq = list(set(S))  # 고유한 알파벳
cnt = [S.count(c) for c in unq]  # 알파벳별 카운트
max_cnt = max(cnt)

if cnt.count(max_cnt) == 1:
    idxmax = cnt.index(max_cnt)
    print(unq[idxmax])

else:
    print("?")