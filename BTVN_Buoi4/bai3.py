def find(num_lst1, num_lst2):
    count_num = {}
    for num in num_lst1:
        if num in count_num:
            count_num[num] += 1
        else:
            count_num[num] = 1
    
    solve = []
    
    for num in num_lst2:
        if num in count_num and count_num[num] > 0:
            solve.append(num)
            count_num[num] -= 1
    return solve

nums1 = [1, 3, 2, 2, 1]
nums2 = [1, 1, 1, 1, 1, 1, 3]
print(find(nums1, nums2)) 
