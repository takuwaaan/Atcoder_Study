n,k = map(int,input().split())
a = list(map(int,input().split()))
mol = []
for i in range(n):
    j = i+1
    while(True):
        if j == n:
            break
        mol.append(a[i]*a[j])
        j += 1
mol.sort()
print(mol[k-1])