import math

def tinhgiaithua(i):
    if i == 1:
        return 1
    return i * tinhgiaithua(i - 1)

x = int(input())
sum = 1
for i in range (1, 200):
    sum += pow(x, i) / tinhgiaithua(i)

print(sum)