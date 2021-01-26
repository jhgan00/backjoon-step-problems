"""
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.
"""


def test(n):
    ans = True
    if n < 100:
        return ans

    numbers = [int(digit) for digit in str(n)]
    shifted = numbers[1:]
    step = numbers[1] - numbers[0]

    for n, s in zip(numbers, shifted):
        if not step == s - n:
            ans = False
            break

    return ans


N = int(input())
print(sum(test(i) for i in range(1, N + 1)))