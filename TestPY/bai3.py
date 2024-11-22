s_input = input()
lst = []
str = ""
tmp = 0

for char in s_input:
    if char.isdigit():
       tmp = int(char)
    elif char == '[':
        lst.append((str, tmp))
        str = ""
        tmp = 0
    elif char == ']':
        last_str, number = lst.pop()
        str = last_str + str * number
    else:
        str += char

print(str)
