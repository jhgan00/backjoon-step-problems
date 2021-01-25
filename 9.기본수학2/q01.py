"""
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
"""


def is_prime(x):
    if x == 1:
        return False

    MAX = int(x ** 0.5) + 1
    for j in range(2, MAX):
        if x % j == 0:  # 나머지가 없으면
            return False
    else:
        return True


_ = int(input())
nums = [int(x) for x in input().split()]
print(sum(is_prime(x) for x in nums))
