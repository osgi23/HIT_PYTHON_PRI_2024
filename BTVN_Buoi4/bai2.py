def merge_lists_alternating(a, b):
    c = []
    len_a, len_b = len(a), len(b)
    
    for i in range(max(len_a, len_b)):
        if i < len_a:
            c.append(a[i])
        if i < len_b:
            c.append(b[i])
    
    return c

# ex
a = ['a', 'b', 'c']
b = [1, 2, 3, 4, 5]
c = merge_lists_alternating(a, b)
print(c)
