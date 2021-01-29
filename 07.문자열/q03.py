"""
알파벳 소문자로만 이루어진 단어 S가 주어진다.
각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.
"""

from string import ascii_lowercase  # 모든 알파벳 소문자
s = input()

# find 메소드: 찾는 문자열이 있으면 인덱스를 리턴하고 없으면 -1을 리턴
print(" ".join([str(s.find(c)) for c in ascii_lowercase]))