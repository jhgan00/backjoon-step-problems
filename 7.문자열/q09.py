"""
예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다. 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
"""

cas = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
S = input().strip()
for ca in cas:
    S = S.replace(ca, "1")
print(len(S))