"""
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
"""
fmt = "Case #{}: {} + {} = {}"
T = int(input())
for i in range(1, T + 1):
    A, B = [int(x) for x in input().split()]
    print(fmt.format(i, A, B, A + B))