A, B, V = [int(x) for x in input().split()]
q, r = divmod(V - A, A - B)
if r == 0:
    print(q + 1)
else:
    print(q + 2)