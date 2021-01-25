"""
골드바흐의 추측은 유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다.
이러한 수를 골드바흐 수라고 한다. 또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다.
예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다.
10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.
2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오.
만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.
"""


def is_prime(x):
    if x == 1:
        return False

    MAX = int(x**0.5) + 1
    for j in range(2, MAX):
        if x % j == 0:  # 나머지가 없으면
            return False
    else:
        return True


end = 10000
primes = {i for i in range(3, end + 1, 2)}
primes.add(2)

for p in range(2, int(end ** 0.5) + 1):
    if is_prime(p):
        primes -= {j for j in range(2 * p, end, p)}

primes = list(primes)
primes.sort(reverse=True)

N = int(input())

for _ in range(N):

    n = int(input())
    partitions = [0, n]
    for p in primes:
        if (p < n) and (p >= n * 0.5):
            r = n - p
            if is_prime(r):
                if abs(p - r) < abs(partitions[0] - partitions[1]):
                    partitions = [p, r]
    partitions.sort()
    print(partitions[0], partitions[1])