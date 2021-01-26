"""
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
"""


def factorial(x):
    if x <= 0:
        return 1
    else:
        return x * factorial(x-1)


n = int(input())
print(factorial(n))