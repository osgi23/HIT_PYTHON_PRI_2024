
input_dict = eval(input("Nhập dictionary (theo định dạng key: value, cách nhau bởi dấu phẩy): "))

def swap_dict(input_dict):
    swapped = {}
    for key, value in input_dict.items():
        if value in swapped:
            return None
        swapped[value] = key
    return swapped

result = swap_dict(input_dict)
if result is None:
    print("Kết quả: None (có trùng lặp key sau khi hoán đổi)")
else:
    print(f"Kết quả: {result}")
