def create_matrix_from_list(a, n, m):
    k = len(a)
    
    if k < n * m:
        print("Không thể tạo được ma trận.")
        return
    
    matrix = []
    for i in range(n):
        row = a[i * m: (i + 1) * m]
        matrix.append(row)
    
    formatted_matrix = "[ " + " , ".join(str(row) for row in matrix) + " ]"
    print(formatted_matrix)

a = [1, 2, 4, 3, 5, 4, 3, 6, 1, 4, 2, 7, 4, 3, 4, 8, 7, 6]
n = 3
m = 4
create_matrix_from_list(a, n, m)
