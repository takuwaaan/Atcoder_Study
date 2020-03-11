import itertools

n = int(input())
p = input().replace(" ", "")
q = input().replace(" ", "")
m = ""
for i in range(1, n + 1):
    m += str(i)
anagram_list = ["".join(v) for v in itertools.permutations(m)]

pa = 0
qa = 0

for i in range(len(anagram_list)):
    if anagram_list[i] == p:
        pa = i+1
    if anagram_list[i] == q:
        qa = i+1
print(abs(pa-qa))