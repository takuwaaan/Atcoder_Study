s = input()
t = input()
s_st = ''.join(sorted(s))
t_strv = ''.join(sorted(t,reverse=True))
if s_st < t_strv:
    print("Yes")
else:
    print("No")