"""
베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.
이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.
예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다.
(11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)
자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오.
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


end = 123456 * 2 + 1
primes = {i for i in range(2, end)}
for p in range(2, int(end ** 0.5) + 1):
    if is_prime(p):
        primes -= {j for j in range(2 * p, end, p)}

while True:
    n = int(input())
    if not n:
        break

    start = n
    end = 2 * n
    print(sum(1 for x in primes if (x > start) and (x <= end)))