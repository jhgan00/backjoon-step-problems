"""
주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.
"""

while True:
    inputs = [int(x) for x in input().split()]
    if not inputs[0]:
        break
    hypo = max(inputs)
    if sum(i ** 2 for i in inputs if i != hypo) ** 0.5 == hypo:
        print("right")
    else:
        print("wrong")