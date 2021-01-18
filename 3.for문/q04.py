import sys
T = int(input())
for _ in range(T):
    A, B = [int(x) for x in sys.stdin.readline().rstrip().split()]
    print(A + B)