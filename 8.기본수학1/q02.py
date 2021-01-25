n = int(input())

i = 1
while n > 1:  # 뺐을 때 나머지가 1이면
    n -= i * 6
    i += 1
print(i)