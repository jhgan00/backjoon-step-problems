"""
상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다. 즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다. 예를 들어, UNUCIC는 868242와 같다.
할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.
"""


from string import ascii_uppercase
times = []
for i in range(3, 11):
    if i in [8, 10]:
        for _ in range(4):
            times.append(i)
    else:
        for _ in range(3):
            times.append(i)

keymap = {c:t for c, t in zip(ascii_uppercase, times)}

S = input().replace(" ", "")
print(sum(keymap.get(s) for s in S))