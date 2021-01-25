n = int(input())

i = 0
while n > i:
    n -= i
    i += 1


a = i - n + 1
b = n

if i % 2 == 0:
    print("{}/{}".format(b, a))
else:
    print("{}/{}".format(a, b))