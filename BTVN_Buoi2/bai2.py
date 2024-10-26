s = input()

s_tmp = "HIT"
s_tmp2 = "hit"

if s.find(s_tmp) != -1 or s.find(s_tmp2) != -1:
    print("true")
else:
    print("false")

if s.find("15") == -1:
    print("true")
else:
    print("false")