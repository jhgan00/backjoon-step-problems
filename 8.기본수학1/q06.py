def search(k, n):
    row = [i for i in range(1, n + 1)]
    for _ in range(k - 1):

        x = 1
        new_row = [x]
        for r in row[1:]:
            x += r
            new_row.append(x)

        row = new_row
    return sum(row)


T = int(input())

for _ in range(T):

    K = int(input())
    N = int(input())

    if K == 0:
        print(N)

    else:
        print(search(K, N))