# bai 1_1 tinh e^x

def giaithua(n):
    if n == 1 or n == 0:
        return 1
    return n * giaithua(n - 1)

x = float(input())
n1 = 30
sum1 = 1.0
for i in range(1, n1, 1):
    sum1 += pow(x, i) / giaithua(i)

print("Gia tri cua e^x la", sum1)


# bai 1_2 tinh gia tri bieu thuc
n = int(input())
sum2 = 1.0

for i in range(1, n, 1):
    sum2 += 1 / giaithua(i)

print("gia tri cua bieu thuc la: ", sum2)