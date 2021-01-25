"""
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
"""


def is_prime(x):

    MAX = int(x**0.5) + 1
    for j in range(2, MAX):
        if x % j == 0:  # 나머지가 없으면
            return False
    else:
        return True


M, N = [int(x) for x in input().split()]

if M == 1:
    M += 1

elif M == 2 or N == 2:
    print(2)

primes = {i for i in range(3, N + 1, 2)}
for p in range(3, int(N**0.5) + 1, 2):
    if is_prime(p):
        primes -= {j for j in range(2 * p, N + 1, p)}

primes = list(primes)
primes.sort()
[print(x) for x in primes if x >= M]