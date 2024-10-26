# Khởi tạo danh sách để lưu thông tin
student = []

n = int(input())

for i in range(n):    
    name = input()
    age = int(input())
    gioitinh = input()
    honnhan = input()

    student_info = {
        "Họ và tên": name,
        "Tuổi": age,
        "Giới tính": gioitinh,
        "Tình trạng hôn nhân": honnhan
    }

    student.append(student_info)

for student_info in student:
    for key, value in student_info.items():
        print(f"{key}: {value}")
    print()  
