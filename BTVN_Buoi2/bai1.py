a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))

# a. a cộng b
print("a cộng b:", a + b)

# b. a trừ b
print("a trừ b:", a - b)

# c. a nhân b
print("a nhân b:", a * b)

# d. a chia lấy nguyên b
print("a chia lấy nguyên b:", a // b)

# e. a mũ b
print("a mũ b:", a ** b)

# f. a chia dư b
print("a chia dư b:", a % b)

# g. so sánh a và b
if a > b:
    print("a lớn hơn b")
elif a < b:
    print("a nhỏ hơn b")
else:
    print("a bằng b")

# h. a AND b
print("a AND b:", a & b)

# i. a OR b
print("a OR b:", a | b)

# j. a XOR b
print("a XOR b:", a ^ b)

# k. NOT a == b
print("NOT a == b:", not (a == b))

# l. a dịch phải 5 bit
print("a dịch phải 5 bit:", a >> 5)

# m. a dịch trái 6 bit
print("a dịch trái 6 bit:", a << 6)

# n. in hệ cơ số 2 đảo ngược của a
binary_a = bin(a)[2:]
reversed_binary_a = binary_a[::-1]
print("Hệ cơ số 2 đảo ngược của a:", reversed_binary_a)
