S = input()
year = int(S[0:4])
mon = int(S[5:7])
day = int(S[8:])
#print(year,mon,day)
if year <= 2019 and 1 <= mon <= 4 and 1 <= day <= 30:
    print("Heisei")
else:
    print("TBD")