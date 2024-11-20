A = tuple(map(int, input().split(',')))
B = tuple(input().split(','))

mean_A = sum(A) / len(A)
count_greater_mean = sum(1 for x in A if x > mean_A)
print(f"Số lượng phần tử trong A lớn hơn trung bình cộng: {count_greater_mean}")

even_A = tuple(x for x in A if x % 2 == 0)
odd_A = tuple(x for x in A if x % 2 != 0)
print(f"Tuple các số chẵn: {even_A}")
print(f"Tuple các số lẻ: {odd_A}")

k = input()
count_k = sum(1 for s in B if k in s)
print(f"Số lần xuất hiện của ký tự '{k}' trong B: {count_k}")

long_strings = tuple(s for s in B if len(s) >= 5)
print(f"Các phần tử trong B có độ dài lớn hơn hoặc bằng 5 ký tự: {long_strings}")

C = tuple(zip(A, B))
print(f"Tuple mới C: {C}")
