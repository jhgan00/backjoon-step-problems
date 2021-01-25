"""
10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
"""


def d(n):
    return n + sum(int(i) for i in str(n))


target = {x for x in range(10000)}
ans = list(target - {d(x) for x in target})
ans.sort()
for i in ans:
    print(i)