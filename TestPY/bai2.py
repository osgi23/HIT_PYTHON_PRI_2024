s = input()
dic = {}
for char in s:
    if (char <= 'z' and char >= 'a') or (char <= 'Z' and char >= 'A'):
        if char in dic:
            dic[char] += 1
        else:
            dic[char] = 1

print(dic)