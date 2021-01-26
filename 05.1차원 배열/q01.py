"""
N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
"""
import sys
_ = input()
inputs = set(sys.stdin.readline().rstrip().split())
inputs = set(map(int, inputs))
print(min(inputs), max(inputs))