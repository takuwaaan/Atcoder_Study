import sys
s = input()
if s[0] == "A" and s.count("C") == 1 and "C" in s[2:-1]:
    ss = set(s)
    ss.remove("A")
    ss.remove("C")
    SS = set([i.upper() for i in ss])
    if len(ss & SS) == 0:
        print("AC")
        sys.exit()
print("WA")