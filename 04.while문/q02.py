import sys
inputs = sys.stdin.readline().rstrip()
while inputs:
    print(sum(int(x) for x in inputs.split()))
    inputs = sys.stdin.readline().rstrip()