print("Chao mung den CLB Tin Hoc HIT")
print("CLB Tin Hoc HIT truc thuoc Khoa CNTT - '10 diem'")
text = "CLB Tin Hoc HIT truc thuoc Khoa CNTT"

uppercase_letters = ''.join([char for char in text if char.isupper()])
print("Các chữ cái in hoa:", uppercase_letters)

lowercase_letters = ''.join([char for char in text if char.islower()])
print("Các chữ cái thường:", lowercase_letters)

if 'CNTT' in text:
    print('Yes')
else:
    print('No')

swapped_case = text.swapcase()
print("Chuỗi sau khi thay thế:", swapped_case)
