"""
자연수 M과 N이 주어질 때 M이상 N 이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.
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


M = int(input())
N = int(input())

prime_nums = [x for x in range(M, N+1) if is_prime(x)]

if prime_nums:
    print(sum(prime_nums))
    print(min(prime_nums))

else:
    print(-1)
