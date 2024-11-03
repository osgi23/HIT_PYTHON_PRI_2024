import math

# a

a = int(input())

octal_a = oct(a)[2:]
num_digits = len(octal_a)
bits_needed = math.ceil(num_digits * math.log2(3))
print(bits_needed)

#b

number = 10
attributes_methods = dir(number)
print(attributes_methods)


