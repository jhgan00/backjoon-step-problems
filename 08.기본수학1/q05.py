N = int(input())

for _ in range(N):
    H, W, N = [int(x) for x in input().split()]
    q, r = divmod(N, H)

    if r == 0:
        print(str(H) + str(q).zfill(2))

    else:
        print(str(r) + str(q + 1).zfill(2))