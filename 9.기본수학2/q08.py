"""
세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.
"""
xs = []
ys = []
for _ in range(3):
    x, y = input().split()
    xs.append(x)
    ys.append(y)

coords = [0, 0]
for x, y in zip(xs, ys):
    if xs.count(x) == 1:
        coords[0] = x
    if ys.count(y) == 1:
        coords[1] = y

print(coords[0], coords[1])