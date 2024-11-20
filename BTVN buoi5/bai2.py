registered = set(input().split(','))
checked_in = set(input().split(','))

not_checked_in = registered - checked_in
print(f"Các bạn chưa check-in: {', '.join(not_checked_in)}")

total_participants = len(registered | checked_in)  # Hợp của 2 tập hợp
print(f"Tổng số lượng các bạn đã đăng ký và đã check-in: {total_participants}")

sorted_registered = sorted(registered)
print(f"Danh sách các bạn đã đăng ký (theo thứ tự từ điển): {', '.join(sorted_registered)}")
