while True:
    N = int(input())

    q = N // 5
    ans = -1
    for i in range(q, -1, -1):
        div = (N - 5 * i)
        q, r = divmod(div, 3)
        if r == 0:
            ans = i + q
            break
    print(ans)