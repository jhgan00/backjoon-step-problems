# 두 정수 A와 B를 입력받은 다음, AxB를 출력하는 프로그램을 작성하시오.
inputs = input()
A, B = [int(x) for x in inputs.split()]
print(A * B)