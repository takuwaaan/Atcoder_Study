s = input()
st=0
ed=0
for i,word in enumerate(s):
    if word == "A":
        st = i
        break
for i,word in enumerate(reversed(s)):
    if word == "Z":
        ed = len(s)-i
        break
print(ed-st)